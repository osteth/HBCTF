import HBCTF
from HBCTF.scripts import api

def test_token_generator():
	test_token = api.RandomToken(20)
	assert test_token is not ''
	assert len(test_token) == 20
	
def test_checkinupdate():
	data = api.CheckinUpdate('192.168.0.1', '5000', 'mudkips')
	assert data is not None

def test_checkin():
	data = api.Player_Checkin()
	assert data == {'Invalid': 'request'}

	
def test_STS():
	data = api.STS()
	assert data == {'Invalid': 'request'}