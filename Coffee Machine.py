# It requests the amounts of water, milk, and coffee beans available at the moment, and then asks for the number of cups a user needs.
import math
print('Write how many ml of water the coffee machine has:')
water = int(input())
print('Write how many ml of milk the coffee machine has:')
milk = int(input())
print('Write how many grams of coffee beans the coffee machine has:')
beans = int(input())
print('Write how many cups of coffee you will need:')
cups_need = int(input())
cups_water = water / 200
cups_milk = milk / 50 
cups_beans = beans / 15
extra = math.floor(min(cups_water - cups_need, cups_milk - cups_need, cups_beans - cups_need))
cups = math.floor(min(cups_water, cups_milk, cups_beans))
if cups == cups_need:
    print('Yes, I can make that amount of coffee')
elif cups > cups_need:
    print(f'Yes, I can make that amount of coffee (and even {extra} more than that)')
else:
    print(f'No, I can make only {cups} cups of coffee')

# It prints the coffee machine's state, processes one query from the user (buy, fill, take), and prints the state after that.
w = 400
mi = 540
b = 120
d = 9
mo = 550

def choose():
    print('Write action (buy, fill, take):')
    choice = input()
    if choice == 'buy':
        return buy()
    if choice == 'fill':
        return fill()
    if choice == 'take':    
        return take()

def state():
    print('The coffee machine has:')
    print(w, 'of water')
    print(mi, 'of milk')
    print(b, 'of coffee beans')
    print(d, 'of disposable cups')
    print(mo, 'of money')

def buy():
    global w, mi, b, d, mo
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
    n = int(input())
    if n == 1:
        w -= 250
        b -= 16
        mo += 4
    elif n == 2:
        w -= 350
        mi -= 75
        b -= 20
        mo += 7
    elif n == 3:
        w -= 200
        mi -= 100
        b -= 12
        mo += 6
    d -= 1    

def fill():
    global w, mi, b, d
    print('Write how many ml of water do you want to add:')
    w += int(input())
    print('Write how many ml of milk do you want to add:')
    mi += int(input())
    print('Write how many grams of coffee beans do you want to add:')
    b += int(input())
    print('Write how many disposable cups of coffee do you want to add:')
    d += int(input())

def take():
    global mo
    print(f'I gave you ${mo}')
    mo = 0

state()
choose()
state()

# loops for query from the user (buy, fill, take, remaining) or exit.
import sys

w = 400
mi = 540
b = 120
d = 9
mo = 550
w1 = 250
mi1 = 0
b1 = 16
mo1 = 4
w2 = 350
mi2 = 75
b2 = 20
mo2 = 7
w3 = 200
mi3 = 100
b3 = 12
mo3 = 6

def choose():
    while True:
        print('Write action (buy, fill, take, remaining, exit):')
        choice = input()
        if choice == 'buy':
            return buy()
        if choice == 'fill':
            return fill()
        if choice == 'take':
            return take()
        if choice == 'remaining':
            return remaining()
        if choice == 'exit':
            sys.exit()

def remaining():
    print('\nThe coffee machine has:')
    print(w, 'of water')
    print(mi, 'of milk')
    print(b, 'of coffee beans')
    print(d, 'of disposable cups')
    print(f'${mo} of money\n')
    return

def buy():
    global w, mi, b, d, mo
    print('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    x = input()
    if x == 'back':
        return choose()
    elif int(x) == 1:
        if enough(w1, mi1, b1) == True:
            w -= w1
            b -= b1
            mo += mo1
            d -= 1
        return enough(w1, mi1, b1)
    elif int(x) == 2:
        if enough(w2, mi2, b2) == True:
            w -= w2
            mi -= mi2
            b -= b2
            mo += mo2
            d -= 1
        return enough(w2, mi2, b2)
    elif int(x) == 3:
        if enough(w3, mi3, b3) == True:
            w -= w3
            mi -= mi3
            b -= b3
            mo += mo3
            d -= 1
        return enough(w3, mi3, b3)

def enough(a1, a2, a3):
    global w, mi, b, d
    if w / a1 < 1:
        print('Sorry, not enough water!\n')
        return False
    if a2 != 0:
        if mi / a2 < 1:
            print('Sorry, not enough milk!\n')
            return False
    if b / a3 < 1:
        print('Sorry, not enough coffee beans!\n')
        return False
    if d < 1:
        print('Sorry, not enough disposable cups!\n')
        return False
    print('I have enough resources, making you a coffee!\n')
    return True

def fill():
    global w, mi, b, d
    print('\nWrite how many ml of water do you want to add:')
    w += int(input())
    print('Write how many ml of milk do you want to add:')
    mi += int(input())
    print('Write how many grams of coffee beans do you want to add:')
    b += int(input())
    print('Write how many disposable cups of coffee do you want to add:')
    d += int(input())
    return

def take():
    global mo
    print(f'I gave you ${mo}\n')
    mo = 0
    return

def main():
    while True:
        choose()

main()
