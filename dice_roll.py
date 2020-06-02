leaveprogram =[]
count_of_rolls=0
sum=0
sum1=0
sum2=0
play1=input("player 1 enter your name:")
play2=input("player 2 enter your name:")
print("hello",play1,"and",play2,"lets play the dice rolling game")
while leaveprogram!= "q":

    print(play1,":enter your expected number from 1 to 6\n")
    player1=int(input())
    print(play2,":enter your expected number from 1 to 6\n")
    player2=int(input())
    import random    
    input()
    count_of_rolls+=1
    num=random.randint(1,6)
    sum=sum+num
    if num==1:
        print('''
                 [--------]
                 [        ]
                 [   0    ]
                 [        ]
                 [--------]''')
        print()
        
    if num==2:
        print('''
                 [--------]
                 [        ]
                 [ 0   0  ]
                 [        ]
                 [--------]''')
        print()
        
    if num==3:
        print('''
                 [--------]
                 [   0    ]
                 [        ]
                 [ 0   0  ]
                 [--------]''')
        print()
        
    if num==4:
        print('''
                 [--------]
                 [ 0   0  ]
                 [        ]
                 [ 0   0  ]
                 [--------]''')
        print()
        
    if  num==5:     
        print('''
                 [--------]
                 [ 0   0  ]
                 [   0    ]
                 [ 0   0  ]
                 [--------]''')
        print()
        
    if num==6:
        print('''
                  [--------]
                  [ 0 0 0  ]
                  [        ]
                  [ 0 0 0  ]
                  [--------]''')
        print()
        
    print("number of rolls = ",count_of_rolls)
    print("overall total score for all rolls = ",sum)
    if player1==num:
       sum1=sum1+num
       print(play1,",your current score is:",sum1)
    else:
      print(play1,",beter luck next time")
      print(play1,",your current score is:\n",sum1)
    if player2==num:
      sum2=sum2+num
      print(play2,",your current score is:",sum2)
    else:
      print(play2,",better luck next time")
      print(play2,",your current score is:\n",sum2)
    print("type q to leave the program or press enter to continue")
    leaveprogram=input()
    
print(play1,",your total score:",sum1)
print(play2,",your total score:",sum2)
if (sum1>sum2):
  print(paly1,"wins")
else:
  print(play2,"wins")
    
       
