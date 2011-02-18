#!/usr/bin/env python

import colors

CONSUMER_KEY = '9qKm6RmzrSnTJH5AG09g'
CONSUMER_SECRET = 'o7sPZgmVy7zxgwWMDqRstKn1Sp8UJX2dsJHfa6Mm7M'
app_name = 'Tweet Bash'

def split_tweet(tweet):
	words = tweet.split(" ")
	lines = []
	lines.append("")
	for word in words: 
		if (len(lines[len(lines) - 1]) + len(word) + 1) < 76:
				lines[len(lines) - 1] += " " + word
		else:
			lines[len(lines) - 1] = add_symbol(lines[len(lines) - 1], 80)
			lines.append("  " + word)
	lines[len(lines) - 1] = add_symbol(lines[len(lines) - 1], 80)
	return lines
	
def split_user_bio(bio):	
	words = bio.split(" ")
	lines = []
	lines.append("")
	for word in words: 
		if (len(lines[len(lines) - 1]) + len(word) + 1) < 76:
				lines[len(lines) - 1] += " " + word
		else:
			lines[len(lines) - 1] = add_symbol(colorize(lines[len(lines) - 1], "YELLOW"), 90)
			lines.append(" " + word)
	lines[len(lines) - 1] = add_symbol(colorize(lines[len(lines) - 1], "YELLOW"), 90)
	return lines

def add_symbol(line, line_size):
	line = "| " + line + " "*(line_size - len(line) - 3) + "|"
	return line
	
def colorize(text, color):
	return colors.get_color(color) + text + colors.get_color("NORMAL")
