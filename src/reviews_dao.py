import uuid

import flask_login

from src.logger import get_logger
from src.mongo_connection import connect_mongo
from src.PyMongo_Operations import fetch_data

logger = get_logger()


class GetData:
    def __init__(self):
        # self.username = 'John Doe'
        # self.post_id = '#1234TY'
        self.db = connect_mongo()
        self.reviews_collection = self.db['user_reviews']

    def get_reviews_from_db(self,req_data):
        try:
            # print(flask_login.current_user)
            # print(req_data + "  --Testing")
            if req_data == 'ALL':
                data = self.reviews_collection.find({})
            else:
                data = self.reviews_collection.find({'brand': req_data.lower()})
            # print(data)
            return data
        except Exception as e:
            logger.error(e)
            raise e

    def set_review_data(self, data, email):
        try:
            __user_data = self.__get_user_details(email)
            uid = uuid.uuid4().hex
            data['uid'] = uid
            data['name'] = __user_data['name']
            data['email'] = __user_data['email']

            logger.info(f'Inserting document uid: {uid}')
            res = self.reviews_collection.insert_one(data)

            logger.info(f'Record inserted with id: {res.inserted_id}  successfully')
            return True
        except Exception as e:
            logger.error(e)
            raise e

    def update_review(self, uid, new_data):
        try:
            query = {'uid': uid}
            new_values = {'$set': {'review_text': new_data}}
            res = self.reviews_collection.update_one(query, new_values)
            if res.matched_count > 0:
                logger.info('Record updated successfully')
                return True
            else:
                logger.info('Record not found.')
                return False
        except Exception as e:
            logger.error(e)
            raise e

    def check_id(self, data, email):
        try:
            res = self.reviews_collection.find_one({'uid': data, 'email': email['email']})
            # print(res)
            return res['review_text'] if res is not None else 'NULL'
        except Exception as e:
            logger.error(e)
            raise e

    def modify_review(self, data):
        try:
            # print(data)
            res = self.reviews_collection.update_one({'uid': data['uid']},
                                                     {'$set': {'review_text': data['review_text']}})
            # print(res.modified_count)
            return '1'
        except Exception as e:
            logger.error(e)
            raise e

    def delete_review(self, data):
        try:
            query = {"uid": data['uid']}
            res = self.reviews_collection.delete_one(query)
            return res.deleted_count
        except Exception as e:
            logger.error(e)
            raise e

    def __get_user_details(self, email):
        try:
            data = fetch_data(email)
            for rec in data:
                return rec
        except Exception as e:
            logger.error(e)
            raise e
