#!/usr/bin/env python

import ConfigParser
import utils
import tweepy
import getpass
import hashlib

class Auth:

	config = ConfigParser.RawConfigParser()

	def save_user(self, name, password, key, secret):
		if not self.username_exists(name):
			self.config.add_section(name)
			self.config.set(name, "password", self.encrypt_password(password))
			self.config.set(name, "key", key)
			self.config.set(name, "secret", secret)
			with open('config.cfg', 'wb') as configfile:
				self.config.write(configfile)
				print utils.colorize('User saved successfully!', "GREEN")
		else:
			print utils.colorize("User name already exists!", "RED")
			
	def remove_user(self, name):
		if self.username_exists(name):
			self.config.remove_section(name)
			with open('config.cfg', 'wb') as configfile:
				self.config.write(configfile)			
		
	def username_exists(self, name):
		return self.config.has_option(name, "key")

	def encrypt_password(self, password):
		return hashlib.sha224(password).hexdigest()

	def login(self, user_name):
		try:
			user = self.get_user(user_name)
			password = getpass.getpass('Password: ')
			if user and user.password == self.encrypt_password(password):
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
			else:
				print utils.colorize("User name already exists, please choose another.", "RED")					
			if ' ' in name:
				print utils.colorize("User name cannot contain any spaces.", "RED")
				sucess = False
		auth = tweepy.OAuthHandler(utils.CONSUMER_KEY, utils.CONSUMER_SECRET)
		print utils.colorize('Retrieving authorization url from twitter.com, please wait.....', "YELLOW")
		auth_url = auth.get_authorization_url()
		print utils.colorize('You must now authorize access to your Twitter account.', "CYAN")
		print utils.colorize('Please go to this url and authorize access: ' + auth_url, "CYAN")
		print utils.colorize('After authorization paste the PIN provided by Twitter here:', "CYAN")
		verifier = raw_input('PIN: ').strip()
		print 'Now create a password for logging in your new ' + utils.app_name + ' account:'
		password = getpass.getpass('Password: ')
		auth.get_access_token(verifier)
		key = auth.access_token.key.strip()
		secret = auth.access_token.secret.strip()
		self.save_user(name, password, key, secret)

	def edit_user_name(self, current_user):
		try:
			print 'Type in your new user name:'
			print '(type "\cancel" to cancel)'
			sucess = False
			while not sucess:
				new_name = raw_input('Username: ')
				if new_name == '\cancel':
					return ''
				elif ' ' in new_name:
					print utils.colorize("User name cannot contain any spaces.", "RED")
				elif len(new_name) == 0:
					print utils.colorize("User name cannot be empty!", "RED")
				elif self.username_exists(new_name):
					print utils.colorize("User name already exists.", "RED")
				else:
					sucess = True
			self.remove_user(current_user.name)
			self.save_user(new_name, current_user.password, current_user.key, current_user.secret)
			return new_name
		except:
			print utils.colorize('An error occurred while saving your new username, sorry.', "B_RED")
			return ''
			
	def edit_password(self, current_user):
		try:
			sucess = False
			while not sucess:		
				print 'Type in your new password:'
				print '(type "\cancel" to cancel)'
				password = getpass.getpass('Password: ')
				if password == '\cancel':
					return ''
				elif len(password) == 0:
					print utils.colorize("Password cannot be empty!", "RED")
				double_check = ''
				print 'Say your new password again:'
				double_check = getpass.getpass('Password: ')
				if not password == double_check:
					print utils.colorize("Passwords didn't match, please try again.", "RED")
				else:
					sucess = True
			self.remove_user(current_user.name)
			self.save_user(current_user.name, password, current_user.key, current_user.secret)
		except:
			print utils.colorize('An error occurred while saving your new password, sorry.', "B_RED")
			return ''
		

	def __init__(self):
		self.config.readfp(open('config.cfg', 'rb'))
		
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
