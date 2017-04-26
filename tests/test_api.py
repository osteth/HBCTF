import HBCTF
from HBCTF.scripts import api


def test_token_generator():
	test_token = api.RandomToken(20)
	assert test_token is not ''
	assert len(test_token) == 20