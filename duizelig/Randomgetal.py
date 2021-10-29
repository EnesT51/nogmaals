from random import randint, randrange
game = True
kansen_10 = 10
while game:
        number = randint(1,1000)
        print(number)
        

        while kansen_10 >1:
            kansen_10 -=1
            print("je hebt nog" ,kansen_10,"kans!")
            raden =(input("raad het getal tussen 1 en de 1000 "))
            game = False
            

        
