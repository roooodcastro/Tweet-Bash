require "twitter"
require "oauth"
require "ini"
require 'digest/sha2'

class Auth

    attr_accessor :config

	def save_user(name, password, key, secret)
		if not @config.has_section? name
			@config[name] = { :password => encrypt_password(password) }
			@config[name] = { :key => key }
			@config[name] = { :secret => secret }
			@config.write
			puts Terminal.colorize("User saved successfully!", :green)
		else
			puts Terminal.colorize("User name already exists!", :red)
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
		if user and user.password == encrypt_password(password)
			return user
		else
			puts Terminal.colorize("Username or password incorrect. Please try again.", :b_red)
			return nil
		end
	end

	def get_user(username)
		if @config.has_section? username
			User.new(username, @config[username][:password], @config[username][:key], @config[username][:secret])
		end
	end

	def create_user
		success = false
		while not success
			puts "Type in your desired username"
			puts "(type '\\cancel'' to cancel)"
			name = Terminal.input(" >")
			if name == '\cancel'
				return false
			end
			if not name =~ /^[A-Za-z0-9._+$@-]+$/
				puts Terminal.colorize("User name must be alfanumeric and may include these symbols: ._-+@$", :red)
				sucess = false
			elsif not username_exists(name)
				success = true
			else
				puts Terminal.colorize("User name already exists, please choose another.", :red)
			end
		end
		puts Terminal.colorize("Retrieving authorization url from twitter.com, please wait.....", :yellow)
		client = TwitterOAuth::Client.new( :consumer_key => Utils.CONSUMER_KEY, :consumer_secret => Utils.CONSUMER_SECRET )
		request_token = client.request_token
		auth_url = 
		request_token.authorize_url
		puts Terminal.colorize("You must now authorize access to your Twitter account.", :cyan)
		puts Terminal.colorize("Please go to this url and authorize access: " + auth_url, :cyan)
		puts Terminal.colorize("After authorization paste the PIN provided by Twitter here:", :cyan)		
		verifier = Terminal.input("PIN:").strip()
		puts "Now create a password for logging in your new " + Utils.APP_NAME + " account:"
		password = Terminal.input_password("Password:")
		access_token = client.authorize( request_token.token, request_token.secret, :oauth_verifier => verifier )
		if client.authorized?
			key = access_token.token.strip()
			secret = access_token.secret.strip()
			save_user(name, password, key, secret)
		end
	end

	def initialize
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

auth = Auth.new
auth.create_user
