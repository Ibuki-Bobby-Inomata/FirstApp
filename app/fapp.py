#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template

#Flaskオブジェクトの生成
app = Flask(__name__)


#「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/")
def hello():
    return "Hello World"


#「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/index")
def index():
    return render_template("home.html")

#「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/index/todo")
def todo():
    return render_template("todo.html")

#「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/index/architecture")
def architecture():
    return render_template("architecture.html")

if __name__ == "__main__":
    app.run(debug=True)