from flask_wtf import FlaskForm
from flask_wtf.file import DataRequired
from wtforms import FileField, SubmitField, StringField

class UploadForm(FlaskForm):
    file = FileField('Please upload a flat file', validators=[DataRequired()])
    data_column = StringField('Mention data column', validators=[DataRequired()])
    submit = SubmitField('Submit')
