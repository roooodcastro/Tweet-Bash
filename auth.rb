require "utils"
require "twitter"
require "oauth"
require "ini"
require "highline"
require 'digest/sha2'

class Auth:

    attr_accessor :config

	def save_user(name, password, key, secret)
		if not @config.has_section? name
			@config[name] = { :password => encrypt_password(password) }
			@config[name] = { :key => key }
			@config[name] = { :secret => secret }
			@config.write
			puts utils.colorize("User saved successfully!", :green)
		else
			puts utils.colorize("User name already exists!", :red)
		end
	end
			
	def remove_user(name)
		@config.delete_section name
		@config.write
	end
	
	def encrypt_password(password)
		Digest::SHA2.new << password
	end

	def login(user_name)
			user = get_user(user_name)
			password =  ask("Password: ") { |q| q.echo = false }
			if user and user.password == encrypt_password(password):
				return user
			else:
				puts utils.colorize("Username or password incorrect. Please try again.", :b_red)
				return nil
#			puts utils.colorize("An error ocurred. Please try again.", :red)
#			return nil

	def get_user(username)
		if @config.has_section? username
			User.new(username, @config[username][:password], @config[username][:key], @config[username][:secret])
		end
	end

	def create_user(auth)
		success = false
		while not success
			puts "Type in your desired username"
			puts "(type '\\cancel'' to cancel)"
			name = raw_input(" > ")
			if name == "\\cancel":
				return False
			elif not @username_exists(name):
				success = True
			else:
				puts utils.colorize("User name already exists, please choose another.", "RED")					
			if " " in name:
				puts utils.colorize("User name cannot contain any spaces.", "RED")
				sucess = False
		auth = tweepy.OAuthHandler(utils.CONSUMER_KEY, utils.CONSUMER_SECRET)
		puts utils.colorize("Retrieving authorization url from twitter.com, please wait.....", "YELLOW")
		auth_url = auth.get_authorization_url()
		puts utils.colorize("You must now authorize access to your Twitter account.", "CYAN")
		puts utils.colorize("Please go to this url and authorize access: " + auth_url, "CYAN")
		puts utils.colorize("After authorization paste the PIN provided by Twitter here:", "CYAN")
		verifier = raw_input("PIN: ").strip()
		puts "Now create a password for logging in your new " + utils.app_name + " account:"
		password = getpass.getpass("Password: ")
		auth.get_access_token(verifier)
		key = auth.access_token.key.strip()
		secret = auth.access_token.secret.strip()
		@save_user(name, password, key, secret)

	def edit_user_name(self, current_user):
		try:
			puts "Type in your new user name:"
			puts "(type "\cancel" to cancel)"
			sucess = False
			while not sucess:
				new_name = raw_input("Username: ")
				if new_name == "\cancel":
					return ""
				elif " " in new_name:
					puts utils.colorize("User name cannot contain any spaces.", "RED")
				elif len(new_name) == 0:
					puts utils.colorize("User name cannot be empty!", "RED")
				elif @username_exists(new_name):
					puts utils.colorize("User name already exists.", "RED")
				else:
					sucess = True
			@remove_user(current_user.name)
			@save_user(new_name, current_user.password, current_user.key, current_user.secret)
			return new_name
		except:
			puts utils.colorize("An error occurred while saving your new username, sorry.", "B_RED")
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
					puts utils.colorize("Password cannot be empty!", "RED")
				double_check = ""
				puts "Say your new password again:"
				double_check = getpass.getpass("Password: ")
				if not password == double_check:
					puts utils.colorize("Passwords didn't match, please try again.", "RED")
				else:
					sucess = True
			@remove_user(current_user.name)
			@save_user(current_user.name, password, current_user.key, current_user.secret)
		except:
			puts utils.colorize("An error occurred while saving your new password, sorry.", "B_RED")
			return ""
		

	def __init__(self):
    	@config = IniFile.new("config.cfg")
	end
	
end
		
class User

    attr_accessor :name, :password, :key, :secret
	
	def initialize(name, password, key, secret)
		@name = name
		@password = password
		@key = key
		@secret = secret
	end
end
