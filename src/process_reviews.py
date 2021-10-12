from src.logger import get_logger
from src.reviews_dao import GetData

logger = get_logger()


class Reviews:

    def __init__(self):
        self.reviews_data = GetData()

    def get_reviews(self):
        try:
            data = self.reviews_data.get_reviews_from_db()
            li = list()
            for i in data:
                obj = {
                    'name': i['name'],
                    'brand': i['brand'],
                    'model': i['model'],
                    'review_text': i['review_text']
                }
                li.append(obj)
            return li
        except Exception as e:
            logger.error(e)
            raise e

    def set_review_data(self, data):
        try:
            res = self.reviews_data.set_review_data(data)
            return res
        except Exception as e:
            logger.error(e)
            raise e
