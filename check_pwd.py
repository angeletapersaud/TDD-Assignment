

symbols = "~`!@#$%^&*()_+-="


    
def check_pwd(password: str) -> bool:
	if (len(password) < 8 or len(password) > 20
		or not any(character.islower() for character in password)
		or not any(character.isupper() for character in password)
		or not any(character.isdigit() for character in password)
		or not any(character in symbols for character in password)):
		return False
	return True
	