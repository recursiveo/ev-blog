import pymongo

from src.logger import get_logger

logger = get_logger()


def connect_mongo():
    try:
        connection_string = 'mongodb+srv://blog4ev:blog4ev123@cluster0.yvfuz.mongodb.net/EV_Trendz?retryWrites=true&w=majority'
        mongo_client = pymongo.MongoClient(connection_string)
        EV_Trendz = mongo_client.EV_Trendz
        return EV_Trendz
    except Exception as e:
        logger.log(e)
        raise e
