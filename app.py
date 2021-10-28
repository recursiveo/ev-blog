from flask import Flask, jsonify, render_template,request
from src.ContactUs import insertContactUs, deleteEnquiry, replyTextUpodate, replyEmail,mail_settings
from src.MongoConnection import connect_mongo
import json
from flask_mail import Mail, Message
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/contactUs/')
def openContactUs():
    return render_template('ContactUs.html')

@app.route("/open_Enquiry_page/")
def openEnquiryPage():
    return render_template('EnquiryDetails.html')


@app.route("/sendContact_us/",methods = ['POST', 'GET']) #default method is get
def contactus():
    if request.method == 'POST':
        rec = request.get_json()
        print(rec)
        insertContactUs(rec)
    return jsonify(recipients=rec['contactobj']['email'])


@app.route("/deleteDocument/",methods = ['POST', 'GET']) #default method is get
def deleteDocFromContactUs():
    if request.method == 'POST':
        rec = request.get_json()
        print(rec)
        deleteEnquiry(rec.get('docId'))
    return jsonify(documentId=rec.get('docId'))


@app.route("/updateReply/",methods = ['POST', 'GET']) #default method is get
def updateReplyInContactUs():
    if request.method == 'POST':
        rec = request.get_json()
        print(rec)
        replyTextUpodate(rec.get('id'),rec.get('replyText'),rec.get('email'))
    return jsonify(documentId=rec.get('docId'))



@app.route("/get_contact_us/") #default method is get
def get_contact_us():
    EV_Trendz = connect_mongo()
    ObjContactUs = EV_Trendz['Contact_Us']
    result = ObjContactUs.find({})
    response = []
    for document in result:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)


#http://127.0.0.1:5000/send-mail/
@app.route("/send-mail/",methods = ['POST', 'GET']) #default method is get
def sendmail():
    if request.method == 'POST':
        rec = request.get_json()
        app.config.update(mail_settings)
        mail = Mail(app)
        msg = replyEmail(rec.get('id'),rec.get('replyText'),rec.get('email'))
        mail.send(msg)
    return jsonify(recipients=rec.get('email'))




if __name__ == '__main__':
    app.run(port=7000)
