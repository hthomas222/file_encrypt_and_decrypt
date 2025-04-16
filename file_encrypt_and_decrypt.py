from cryptography.fernet import Fernet
from rich.console import Console
from rich.table import Table
from rich import print
import sys
import os 

def gen_key():
	k = Fernet.generate_key()
	with open("key.key", "wb") as key:
		key.write(k)


def retreive():
	rk = open("key.key", "rb")
	key = rk.read()
	print(key)

def ls(): 
	li = os.listdir('.')
	for i in li: 
		console.log(f"[green]{i}")

def file_encryption(file, key):
	key = Fernet(key)
	with open(file, "rb") as e_file: 
		content = e_file.read()
		e_data = key.encrypt(content)
	with open(file, "wb") as e_file:
		e_file.write(e_data)


def file_decryption(file, key):
	key = Fernet(key)
	with open(file, "rb") as d_file: 
		content = d_file.read()
	d_data = key.decrypt(content)
	with open(file, "wb") as d_file:
		d_file.write(d_data)


def check(test):
    if test == "2":
        return test
    if test == "1":
        sys.exit()
    sel = ["1", "2"]
    while test not in sel:
            console.log("Please enter either 1 or 2")
            test = console.input(f"[bold red]Select 1 to exit |""[bold green]| Select 2 to continue: ")
    return test


# Main
test = ""
while test != "1":
    print()
    table = Table(title="File Encrypter Commands")
    table.add_column("NUM", style="green")
    table.add_column("TASK", style="red")
    table.add_column("Description", style="blue")
    table.add_row("1", "GEN_KEY", "This will generate a key that is needed for the encryption and decryption.")
    table.add_row("2", "KEY_RETREIVE", "This will display your key.")
    table.add_row("3", "LS", "List the files.")
    table.add_row("4", "Encrypt", "This will encrypt the file")
    table.add_row("5", "Decrypt", "This will decrypt the file")
    console = Console()
    console.print(table)
    print()
    selection = input("enter a number to execute the command: ")
    if selection == "1":
        gen_key()
    elif selection == "2":
        print()
        retreive()
        print()
    elif selection == "3":
        print()
        ls()
        print()        
    elif selection == "4":
        print()
        file = console.input(f"[bold purple] Please enter a file you want to encrypt: ")
        rk = open("key.key", "rb")
        key = rk.read()
        file_encryption(file, key)
        print()
    elif selection == "5":
        print()
        file = console.input(f"[bold purple] Please enter a file you want to decrypt: ")
        rk = open("key.key", "rb")
        key = rk.read()
        file_decryption(file, key)
        print()
    else:
        console.log("[bold red]Please enter a valid choice!")
    print()
    test = console.input(f"[bold red]Select 1 to exit |""[bold green]| Select 2 to continue: ")
    if test != "1":
        x = check(test)
        if x == "1":
            sys.exit()
