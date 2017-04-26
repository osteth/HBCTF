import HBCTF
from HBCTF.scripts import subcipher

def test_subcipher():
	message = 'Your invited to a unicorn party! - will you Bring NINJA chips?'
	key = subcipher.generate_key()
	ciphertext = subcipher.encrypt(key, message)
	decrypted = subcipher.decrypt(key, ciphertext)
	assert decrypted == 'Your invited to a unicorn party! - will you Bring NINJA chips?'
	