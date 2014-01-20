from flask import Flask
from flask import render_template,session,redirect,request,url_for
import urllib2

app=Flask(__name__)
app.secret_key = "PTC"

@app.route('/',methods=["POST","GET"])
def home():
        if request.method == 'GET':
                return render_template("index.html")

@app.route('/parentlogin',methods=["POST","GET"])
def pl():
        if request.method == 'GET':
                return render_template("parentlogin.html")

@app.route('/teacherlogin',methods=["POST","GET"])
def tl():
        if request.method == 'GET':
                return render_template("teacherlogin.html")

@app.route('/parentregister',methods=["POST","GET"])
def pr():
        if request.method == 'GET':
                return render_template("parentregister.html")

@app.route('/teacherregister',methods=["POST","GET"])
def tr():
        if request.method == 'GET':
                return render_template("teacherregister.html")




if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port =7002)
