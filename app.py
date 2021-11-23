from flask import Flask, request, jsonify, render_template, session, flash
from functools import wraps
from src.PyMongo_Operations import insert_mongo, search_mongo, fetch_data, update_data, delete_data
import logging
from src.logger import get_logger
from src.process_reviews import Reviews
from src.ContactUs import insertContactUs, deleteEnquiry, replyTextUpodate, replyEmail, mail_settings
from src.MongoConnection import connect_mongo
import json
from flask_mail import Mail, Message
from bson import json_util

app = Flask(__name__)
app.secret_key="4564544532643869758"
process_reviews = Reviews()

logger = get_logger()


@app.route('/')
def index():
    logging.info("Entering into index")
    if 'username' in session:
        logging.info("User logged in")
        return 'You are logged in as ' + session['username']
    logging.info("Exiting from index")
    return render_template('reg.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['email'] = email = request.form['username']
        session['password'] = password = request.form['pass']
        data = {'email': email, 'password': password}
        existing_data = search_mongo(data)
        if existing_data:
            return render_template('index.html')
        else:
            flash('Invalid Credentials. Please do register/login accordingly!!!')
            return render_template('signup.html')
    # if 'username' not in session:
    #     print("lohhh")
    #     return render_template('login.html')
    # else:
    #     print("indd")
    #     return render_template('index.html')
    return render_template('reg.html')


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "email" in session:
            return f(*args, **kwargs)
        else:
            flash("\"You shall not pass!\" ")
            return render_template('reg.html')
    return wrap


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    logging.info("Entering into signup")
    if request.method == "POST":

        email = request.form['email']
        logging.info(f"Username {email}")
        data = {'email': email}
        existing_user = search_mongo(data)
        logging.info(f'existing_user {existing_user}')
        if existing_user > 0:
            flash("User already exist with this email id.Try to login or register with another mail id!!")
            return render_template('signup.html')
        password = request.form['pass']
        username = request.form['username']
        logging.info('username and password {} {}'.format(username, password))
        output = insert_mongo(username, password, email)
        logging.info("Result from data insertion into db {}".format(output))

    logging.info("Exiting from signup")
    return render_template('reg.html')


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    errors = None
    query_data = {"email": session['email']}
    data = fetch_data(query_data)
    count = search_mongo(query_data)
    if count == 0:
        errors = 'Invalid Credentials. Please try again.'
        flash('User not found!!!')
        return render_template('index.html', errors=errors)
    a = {}
    print(session['email'])
    password = None
    for i in data:
        password = i['password']
        print("ppppp", password)
        a['email'] = json.loads(json_util.dumps(i['email']))
        print("name", i['name'])
        a['name'] = json.loads(json_util.dumps(i['name']))
        print("jsonnnn", a['name'])
        if 'mobile' in i:
            a['mobile'] = json.loads(json_util.dumps(i['mobile']))
        else:
            a['mobile'] = ''

    if request.method == "POST":
        if request.form['action'] == 'Submit':
            if all([request.form['password'], request.form['confirm_mobile'], request.form['confirm_name']]):
                if request.form['update_password'] == request.form['confirm_password'] and request.form['mobile'] == request.form['confirm_mobile'] and request.form['name'] == request.form['confirm_name']:
                    a['mobile'] = request.form['mobile']
                    a['name'] = request.form['name']
                    if password == request.form['password']:
                        if request.form['update_password'] == request.form['confirm_password']:
                            update_data(query_data, {
                                '$set': {
                                             "name": request.form['name'],
                                             "password": request.form['update_password'],
                                             "mobile": request.form['mobile']
                                         }
                                         })
                        else:
                            flash("Password mismatch. Please do confirm with new password!!")
                            return render_template('profilepage.html')
                    else:
                        flash("Password mismatch. Please re-enter current password!!")
                else:
                    flash("Data mismatch!!")

            elif all([request.form['password'], request.form['confirm_mobile']]):
                a['mobile'] = request.form['mobile']
                if password == request.form['password']:
                    if request.form['update_password'] == request.form['confirm_password']:
                        if request.form['mobile'] == request.form['confirm_mobile']:
                            update_data(query_data, {
                                '$set': {
                                             "name": request.form['name'],
                                             "password": request.form['update_password']
                                         }
                                         })
                        else:
                            flash("Mobile number doesn't match. Please enter correct mobile!!")
                    else:
                        flash("Password mismatch. Please do confirm with new password!!")
                else:
                    flash("Password mismatch. Please re-enter current password!!")

            elif all([request.form['confirm_mobile'], request.form['confirm_name']]):
                if request.form['mobile'] == request.form['confirm_mobile'] and request.form['name'] == request.form['confirm_name']:
                    a['mobile'] = request.form['mobile']
                    a['name'] = request.form['name']

                    update_data(query_data, {
                        '$set': {
                                     "name": request.form['name'],
                                     "mobile": request.form['mobile']
                                 }
                                 })
                else:
                    flash("Entered name/mobile number mismatch. Please do verify and re-enter it!!")

            elif all([request.form['password'], request.form['name']]):
                if password == request.form['password']:
                    if request.form['update_password'] == request.form['confirm_password']:
                        a['name'] = request.form['name']
                        update_data(query_data, {
                            '$set': {
                                         "name": request.form['name'],
                                         "password": request.form['update_password']
                                     }
                                     })
                    else:
                        flash("Password mismatch. Please do confirm with new password!!")
                else:
                    flash("Password mismatch. Please re-enter current password!!")

            elif request.form['password'] and not all([request.form['mobile'], request.form['name']]):
                if password == request.form['password']:
                    if request.form['update_password'] == request.form['confirm_password']:
                        update_data(query_data, {
                            '$set': {
                                         "password": request.form['update_password']
                                     }
                                     })
                    else:
                        flash("Password mismatch. Please do confirm with new password!!")
                else:
                    flash("Password mismatch. Please re-enter current password!!")

            elif request.form['mobile'] and request.form['confirm_mobile'] and not all([request.form['password'], request.form['name']]):
                if request.form['mobile'] == request.form['confirm_mobile']:
                    a['mobile'] = request.form['mobile']
                    update_data(query_data, {
                        '$set': {
                                     "mobile": request.form['mobile']
                                 }
                                 })
                else:
                    flash("Mobile number mismatch. Please do verify!!")

            elif request.form['name'] and not all([request.form['mobile'], request.form['password']]):
                if request.form['name'] == request.form['confirm_name']:
                    a['name'] = request.form['name']
                    update_data(query_data,
                             {'$set': {
                                 "name": request.form['name']
                             }
                                 })
                else:
                    flash("Name mismatch. Please do verify!!")

        elif request.form['action'] == 'Delete':
            data = delete_data(query_data)
            session.pop('email', None)
            return render_template('reg.html')
    return render_template('profilepage.html', error=errors, mobile=a['mobile'] if a['mobile'] else '', name=a['name'] if a['name'] else None, email=session['email'])


@app.route('/review-home')
def reviews():
    try:
        # return render_template('view-reviews.html')
        return render_template('review-home.html')
    except Exception as e:
        logger.error(e)
        raise e


@app.route('/reviews', methods=['GET'])
def show_reviews():
    try:
        data = process_reviews.get_reviews()
        return render_template('view-reviews.html', list_data=data)
    except Exception as e:
        logger.error(e)
        raise e


@app.route('/submit-review', methods=['POST'])
def submit_review():
    try:
        data = request.get_json()
        logger.info(data)
        res = process_reviews.set_review_data(data)
        if res:
            return {'status': 'review updated'}, 200
        else:
            return {'status': 'review not found'}, 400
    except Exception as e:
        logger.error(e)
        raise e


@app.route('/update-review', methods=['POST'])
def update_reviews():
    try:
        data = request.get_json()
        logger.info(data)
        res = process_reviews.update_reviews(data)
        if res:
            return {'status': 'review updated'}, 200
        else:
            return {'status': 'review not found'}, 400
    except Exception as e:
        logger.error(e)
        raise e


@app.route('/add-review', methods=['GET'])
def add_reviews():
    return render_template('add-review.html')

@app.route('/edit-review', methods=['GET'])
def edit_review():
    return render_template('edit-review.html')

@app.route('/contactUs/')
def openContactUs():
    return render_template('ContactUs.html')

@app.route("/open_Enquiry_page/")
def openEnquiryPage():
    return render_template('EnquiryDetails.html')


@app.route("/sendContact_us/",methods = ['POST', 'GET'])  # default method is get
def contactus():
    if request.method == 'POST':
        rec = request.get_json()
        print(rec)
        insertContactUs(rec)
    return jsonify(recipients=rec['contactobj']['email'])


@app.route("/deleteDocument/", methods=['POST', 'GET'])  # default method is get
def deleteDocFromContactUs():
    if request.method == 'POST':
        rec = request.get_json()
        print(rec)
        deleteEnquiry(rec.get('docId'))
    return jsonify(documentId=rec.get('docId'))


@app.route("/updateReply/", methods=['POST', 'GET'])  # default method is get
def updateReplyInContactUs():
    rec = None
    if request.method == 'POST':
        rec = request.get_json()
        print(rec)
        replyTextUpodate(rec.get('id'), rec.get('replyText'), rec.get('email'))
    return jsonify(documentId=rec.get('docId'))


@app.route("/get_contact_us/")  # default method is get
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


@app.route("/send-mail/", methods=['POST', 'GET'])
def sendmail():
    rec = None
    if request.method == 'POST':
        rec = request.get_json()
        app.config.update(mail_settings)
        mail = Mail(app)
        msg = replyEmail(rec.get('id'), rec.get('replyText'), rec.get('email'))
        mail.send(msg)
    return jsonify(recipients=rec.get('email'))


@app.route('/logout')
def logout():
    session.pop('email', None)
    return render_template('reg.html')


if __name__ == '__main__':
    app.run(port=7000, debug=True)
