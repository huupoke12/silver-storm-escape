#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from sys import exit
import hashlib
from random import randint

print "Welcome, you are in my game."
print "This game made by Huupoke."
print "All you have to do to escape this house."
print "The house based on Sliver Storm's house."
print "You play the game by typing commands."
print "Good luck."
print "Use command \"where\" to know where you are and detail about it." 
print "\nSliver Storm's room"

# golbal variables
items = []
flags = []
place = 1
SS_room_1 = place
SS_room_2 = 2
third_floor_1 = 3
third_floor_2 = 4
game = 1
random_sample = randint(0,99)

while game==1:

	while place == 1:
		SS_door = False
		computer = False
		admin = False
		air = False
		place = 2

	while place == 2:
		print "\nWhat will you do?"
		cm = raw_input("> ").lower()
		if cm=="where":
			print "\nSliver Storm's room"
			print "\nYou are in the room which has a bed, a computer and an air-conditioner."
			if not SS_door:
				print "There is door which has been locked."
			else:
				print "The door has been opened."
			if 'Sliver Storm\'s key' in items:
				pass
			else:
				print "There is a key on the table."

		elif cm=="i" or cm=="item" or cm=="inventory":
			for item in items:
				print "\nYou have:"
				print "%s" %item

		elif cm=="turn on computer" or cm=="turn computer on" or cm=="open computer":
			computer = True
			print "You turned it on."
			if 'A piece of paper' in items and not admin:
				print "You filled the password."
				admin = True
			elif 'A piece of paper' not in items and not admin:
				print "However, the computer has been locked with account named \"Sliver Storm\"."
				print "And you don't know his password and there is no hint."
				computer = False
				print "You turned it off because there isn't anything you can do on it now."
			else:
				pass

			if admin and computer:
				print "You are logged as Sliver Storm (Administrator)."
				print "There is a file named \"password.txt\"."
				print "Will you open it?"
				op = raw_input("> ").lower()
				if op =="yes" or op =="open" or op=="open it" or op=="open the file":
					print "The file print:"
					print random_samole
					computer = False
					print "Ok, you got the password, you turned it off to save energy."
				else:
					print "You don't want to open the file? So, turn it off."
					computer = False
					print "You turned it off."
					

		elif cm=="turn off computer" or cm=="turn computer off":
			computer = False
			print "You turned it off."

		elif cm=="turn on air-conditioner" or cm=="turn air-conditioner on" or cm=="open air-conditioner":
			if 'air_remote' not in items:
				print "You can't turn it on."
				print "You need a remote control."
			else:
				air = True
				print "You turned it on."
				print "Sooooo cool!"
				if 'A piece of paper' not in items:
					print "WHAT, a piece of paper is fallling from it!"
					items.append('A piece of paper')
					print "You took the paper and read it."
					print "The computer's password is: *********"
					print "Ok, time to turn it off."
					air = False
				else:
					air = False
					print "Becase of saving energy, you turned it off."


		elif cm=="get key" or cm=="take key":
			if 'Sliver Storm\'s key' not in items:
				items.append('Sliver Storm\'s key')
				print "You took Sliver Storm's key."
			else:
				print "You have already taken the key."

		elif cm=="open door" or cm=="open the door":
			if 'Sliver Storm\'s key' in items:
				SS_door = True
				print "You opened the door."

			else:
				print "The door has been locked."

		elif cm=="go out" and not SS_door:
			print "The door has been locked."

		elif cm=="go out" and SS_door:
			if 'SS_room' not in flags:
				place = 3
				flags.append('SS_room')
				print "You have escaped from the room."
				print "That is too easy, right."
				print "But you have to go out of the house."
				print "\nYou went to third floor."
			else:
				place = 4
				print "\nThird floor"

		elif cm=="":
			pass
		else:
			print "Invaild command or you can't do it right now."




	while place == 3:
		insect = False
		place = 4

	while place == 4:
		print "\nWhat will you do?"
		cm = raw_input("> ").lower()
		if cm=="where":
			print "\nThird floor"








