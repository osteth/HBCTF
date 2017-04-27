import HBCTF
from HBCTF.scripts import subcipher
from HBCTF.scripts import cesarcipher

	
def test_subcipher():
	'''encrypts and decrypts the message and tests if the messes is the same before and after to ensure cipher script is not broken'''
	message = 'Your invited to a unicorn party! - will you Bring NINJA chips?'
	key = subcipher.generate_key()
	ciphertext = subcipher.encrypt(key, message)
	decrypted = subcipher.decrypt(key, ciphertext)
	assert decrypted == 'Your invited to a unicorn party! - will you Bring NINJA chips?'
	
def test_subcipher2():
	'''test the subcipher module by calling its built in test intead of calling functions independantly'''
	output = subcipher.show_result('Without strong encryption, you will be spied on systematically by lots of people. - Whitfield Diffie')
	# print(output)
	assert output == 'Without strong encryption, you will be spied on systematically by lots of people. - Whitfield Diffie'
	

def test_cesarcipher():
	'''test the cesarcipher module'''
	output = cesarcipher.show_result('Experience is the teacher of all things', 13)
	#print(output)
	assert output == 'experience is the teacher of all things'
