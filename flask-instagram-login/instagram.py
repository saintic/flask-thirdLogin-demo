# -*- coding: utf-8 -*-

import os
import json
import requests
from flask import Flask, redirect, url_for, request, jsonify, g, render_template
from SpliceURL import Splice

INSTAGRAM_APP_ID  = '05602bf1f7e648b89d50ea30d02dc295'
INSTAGRAM_APP_KEY = 'bcea24fd61434f78b9b28479e3ddcc75'
REDIRECT_URI      = 'http://101.200.125.9:15000/'

app = Flask(__name__)

timeout = 5
verify  = False
proxies = {
        "http": "http://101.200.125.9:7071",
        "https": "http://101.200.125.9:7071",
    }

class ServerError(Exception):
    pass

def Get_Authorization_Code():
    ''' Redirect GitHub Landing Page URL '''
    return Splice(scheme="https", netloc="api.instagram.com", path="/oauth/authorize/", query={"client_id": INSTAGRAM_APP_ID, "redirect_uri": REDIRECT_URI, "response_type": "code"}).geturl

def Get_Access_Token(code):
    ''' Authorization Code cannot repeat '''
    Get_Access_Token_Url = Splice(scheme="https", netloc="api.instagram.com", path="/oauth/access_token", query={"client_id": INSTAGRAM_APP_ID, "client_secret": INSTAGRAM_APP_KEY, "code": code, "redirect_uri": REDIRECT_URI}).geturl
    access_token_data = requests.post(Get_Access_Token_Url, timeout=timeout, verify=verify, proxies=proxies).json()
    """
    {
        "access_token": "fb2e77d.47a0479900504cb3ab4a1f626d174d2d",
        "user": {
            "id": "1574083",
            "username": "snoopdogg",
            "full_name": "Snoop Dogg",
            "profile_picture": "..."
        }
    }
    """

    if isinstance(access_token_data, dict):
        return access_token_data
    else:
        raise ServerError("Get Access Token Error with Authorization Code")

def Get_User_Info(access_token):
    Get_User_Info_Url = Splice(scheme="https", netloc="api.instagram.com", path="/v1/users/self/", query={"access_token": access_token}).geturl
    return requests.get(Get_User_Info_Url, timeout=timeout, verify=verify, proxies=proxies).json()
    """
    {
    "data": {
        "id": "1574083",
        "username": "snoopdogg",
        "full_name": "Snoop Dogg",
        "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_1574083_75sq_1295469061.jpg",
        "bio": "This is my bio",
        "website": "http://snoopdogg.com",
        "counts": {
            "media": 1320,
            "follows": 420,
            "followed_by": 3410
        }
    }
    """

@app.before_request
def before_request():
    ''' Before every request '''
    g.signin = True if request.cookies.get("logged_in", "") in ("true", "True", True) else False
    app.logger.info(g.signin)

@app.route('/')
def index():
    code = request.args.get("code", "")
    app.logger.debug("code: %s" %code)
    #app.logger.debug(request.args)
    if g.signin:
        return "logged_in"
    elif code:
        _data = Get_Access_Token(code)
        access_token  = _data.get('access_token')
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
