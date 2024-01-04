from datetime import datetime

import argparse,re,socket,concurrent.futures,random,colorama

from queue import Queue

import scapy.all as scapy

from termcolor import colored

from colorama import Fore, Style

colorama.init(autoreset=True)

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

global_output=[]

def get_args():
    
    parser=argparse.ArgumentParser(description=f"""{bold}{random_color}portProbe is a tool designed to efficiently probe for open ports. It will take both IP Address and Subdomains.""")
    
    # parser.add_argument('-d','--Domain',metavar='Domain',type=str,help=f"[{bold}{random_color}INFO]: {bold}{random_color}Domain to probe.")
    
    # parser.add_argument('-dL','--DomainList',metavar='DomainList',type=str,help=f"[{bold}{random_color}INFO]: {bold}{random_color}List of Domain to probe.")
    
    parser.add_argument('-i','--ip',metavar='ip',type=str,help=f"[{bold}{random_color}INFO]: {bold}{random_color}IP Address to probe.")
    
    # parser.add_argument('-iL','--IpList',metavar='IpList',type=str,help=f"[{bold}{random_color}INFO]: {bold}{random_color}List of Ip to probe.")
    
    parser.add_argument("-arp", dest="arp",help=f"[{bold}{random_color}INFO]: {bold}{random_color}Use this for ARP ping!",required=False,action="store_true")
   
    parser.add_argument("-pT", dest="tcpPortScan", help=f"[{bold}{random_color}INFO]: {bold}{random_color}TCP Port Scan", required=False, action="store_true")
    
    parser.add_argument( "-pU", dest="udpPortScan", help=f"[{bold}{random_color}INFO]: {bold}{random_color}UDP Port Scan", required=False, action="store_true")
   
    parser.add_argument( "-p", "--ports",dest="ports",help=f"[{bold}{random_color}INFO]: {bold}{random_color}Port range to scan, default is 1-65535 (all ports)",required=False,action="store",default="1-65535")

    parser.add_argument("-t", "--threads", help=f"[{bold}INFO{random_color}]: {random_color}{random_color}Threading level to make fast process", type=int, default=50,required=False) 
   
    parser.add_argument('-o','--output',metavar='output',type=str,default="portProbe.txt",help=f"[{bold}{random_color}INFO]: {bold}{random_color}File to save our output.")
    
    return parser.parse_args()



def banner():

    print(f'''{bold}{random_color}
█
██████╗░░█████╗░██████╗░████████╗██████╗░██████╗░░█████╗░██████╗░███████╗
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝
██████╔╝██║░░██║██████╔╝░░░██║░░░██████╔╝██████╔╝██║░░██║██████╦╝█████╗░░
██╔═══╝░██║░░██║██╔══██╗░░░██║░░░██╔═══╝░██╔══██╗██║░░██║██╔══██╗██╔══╝░░
██║░░░░░╚█████╔╝██║░░██║░░░██║░░░██║░░░░░██║░░██║╚█████╔╝██████╦╝███████╗
╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═════╝░╚══════╝
          
          Github   : https://github.com/aashishsec
          
          portProbe is a tool designed to efficiently probe for open ports. It will take both IP Address and Subdomains.
''')



def subdomainToIP(Domain):

    ip = socket.gethostbyname(Domain)

    return ip

def saveOutput(output):

    with open(output, 'w') as file:
        
        file.writelines(global_output)


def arp_ping(ip):

    if not re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$", ip):
       
       print(colored("[-] Please provide a valid IP address range for ARP ping!",'red',attrs=['bold']))

       exit(1)
       
    try:

        arp_request_frame = scapy.ARP(pdst=ip)

        ether_broadcast_frame = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

        broadcast_arp_packet = ether_broadcast_frame / arp_request_frame

        active_clients = scapy.srp(broadcast_arp_packet, timeout=3, verbose=False)[0]
        
        for _, reply in active_clients:

            print(f"[+]\t{reply.psrc}\t{reply.hwsrc}")

    except Exception as err:

        print(colored(f"[-] Error occurred! Reason: {err}",'red',attrs=['dark']))
        

def scan_thread(host, scan_type, port_queue):

    while True:

        try:

            port = port_queue.get_nowait()

            port_scan(port, host, scan_type)

            port_queue.task_done()

        except port_queue.Empty:

            break   

def port_scan(port, host, scan_type):

    try:

        if scan_type == "T":

            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            client.settimeout(1)

            client.connect((host, port))

            client.close()

            print(f"[*]\t{port}\tOpen")

        elif scan_type == "U":

            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            sock.settimeout(1)

            client.connect((host, port))

            print(f"[*]\t{port}\tOpen")

            sock.close()

    except KeyboardInterrupt:

        print("You pressed Ctrl+C")

        exit(1)

    except:

        pass

def main():

    banner()

    args = get_args()

    host = args.ip

    start_port, end_port = map(int, args.ports.split("-"))

    scan_type = ""

    port_queue = Queue()

    print(colored("-"*65, 'cyan', attrs=['dark']))

    print(colored(f"\tportProbe starting at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", 'cyan', attrs=['dark']))

    print(colored("-"*65, 'cyan', attrs=['dark']))

    if args.arp:

        print(colored("-"*50,'light_red'))

        print(colored("\tARP Ping Scan Results",'light_red'))

        print(colored("-"*50,'light_red'))

        print(colored("="*30,'black'))

        print(colored("\tPort\tState",'black',attrs=['bold']))

        print(colored("="*30,'black'))

        arp_ping(host)

        
    if ((args.tcpPortScan)or(args.udpPortScan)):

        print(colored("-"*50,'light_red'))

        if args.tcpPortScan:

            print(colored("\tTCP Port Scan Results",'light_red'))

            scan_type="T"

        elif (args.udpPortScan):

            print(colored("\tUDP Port Scan Results",'light_red'))

            scan_type="U"

        print(colored("-"*50,'light_red'))

        print()

        print(colored("="*30,'dark_grey'))

        print(colored("\tPort\tState",'dark_grey',attrs=['bold']))

        print(colored("="*30,'dark_grey'))
        
        
        for port in range(start_port, end_port + 1):

            port_queue.put(port)

        with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:

            for _ in range(args.threads):

                executor.submit(scan_thread, host, scan_type, port_queue)

        port_queue.join()


if __name__ == "__main__":

    main()

