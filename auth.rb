require "rubygems"
require "terminal"
require "utils"
require "text"
require "twitter"
require "twitter_oauth"
require "inifile"
require 'digest/sha2'

class Auth

	include Terminal
	include Utils
	include PrintText
	
	
    attr_accessor :config

	def initialize
		puts t "account.saved"
    	@config = IniFile.new("config.cfg")
	end

	def save_user(name, password, key, secret)
		if not @config.has_section? name
			@config[name]["password"] = encrypt_password(password)
			@config[name]["key"] = key
			@config[name]["secret"] = secret
			@config.save
			puts colorize(t("account.saved"), :green)
		else
			puts colorize(t("account.exists"), :red)
		end
	end
			
	def remove_user(name)
		@config.delete_section name
		@config.write
	end

	def login(user_name)
		user = get_user(user_name)
		password = input_password(t("general.prompt_password"))
		if user and user.password == encrypt_password(password)
			return user
		else
			puts colorize(t("login.incorrect"), :b_red)
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
			puts t("account.ask_name")
			puts t("general.cancel")
			name = input(" >")
			if name == '\cancel'
				return false
			end
			if not name =~ /^[A-Za-z0-9._+$@-]+$/
				puts colorize(t("account.name_limits"), :red)
				sucess = false
			elsif not @config.has_section? name
				success = true
			else
				puts colorize(t("account.exists"), :red)
			end
		end
		puts colorize(t("account.retrieving"), :yellow)
		client = TwitterOAuth::Client.new( :consumer_key => consumer_key, :consumer_secret => consumer_secret )
		request_token = client.request_token
		auth_url = request_token.authorize_url
		puts colorize(t("account.go_authorize", app_name), :cyan)
		puts colorize(auth_url, :cyan)
		puts colorize(t("account.ask_pin"), :cyan)
		verifier = input("PIN:").strip()
		puts t("account.ask_password", app_name)
		password = input_password(t("general.prompt_password"))
		access_token = client.authorize( request_token.token, request_token.secret, :oauth_verifier => verifier )
		if client.authorized?
			key = access_token.token.strip()
			secret = access_token.secret.strip()
			save_user(name, password, key, secret)
		end
	end
	
	def edit_user_name(current_user)
		puts t("account.ask_name")
		puts t("general.cancel")
		sucess = false
		while not sucess:
			new_name = input(t("general.prompt_name"))
			if new_name == '\cancel'
				return ""
			elsif not name =~ /^[A-Za-z0-9._+$@-]+$/
				puts colorize(t("account.name_limits"), :red)
			elsif new_name.size == 0
				puts colorize(t("account.name_empty"), :red)
			elsif username_exists(new_name)
				puts colorize(t("account.exists"), :red)
			else
				sucess = True
			end
		end
		remove_user(current_user.name)
		save_user(new_name, current_user.password, current_user.key, current_user.secret)
		return new_name
		#except:
		#	puts Terminal.colorize("An error occurred while saving your new username, sorry.", "B_RED")
		#	return ""
	end

	private

	def encrypt_password(password)
		Digest::SHA2.new << password
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
puts auth.t("help.description", {:app_name => app_name})
auth.create_user
