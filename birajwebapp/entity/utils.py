from os import path
from flask import Blueprint, flash
from birajwebapp import db
from birajwebapp.config import Config

entity = Blueprint('entity', __name__)

def save_data(data_dao, data_uploaded):
        data_path = path.join(Config.DATA_DIR, data_dao.file_name)

        try:
          data_uploaded.save(data_path)
          return data_path
        
        except Exception as e:
          flash("Data Saving on Database Failed")
          return None