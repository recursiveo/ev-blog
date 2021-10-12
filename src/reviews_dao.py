import logging

from src.mongo_connection import connect_mongo

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

dummy_txt = "No matter which one of its silky powertrains is on duty, " \
            "the 2022 BMW 3-series is supremely satisfying to drive. While its remarkable refinement " \
            "is offset by not-quite-great steering feel, its body is composed on any kind of road, its " \
            "brakes are strong, and its ride is comfortable for daily chores. Plus, its interior is rich " \
            "and roomy and it has a sizable trunk. Rivals such as the Genesis G70 offer better value, and " \
            "the Alfa Romeo Giulia is a sexier alternative, but no other sports sedan possesses the bandwidth " \
            "of the Bimmer. Along with a sublime eight-speed automatic and rear- or all-wheel drive, " \
            "the 3-series is available with a terrific turbocharged four-cylinder (330i), a plug-in-hybrid " \
            "setup (330e) with up to 23 miles of all-electric range, or a ferocious 382-hp turbo " \
            "straight-six (M340i) that's as eager and effortless as engines come. Thankfully, " \
            "the sedan's excellence doesn't begin and end with driving excitement. That's because " \
            "the 2022 3-series is sporty any time but luxurious and practical all the time."


class GetData:
    def __init__(self):
        self.username = 'John Doe'
        self.post_id = '#1234TY'
        self.data = dummy_txt

    def get_reviews_from_db(self):
        try:
            db = connect_mongo()
            table = db['user_reviews']
            data = table.find({})
            return data
        except Exception as e:
            logger.error(e)
            raise e

    def set_review_data(self, data):
        try:
            db = connect_mongo()
            reviews_collection = db['user_reviews']
            res = reviews_collection.insert_one(data)
            logger.info(res)
            return res
        except Exception as e:
            logger.error(e)
            raise e
