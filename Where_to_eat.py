#!/usr/bin/env python3
import sys,time,random


def typing(words):
	for char in words:
		time.sleep(random.uniform(0.2, 0.09))
		sys.stdout.write(char)
		sys.stdout.flush()

places =  ['Wendys','Checkers','Taco Bell','McDonalds','KFC','Chick-fil-A','BBQ','SubWay','Pizza']
#print(f"Here are your choices:\n{places}\n")
typing("Searching for a place to eat......\n")
whereToEat = random.choice(places)
typing("I found a place you might like.\n")
typing("How about...\n")
print("=====================================")
print(f"{whereToEat}?")
print("=====================================")
typing("Do you want to eat here or would you like me to pick something else? type 'yes' or 'no':\n")

decide = input()

if decide == 'yes':
	typing("Searching for another place to eat......\n")
	whereToEat = random.choice(places)
	typing("Okay you are eating...\n")
	print("=====================================")
	print(f"{whereToEat}?")
	print("=====================================")
	typing("bye!")
	time.sleep(2)
	sys.exit
elif decide == 'no':
	typing(f"enjoy {whereToEat}\n bye!")
	time.sleep(2)
	sys.exit()
else:
	print("I didn't understand your input\n I'm going to exit now\n bye!")
	time.sleep(2)
	sys.exit()
