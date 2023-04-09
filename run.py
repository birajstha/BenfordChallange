"""
This script creates a Flask app instance and runs it.

The app instance is created using the 'create_app' function from the 'birajwebapp' package. 
The 'db' module from the same package is also imported to create the necessary database tables.

The script checks if the '__name__' variable is set to '__main__'. This is done to ensure that 
the code inside the 'if' block is only executed if the script is run directly, and not if it is 
imported as a module.

The database is created using the 'db.create_all()' method. This will create all the necessary tables
in the database specified in the app's configuration.

Finally, the Flask app is run using the 'app.run()' method. The 'debug' parameter is set to 'True', 
which enables debug mode, allowing for easy debugging of the application.
"""

from birajwebapp import create_app
from birajwebapp import db

app = create_app()
app.app_context().push()
data_path = app.config['DATA_DIR']

if __name__ == "__main__":
    db.create_all()
    app.run()
