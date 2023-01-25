import time
import os


def clear():
    os.system('clear||cls')
def print_menu():

    clear()
    print('**********************************************************************************************************************************************************************')
    print('*                                                                                                                                                                    *')
    print('*                                                                                                                                                                    *')
    print('*                                                               \u001b[36;1m ███╗   ███╗███████╗███╗   ██╗██╗   ██╗\u001b[37m                                                              *')
    print('*                                                               \u001b[36;1m ████╗ ████║██╔════╝████╗  ██║██║   ██║\u001b[37m                                                              *')
    print('*                                                               \u001b[36;1m ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║\u001b[37m                                                              *')
    print('*                                                               \u001b[36;1m ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║\u001b[37m                                                              *')
    print('*                                                               \u001b[36;1m ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝\u001b[37m                                                              *')
    print('*                                                               \u001b[36;1m ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ \u001b[37m                                                              *')
    print('*                                                                                                                                                                    *')        
    print("*                                                                                                                                                                    *")
    print('*                                                                                                                                                                    *')
    print('*                                                                 ▄█─ ─    ░█▀▀█ ░█─── ─█▀▀█ ░█──░█                                                                  *')    
    print('*                                                                 ─█─ ▄    ░█▄▄█ ░█─── ░█▄▄█ ░█▄▄▄█                                                                  *') 
    print('*                                                                 ▄█▄ █    ░█─── ░█▄▄█ ░█─░█ ──░█──                                                                  *')
    print('*                                                                                                                                                                    *')
    print('*                                                                 █▀█ ─   ─█▀▀█ ░█▀▀█ ░█▀▀▀█ ░█─░█ ▀▀█▀▀                                                             *')                                                                  
    print('*                                                                 ─▄▀ ▄   ░█▄▄█ ░█▀▀▄ ░█──░█ ░█─░█ ─░█──                                                             *')                                                                  
    print('*                                                                 █▄▄ █   ░█─░█ ░█▄▄█ ░█▄▄▄█ ─▀▄▄▀ ─░█──                                                             *')
    print('*                                                                                                                                                                    *')                                                        
    print('*                                                                 █▀▀█ ─   ░█▀▀▀ ▀▄░▄▀ ▀█▀ ▀▀█▀▀                                                                     *')
    print('*                                                                 ──▀▄ ▄   ░█▀▀▀ ─░█── ░█─ ─░█──                                                                     *')
    print('*                                                                 █▄▄█ █   ░█▄▄▄ ▄▀░▀▄ ▄█▄ ─░█──                                                                     *')
    print('*                                                                                                                                                                    *')       
    print('*                                                                                                                                                                    *')       
    print("**********************************************************************************************************************************************************************")

  
    option=input("Enter your choice: ")
    if option == "1":
        time.sleep(1.0)
        clear()
        from menu import print_menu1
    elif option == "2":
     
      print("PROJECT DESCRIPTION")
      print("This project consists of three basic games that use data structures.")
      print("i. Stack - 4 in a row ")
      print("ii. Queue - Word Guessing")
      print("iii. Linked List - Snake")

      print("ABOUT THE AUTHORS")
      print("The project was created by Armie Miranda & Rieza Espejo.")

      
      time.sleep(5.0)
      
      print(print_menu())
    elif option == "3":
     exit()

print(print_menu())

