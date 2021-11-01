from src.MongoConnection import connect_mongo
from bson.objectid import ObjectId
from flask_mail import Mail, Message


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

def replyTextUpodate(id,replyText,email):
    #update Record
    EV_Trendz = connect_mongo()
    ObjContactUs = EV_Trendz['Contact_Us']
    update_record = {'$set' :{'reply':replyText}}
    output = ObjContactUs.update_one({'_id': ObjectId(id)},update_record)
    print(output)

mail_settings = {
        "MAIL_SERVER": 'smtp.gmail.com',
        "MAIL_PORT": 465,
        "MAIL_USE_TLS": False,
        "MAIL_USE_SSL": True,
        "MAIL_USERNAME": 'blog4ev@gmail.com',
        "MAIL_PASSWORD": 'blog4ev123'
    }

def replyEmail(id,replyText,email):

    msg = Message(subject="Enquiry Reply From EV BLOG",
                  sender="blog4ev@gmail.com",
                  recipients=[email],  # use your email for testing
                  body=replyText)
    return msg
    #mail.send(msg)
    #return jsonify(recipients='ronypshaji@gmail.com')



