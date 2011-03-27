#!/usr/bin/env python

import tweepy
import os
import utils
from textwrap import TextWrapper

class StreamWatcherListener(tweepy.StreamListener):

	status_wrapper = TextWrapper(width=75, initial_indent='|  ', subsequent_indent='|  ', break_long_words=True, break_on_hyphens=True)
	
	def on_status(self, status):
		try:
			print "|" + "_"*78 + "|"
			print utils.add_symbol(utils.colorize(status.author.screen_name, "B_CYAN"), 90)
			for line in self.status_wrapper.wrap(status.text):
				print utils.add_symbol_end(line, 80)
			timestamp = utils.colorize("at " + status.created_at.strftime("%A, %d/%m/%y, %H:%M:%S") + " from " + status.source, "CYAN")
			print utils.add_symbol(timestamp, 90)
		except:
			print 'error'
			
	def on_error(self, status_code):
		print utils.colorize('An error has occurred! Status code = %s' % status_code, "B_RED")
	
	def on_timeout(self):
		print utils.colorize('Connection lost due to timeout.', "RED")
