#!/usr/bin/env python

import tweepy
from time import sleep
from auth import startAuth

#Authorize this application
api = startAuth()

#Get yourself's object
myself = api.me()

#This functions gets the people an user follows given his id
def getFollowing(userID):
	
	following = []
	for result in tweepy.cursor.Cursor(api.friends,id=userID).items():
		following = following + [result]
	return following

#This functions gets the people who follows an user given his id
def getFollowers(userID):
	
	following = []
	for result in tweepy.cursor.Cursor(api.followers,id=userID).items():
		following = following + [result]
	return following


#It checks differences between followings and followers	
def matchFollowers(user,otherUser=myself):
	
	#First user's followings
	print 'Getting',user.screen_name,'followings...'
	follo1 = getFollowing(user.id)
	
	#Then otherUser's followers
	print 'Getting',otherUser.screen_name,'followers...'
	follo2 = getFollowers(otherUser.id)
	
	common = []
	unCommon = []
	
	print 'Ckecking lists...'
	
	#Common followers/following
	for f1 in follo1:
		ID1 = f1.id
		for f2 in follo2:
			ID2 = f2.id
			if ID1==ID2:
				common = common + [f1]
				break #Only one follower can match
	
	#Uncommon followers/following
	for f in follo1:
		if f not in common:
			unCommon = unCommon + [f]
	
	return [common,unCommon]


#It simple defollows an user
def defollow(user):
	api.destroy_friendship(user.id)
	return
	

def checkMatch():
	print 'Wait for followers/following scan \n'
	matches = matchFollowers(myself)
	
	goodList = []
	badList = []
	
	for match in matches[0]:
		goodList += [match.screen_name]
	
	for match in matches[1]:
		badList += [match.screen_name]
	
	
	print '\n'
	print 'These are',myself.screen_name,"'s followings who followback \n"
	for i in goodList:
		print i
	
	print '\n'
	print 'These are',myself.screen_name,"'s followings who don't followback \n"
	for i in badList:
		print i
	
	for i in matches[1]:
		print ''
		print 'Do you want to defollow', i.screen_name,'?'
		print 'Type "d" to defollow, "x" to exit, any other to ignore'
		answer = raw_input()
		if answer == 'd':
			defollow(i)
			print i.screen_name,' has been defollowed \n'
		elif answer=='exit':
			break
		else:
			print 'Next... \n'
			
	print 'All operations done'			

def massDM():
	#It gets all your followers, first.
	print 'Searching followers...'
	x = getFollowers(myself.id)
	print 'You have '+str(len(x))+' followers'
	print 'Write your DM here (max 140 chars)'
	dmText = raw_input()
	if len(dmText) > 140:
		print 'You talk too much'
		print 'Write your DM again'
		dmText = raw_input()
		
	countSent = 0 #Sent DMs
	countUnsent = 0 #Unsent DMs
	
	#Sends 1 DM every second
	for follower in x:
		try:
			receiverID = follower.id
			api.send_direct_message(user_id=receiverID,text=dmText)
			countSent += 1
		except:
			countUnsent += 1 #If anyone unfollow you during the process
		sleep(1)
		
	print '\n'+str(countSent)+' DMs have been sent'
	print 'PythonBird could not send '+str(countUnsent)+' DMs\n'
	return
	
	
		
		
	

if __name__=="__main__":
	begin = 'R'
	print '\n'
	print '=================================================='
	print 'WELCOME TO PYTHONBIRD, A PYTHON-SHELL TWITTER TOOL'
	print '=================================================='
	print '\n'
	print 'Hello', myself.screen_name
	print '______________________________________________'
	while(begin is 'R'):
		print 'Do you want to unfollow (u) or mass-DM (m)?'
		answer = raw_input()
		while (not ((answer is 'u') or (answer is 'm'))):
			print 'Bad choice, try again: u = unfollow, m = mass-DM'
			answer = raw_input()
	
		if answer is 'u':
			checkMatch()
		elif answer is 'm':
			massDM()
		
		print 'Type R to restart, X to exit'
		begin = raw_input()

		
	
