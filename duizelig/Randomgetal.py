from random import randint, randrange
game = True
kansen_10 = 10
while game:
        number = randint(1,1000)
        print(number)
        

        while kansen_10 >1:

            kansen_10 -=1
            raden = (input("raad het getal tussen 1 en de 1000, of als je wil stoppen type stop "))
            
            if raden == "stop":
                print("je hebt de game gestopt")
                game = False
                kansen_10 = 1

            elif int(raden) == number:
                print("je hebt de juiste antwoord geraden!!")
                
            
                
            else:
                print("je hebt het fout probeer nogmaals!")
                print("je hebt nog" ,kansen_10,"pogingen!")
            

            

        
