from src.MongoConnection import connect_mongo

def insertContactUs(rec):
    EV_Trendz = connect_mongo()
    print(rec['contactobj'])
    ObjContactUs = EV_Trendz['Contact_Us']
    output = ObjContactUs.insert_one(rec['contactobj'])
    print(output)


