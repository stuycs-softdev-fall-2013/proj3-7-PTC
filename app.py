from flask import Flask
from flask import render_template,session,redirect,request,url_for
import urllib2
import login

app=Flask(__name__)
app.secret_key = "PTC"
registeredteacherlist = ["Zamansky, Mike", "Brownmykolyk, Topher", "Brooks, Peter", "Cocoros, Jim"]


@app.route('/',methods=["POST","GET"])
def home():
        if request.method == 'GET':
                return render_template("index.html")

@app.route('/parentlogin',methods=["POST","GET"])
def pl():
        if request.method == 'GET':
                return render_template("parentlogin.html")
	else:
		usern = request.form['Username'].encode('ascii','ignore')
		passw = request.form['Password'].encode('ascii','ignore')
		if login.loginParent(usern,passw):
			session['Username'] = usern
			return redirect ("/success")
		else:
			return redirect ("/login")
		
		

@app.route('/teacherlogin',methods=["POST","GET"])
def tl():
        if request.method == 'GET':
                return render_template("teacherlogin.html")
	else:
		usern = request.form['Username'].encode('ascii','ignore')
		passw = request.form['Password'].encode('ascii','ignore')
		if login.loginTeacher(usern,passw):
			session['Username'] = usern
			return redirect ("/success")
		else:
			return redirect ("/login")

@app.route('/parentregister',methods=["POST","GET"])
def pr():
        if request.method == 'GET':
                return render_template("parentregister.html")
	else:
		usern = request.form["Username"].encode('ascii','ignore')
		passw = request.form["Password required"].encode('ascii','ignore')

@app.route('/teacherregister',methods=["POST","GET"])
def tr():
        if request.method == 'GET':
                return render_template("teacherregister.html")


@app.route('/parentpostlogin',methods=["POST","GET"])
def ppl():
#IMPORTANT, implement a check for login so that people cannot just type in the url! Implement after this page is done
        if request.method == 'GET':
                return render_template("parentpostlogin.html", teacher = registeredteacherlist, length = len(registeredteacherlist))

@app.route('/teacherpostlogin',methods=["POST","GET"])
def tpl():
#IMPORTANT, implement a check for login so that people cannot just type in the url! Implement after this page is done
        if request.method == 'GET':
                return render_template("teacherpostlogin.html")

@app.route('/logout',methods=["POST","GET"])
def logout():
        if request.method == 'GET':
		#logoutcode
                return redirect("/")
	



if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port =7002)
