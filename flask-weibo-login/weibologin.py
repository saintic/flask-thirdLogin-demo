# -*- coding: utf-8 -*-

import os
import json
import requests
from flask import Flask, redirect, url_for, request, jsonify, g
from SpliceURL import Splice

WEIBO_APP_ID    = '1746902937'
WEIBO_APP_KEY   = '8853e9ba5835e5a26fa0b4907c2995ce'
REDIRECT_URI    = 'https://passport.saintic.com/'

app = Flask(__name__)

timeout = 5
verify  = False

def Get_Authorization_Code():
    ''' Redirect Weibo Landing Page URL '''
    return Splice(scheme="https", netloc="api.weibo.com", path="/oauth2/authorize", query={"response_type": "code", "client_id": WEIBO_APP_ID, "redirect_uri": REDIRECT_URI}).geturl

def Get_Access_Token(code):
    ''' Authorization Code cannot repeat '''
    Access_Token_Url = Splice(scheme="https", netloc="api.weibo.com", path="/oauth2/access_token", query={"grant_type": "authorization_code", "client_id": WEIBO_APP_ID, "client_secret": WEIBO_APP_KEY, "code": code, "redirect_uri": REDIRECT_URI}).geturl
    return  requests.post(Access_Token_Url, timeout=timeout, verify=verify).json()

def Get_User_Info(access_token, uid):
    User_Info_Url = Splice(scheme="https", netloc="api.weibo.com", path="/2/users/show.json", query={"access_token": access_token, "uid": uid}).geturl
    return requests.get(User_Info_Url, timeout=timeout, verify=verify).json()

@app.before_request
def before_request():
    ''' Before every request '''
    g.signin = True if request.cookies.get("logged_in", "") in ("true", "True", True) else False
    app.logger.info(g.signin)

@app.route('/')
def index():
    code = request.args.get("code", "")
    #app.logger.debug("code:%s" %code)
    #app.logger.debug(request.args)
    if g.signin:
        return "logged_in"
    elif code:
        _data = Get_Access_Token(code)
        app.logger.debug(_data)
        access_token  = _data['access_token']
        uid = _data['uid']
        userData = Get_User_Info(access_token, uid)

        app.logger.debug(userData)

        #resp = render_template('info.html', userData=userData)
        #resp.set_cookie(key="logged_in", value='true', expires=None)

        resp = jsonify(userData)
        resp.set_cookie(key="logged_in", value='true', expires=None)
        return resp
    else:
        return redirect(url_for("login"))

@app.route('/login/')
def login():
    return redirect(Get_Authorization_Code())

@app.route('/logout/')
def logout():
    resp = jsonify(state="logout")
    resp.set_cookie(key="logged_in", value='false', expires=0)
    return resp

if __name__ == '__main__':
    app.run(debug=True, port=15000, host='0.0.0.0')
