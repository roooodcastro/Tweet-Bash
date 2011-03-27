
	def edit_user_name(current_user)
		try
			puts "Type in your new user name:"
			puts "(type "\cancel" to cancel)"
			sucess = False
			while not sucess:
				new_name = raw_input("Username: ")
				if new_name == "\cancel":
					return ""
				elif " " in new_name:
					puts Terminal.colorize("User name cannot contain any spaces.", "RED")
				elif len(new_name) == 0:
					puts Terminal.colorize("User name cannot be empty!", "RED")
				elif @username_exists(new_name):
					puts Terminal.colorize("User name already exists.", "RED")
				else:
					sucess = True
			@remove_user(current_user.name)
			@save_user(new_name, current_user.password, current_user.key, current_user.secret)
			return new_name
		except:
			puts Terminal.colorize("An error occurred while saving your new username, sorry.", "B_RED")
			return ""
			
	def edit_password(self, current_user):
		try:
			sucess = False
			while not sucess:		
				puts "Type in your new password:"
				puts "(type "\cancel" to cancel)"
				password = getpass.getpass("Password: ")
				if password == "\cancel":
					return ""
				elif len(password) == 0:
					puts Terminal.colorize("Password cannot be empty!", "RED")
				double_check = ""
				puts "Say your new password again:"
				double_check = getpass.getpass("Password: ")
				if not password == double_check:
					puts Terminal.colorize("Passwords didn't match, please try again.", "RED")
				else:
					sucess = True
			@remove_user(current_user.name)
			@save_user(current_user.name, password, current_user.key, current_user.secret)
		except:
			puts Terminal.colorize("An error occurred while saving your new password, sorry.", "B_RED")
			return ""
		
