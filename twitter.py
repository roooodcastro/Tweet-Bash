#!/usr/bin/env python

import tweepy
import os
import colors
import utils
import auth
import print_text
from datetime import datetime
from time import strftime
from auth import Auth

class Twitter:

	logged_in = False
	user = None
	display_name = ">"
	api = None
	auth = tweepy.OAuthHandler(utils.CONSUMER_KEY, utils.CONSUMER_SECRET)
	user_auth = Auth()

	def update(self):
		success = False
		print utils.colorize( 'What\'s happening?\n (type "\cancel" to cancel)' + ' '*(99) + '140char limit -->|', "YELLOW")
		while not success:
			message = raw_input('  > ')
			if message == '\cancel':
				return success
			elif len(message) <= 140 and len(message) > 0:
				self.api.update_status(message)
				print utils.colorize('Tweet sent succefully!', "GREEN")
				success = True
			elif len(message) > 140:
				print utils.colorize('Your message had ' + str(len(message)) + ' characteres, please reduce it to a maximum of 140 and try again.', "RED")
			elif len(message) == 0:
				print utils.colorize('You must say something!', "RED")
			
	def clear(self):
		os.system("clear")

	def get_timeline(self):
		print utils.colorize("Fetching latests tweets, please wait.....", "YELLOW")
		statuses = self.api.home_timeline(count=20)
		statuses = reversed(statuses)
		print "Twitter timeline: last updated at " + datetime.now().strftime("%A, %d/%m/%Y %I:%M%p")
		for status in statuses:
			self.print_status(status)
		print "|" + "_"*78 + "|"
		
	def get_user(self, user_input):
		try:
			name = user_input.split(' ')[1]
			print "Loading user....."
			user = self.api.get_user(name)
			print "|" + "_"*78 + "|"
			print utils.add_symbol(utils.colorize(user.name, "B_YELLOW"), 90)
			print "|" + " "*78 + "|"
			print utils.add_symbol(utils.colorize(" Location: " +user.location, "YELLOW"), 90)
			lines = utils.split_user_bio("Bio: " + user.description)
			for line in lines:
				print line
			print "|" + " "*78 + "|"
			print utils.add_symbol(utils.colorize(" " + str(user.statuses_count) + " tweets", "YELLOW"), 90)
			print utils.add_symbol(utils.colorize(" Followers: " + str(user.followers_count), "YELLOW"), 90)
			print utils.add_symbol(utils.colorize(" Following: " + str(user.friends_count), "YELLOW"), 90)
			print utils.add_symbol(utils.colorize(" " + str(user.favourites_count) + " tweets favorited", "YELLOW"), 90)
			print "|" + "_"*78 + "|"
			print utils.add_symbol("Loading tweets.....", 80)
			statuses = self.api.user_timeline(screen_name=name, count=20)
			print utils.add_symbol("User tweets: last updated at " + datetime.now().strftime("%A, %d/%m/%Y %I:%M%p"), 80)
			for status in statuses:
				self.print_status(status)
			print "|" + "_"*78 + "|"
		except:
			print utils.colorize('User not found', "RED")

	def print_status(self, status):
		print "|" + "_"*78 + "|"
		print utils.add_symbol(utils.colorize(status.author.screen_name, "B_CYAN"), 90)
		lines = utils.split_tweet(status.text)
		for line in lines:
			print line
		timestamp = utils.colorize("at " + status.created_at.strftime("%A, %d/%m/%y, %H:%M:%S") + " from " + status.source, "CYAN")
		print utils.add_symbol(timestamp, 90)
				
	def complete_login(self):
		self.logged_in = True
		self.auth.set_access_token(self.user.key, self.user.secret)
		self.api = tweepy.API(self.auth)
		self.display_name = self.user.name + " "
		os.system('reset')
		print_text.header_user(self.user.name)
		print utils.colorize("You have successfully logged in!", "GREEN")
		
	def try_login(self, login_string):
		params = login_string.split(" ")
		if len(params) == 3:
			self.user = self.user_auth.login(params)
			if self.user:
				self.complete_login()
		elif params[0] == 'login':
			print utils.colorize('Command syntax incorrect. Please refer to "help" to see the correct syntax.', "B_RED")
		else:
			print utils.colorize('The command "' + login_string + '" was not recognized.', "B_RED")

	def logout(self):
		print utils.colorize('Logging out of ' + self.user.name + '. You can log in to a diferent account now.', "YELLOW")
		self.logged_in = False
		self.user = None
		self.display_name = ">"
		self.api = None
		self.auth = tweepy.OAuthHandler(utils.CONSUMER_KEY, utils.CONSUMER_SECRET)

	def parse_commands(self):
		try:
			while True:
				user_input = raw_input(self.display_name + '> ')
				if len(user_input.strip()) == 0:
					print utils.colorize("Type in a command!", "RED")
				elif user_input == 'exit':
					print_text.exit()
					return
				elif self.logged_in:
					if user_input == 'help':
						print_text.help_user()
					elif user_input == 'update':
						self.update()
					elif user_input == 'timeline':
						self.get_timeline()
					elif user_input == 'logout':
						self.logout()
					elif 'user' in user_input:
						self.get_user(user_input)
					else:
						print utils.colorize('The command "' + user_input + '" was not recognized.', "B_RED")
				else:
					if user_input == 'help':
						print_text.help_guest()
					elif 'login' in user_input:
						self.try_login(user_input)
					elif user_input == 'create':
						self.user_auth.create_user(self.auth)
					else:
						print utils.colorize('The command "' + user_input + '" was not recognized.', "B_RED")
		except KeyboardInterrupt:
			print ''
			print_text.exit()

	def __init__(self):
		os.system("reset")
		print_text.header()
		self.parse_commands()
		
	def __main__(self):
		Twitter().__init__

twitter = Twitter()
