import HBCTF
from HBCTF.scripts import subcipher

def test_has_legs():
    assert not HBCTF.has_legs

	
def test_subcipher():
	'''encrypts and decrypts the message and tests if the messes is the same before and after to ensure cipher script is not broken'''
	message = 'Your invited to a unicorn party! - will you Bring NINJA chips?'
	key = subcipher.generate_key()
	ciphertext = subcipher.encrypt(key, message)
	decrypted = subcipher.decrypt(key, ciphertext)
	assert decrypted == 'Your invited to a unicorn party! - will you Bring NINJA chips?'
	