from datetime import datetime
from birajwebapp import db

class Data(db.Model):
    """
    A class representing uploaded data.

    Attributes:
    -----------
    id : int
        The unique identifier of the data.
    date_uploaded : datetime
        The date and time when the data was uploaded.
    file_name : str
        The name of the file containing the uploaded data.
    data_column : str
        The name of the column containing the data of interest.
    """

    __tablename__ = "SiteUploadedData"

    id = db.Column(db.Integer, primary_key=True)
    date_uploaded = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    file_name = db.Column(db.String(120), nullable=False)
    data_column = db.Column(db.String(20), nullable=False)

    def __init__(self, file_name, data_column):
        """
        Constructs a new Data instance.

        Parameters:
        -----------
        file_name : str
            The name of the file containing the uploaded data.
        data_column : str
            The name of the column containing the data of interest.
        """
        self.file_name = file_name
        self.data_column = data_column

    def __repr__(self):
        """
        Returns a string representation of the Data instance.

        Returns:
        --------
        str
            A string representation of the Data instance.
        """
        return f"('{self.date_uploaded}', '{self.file_name}', '{self.data_column}')"
