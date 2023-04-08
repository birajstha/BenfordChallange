from os import path
from flask import Blueprint, flash
from birajwebapp import db
from birajwebapp.config import Config

entity = Blueprint('entity', __name__)

def save_data(data_dao, data_uploaded):
        data_path = path.join(Config.DATA_DIR, data_dao.file_name)

        try:
          data_uploaded.save(data_path)
          db.session.add(data_dao)
          db.session.commit()
          flash("Data Saved on Database")
          return data_path
        
        except Exception as e:
          flash("Data Saving on Database Failed")
          return None