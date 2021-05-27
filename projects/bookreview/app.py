from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/review', methods=['POST']) #localhost:5000/review 로 들어가면 API가 적혀있다.
def write_review():
    # 3가지의 데이터를 받아오기 위한 장치!
    # 클라이언트에게 title_give라는 값으로 데이터를 받아올거야!
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']

    # 전달받은 데이터를 db에 저장하기!
    doc = {'title': title_receive,
           'author': author_receive,
           'review': review_receive}
    db.bookreview.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})


@app.route('/review', methods=['GET'])
def read_reviews():
    # db에서 bookreview 안에 있는 모든 데이터를 가져오되 _id 값은 넣지 않는다.
    reviews = list(db.bookreview.find({}, {'_id':False}))
    # 'all_reviews'의 value로 가져온 데이터들을 넣는다.
    return jsonify({'all_reviews': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)