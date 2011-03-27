#!/usr/bin/env python

import bash_utils
import utils
	
def help_user():
	print bash_utils.get_color("CYAN")
	print utils.app_name + " is a simple python app that lets you read your timeline and send tweets."
	print "There are currently 8 commands available:"
	print " - update: Send a tweet."
	print " - timeline: Fetches the latest 20 tweets from your timeline."
	print " - logout: Logs you out and lets you log in with a diferent account."
	print " - user (username): finds and displays information about a specific user. Also gets the last 20 tweets from the person."
	print " - edit name: Lets you edit your " + utils.app_name + " user name."
	print " - edit password: Lets you edit your " + utils.app_name + " password."
	print " - help: Displays this."
	print " - exit: Quit this application."
	print "\nPlease send any suggestions or bug reports to castro.digao@gmail.com or @rod_igo. Help me make this app better!" + bash_utils.get_color("NORMAL")
	
def help_guest():
	print bash_utils.get_color("CYAN")
	print utils.app_name + " is a simple python app that lets you read your timeline and send tweets."
	print "There are currently 4 commands available for you:"
	print " - login (username): login to your " + utils.app_name + " acount. You must specify your " + utils.app_name + " user name, not Twitter's."
	print " - create: Creates a new user. User then specifies a username, password and then go to twitter.com to authorize access to the Twitter account."
	print " - help: Displays this."
	print " - exit: Quit this application."
	print "\nPlease send any suggestions or bug reports to castro.digao@gmail.com or @rod_igo. Help me make this app better!" + bash_utils.get_color("NORMAL")
	
def header():
	print utils.colorize('Welcome to ' + utils.app_name + ' ' + utils.app_version + '.\nTo get the list of available commands, type "help".', "GREEN")
	print utils.colorize('Before continuing, you must log in with "login" or create a new account with "create".', "GREEN")

def header_user(username):
	print utils.colorize('Welcome, ' + username + '.\nTo get the list of available commands, type "help".', "GREEN")
	print utils.colorize('To see your timeline, use "timeline", and to send a tweet, use "update".', "GREEN")

def exit():
	print utils.colorize(utils.app_name + ' will now quit, bye.', "YELLOW")
