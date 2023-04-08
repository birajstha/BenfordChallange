from datetime import datetime
from birajwebapp import db

class Data(db.Model):
    __tablename__ = "SiteUploadedData"

    id = db.Column(db.Integer, primary_key=True)
    date_uploaded = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    file_name = db.Column(db.String(120), nullable=False)
    data_column = db.Column(db.String(20), nullable=False)

    
    def __init__(self, file_name, data_column):
        self.file_name = file_name
        self.data_column = data_column

    def __repr__(self):
        return f"('{self.date_uploaded}', '{self.file_name}', '{self.data_column}')"
