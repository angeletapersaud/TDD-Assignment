

symbols = "~`!@#$%^&*()_+-="


def check_pwd(password: str) -> bool:
	if len(password) < 8 :
		return False
	return True
    

	