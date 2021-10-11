from flask import Flask, jsonify, render_template,request
from src.ContactUs import insertContactUs
from src.MongoConnection import connect_mongo
import json
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


if __name__ == '__main__':
    app.run(port=7000)
