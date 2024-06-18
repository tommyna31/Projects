# -*- coding: utf-8 -*-
"""guesstheseasonalsong.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1A1qtxCCcdjAJaGiHSZ5AcvXDlasFaDIM
"""

import random

genres = ['1) Spring','2) Summer','3) Fall', '4) Winter']

user_points = 5
points_system = {'points':3}

SpringSongs = ['\n\tSun, sun, sun here it comes \n\t Sun, sun, sun here it comes \n\tSun, sun, sun here it comes', '\n\tThat maybe all I need \n\tIn darkness, she is all I see \n\tCome and rest your bones with me', '\n\tYoure so golden \n\tYoure so golden \n\tIm out of my head']
SummerSongs = ['\n\tWhen I met you in the summer \n\t To my heartbeats sound \n\tWe fell in love', '\n\tI hopped off the plane at LAX with a dream and my cardigan \n\tWelcome to the land of fame excess', '\n\tNow hes thinkin bout me every night, oh \n\tIs it that sweet?\n\tI guess so']
FallSongs = ['\n\tAnd it was called Yellow \n\tSo then I took my turn \n\tOh, what a thing to have done','\n\tCause its too cold \n\tFor you here\n\tAnd now, so let me hold','\n\tBut its over \n\tThen youre driving me home \n\tAnd it kinda comes out as I get up to go']
WinterSongs = ['\n\tI really cant stay ) \n\tBut Baby its cold outside \n\tIve got to go away \n\tbut Baby its cold outside', '\n\tSlow down you crazy child \n\tYoure so ambitious for a juvenile','\n\tI just want you for my own \n\tMore than you could ever know \n\tMake my wish come true']

SpringSongTitles = ['Here Comes The Sun','Sunday Morning','Golden']
SummerSongTitles = ['Summer','Party In The USA','Espresso']
FallSongTitles = ['Yellow','Sweater Weather','Ceilings']
WinterSongTitles = ['Baby, Its Cold Outside','Vienna','All I Want For Christmas Is You']


print("Hi, welcome to Guess The Song!\n\nThe objective of this game is to guess the song by having the song lyrics presented to you. \n\nDon’t worry, you can choose the genre you want from the list I've provided!\nPlus, you start off with 5 points. Cool right? \n\nHowever, if you keep getting the wrong answer, you'll lose a point each guess. So, try to get it right the first time!")

choices = ['yes', 'no']

active = True
while active:
  choices = input("\nWant to play? \nSay YES or NO. (You should say YES. Just saying.)\n")
  if choices == 'yes':
    genres = input(f"Okay! Which genre do you choose? \n\t1) Spring \n\t2) Summer \n\t3) Fall \n\t4) Winter\n")
    if genres == 'spring':
      random_Spring = random.randint(0,2)
      print(SpringSongs[random_Spring])
      while True:
        user_inputAnswer = input("Ok then, guess the song!")
        if user_inputAnswer == SpringSongTitles[random_Spring]:
          user_points += 3
          print(f"Good job! You get {points_system['points']} points. Your total points are {user_points}.")
          break

        else:
          user_points -= 1
          print(f"Hmm, try again. You lost a point, BOOOOO, so you now have {user_points} points.")

    elif genres == 'summer':
      random_Summer = random.randint(0,2)
      print(SummerSongs[random_Summer])
      while True:
        user_inputAnswer = input("Ok then, guess the song!")
        if user_inputAnswer == SummerSongTitles[random_Summer]:
          user_points += 3
          print(f"Good job! You get {points_system['points']} points. Your total points are {user_points}.")
          break

        else:
          user_points -= 1
          print(f"Hmm, try again. You lost a point, BOOOOO, so you now have {user_points} points.")

    elif genres == 'fall':
      random_Fall = random.randint(0,2)
      print(FallSongs[random_Fall])
      while True:
        user_inputAnswer = input("Ok then, guess the song!")
        if user_inputAnswer == FallSongTitles[random_Fall]:
          user_points += 3
          print(f"Good job! You get {points_system['points']} points. Your total points are {user_points}.")
          break

        else:
          user_points -= 1
          print(f"Hmm, try again. You lost a point, BOOOOO, so you now have {user_points} points.")

    elif genres == 'winter':
      random_Winter = random.randint(0,2)
      print(WinterSongs[random_Winter])
      while True:
        user_inputAnswer = input("Ok then, guess the song!")
        if user_inputAnswer == WinterSongTitles[random_Winter]:
          user_points += 3
          print(f"Good job! You get {points_system['points']} points. Your total points are {user_points}.")
          break

        else:
          user_points -= 1
          print(f"Hmm, try again. You lost a point, BOOOOO, so you now have {user_points} points.")

  elif choices == 'no':
    print("You're lame, see you next time!")
    active = False
  else:
    print("Invalid option.")