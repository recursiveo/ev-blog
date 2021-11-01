import uuid

from src.logger import get_logger
from src.mongo_connection import connect_mongo

logger = get_logger()


class GetData:
    def __init__(self):
        # self.username = 'John Doe'
        # self.post_id = '#1234TY'
        self.db = connect_mongo()
        self.reviews_collection = self.db['user_reviews']

    def get_reviews_from_db(self):
        try:
            data = self.reviews_collection.find({})
            return data
        except Exception as e:
            logger.error(e)
            raise e

    def set_review_data(self, data):
        try:
            uid = uuid.uuid4().hex
            data['uid'] = uid

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