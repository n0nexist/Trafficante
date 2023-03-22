# github.com/n0nexist/Trafficante

import os
import sys

class colors:
    """ ansi escape codes for colors 
        (including bold and italic styles) """
        
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m'
 
def cls():
    """ clears the console """
    
    os.system("clear")
    
def enable_forwarding():
    """ enables packet forwarding """
    
    os.popen("iptables -I FORWARD -j NFQUEUE --queue-num 0").read()
    
def disable_forwarding():
    """ disables packet forwarding """
    
    os.popen("iptables -D FORWARD -j NFQUEUE --queue-num 0").read()
    
def checkroot():
    """ quits if we're not root """
    
    if os.getuid() != 0:
        print(f"{colors.FAIL}run this script as root.{colors.RESET}")
        exit(-2)
    
def logo():
    """ prints the logo """
    
    print(f"""{colors.BOLD}{colors.BLUE}
___     _ _              
 | _ _ (_(_. _ _  _ |_ _    {colors.RESET}v1.2{colors.BLUE}{colors.BOLD}
 || (_|| | |(_(_|| )|_(-    {colors.RESET}by {colors.ITALIC}{colors.GREEN}{colors.UNDERLINE}n0nexist.github.io{colors.RESET}
""")
    
def showhelp():
    """ shows help menu and exits """
    
    print(f"{colors.FAIL}{sys.argv[0]}{colors.ITALIC} (target ip) (gateway ip) (attack) (file)")
    print(f"""\n{colors.FAIL}attacks:{colors.ITALIC}
js -> arbitrary javascript injection on http traffic
dns -> dns spoofing
custom -> custom handler      
{colors.RESET}""")
    exit(-1)
    
def args():
    """ returns system arguments """
    
    try:
        return sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    except:
        showhelp()
        