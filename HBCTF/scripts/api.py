from flask import request, url_for
from flask.ext.api import FlaskAPI, status, exceptions
import json

app = FlaskAPI(__name__)

def CheckinUpdate(IP, Port, TeamID):
	return()
	
@app.route("/checkin/", methods=['GET', 'POST'])
def Player_Checkin():
	checkin_resp = request.data
	IP = checkin_resp.get('IP')
	Port  = checkin_resp.get('Port')
	TeamID  = checkin_resp.get('TeamID')
	# print(IP)
	# print(Port)
	# print(TeamID)
	CheckinUpdate(IP, Port, TeamID)
	
	return {'request data': request.data}


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)
