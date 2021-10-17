from src.MongoConnection import connect_mongo
from bson.objectid import ObjectId

def insertContactUs(rec):
    EV_Trendz = connect_mongo()
    print(rec['contactobj'])
    ObjContactUs = EV_Trendz['Contact_Us']
    output = ObjContactUs.insert_one(rec['contactobj'])
    print(output)


def deleteEnquiry(recId):
    EV_Trendz = connect_mongo()
    ObjContactUs = EV_Trendz['Contact_Us']
    output = ObjContactUs.delete_one({'_id': ObjectId(recId)})
    print(output)

