import random
a = random.randint(1 , 6)
while True:
    if(a == 1):
        
        print("[                    ]")
        print("[         • 	        ]")
        print("[                    ]")
        print("[                    ]")
        
    elif(a == 2):
        
        print("[                    ]")
        print("[       •     •      ]")
        print("[                    ]")
        print("[                    ]")
        
    elif(a == 3):
        print("[                    ]")
        print("[          •         ]")
        print("[      •       •     ]")
        print("[                    ]")
        
       
    elif(a == 4):
        print("[                    ]")
        print("[                    ]")
        print("[     •     •        ]")
        print("[     •     •        ]")
        print("[                    ]")
        
    elif(a == 5):
        print("[                    ]")
        print("[     •       •      ]")
        print("[         •          ]")
        print("[     •       •      ]")
        print("[                    ]")
        
    elif(a == 6):
        print("[                    ]")
        print("[      •       •     ]")
        print("[      •       •     ]")
        print("[      •       •     ]")
        print("[                    ]")
        
    
    temp = input("If you want to roll the dice again enter C or c : ")

    if(not temp == 'c' or not temp != 'C'):
        break
    else:
         a = random.randint(1 , 6) 
          
        
        