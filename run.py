from birajwebapp import create_app
from birajwebapp import db

app = create_app()
app.app_context().push()
data_path = app.config['DATA_DIR']

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
    
