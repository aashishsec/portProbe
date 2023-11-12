import socket
import ipaddress
import colorama
import random
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import argparse


green = Fore.GREEN
magenta = Fore.MAGENTA
cyan = Fore.CYAN
mixed = Fore.RED + Fore.BLUE
red = Fore.RED
blue = Fore.BLUE
yellow = Fore.YELLOW
white = Fore.WHITE
colors = [magenta,cyan,mixed,red,blue,yellow, white]
random_color = random.choice(colors)
bold = Style.BRIGHT

parser=argparse.ArgumentParser(description=f"""{bold}{random_color}portProbe is a tool designed to efficiently probe for open ports. It will take both IP Address and Subdomains.""")
parser.add_argument('-d','--Domain',metavar='Domain',type=str,help=f"[{bold}{random_color}INFO]: {bold}{random_color}Domain to probe.")
parser.add_argument('-dL','--DomainList',metavar='DomainList',type=str,help=f"[{bold}{random_color}INFO]: {bold}{random_color}List of Domain to probe.")
parser.add_argument('-i','--ip',metavar='ip',type=str,help=f"[{bold}{random_color}INFO]: {bold}{random_color}IP Address to probe.")
parser.add_argument('-iL','--IpList',metavar='IpList',type=str,help=f"[{bold}{random_color}INFO]: {bold}{random_color}List of Ip to probe.")
parser.add_argument('-o','--output',metavar='output',type=str,help=f"[{bold}{random_color}INFO]: {bold}{random_color}File to save our output.")
args=parser.parse_args()
Domain=args.Domain
DominList=args.DomainList
ip=args.ip
IpList=args.IpList
output=args.output

def banner():
    print(f'''{bold}{random_color}

█
██████╗░░█████╗░██████╗░████████╗██████╗░██████╗░░█████╗░██████╗░███████╗
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝
██████╔╝██║░░██║██████╔╝░░░██║░░░██████╔╝██████╔╝██║░░██║██████╦╝█████╗░░
██╔═══╝░██║░░██║██╔══██╗░░░██║░░░██╔═══╝░██╔══██╗██║░░██║██╔══██╗██╔══╝░░
██║░░░░░╚█████╔╝██║░░██║░░░██║░░░██║░░░░░██║░░██║╚█████╔╝██████╦╝███████╗
╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═════╝░╚══════╝
          
          Github   : https://github.com/aashish36
          
          portProbe is a tool designed to efficiently probe for open ports. It will take both IP Address and Subdomains.
''')



def portScan(ip):
    return ip


def outputSave():
    return 0

def main():
    banner()


if __name__ == "__main__":
    main()

