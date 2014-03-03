from google.appengine.ext import db
from google.appengine.api import users
import json

class User(db.Model):
    username = db.StringProperty(required=True)
    password = db.StringProperty(required=True)

    def toJsonString(self):
        objDict = {"username": self.username, "password": self.password}
        return json.dumps(objDict)

class Notification(db.Model):
    cam_id = db.StringProperty(required=True)
    video_id = db.StringProperty(required=True)
    date_time = db.DateTimeProperty(required=True)

    def toJsonString(self):
        objDict = {"cam_id": self.cam_id, "video_id": self.video_id, "date_time": self.date_time}
        return json.dumps(objDict)

class Camera(db.Model):
    cam_id = db.StringProperty(required=True)
    location = db.StringProperty(required=True)
    owner = db.StringProperty(required=True)

    def toJsonString(self):
        objDict = {"cam_id": self.cam_id, "location": self.location, "owner": self.owner}
        return json.dumps(objDict)
