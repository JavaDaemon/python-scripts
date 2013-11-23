#!/usr/bin/env python

"""
osrs_players.py:

Checks how many players is currently plaing OldSchool Runescape,
and logs the amount to a file "osrs_logs/osrs_player_log.txt".
The script does this continously, with 10 second intervals, until terminated.
"""
__author__      = "Mads Peter Horndrup"

import urllib.request
import re
import time
import datetime

def writeLine(fileName, line):
    f = open(fileName, "a")
    f.write(line+"\n")
    f.close()

if __name__ == '__main__':
    while (True):
        response = urllib.request.urlopen('http://oldschool.runescape.com/')
        html = response.read()

        result = re.search("There are currently (\d*) people playing!", html.decode("ascii"))
        now = datetime.datetime.now()

        line = result.group(1) + " " + now.strftime("%Y-%m-%d %H:%M:%S")
        writeLine("osrs_logs/osrs_player_log.txt", line)
        
        print(result.group(1), now.strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(10)

