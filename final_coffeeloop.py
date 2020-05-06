global milk
global water
global cups
global beans


milk = 540
water = 400
beans = 120
cups=9
money = 550


while True:
    print("Write action (buy, fill, take, remaining, exit):")
    choose = input()
    
    if choose == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        type =input()
        if type == "back":
         continue
        else:
          type1 = int(type)
          if water >= 250:
            water = water - 250
          else:
            print("Sorry, not enough water!")
            continue
       
          if beans >=16:
            beans = beans - 16
          else:
            print("Sorry, not enough coffee beans!")
            continue
          if cups >=1:
            cups = cups - 1
          else:
            print("Sorry, not enough cups!")
            continue
          
            milk = milk - 0
          money = money + 4
          print("I have enough resources, making you a coffee!")

         
       

        if type1 == 2:
            if water >= 350:
              water = water - 350
            else:
               print("Sorry, not enough water!")
               continue
            if milk >= 75:  
              milk = milk - 75
            else:
               print("Sorry, not enough milk!")
               continue
            if beans >=20:
              beans = beans - 20
            else:
               print("Sorry, not enough coffee beans!")
               continue
            if cups>= 1:
              cups = cups - 1
            else:
               print("Sorry, not enough cups!")
               continue
            money =  money + 7
        
            print("I have enough resources, making you a coffee!")

        if type1 == 3:
            if water >= 200:
              water = water - 200
            else:
               print("Sorry, not enough water!")
               continue
            if milk >= 100:  
              milk = milk - 100
            else:
               print("Sorry, not enough milk!")
               continue
            if beans >=12:
              beans = beans - 12
            else:
               print("Sorry, not enough coffee beans!")
               continue
            if cups>= 1:
              cups = cups - 1
            else:
               print("Sorry, not enough cups!")
               continue
            
            money =  money + 6
            print("I have enough resources, making you a coffee!")


    elif choose == "fill":
        print("Write how many ml of water do you want to add:")
        water1 = int(input())
        print("Write how many ml of milk do you want to add:")
        milk1 = int(input())
        print("Write how many grams of coffee beans do you want to add:")
        beans1 = int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        cups1 = int(input())
        water = water + water1
        milk = milk + milk1
        beans = beans + beans1
        cups = cups + cups1
       
    elif (choose =="take"):
       
        money = 0

    elif (choose =="remaining"):
        print("The coffee machine has:")
        print(water, "of water")
        print(milk, "of milk")
        print(beans, "of coffee beans")
        print(cups, "of disposable cups")
        print(money, " of money")

    elif(choose == "exit"):
      break
