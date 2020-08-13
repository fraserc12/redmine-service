from flask import (
    Flask,
    render_template
)
from jsons import dumps
from get_hours_logged import *

# Create the application instance
app = Flask(__name__, template_folder="templates")

# Create a URL route in our application for "/"
@app.route('/time-logged')
def time_logged():
  entries = fetch_time_entries('573')
  hour_summary = construct_hour_summary(entries)
  return dumps(hour_summary)

# Create a URL route in our application for "/"
@app.route('/projects')
def projects():
  all_projects = fetch_project_details()
  return dumps(all_projects)

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)