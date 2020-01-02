# DATABASE MODELS 
from marshmallow import fields, Schema
import datetime
from . import db  
from sqlalchemy.orm import relationship


class Searched_queries(db.Model):
 
  __tablename__ = 'Searched_queries'

  id = db.Column(db.Integer, primary_key=True)
  query_name = db.Column(db.String, nullable=False)
  
  results = db.relationship("Query_result",backref = "owner")


class Query_result(db.Model):
  __tablename__ = 'Query_result'
  id = db.Column(db.Integer, primary_key=True)
  query_id = db.Column(db.Integer,db.ForeignKey("Searched_queries.id"),nullable=False)
  url = db.Column(db.String, nullable=False)


class User_details(db.Model):
  __tablename__ = 'User_details'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String, nullable=False,)
  email = db.Column(db.String, nullable=False,unique=True)
  password = db.Column(db.String,nullable=False)







