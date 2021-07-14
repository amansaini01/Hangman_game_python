
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 19:07:43 2021

@author: Mr. Aman Saini
IIT Mandi
"""




import random
import time


name = input("What is Your Name - ")
print("Good Luck ! ", name)

play_again = 'y'

while ((play_again == 'y')):

    list_words = ['rainbow', 'computer', 'science', 'programming',
    		'python', 'mathematics', 'player', 'condition',
    		'reverse', 'water', 'board', 'geeks']
    
    random_index = random.randint(0,len(list_words))
    word = list_words[random_index]
    
    print("\nStarting the Game......")
    time.sleep(1)
    print("\nGuess the characters :)\n")
    
    guess = ''
    
    turns = 10
    
    while turns > 0:
    	
    	wrong = 0
    	
    	for char in word:
    		
    		if char in guess:
    			print(char, end = "")
    			
    		else:
    			print("*", end = "")
    			wrong += 1
    	print("")		
    
    	if wrong == 0:
            print("You Win")
            print("The word is: ", word)
            break
    	
    	guess_another = input("guess a character: ").lower()
    	guess += guess_another
    	
    	if guess_another not in word:
    		turns -= 1
    		print("You have", + turns, 'more guesses left..')
    		
    		if turns == 0:
    			print("\nSorry, You Lost\n")
            
    
    play_again = input("Wants to play another Game(y/n).. ")
    play_again.lower()
    if (play_again == 'n'):
        print("Closing the Game....")
        time.sleep(1)
            



