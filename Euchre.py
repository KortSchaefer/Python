import random
import time
'''test'''
#Card values aka. tier of card
card_values ={
  
  'Nine of clubs'  :9,
  'Ten of clubs'   :10,
  'Jack of clubs'  :11,
  'Queen of clubs' :12,
  'King of clubs'  :13,
  'Ace of clubs'   :14, 
  
  'Nine of spades ♠️'  :9,
  'Ten of spades ♠️'   :10,
  'Jack of spades ♠️'  :11,
  'Queen of spades ♠️' :12,
  'King of spades ♠️'  :13,
  'Ace of spades ♠️'   :14,
  
  'Nine of diamonds'  :9,
  'Ten of diamonds'   :10,
  'Jack of diamonds'  :11,
  'Queen of diamonds' :12,
  'King of diamonds'  :13,
  'Ace of diamonds'   :14,
  
  'Nine of hearts'  :9,
  'Ten of hearts'   :10,
  'Jack of hearts'  :11,
  'Queen of hearts' :12,
  'King of hearts'  :13,
  'Ace of hearts'   :14,
  
}
card_values_clubs ={
  
  'Nine of clubs'  :15,
  'Ten of clubs'   :16,
  'Jack of clubs'  :22,
  'Queen of clubs' :18,
  'King of clubs'  :19,
  'Ace of clubs'   :20,
  
  'Nine of spades ♠️'  :9,
  'Ten of spades ♠️'   :10,
  'Jack of spades ♠️'  :21,
  'Queen of spades ♠️' :12,
  'King of spades ♠️'  :13,
  'Ace of spades ♠️'   :14,
  
  'Nine of diamonds'  :9,
  'Ten of diamonds'   :10,
  'Jack of diamonds'  :11,
  'Queen of diamonds' :12,
  'King of diamonds'  :13,
  'Ace of diamonds'   :14,
  
  'Nine of hearts'  :9,
  'Ten of hearts'   :10,
  'Jack of hearts'  :11,
  'Queen of hearts' :12,
  'King of hearts'  :13,
  'Ace of hearts'   :14,
  
}
card_values_spades ={
  
  'Nine of clubs'  :9,
  'Ten of clubs'   :10,
  'Jack of clubs'  :21,
  'Queen of clubs' :12,
  'King of clubs'  :13,
  'Ace of clubs'   :14,
  
  'Nine of spades ♠️'  :15,
  'Ten of spades ♠️'   :16,
  'Jack of spades ♠️'  :22,
  'Queen of spades ♠️' :18,
  'King of spades ♠️'  :19,
  'Ace of spades ♠️'   :20,
  
  'Nine of diamonds'  :9,
  'Ten of diamonds'   :10,
  'Jack of diamonds'  :11,
  'Queen of diamonds' :12,
  'King of diamonds'  :13,
  'Ace of diamonds'   :14,
  
  'Nine of hearts'  :9,
  'Ten of hearts'   :10,
  'Jack of hearts'  :11,
  'Queen of hearts' :12,
  'King of hearts'  :13,
  'Ace of hearts'   :14,
  
}
card_values_diamonds ={
  
  'Nine of clubs'  :9,
  'Ten of clubs'   :10,
  'Jack of clubs'  :11,
  'Queen of clubs' :12,
  'King of clubs'  :13,
  'Ace of clubs'   :14,
  
  'Nine of spades ♠️'  :9,
  'Ten of spades ♠️'   :10,
  'Jack of spades ♠️'  :11,
  'Queen of spades ♠️' :12,
  'King of spades ♠️'  :13,
  'Ace of spades ♠️'   :14,
  
  'Nine of diamonds'  :15,
  'Ten of diamonds'   :16,
  'Jack of diamonds'  :22,
  'Queen of diamonds' :18,
  'King of diamonds'  :19,
  'Ace of diamonds'   :20,
  
  'Nine of hearts'  :9,
  'Ten of hearts'   :10,
  'Jack of hearts'  :21,
  'Queen of hearts' :12,
  'King of hearts'  :13,
  'Ace of hearts'   :14,
  
}
card_values_hearts ={
  
  'Nine of clubs'  :9,
  'Ten of clubs'   :10,
  'Jack of clubs'  :11,
  'Queen of clubs' :12,
  'King of clubs'  :13,
  'Ace of clubs'   :14,
  
  'Nine of spades ♠️'  :9,
  'Ten of spades ♠️'   :10,
  'Jack of spades ♠️'  :11,
  'Queen of spades ♠️' :12,
  'King of spades ♠️'  :13,
  'Ace of spades ♠️'   :14,
  
  'Nine of diamonds'  :9,
  'Ten of diamonds'   :10,
  'Jack of diamonds'  :21,
  'Queen of diamonds' :12,
  'King of diamonds'  :13,
  'Ace of diamonds'   :14,
  
  'Nine of hearts'  :15,
  'Ten of hearts'   :16,
  'Jack of hearts'  :22,
  'Queen of hearts' :17,
  'King of hearts'  :18,
  'Ace of hearts'   :19,
  
}
card_values_clubs_spades ={
  
  'Nine of clubs'  :15,
  'Ten of clubs'   :16,
  'Jack of clubs'  :30,
  'Queen of clubs' :17,
  'King of clubs'  :18,
  'Ace of clubs'   :19,
  
  'Nine of spades ♠️'  :20,
  'Ten of spades ♠️'   :21,
  'Jack of spades ♠️'  :31,
  'Queen of spades ♠️' :22,
  'King of spades ♠️'  :23,
  'Ace of spades ♠️'   :25,
  
  'Nine of diamonds'  :9,
  'Ten of diamonds'   :10,
  'Jack of diamonds'  :11,
  'Queen of diamonds' :12,
  'King of diamonds'  :13,
  'Ace of diamonds'   :14,
  
  'Nine of hearts'  :9,
  'Ten of hearts'   :10,
  'Jack of hearts'  :11,
  'Queen of hearts' :12,
  'King of hearts'  :13,
  'Ace of hearts'   :14,
  
}
card_values_clubs_diamonds ={
  
  'Nine of clubs'  :15,
  'Ten of clubs'   :16,
  'Jack of clubs'  :17,
  'Queen of clubs' :18,
  'King of clubs'  :19,
  'Ace of clubs'   :20,
  
  'Nine of spades ♠️'  :9,
  'Ten of spades ♠️'   :10,
  'Jack of spades ♠️'  :11,
  'Queen of spades ♠️' :12,
  'King of spades ♠️'  :13,
  'Ace of spades ♠️'   :14,
  
  'Nine of diamonds'  :21,
  'Ten of diamonds'   :22,
  'Jack of diamonds'  :33,
  'Queen of diamonds' :23,
  'King of diamonds'  :24,
  'Ace of diamonds'   :25,
  
  'Nine of hearts'  :9,
  'Ten of hearts'   :10,
  'Jack of hearts'  :30,
  'Queen of hearts' :12,
  'King of hearts'  :13,
  'Ace of hearts'   :14,
  
}
card_values_clubs_hearts ={
  
  'Nine of clubs'  :15,
  'Ten of clubs'   :16,
  'Jack of clubs'  :17,
  'Queen of clubs' :18,
  'King of clubs'  :19,
  'Ace of clubs'   :20,
  
  'Nine of spades ♠️'  :9,
  'Ten of spades ♠️'   :10,
  'Jack of spades ♠️'  :11,
  'Queen of spades ♠️' :12,
  'King of spades ♠️'  :13,
  'Ace of spades ♠️'   :14,
  
  'Nine of diamonds'  :9,
  'Ten of diamonds'   :10,
  'Jack of diamonds'  :30,
  'Queen of diamonds' :12,
  'King of diamonds'  :13,
  'Ace of diamonds'   :14,
  
  'Nine of hearts'  :21,
  'Ten of hearts'   :22,
  'Jack of hearts'  :33,
  'Queen of hearts' :23,
  'King of hearts'  :24,
  'Ace of hearts'   :25,
  
}
card_values_spades_clubs ={
  
  'Nine of clubs'  :21,
  'Ten of clubs'   :22,
  'Jack of clubs'  :33,
  'Queen of clubs' :23,
  'King of clubs'  :24,
  'Ace of clubs'   :25,
  
  'Nine of spades ♠️'  :15,
  'Ten of spades ♠️'   :16,
  'Jack of spades ♠️'  :30,
  'Queen of spades ♠️' :17,
  'King of spades ♠️'  :18,
  'Ace of spades ♠️'   :19,
  
  'Nine of diamonds'  :9,
  'Ten of diamonds'   :10,
  'Jack of diamonds'  :11,
  'Queen of diamonds' :12,
  'King of diamonds'  :13,
  'Ace of diamonds'   :14,
  
  'Nine of hearts'  :9,
  'Ten of hearts'   :10,
  'Jack of hearts'  :11,
  'Queen of hearts' :12,
  'King of hearts'  :13,
  'Ace of hearts'   :14,
  
}
card_values_spades_diamonds ={
  
  'Nine of clubs'  :9,
  'Ten of clubs'   :10,
  'Jack of clubs'  :11,
  'Queen of clubs' :12,
  'King of clubs'  :13,
  'Ace of clubs'   :14,
  
  'Nine of spades ♠️'  :15,
  'Ten of spades ♠️'   :16,
  'Jack of spades ♠️'  :30,
  'Queen of spades ♠️' :18,
  'King of spades ♠️'  :19,
  'Ace of spades ♠️'   :20,
  
  'Nine of diamonds'  :21,
  'Ten of diamonds'   :22,
  'Jack of diamonds'  :33,
  'Queen of diamonds' :23,
  'King of diamonds'  :24,
  'Ace of diamonds'   :25,
  
  'Nine of hearts'  :9,
  'Ten of hearts'   :10,
  'Jack of hearts'  :30,
  'Queen of hearts' :12,
  'King of hearts'  :13,
  'Ace of hearts'   :14,
  
}
card_values_spades_hearts ={
  
  'Nine of clubs'  :9,
  'Ten of clubs'   :10,
  'Jack of clubs'  :11,
  'Queen of clubs' :12,
  'King of clubs'  :13,
  'Ace of clubs'   :14,
  
  'Nine of spades ♠️'  :15,
  'Ten of spades ♠️'   :16,
  'Jack of spades ♠️'  :30,
  'Queen of spades ♠️' :18,
  'King of spades ♠️'  :19,
  'Ace of spades ♠️'   :20,
  
  'Nine of diamonds'  :9,
  'Ten of diamonds'   :9,
  'Jack of diamonds'  :30,
  'Queen of diamonds' :9,
  'King of diamonds'  :9,
  'Ace of diamonds'   :9,
  
  'Nine of hearts'  :21,
  'Ten of hearts'   :22,
  'Jack of hearts'  :33,
  'Queen of hearts' :23,
  'King of hearts'  :24,
  'Ace of hearts'   :25,
  
}
card_values_diamonds_clubs ={
  
  'Nine of clubs'  :21,
  'Ten of clubs'   :22,
  'Jack of clubs'  :33,
  'Queen of clubs' :23,
  'King of clubs'  :24,
  'Ace of clubs'   :25,
  
  'Nine of spades ♠️'  :9,
  'Ten of spades ♠️'   :10,
  'Jack of spades ♠️'  :30,
  'Queen of spades ♠️' :11,
  'King of spades ♠️'  :12,
  'Ace of spades ♠️'   :13,
  
  'Nine of diamonds'  :15,
  'Ten of diamonds'   :16,
  'Jack of diamonds'  :17,
  'Queen of diamonds' :18,
  'King of diamonds'  :19,
  'Ace of diamonds'   :20,
  
  'Nine of hearts'  :9,
  'Ten of hearts'   :10,
  'Jack of hearts'  :30,
  'Queen of hearts' :12,
  'King of hearts'  :13,
  'Ace of hearts'   :14,
  
}
card_values_diamonds_spades ={
  
  'Nine of clubs'  :10,
  'Ten of clubs'   :11,
  'Jack of clubs'  :30,
  'Queen of clubs' :12,
  'King of clubs'  :13,
  'Ace of clubs'   :14,
  
  'Nine of spades ♠️'  :21,
  'Ten of spades ♠️'   :22,
  'Jack of spades ♠️'  :32,
  'Queen of spades ♠️' :23,
  'King of spades ♠️'  :24,
  'Ace of spades ♠️'   :25,
  
  'Nine of diamonds'  :15,
  'Ten of diamonds'   :16,
  'Jack of diamonds'  :17,
  'Queen of diamonds' :18,
  'King of diamonds'  :19,
  'Ace of diamonds'   :20,
  
  'Nine of hearts'  :9,
  'Ten of hearts'   :10,
  'Jack of hearts'  :30,
  'Queen of hearts' :12,
  'King of hearts'  :13,
  'Ace of hearts'   :14,
  
}
card_values_diamonds_hearts ={
  
  'Nine of clubs'  :9,
  'Ten of clubs'   :9,
  'Jack of clubs'  :9,
  'Queen of clubs' :9,
  'King of clubs'  :9,
  'Ace of clubs'   :9,
  
  'Nine of spades ♠️'  :9,
  'Ten of spades ♠️'   :10,
  'Jack of spades ♠️'  :30,
  'Queen of spades ♠️' :11,
  'King of spades ♠️'  :12,
  'Ace of spades ♠️'   :13,
  
  'Nine of diamonds'  :15,
  'Ten of diamonds'   :16,
  'Jack of diamonds'  :30,
  'Queen of diamonds' :18,
  'King of diamonds'  :19,
  'Ace of diamonds'   :20,
  
  'Nine of hearts'  :21,
  'Ten of hearts'   :22,
  'Jack of hearts'  :33,
  'Queen of hearts' :23,
  'King of hearts'  :24,
  'Ace of hearts'   :25,
  
}
card_values_hearts_clubs ={
  
  'Nine of clubs'  :21,
  'Ten of clubs'   :22,
  'Jack of clubs'  :33,
  'Queen of clubs' :23,
  'King of clubs'  :24,
  'Ace of clubs'   :25,
  
  'Nine of spades ♠️'  :9,
  'Ten of spades ♠️'   :10,
  'Jack of spades ♠️'  :30,
  'Queen of spades ♠️' :11,
  'King of spades ♠️'  :12,
  'Ace of spades ♠️'   :13,
  
  'Nine of diamonds'  :9,
  'Ten of diamonds'   :10,
  'Jack of diamonds'  :11,
  'Queen of diamonds' :12,
  'King of diamonds'  :13,
  'Ace of diamonds'   :14,
  
  'Nine of hearts'  :15,
  'Ten of hearts'   :16,
  'Jack of hearts'  :17,
  'Queen of hearts' :18,
  'King of hearts'  :19,
  'Ace of hearts'   :20,
  
}
card_values_hearts_spades ={
  
  'Nine of clubs'  :9,
  'Ten of clubs'   :10,
  'Jack of clubs'  :30,
  'Queen of clubs' :12,
  'King of clubs'  :13,
  'Ace of clubs'   :14,
  
  'Nine of spades ♠️'  :21,
  'Ten of spades ♠️'   :22,
  'Jack of spades ♠️'  :33,
  'Queen of spades ♠️' :24,
  'King of spades ♠️'  :25,
  'Ace of spades ♠️'   :26,
  
  'Nine of diamonds'  :9,
  'Ten of diamonds'   :10,
  'Jack of diamonds'  :11,
  'Queen of diamonds' :12,
  'King of diamonds'  :13,
  'Ace of diamonds'   :14,
  
  'Nine of hearts'  :15,
  'Ten of hearts'   :16,
  'Jack of hearts'  :17,
  'Queen of hearts' :18,
  'King of hearts'  :19,
  'Ace of hearts'   :20,
  
}
card_values_hearts_diamonds ={
  
  'Nine of clubs'  :9,
  'Ten of clubs'   :10,
  'Jack of clubs'  :11,
  'Queen of clubs' :12,
  'King of clubs'  :13,
  'Ace of clubs'   :14,
  
  'Nine of spades ♠️'  :9,
  'Ten of spades ♠️'   :10,
  'Jack of spades ♠️'  :11,
  'Queen of spades ♠️' :11,
  'King of spades ♠️'  :12,
  'Ace of spades ♠️'   :13,
  
  'Nine of diamonds'  :20,
  'Ten of diamonds'   :21,
  'Jack of diamonds'  :33,
  'Queen of diamonds' :23,
  'King of diamonds'  :24,
  'Ace of diamonds'   :25,
  
  'Nine of hearts'  :15,
  'Ten of hearts'   :16,
  'Jack of hearts'  :30,
  'Queen of hearts' :18,
  'King of hearts'  :19,
  'Ace of hearts'   :20,
  
}


#deck to be sorted into 2 hands

deck=[("Nine of clubs"),("Ten of clubs"),("Jack of clubs"),("Queen of clubs"),("King of clubs"),("Ace of clubs"),("Nine of diamonds"),("Ten of diamonds"),("Jack of diamonds"),("Queen of diamonds"),("King of diamonds"),("Ace of diamonds"),("Nine of hearts"),("Ten of hearts"),("Jack of hearts"),("Queen of hearts"),("King of hearts"),("Ace of hearts"),("Nine of spades ♠️"),("Ten of spades ♠️"),("Jack of spades ♠️"),("Queen of spades ♠️"),("King of spades ♠️"),("Ace of spades ♠️"),]
#Defining varribles / lists
x=0
you=[]
opp=[]
you2=[]
opp2=[]
blind=[]
dis = 0
call = 0
opp_draw=()
opp2_draw=()
you_draw=()
you2_draw=()
trumpsuit=()


for x in range(4):
  c5 = random.choice(deck)
  blind.append(c5)

#shuffle
while len(deck) > 0:
 c1 = random.choice(deck)
 you.append(c1)
 deck.remove(c1)
 c2 = random.choice(deck)
 opp.append(c2)
 deck.remove(c2)
 c3 = random.choice(deck)
 you2.append(c3)
 deck.remove(c3)
 c4 = random.choice(deck)
 opp2.append(c4)
 deck.remove(c4)




print('You have the first deal, and your cards are:')
print(you[0]+'\n'+you[1]+'\n'+you[2]+'\n'+you[3]+'\n'+you[4]+'\n')

blind_up= random.choice(blind)
print('The cards are dealt, and a '+blind_up+' is turned up\n')
if 'clubs' in (blind_up):
  trump = (card_values_clubs)
elif 'hearts' in (blind_up):
  trump = (card_values_hearts)
elif 'spades' in (blind_up):
  trump = (card_values_spades)
elif 'diamonds' in (blind_up):
  trump = (card_values_diamonds)


opp_hand = trump[opp[0]]+trump[opp[1]]+trump[opp[2]]+trump[opp[3]]+trump[opp[4]]

opp2_hand = trump[opp2[0]]+trump[opp2[1]]+trump[opp2[2]]+trump[opp2[3]]+trump[opp2[4]]

you2_hand = trump[you2[0]]+trump[you2[1]]+trump[you2[2]]+trump[you2[3]]+trump[you2[4]]

if opp_hand > 80:
  call = 1
  print(' Sparky, your opponent, ordered you up!')
elif you2_hand > 80:
  call = 2
  print(' Bobby, your teamate, ordered you up!')
elif opp2_hand > 80:
  call = 3
  print(' S-money, your opponent, ordered you up!')
else:
  print('Everyone else passed, its up to you\n')
  print('Pick it up? y/n')
  pickup = input('[]: ')
  if pickup == 'y' or pickup == 'Y':
    call = 4
    print('You picked it up\n')
  else:
    print("Okay! it's going back around\n")
    print('it came back to you, do you want to make it? y/n')
    cont1 = input('[]:')
    if cont1 == 'y' or cont1 == 'Y':
      print('What do you want to make it? keep it lowercase')
      trumpyou = input('[]: ')
      if trumpyou == 'spades':
       trump = card_values_spades
       trumpsuit = 'spades'
      elif trumpyou == 'clubs':
       trump = card_values_clubs
       trumpsuit = 'clubs'
      elif trumpyou == 'diamonds':
       trump = card_values_diamonds
       trumpsuit = 'diamonds'
      elif trumpyou == 'hearts':
       trump = card_values_hearts
       trumpsuit = 'hearts'
      else:
        print('Please enter a valid card suit.')
      print('Okay, '+str(trumpyou)+' is trump')

opp_draw = random.choice(opp)
opp.remove(opp_draw)
opp2_draw = random.choice(opp2)
opp2.remove(opp2_draw)
you2_draw = random.choice(you2)
you2.remove(you2_draw)

if 'diamonds' in opp_draw and trump is card_values_clubs:
  trump= card_values_diamonds_clubs
elif 'diamonds' in opp_draw and trump is card_values_spades:
  trump= card_values_diamonds_spades
elif 'diamonds' in opp_draw and trump is card_values_hearts:
  trump= card_values_diamonds_hearts
elif 'clubs' in opp_draw and trump is card_values_spades:
  trump= card_values_clubs_spades
elif 'clubs' in opp_draw and trump is card_values_diamonds:
  trump= card_values_clubs_diamonds
elif 'clubs' in opp_draw and trump is card_values_hearts:
  trump= card_values_clubs_hearts
elif 'spades' in opp_draw and trump is card_values_clubs:
  trump= card_values_spades_clubs
elif 'spades' in opp_draw and trump is card_values_hearts:
  trump= card_values_spades_hearts
elif 'spades' in opp_draw and trump is card_values_diamonds:
  trump= card_values_spades_diamonds
elif 'hearts' in opp_draw and trump is card_values_spades:
  trump= card_values_hearts_spades
elif 'hearts' in opp_draw and trump is card_values_clubs:
  trump= card_values_hearts_clubs
elif 'hearts' in opp_draw and trump is card_values_spades:
  trump= card_values_hearts_spades







print('\nYour opponent draws a '+opp_draw)
time.sleep(1)
print('\nYour patner draws a '+you2_draw)
time.sleep(1)
print('\nYour other opponent draws a '+opp2_draw)
print('\nNow its your turn. Pick one of your cards by entering their number in the list. ex. 2 for the seccond card')
choice=int(input('[]: '))
xxyy=int(choice-1)
you_draw = you[int(xxyy)]
print('You draw a '+you_draw)

if trump[opp_draw] < trump[you_draw] and trump[opp_draw] < trump[opp2_draw] and trump[opp_draw] < trump[you2_draw]:
  print('opponent wins')
if trump[opp2_draw] < trump[you_draw] and trump[opp2_draw] < trump[opp_draw] and trump[opp2_draw] < trump[you2_draw]:
  print('opponent 2 wins')
if trump[you2_draw] < trump[you_draw] and trump[you2_draw] < trump[opp2_draw] and trump[you2_draw] < trump[opp_draw]:
  print('your patner wins')
if trump[you_draw] < trump[opp_draw] and trump[you_draw] < trump[opp2_draw] and trump[you_draw] < trump[you2_draw]:
  print('you win')
print(trump)

if call == (1,2,3,4):
  print()
