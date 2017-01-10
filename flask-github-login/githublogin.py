# -*- coding: utf-8 -*-

import os
import json
import requests
from flask import Flask, redirect, url_for, request, jsonify, g, render_template
from SpliceURL import Splice

GITHUB_APP_ID  = 'xxx'
GITHUB_APP_KEY = 'xxx'
REDIRECT_URI   = 'https://passport.saintic.com/callback/github/'

app = Flask(__name__)

timeout = 5
verify  = False

class ServerError(Exception): pass

def Parse_Access_Token(x):
    ''' parse string, such as access_token=E8BF2BCAF63B7CE749796519F5C5D5EB&expires_in=7776000&refresh_token=30AF0BD336324575029492BD2D1E134B'''
    print x
    return dict( _.split('=') for _ in x.split('&') )

def Get_Authorization_Code():
    ''' Redirect GitHub Landing Page URL '''
    return Splice(scheme="https", netloc="github.com", path="/login/oauth/authorize", query={"client_id": GITHUB_APP_ID, "redirect_uri": REDIRECT_URI}).geturl

def Get_Access_Token(code):
    ''' Authorization Code cannot repeat '''
    Get_Access_Token_Url = Splice(scheme="https", netloc="github.com", path="/login/oauth/access_token", query={"client_id": GITHUB_APP_ID, "client_secret": GITHUB_APP_KEY, "code": code, "redirect_uri": REDIRECT_URI}).geturl
    access_token_data = requests.post(Get_Access_Token_Url, timeout=timeout, verify=verify).text

    data = Parse_Access_Token(access_token_data)

    #Should returned right data, such as {'access_token': '79D493208A237BAB3C9AE93FAD2798CE', 'expires_in': '7776000', 'refresh_token': '30AF0BD336324575029492BD2D1E134B'}
    if isinstance(data, dict):
        return data
    else:
        raise ServerError("Get Access Token Error with Authorization Code")

def Get_User_Info(access_token):
    Get_User_Info_Url = Splice(scheme="https", netloc="api.github.com", path="/user", query={"access_token": access_token}).geturl
    return requests.get(Get_User_Info_Url, timeout=timeout, verify=verify).json()

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
        access_token  = _data['access_token']
        userData = Get_User_Info(access_token)

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
