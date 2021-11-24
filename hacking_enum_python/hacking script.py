#!/usr/bin/python3

#libraries
import subprocess, os, os.path
from menu1HS import menu1meat

HS_directory = "./HS"

os.mkdir(HS_directory)

def main():

    choice ='0'
    while choice =='0':
        print("Main Choice: Choose 1 of 5 choices")
        print("Choose 1 for Enumeration: nmap, smb")
        print("Choose 2 for apache vulnerability checks")
        print("Choose 3 to enumerate with nmap")
        print("Choose 4 for something")
        print("Choose 5 to go to another menu")

        choice = input ("Please make a choice: ")

        if choice == "5":
            print("Go to another menu")
            second_menu()
        elif choice == "4":
            print("Do Something 4")
        elif choice == "3":
            nmapEnum
        elif choice == "2":
            apacheVUL()
        elif choice == "1":
            nmap()
            SMBEnum()
        else:
            print("I don't understand your choice.")

def second_menu():
    print("This is the second menu")

main()
os.rmdir(HS_directory)