import argparse,socket,concurrent.futures,random,colorama,ipaddress

from termcolor import colored

from datetime import datetime

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
    print("-" * 80)

    print(f"{bold}{random_color}portProbe starting at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

    print("-" * 80)

    
def saveOutput(output):

    with open(output, 'w') as file:
        
        file.writelines(global_output)

def get_args():
    
    parser=argparse.ArgumentParser(description=f"""{bold}{random_color}portProbe is a tool designed to efficiently probe for open ports. It will take both IP Address and Subdomains.""")
    
    parser.add_argument('-d','--domain',metavar='domain',type=str,help=f"[{bold}{random_color}INFO]: {bold}{random_color}Domain to probe.")
        
    parser.add_argument('-i','--ip',metavar='ip',type=str,help=f"[{bold}{random_color}INFO]: {bold}{random_color}IP Address to probe.")
           
    parser.add_argument("-pT", dest="tcpPortScan", help=f"[{bold}{random_color}INFO]: {bold}{random_color}TCP Port Scan.", required=False, action="store_true")
    
    parser.add_argument( "-pU", dest="udpPortScan", help=f"[{bold}{random_color}INFO]: {bold}{random_color}UDP Port Scan.", required=False, action="store_true")
   
    # parser.add_argument( "-p", "--ports",dest="ports",help=f"[{bold}{random_color}INFO]: {bold}{random_color}Port range to scan, default is 1-65535 (all ports)",required=False,action="store",default="1-65535")

    parser.add_argument("-t", "--threads", help=f"[{bold}INFO{random_color}]: {random_color}{random_color}Threading level to make fast process. default=100", type=int, default=100,required=False) 
   
    parser.add_argument('-o','--output',metavar='output',type=str,default="portProbe.txt",help=f"[{bold}{random_color}INFO]: {bold}{random_color}File to save our output.")
    
    return parser.parse_args()



def portProbe(host,port,scan_type):
        
        global global_output
    
        try:
            
            if scan_type=="TCP":
                    
                    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                    client.settimeout(2)

                    client.connect((host, port))

                    client.close()

                    print(f"{bold}{random_color}[*]\t{port}\tOpen")

                    global_output.append(f"[*]\t{port}\tOpen")

            elif scan_type=="UDP":
                    
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

                    sock.settimeout(2)

                    client.connect((host, port))

                    print(f"{bold}{random_color}[*]\t{port}\tOpen")

                    sock.close()

                    global_output.append(f"[*]\t{port}\tOpen")

            elif scan_type=="ICMP":
                   
                    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

                    sock.settimeout(3)

                    client.connect((host, port))

                    print(f"{bold}{random_color}[*]\t{port}\tOpen")

                    sock.close()

                    global_output.append(f"[*]\t{port}\tOpen")

        except KeyboardInterrupt:

            print(f"You pressed Ctrl+C")

            exit(1)

        except:

           pass
                   

def threading(host):

    args = get_args()
    
    if ((args.tcpPortScan)or(args.udpPortScan)):

        if args.tcpPortScan:

            print(colored(f"\tTCP Port Scan {host} Results",'light_red'))

            scan_type="TCP"

        elif (args.udpPortScan):

            print(colored(f"\tUDP Port Scan {host} Results",'light_red'))

            scan_type="UDP"

    try:

        with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
                
                futures = [executor.submit(portProbe, host,port,scan_type) for port in range(1,65536)]
           
        concurrent.futures.wait(futures)

    except KeyboardInterrupt:

        print(f"You pressed Ctrl+C")

        exit(1)

    except:

        pass

def subdomainToIP(Domain):

    ip = socket.gethostbyname(Domain)

    return ip

def main():
    
    banner()

    args = get_args()

    host=args.ip
    
    if host==ipaddress.IPv4Address:
           
           pass
    
    elif args.domain:
           
           host=subdomainToIP(args.domain)
    
    threading(host)

    saveOutput(args.output)

if __name__ == "__main__":

    main()
