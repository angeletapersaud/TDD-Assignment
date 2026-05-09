

symbols = "~`!@#$%^&*()_+-="

# must be between 8-20 characters long and have one of each: lowercase letter, uppercase letter, integer & symbol
def check_pwd(password: str) -> bool:
	
	if len(password) < 8 or len(password) > 20:
		return True

	