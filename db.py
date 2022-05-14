from flask_sqlalchemy import SQLAlchemy

import base64
import datetime
import os
import random
import re
import string

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable="False")
    email = db.Column(db.String, nullable="False")
    username = db.Column(db.String, nullable="False")

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.email = kwargs.get("email")
        self.username = kwargs.get("username")
    
    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "email" : self.email,
            "username" : self.username
        }
