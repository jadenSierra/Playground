from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def playground():
    return "Welcome to my playground"

@app.route("/play")
def play_1():
    return render_template("index.html",num=3, color="cornflowerblue")

@app.route("/play/<int:num>")
def play_2(num):
    return render_template("index.html",num=num, color = "cornflowerblue")

@app.route("/play/<int:num>/<color>")
def play_3(num,color):
    return render_template("index.html", num=num, color=color)


if __name__ =="__main__":
    app.run(debug=True)