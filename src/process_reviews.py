from src.logger import get_logger
from src.reviews_dao import GetData

logger = get_logger()


class Reviews:

    def __init__(self):
        self.reviews_data = GetData()

    def get_reviews(self,req_data):
        try:
            data = self.reviews_data.get_reviews_from_db(req_data)
            li = list()
            for i in data:
                obj = {
                    'name': i['name'],
                    'brand': i['brand'],
                    'model': i['model'],
                    'review_text': i['review_text'],
                    'uid': i['uid']
                }
                li.append(obj)
            return li
        except Exception as e:
            logger.error(e)
            raise e

    def set_review_data(self, data, email):
        try:
            res = self.reviews_data.set_review_data(data, email)
            return res
        except Exception as e:
            logger.error(e)
            raise e

    def update_reviews(self, req_data):
        try:
            upd_review = req_data['review_text']
            uid = req_data['uid']
            res = self.reviews_data.update_review(uid, upd_review)
            return res
        except Exception as e:
            logger.error(e)
            raise e

    def check_id(self, data, email):
        try:
            res = self.reviews_data.check_id(data, email)
            return res
        except Exception as e:
            logger.error(e)
            raise e

    def modify_review(self, data):
        try:
            res = self.reviews_data.modify_review(data)
            return res
        except Exception as e:
            logger.error(e)
            raise e

    def delete_review(self, data):
        try:
            res = self.reviews_data.delete_review(data)
            return res
        except Exception as e:
            logger.error(e)
            raise e