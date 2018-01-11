# slashspeak

Requires python3, festival, beautifulsoup, urlopen

slashspeaklist.py 

This script reads Slashdot story titles into a list. If the title has not been seen, it reads it with festival. It checks for new stories every 6 minutes.

Added check for time of day. It only reads  stories betweeen 7am and 10pm. At 7am, it reads the stories from last night to catch up. 
