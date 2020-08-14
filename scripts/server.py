from flask import (
    Flask,
    Response,
    request
)
from jsons import dumps
from get_hours_logged import *

# Create the application instance
app = Flask(__name__)

# return time logged
@app.route('/time-logged', methods=['GET'])
def time_logged():
  project_id = request.args.get('project_id')
  print(project_id)
  entries = fetch_time_entries(project_id)
  hour_summary = construct_hour_summary(entries)

  return Response(dumps(hour_summary), mimetype='application/json')

# return project details
@app.route('/projects', methods=['GET'])
def projects():
  all_projects = fetch_project_details()
  return Response(dumps(all_projects), mimetype='application/json')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)