from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return 'This is Home!'

@app.route('/mypage')
def mypage():
   return render_template('index.html')
#render_template라는 함수를 사용하면 자동으로 templates 폴더 안에 있는 파일을 클라이언트에게 보내준다.

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)