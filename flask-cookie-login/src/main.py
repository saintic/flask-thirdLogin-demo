# coding:utf8

__author__ = "Mr.tao <staugur@saintic.com>"

import time, hashlib, uuid
from flask import Flask, request, make_response, render_template, url_for, redirect

app = Flask(__name__)
md5 = lambda pwd:hashlib.md5(pwd).hexdigest()
SecretKey = str(uuid.uuid4())

@app.route('/')
def index():
    app.logger.info(request.cookies)
    if request.cookies.get("username"):
        return render_template("index.html")
    else:
        return """<form action="%s" method='post'>
            <input type="text" name="username" required>
            <input type="password" name="password" required>
            <input type="submit" value="登录">
            </form>""" %url_for("login")

@app.route("/login/", methods=['POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    app.logger.info(username)
    if username == "admin" and password == "admin":
        app.logger.info(url_for('index'))
        resp = make_response(redirect(url_for("index")))
        resp.set_cookie(key='username', value=username, expires=None)
        resp.set_cookie(key='sessionId', value=md5(username + password + SecretKey), expires=None)
        return resp
    else:
        return "login failed"

@app.route("/logout")
def logout():
    resp = make_response(redirect(url_for("index")))
    resp.set_cookie(key='username',  value='', expires=0)
    resp.set_cookie(key='sessionId',  value='', expires=0)
    return resp    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10120, debug=True)
