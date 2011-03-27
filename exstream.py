#!/usr/bin/env python

import time
from getpass import getpass
from textwrap import TextWrapper
import utils

import tweepy


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
            #print self.status_wrapper.fill(status.text)
            #print '\n %s  %s  via %s\n' % (status.author.screen_name, status.created_at, status.source)
        except:
            # Catch any unicode errors while printing to console
            # and just ignore them to avoid breaking application.
            print 'error'

    def on_error(self, status_code):
        print 'An error has occured! Status code = %s' % status_code
        return True  # keep stream alive

    def on_timeout(self):
        print 'Snoozing Zzzzzz'

def main():
    # Prompt for login credentials and setup stream object
    username = 'rod_igo'
    password = '748596d1c'
    stream = tweepy.streaming.Stream(username, password, StreamWatcherListener(), timeout=None)
    stream.sample()

    if mode == 'filter':
        follow_list = raw_input('Users to follow (comma separated): ').strip()
        track_list = raw_input('Keywords to track (comma seperated): ').strip()
        if follow_list:
            follow_list = [u for u in follow_list.split(',')]
        else:
            follow_list = None
        if track_list:
            track_list = [k for k in track_list.split(',')]
        else:
            track_list = None

        stream.filter(follow_list, track_list)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print '\nGoodbye!'


