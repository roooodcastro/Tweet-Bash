#!/usr/bin/env python

##
# Shortcuts for Colored Text ( Bright and FG Only )
##

colors = {
'NORMAL': '\033[m',
'RESET': '\033[0;37;00m',
'BLACK': '\033[0;30m',
'RED': '\033[0;31m',
'GREEN': '\033[0;32m',
'YELLOW': '\033[0;33m',
'BLUE': '\033[0;34m',
'VIOLET': '\033[0;35m',
'CYAN': '\033[0;36m',
'WHITE': '\033[0;37m',
'B_BLACK': '\033[1;30m',
'B_RED': '\033[1;31m',
'B_GREEN': '\033[1;32m',
'B_YELLOW': '\033[1;33m',
'B_BLUE': '\033[1;34m',
'B_VIOLET': '\033[1;35m',
'B_CYAN': '\033[1;36m',
'B_WHITE': '\033[1;37m',
}

def get_color(color):
	return colors[color]
