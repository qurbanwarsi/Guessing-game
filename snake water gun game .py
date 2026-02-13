
snake = 1
water = 0
gun = -1 

import random

while True :	
	computer = random.choice([1, 0, -1])
	
	you1 = input('Enter your choice ( snake (s)/ water (w)/ gun (g) ) :  ')
	
	dic = { 's' : 1 , 'w' : 0 , 'g' : -1 }
	
	if you1 not in dic:
		print('wronge choice')
		continue
	
	you = dic[you1]
	
	reversedic = { 1: 'snake', 0: 'water', -1 : 'gun'}
	print('computer choice: ', reversedic[computer])
	
	if(computer == you):
		print('it is draw')
	else:
		if(computer == 0 and you ==1):
			print('you win')
		elif(computer == -1 and you ==0 ):
			print('you win')
		elif(computer == 1 and you == -1):
			print('you win')
		else:
			print('you lose ')

	play_again= input('\nplay again(y/n):').lower()
	if play_again != 'y':
		print('\n\t\tgame over\n\t thank you for playing')
		break

	
		
	