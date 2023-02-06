#This code will generate game 'Rock, Paper, Scissor'. Enjoy
import random

elemente_computer = {0 : "Piatra", 1 : "Hartie", 2 : "Foarfeca"}
elemente_joc = {"Piatra" : 0, "Hartie" : 1, "Foarfeca" : 2}
is_dorinta_joc = True

while is_dorinta_joc:
    incepere_joc = input("Pentru a incepe/finaliza jocul, introduceti Start/Exit: ").title()
    if incepere_joc =="Start" :
        user_choice = input("Introduceti ce optiune doriti(Piatra, Hartie, Foarfeca): ").title()
        computer_number = random.randint(0, 2)
        if user_choice in elemente_joc:
            if (elemente_joc[user_choice] < computer_number) & (computer_number != 2) : #""" Piatra - Hartie"""
                print(f"Tu ai ales {user_choice}, computerul a ales {elemente_computer[computer_number]}, de aceea a castigat computerul!")
            elif (elemente_joc[user_choice] < computer_number) & (computer_number != 1) & (elemente_joc[user_choice] !=1): #""" Piatra - Foarfeca"""
                print(f"Tu ai ales {user_choice}, computerul a ales {elemente_computer[computer_number]}, de aceea ai castigat!")
            elif (elemente_joc[user_choice] < computer_number) & (user_choice != 0): #""" Hartie - Foarfeca"""
                print(f"Tu ai ales {user_choice}, computerul a ales {elemente_computer[computer_number]}, de aceea a castigat computerul!")
            elif (elemente_joc[user_choice] > computer_number) & (elemente_joc[user_choice] != 2) : #"""Hartie - Piatra"""
                print(f"Tu ai ales {user_choice}, computerul a ales {elemente_computer[computer_number]}, de aceea ai castigat!")
            elif (elemente_joc[user_choice] > computer_number) & (elemente_joc[user_choice] !=1) & (computer_number !=1): #"""Foarfeca - Piatra"""
                print(f"Tu ai ales {user_choice}, computerul a ales {elemente_computer[computer_number]}, de aceea a castigat computerul!")
            elif (elemente_joc[user_choice] > computer_number) & (elemente_joc[user_choice] !=1) & (computer_number !=0): #"""Foarfeca - Hartie"""
                print(f"Tu ai ales {user_choice}, computerul a ales {elemente_computer[computer_number]}, de aceea ai castigat!")
            else:
                print(f"Tu ai ales {user_choice}, computerul a ales {elemente_computer[computer_number]}, de aceea este egalitate!")
        else :
            print("Introduceti una din cele 3 optiuni!")
    elif incepere_joc == "Exit":
        is_dorinta_joc = False
    else :
        print("Alege una din cele 2 obtiuni!")


    










