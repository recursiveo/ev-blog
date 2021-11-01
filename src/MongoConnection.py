import pymongo


def connect_mongo():
    connection_string = 'mongodb+srv://blog4ev:blog4ev123@cluster0.yvfuz.mongodb.net/EV_Trendz?retryWrites=true&w=majority'
    mongo_client = pymongo.MongoClient(connection_string)
    EV_Trendz = mongo_client.EV_Trendz
    return EV_Trendz
