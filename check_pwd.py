

symbols = "~`!@#$%^&*()_+-="


def check_pwd(password: str) -> bool:
	if len(password) < 8 or len(password) > 20:
		return False
	if not any(character.islower() for character in password):
		return False
	if not any(character.isupper() for character in password):
		return False
	return True
    

	