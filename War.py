bigcounter = 0
interations = 0
avgmove = [0]
avgmean = 0
print('\033[1;36;80mHow many Iterations do you want to have?')
iterations=float(input('[]:'))

while (bigcounter) < (iterations):
  bigcounter+=1
  print(' /\_\\__               (_//')
  print('|   `>\-`     _._       //`)')
  print(' \ /` \\  _.-` :::`-._  //')
  print('  `    \|`    :::    `|/')
  print('        |     :::     |')
  print('        |.....:::.....|')
  print('        |:::::::::::::|')
  print('        |     :::     |')
  print('        \     :::     /')
  print('         \    :::    /')
  print("          `-. ::: .-' ")
  print('           //`:::`\\')
  print("          //   '   \\ ")
  print('         |/         \\\ \n ')
  print(" ░██╗░░░░░░░██╗░█████╗░██████╗░░")
  print(" ░██║░░██╗░░██║██╔══██╗██╔══██╗░")
  print(" ░╚██╗████╗██╔╝███████║██████╔╝░")
  print(" ░░████╔═████║░██╔══██║██╔══██╗░")
  print(" ░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║░")
  print(" ░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝░\n")
  
  
  import random
  import time
  print('\033[1;36;80mHow many secconds do you want to have between turns?')
  '''q=float(input('[]:'))'''
  q=0
  print('Do you want to start each turn manualy? y/n')
  '''b=input('[]: ')'''
  b="n"
  
  #Card values aka. tier of card
  card_values ={
    'One of clubs'   :1,
    'Two of clubs'   :2,
    'Three of clubs' :3,
    'Four of clubs'  :4,
    'Five of clubs'  :5,
    'Six of clubs'   :6,
    'Seven of clubs' :7,
    'Eight of clubs' :8,
    'Nine of clubs'  :9,
    'Ten of clubs'   :10,
    'Jack of clubs'  :11,
    'Queen of clubs' :12,
    'King of clubs'  :13,
    'Ace of clubs'   :14,
    'Black Joker'    :15,
    'One of spades ♠️'   :1,
    'Two of spades ♠️'   :2,
    'Three of spades ♠️' :3,
    'Four of spades ♠️'  :4,
    'Five of spades ♠️'  :5,
    'Six of spades ♠️'   :6,
    'Seven of spades ♠️' :7,
    'Eight of spades ♠️' :8,
    'Nine of spades ♠️'  :9,
    'Ten of spades ♠️'   :10,
    'Jack of spades ♠️'  :11,
    'Queen of spades ♠️' :12,
    'King of spades ♠️'  :13,
    'Ace of spades ♠️'   :14,
    'One of diamonds'   :1,
    'Two of diamonds'   :2,
    'Three of diamonds' :3,
    'Four of diamonds'  :4,
    'Five of diamonds'  :5,
    'Six of diamonds'   :6,
    'Seven of diamonds' :7,
    'Eight of diamonds' :8,
    'Nine of diamonds'  :9,
    'Ten of diamonds'   :10,
    'Jack of diamonds'  :11,
    'Queen of diamonds' :12,
    'King of diamonds'  :13,
    'Ace of diamonds'   :14,
    'One of hearts'   :1,
    'Two of hearts'   :2,
    'Three of hearts' :3,
    'Four of hearts'  :4,
    'Five of hearts'  :5,
    'Six of hearts'   :6,
    'Seven of hearts' :7,
    'Eight of hearts' :8,
    'Nine of hearts'  :9,
    'Ten of hearts'   :10,
    'Jack of hearts'  :11,
    'Queen of hearts' :12,
    'King of hearts'  :13,
    'Ace of hearts'   :14,
    'Red Joker'       :15,
  }
  #deck to be sorted into 2 hands
  
  deck=[('One of clubs'),('Two of clubs'),('Three of clubs'),("Four of clubs"),("Five of clubs"),("Six of clubs"),("Seven of clubs"),("Eight of clubs"),("Nine of clubs"),("Ten of clubs"),("Jack of clubs"),("Queen of clubs"),("King of clubs"),("Ace of clubs"),("Black Joker"),('One of diamonds'),('Two of diamonds'),('Three of diamonds'),("Four of diamonds"),("Five of diamonds"),("Six of diamonds"),("Seven of diamonds"),("Eight of diamonds"),("Nine of diamonds"),("Ten of diamonds"),("Jack of diamonds"),("Queen of diamonds"),("King of diamonds"),("Ace of diamonds"),('One of hearts'),('Two of hearts'),('Three of hearts'),("Four of hearts"),("Five of hearts"),("Six of hearts"),("Seven of hearts"),("Eight of hearts"),("Nine of hearts"),("Ten of hearts"),("Jack of hearts"),("Queen of hearts"),("King of hearts"),("Ace of hearts"),("Red Joker"),('One of spades ♠️'),('Two of spades ♠️'),('Three of spades ♠️'),("Four of spades ♠️"),("Five of spades ♠️"),("Six of spades ♠️"),("Seven of spades ♠️"),("Eight of spades ♠️"),("Nine of spades ♠️"),("Ten of spades ♠️"),("Jack of spades ♠️"),("Queen of spades ♠️"),("King of spades ♠️"),("Ace of spades ♠️"),]
  #Defining varribles / lists
  x=0
  you=[]
  opp=[]
  waryou=[]
  waropp=[]
  waryes= 0
  dis = 0
  moves = 0
  yes = "L"
  cardwon = 0
  cardlost = 0
  warwon = 0
  warlost = 0
  doyes = 0
  dono = 0
  #sorting mechanisem
  while len(deck) > 0:
   c1 = random.choice(deck)
   you.append(c1)
   deck.remove(c1)
   c2 = random.choice(deck)
   opp.append(c2)
   deck.remove(c2)
  #While you both have cards, game continues
  while len(you) > 0 and len(opp) > 0 :
    if b == 'y' or b == 'Y':
      n=input('[press ENTER to continue]: ')
    time.sleep(q)
    card1 = (random.choice(you))
    card2 = (random.choice(opp))
    print("\033[1;36;80m[] you draw a "+str(card1)+"!")
    print("[] opponent draws a "+str(card2)+"!")
    war1 = (card_values[(card1)])
    war2 = (card_values[(card2)])
    moves = int(moves) + 1
    #if you draw a higher card
    if (war1) > (war2) :
        you.append(str(card2))
        opp.remove(str(card2))
        cardwon = int(cardwon) + 1
        print('\033[1;33;92m[] You win!   your cards: '+str(len(you))+('    Opponents cards ')+str(len(opp)))
        print('\033[0;37;80mMove: '+str(moves))
        print("\033[0;37;80m--<{=|\_/\_/\_/\_/\_/\_/\_/\_/\_/|=}>--")
    #if opponent draws a higher card
    elif (war2) > (war1) :
        opp.append(str(card1))
        you.remove(str(card1))
        cardlost = int(cardlost) + 1
        print('\033[1;33;91m[] Opponent wins!   your cards: '+str(len(you))+('    Opponents cards ')+str(len(opp)))
        print('\033[0;37;80mMove: '+str(moves))
        print("\033[0;37;80m--<{=|\_/\_/\_/\_/\_/\_/\_/\_/\_/|=}>--")
    #if you tie
    elif (war1) == (war2) and len(you) > 3 and len(opp) > 3 :
        waryes=4
        dis = 4
        print('\033[1;33;80m[] War!')
        #draw 4 cards
        while int(waryes) > 0:
           card1 = (random.choice(you))
           card2 = (random.choice(opp))
           waryou.append(str(card1))
           you.remove(str(card1))
           waropp.append(str(card2))
           opp.remove(str(card2))
           waryes = int(waryes) - 1
        #pick random card from te four you just selected
        warwinyou = (random.choice(waryou))
        warwinopp = (random.choice(waropp))
        #if you win
        if (card_values[(warwinyou)]) > (card_values[(warwinopp)]):
          print('\033[1;33;92m[]You won the war with a '+str(warwinyou)+'!\n you recived:')
          warwon = int(warwon) + 1
          #adds all cards to your hand
          while dis > 0:
             card1 = (random.choice(waryou))
             card2 = (random.choice(waropp))
             you.append(str(card1))
             you.append(str(card2))
             waryou.remove(str(card1))
             waropp.remove(str(card2))
             dis = int(dis) - 1
             print('a '+(str(card1)))
             print('a '+(str(card2)))
             cardwon = int(cardwon) + 1
          print('your cards: '+str(len(you))+('    Opponents cards ')+str(len(opp)))
          print('\033[0;37;80mMove: '+str(moves))
          print("\033[0;37;80m--<{=|\_/\_/\_/\_/\_/\_/\_/\_/\_/|=}>--")
        #if opponent wins
        elif (card_values[(warwinyou)]) < (card_values[(warwinopp)]):
          print('\033[1;33;91m[]Opponent won the war with a '+str(warwinopp)+'!\n they recived:')
          warlost = int(warlost) + 1
          #adds all cards to their hand
          while dis > 0:
             card1 = (random.choice(waryou))
             card2 = (random.choice(waropp))
             opp.append(str(card1))
             opp.append(str(card2))
             waryou.remove(str(card1))
             waropp.remove(str(card2))
             dis = int(dis) - 1
             print('a '+(str(card1)))
             print('a '+(str(card2)))
             cardlost = int(cardlost) + 1
          print('your cards: '+str(len(you))+('    Opponents cards ')+str(len(opp)))
          print('\033[0;37;80mMove: '+str(moves))
          print("\033[0;37;80m--<{=|\_/\_/\_/\_/\_/\_/\_/\_/\_/|=}>--")
        #if card vales are equal
        elif (card_values[(warwinyou)]) == (card_values[(warwinopp)]):
          print('You tied the war! with a '+str(warwinyou)+'!\n you bothe keep your cards!')
          #puts cards back into your hand
          while dis > 0:
            card2 = (random.choice(waropp))
            opp.append(str(card2))
            waropp.remove(str(card2))
            card1 = (random.choice(waryou))
            you.append(str(card1))
            waryou.remove(str(card1))
            dis = int(dis) - 1
          print('your cards: '+str(len(you))+('    Opponents cards ')+str(len(opp)))
          print('\033[0;37;80mMove: '+str(moves))
          print("\033[0;37;80m--<{=|\_/\_/\_/\_/\_/\_/\_/\_/\_/|=}>--")
  #Win/lose statement
  print('\n\n')
  if len(you) == 0:
    print("██╗░░░██╗░█████╗░██╗░░░██╗  ██╗░░░░░░█████╗░░██████╗███████╗")
    print("╚██╗░██╔╝██╔══██╗██║░░░██║  ██║░░░░░██╔══██╗██╔════╝██╔════╝")
    print("░╚████╔╝░██║░░██║██║░░░██║  ██║░░░░░██║░░██║╚█████╗░█████╗░░")
    print("░░╚██╔╝░░██║░░██║██║░░░██║  ██║░░░░░██║░░██║░╚═══██╗██╔══╝░░")
    print("░░░██║░░░╚█████╔╝╚██████╔╝  ███████╗╚█████╔╝██████╔╝███████╗")
    print("░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚══════╝░╚════╝░╚═════╝░╚══════╝\n")
    moves3=int(moves)
    avgmove.append(int(moves3))
    dono=moves3*q
    print("Do you want to see your statistics? y/n")
    '''yes=input("[]: ")'''
    yes = "y"
    if str(yes) == "y" or str(yes) == ("Y") :
      print('\nNumber of moves: '+ str(moves))
      print('Total cards won: '+str(cardwon))
      print("Total cards lost: "+str(cardlost))
      print('Wars won: '+ str(warwon))
      print('Wars lost: '+str(warlost))
      print("Time between moves: "+str(q)+' secconds'); dono = (int(moves) * int(q))
      
      print('Game durration: '+str(dono))
      if str(b) == 'y' or str(b) == "Y":
        b= True
      else:
        b = False
      print('Type between moves: '+str(b))
    else: 
      print('')
      
  
  
  else:
    print("██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗██╗███╗░░██╗")
    print("╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██║████╗░██║")
    print("░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║██╔██╗██║")
    print("░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║██║╚████║")
    print("░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░██║██║░╚███║")
    print("░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝\n")
    moves3=int(moves)
    avgmove.append(int(moves3))
    print("Do you want to see your statistics? y/n")
    '''yes=input("[]: ")'''
    yes = "y"
    if str(yes) == "y" or str(yes) == ("Y") :
      print('\nNumber of moves: '+ str(moves))
      print('Total cards won: '+str(cardwon))
      print("Total cards lost: "+str(cardlost))
      print('Wars won: '+ str(warwon))
      print('Wars lost: '+str(warlost))
      print("Time between moves: "+str(q)+' secconds')
      print('Game durration: '+str(int(moves)*int(q)))
      if str(b) == 'y' or str(b) == "Y":
        b= True
      else:
        b = False
      print('Type between moves: '+str(b))
    else: 
      print('')
      
avgmean = sum(avgmove) / int(iterations)
print("")
print("The average number of moves it takes to win is "+str(avgmean)+" moves")