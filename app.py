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
		usern = request.form['username'].encode('ascii','ignore')
		passw = request.form['password'].encode('ascii','ignore')

		

@app.route('/teacherlogin',methods=["POST","GET"])
def tl():
        if request.method == 'GET':
                return render_template("teacherlogin.html")
	else:
		usern = request.form['username'].encode('ascii','ignore')
		passw = request.form['password'].encode('ascii','ignore')


@app.route('/parentregister',methods=["POST","GET"])
def pr():
        if request.method == 'GET':
                return render_template("parentregister.html")
	else:
		usern = request.form["username"].encode('ascii','ignore')
		passw = request.form["password"].encode('ascii','ignore')
		child = request.form["child"].encode('ascii','ignore')
		name = request.form["parent"].encode('ascii','ignore')
		digit = request.form["id"].encode('ascii','ignore')
		registerParent(usern, passw, child, name, digit)
		return redirect(url_for('pl'))

@app.route('/teacherregister',methods=["POST","GET"])
def tr():
        if request.method == 'GET':
                return render_template("teacherregister.html")
	else:
		usern = request.form["username"].encode('ascii','ignore')
		passw = request.form["password"].encode('ascii','ignore')
		subject = request.form["subject"].encode('ascii','ignore')
		teacher = request.form["teacher"].encode('ascii','ignore')
		veri = request.form["zamansky"].encode('ascii','ignore')
		registerTeacher(usern, passw, subject, teacher, veri)
		return redirect(url_for('tl'))


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
		session.pop('username', None)
                return redirect("/")
	



if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port =7002)
