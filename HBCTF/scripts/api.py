from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
#FlaskAPI docs avilable at http://www.flaskapi.org/
import json, random, string, couchdb, click, subprocess

try:
	from . import subcipher
except:
	import subcipher
	
app = FlaskAPI(__name__)

def RandomToken(length):
   return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

def dbconnect():
    with open('DBdata.json') as data_file:    
        data = json.load(data_file)
        ssl = data.get('ssl')
        username = data.get('username')
        password = data.get('password')
        host = data.get('host')
        port = data.get('port')
        data_file.close()
        if ssl is False:
            ssl = 'http://'
        else: 
            ssl = 'https://'
        couch = couchdb.Server(ssl + str(username) + ':' + str(password) + '@' + str(host) +':' + str(port) + '/')
        return(couch)
        
def initdb():
    couch = dbconnect()
    try:
        couch = couchdb.Server() # assuming localhost
        db = couch['ctf']
    except:
        db = couch.create('ctf')
    subprocess.run(['/bin/bash', '-O', 'extglob', '-c', 'service couchdb start'])
    click.echo('Database Started.')
    return()

def start(port, debug):
    app.run(host='0.0.0.0',port=port,debug=debug)
    couch = couchdb.Server('http://' + str(username) + ':' + str(password) + '@' + str(host) +':' + str(dbport) + '/')
    db = couch.create('services')
    return()

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
	try:
		checkin_resp = request.data
		IP = checkin_resp.get('IP')
		Port  = checkin_resp.get('Port')
		TeamID  = checkin_resp.get('TeamID')
		if IP and Port and TeamID is not None:
			Token, key = CheckinUpdate(IP, Port, TeamID)
			return {'Score Token': Token,
					'Key': key}
		else:
			return {'Invalid': 'request'}
	except:
		return {'Invalid': 'request'}
				
@app.route("/ScoreTokentSubmit/", methods=['GET','POST'])
def STS():
	'''Accepts players score submitions and passes its info over to ServiceScore funtion to validate the token and then update the teams score when its valid.
	json data should be in format {"TeamID": "Highlander","Token": "therecanbeonlyone"}
	Example: 
	curl -H "Content-Type: application/json" -X POST -d '{"TeamID": "Highlander","Token": "therecanbeonlyone"}' http://localhost:5001/ScoreTokentSubmit/
	'''
	try:
		sts_resp = request.data
		Token = sts_resp.get('Token')
		TeamID  = sts_resp.get('TeamID')
		if Token and TeamID is not None:
			print('Team ' + TeamID + 'has scored service points!')
			ServiceScore(TeamID, Token)
			return {'request data': request.data}
		else:
			return {'Invalid': 'request'}
	except:
		return {'Invalid': 'request'}
		
if __name__ == "__main__":
    start()
