
from __future__ import print_function   # GAE.
# GAE is a READ-ONLY filesystem!!!!  (Godammit, Jim...).
# Don't worry bob we'll use the datastore!
from google.appengine.ext import db
from google.appengine.api import users
import os   # GAE.
import sys  # GAE.
from models import User ,Camera
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask import render_template
import datetime
import json
app = Flask(__name__.split('.')[0])

#all @route functions
@app.route('/')
def hello(name=None):
    """ Return hello template at application root URL."""
    return "Raspberry SPi is here!!!!"

@app.route('/addCamera', methods=["POST"])
def addCamera():
    response = None
    content = json.loads(request.json)
    if checkForUser(str(content["user_name"])) is True:#, content["password"])
        newCam = Camera(cam_id='c00001', location=content["location"], owner=content["user_name"])
        newCam.put()
        response = json.dumps({"result": "cam_added"})
        return response
    else:
        return content["user_name"]

@app.route('/recieve_video', methods=["POST"])
def recieveVideo():
    returnMessage = None
    content = json.loads(request.json)
    try:
            #get video
            cam_id = content["cam_id"]
            video_id = "v00001"
            dateTime = datetime.datetime.now()
            #create notification
            newNoti = Notification( cam_id=cam_id, video_id=video_id, date_time=dateTime)
            #add notification to database
            newNoti.put()
            #return confirmation message
            returnMessage = json.dumps({"response":"accepted"})
    except Exception, e:
            returnMessage = json.dumps({"response":"not_accepted"})
    finally:
        return returnMessage

@app.route("/notifications", methods=["POST"])
def getNotifications():
    #get json object
    content = json.loads(request.json)
    #create a user object
    theUser = User(username = content["user_name"],
                        password = content["password"])
    #check if user is in datastore
    if checkForUser(theUser) is True:
        #get the camreas for that user

        #get the notifications for each camera
        query = db.Query(Notification)
        query.filter("cam_id =", theUser.username)
        result = query.fetch(100)
        response = {}
        i = 0
        for Notif in result:
            response[i] = Notif
            i += 1

        #return notifications as json
        return json.dumps(response)
    else:
        #return error
        return json.dumps({"error":"invalid_User"})

@app.route("/user", methods=["POST"])
def recieveUser():
    content = json.loads(request.json)
    theUser = User(username = content["user_name"],
                        password = content["password"])
    if content["method"] == "register":
        if checkForUser(theUser) is False:
            theUser.put()
            return json.dumps({"result": "user_added"})
        else:
            return json.dumps({"result": "user_exists"})
    elif content["method"] == "login":
        #return cameras linked to the account!
        if checkForUser(theUser) is False:
            return json.dumps({"result": "no_login"})
        else:
            return json.dumps({"result": "login"})
    else:
        return json.dumps({"result": "no_method"})

#other functions
def checkForUser(tempUser):
    query = db.Query(User)
    if str(type(tempUser)) == "<type 'str'>":
        query.filter('username =', tempUser)
        result = query.get()
        if result is None:
            return False
        else:
            return True
    elif str(type(tempUser)) == "<class 'models.User'>":
        query.filter('username =', tempUser.username)
        result = query.get()
        if result is None:
            return False
        else:
            return True





