from flask import Flask, render_template, request

from src.logger import get_logger
from src.process_reviews import Reviews

app = Flask(__name__)
review_data = Reviews()

logger = get_logger()

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/review-home')
def reviews():
    try:
        # return render_template('reviews.html')
        return render_template('review-home.html')
    except Exception as e:
        logger.error(e)
        raise e


# @app.route('/reviews-get-data', methods=['GET'])
# def fetch_review_data():
#     try:
#         data = review_data.get_reviews()
#         response = jsonify(data)
#         return response
#     except Exception as e:
#         logger.error(e)
#         raise e

@app.route('/reviews', methods=['GET'])
def show_reviews():
    try:
        data = review_data.get_reviews()
        return render_template('reviews.html', list_data=data)
    except Exception as e:
        logger.error(e)
        raise e


@app.route('/submit-review', methods=['POST'])
def submit_review():
    try:
        data = request.get_json()
        logger.info(data)
        review_data.set_review_data(data)
        return 'ok'
    except Exception as e:
        logger.error(e)
        raise e


if __name__ == '__main__':
    app.run(port=7000)

