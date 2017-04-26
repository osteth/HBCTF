from flask import request, url_for
from flask.ext.api import FlaskAPI, status, exceptions
import json, random, string
import subcipher

app = FlaskAPI(__name__)

def RandomToken(length):
   return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

def CheckinUpdate(IP, Port, TeamID):
	'''Takes in data from Player_Checkin and udates the database.'''
	key = subcipher.generate_key()
	Token = RandomToken(64)
	encrypted = subcipher.encrypt(key, Token)
	return(Token, key)
	
def ServiceScore(TeamID, Token):
	'''takes in data from STS, checks token for validity and increases the teams score if valid.'''
	return()
	
@app.route("/checkin/", methods=['GET', 'POST'])
def Player_Checkin():
	'''Accepts json formatted request containing the teams TeamID, IP, and Port and pushes the info over to CheckinUpdate to be stored in the DB
	json data should be in format {"TeamID": "Mudkips","IP": "192.168.0.1","Port": "5001"}
	Example: 
	curl -H "Content-Type: application/json" -X POST -d '{"TeamID": "Mudkips","IP": "192.168.0.1","Port": "5001"}' http://localhost:5001/checkin/
	'''
	checkin_resp = request.data
	IP = checkin_resp.get('IP')
	Port  = checkin_resp.get('Port')
	TeamID  = checkin_resp.get('TeamID')
	# print(IP, Port, TeamID)
	Token, key = CheckinUpdate(IP, Port, TeamID)
	
	return {'Score Token': Token,
			'Key': key}
	
@app.route("/ScoreTokentSubmit/", methods=['GET','POST'])
def STS():
	'''Accepts players score submitions and passes its info over to ServiceScore funtion to validate the token and then update the teams score when its valid.
	json data should be in format {"TeamID": "Highlander","Token": "therecanbeonlyone"}
	Example: 
	curl -H "Content-Type: application/json" -X POST -d '{"TeamID": "Highlander","Token": "therecanbeonlyone"}' http://localhost:5001/ScoreTokentSubmit/
	'''
	sts_resp = request.data
	Token = sts_resp.get('Token')
	TeamID  = sts_resp.get('TeamID')
	# print(TeamID, Token)
	print('Team ' + TeamID + 'has scored service points!')
	ServiceScore(TeamID, Token)
	
	return {'request data': request.data}

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)
