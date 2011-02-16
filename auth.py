#!/usr/bin/env python

import ConfigParser
import utils
import tweepy

class Auth:

	config = ConfigParser.RawConfigParser()

	def save_user(self, name, password, key, secret):
		if not self.username_exists(name):
			self.config.add_section(name)
			self.config.set(name, "password", password)
			self.config.set(name, "key", key)
			self.config.set(name, "secret", secret)
			with open('config.cfg', 'wb') as configfile:
				self.config.write(configfile)
				print utils.colorize('User saved successfully!', "GREEN")
		else:
			print utils.colorize("User name already exists!", "RED")
		
	def username_exists(self, name):
		return self.config.has_option(name, "key")

	def login(self, login_params):
		try:
			user = self.get_user(login_params[1])
			if user and user.password == login_params[2]:
				return user
			else:
				print utils.colorize('Username or password incorrect. Please try again.', "B_RED")
				return None
		except:
			print utils.colorize('An error ocurred. Please try again.', "RED")
			return None

	def get_user(self, username):
		if self.username_exists(username):
			user = User(username, self.config.get(username, "password"), self.config.get(username, "key"), self.config.get(username, "secret"))
			return user
		return None

	def create_user(self, auth):
		success = False
		while not success:
			print 'Type in your desired username'
			print '(type "\cancel" to cancel)'
			name = raw_input(' > ')
			if name == "\cancel":
				return False
			elif not self.username_exists(name):
				success = True
			elif " " in name:
				print utils.colorize("User name cannot contain any spaces.", "RED")
			else:
				print utils.colorize("User name already exists, please choose another.", "RED")
		auth = tweepy.OAuthHandler(utils.CONSUMER_KEY, utils.CONSUMER_SECRET)
		print utils.colorize('Retrieving authorization url from twitter.com, please wait.....', "YELLOW")
		auth_url = auth.get_authorization_url()
		print utils.colorize('You must now authorize access to your Twitter account.', "CYAN")
		print utils.colorize('Please go to this url and authorize access: ' + auth_url, "CYAN")
		print utils.colorize('After authorization paste the PIN provided by Twitter here:', "CYAN")
		verifier = raw_input('PIN: ').strip()
		print 'Now create a password for logging in your new ' + utils.app_name + ' account:'
		password = raw_input('Password: ')
		auth.get_access_token(verifier)
		key = auth.access_token.key.strip()
		secret = auth.access_token.secret.strip()
		#print "key: '" + key + "'"
		#print "secret: '" + secret + "'"
		self.save_user(name, password, key, secret)

	def __init__(self):
		self.config.readfp(open('config.cfg'))
		
class User:

	name = None
	password = None
	key = None
	secret = None
	
	def __init__(self, name, password, key, secret):
		self.name = name
		self.password = password
		self.key = key
		self.secret = secret
