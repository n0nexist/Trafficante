# github.com/n0nexist/Trafficante

from scapy.all import *
import importlib
import modules.utils as utils
from netfilterqueue import NetfilterQueue

handler_func = None

def process_packet(packet):
    """ processes captured packets """
    
    global handler_func
    
    scapy_packet = IP(packet.get_payload())
    try:
        print(f"{utils.colors.BLUE}modifying {utils.colors.UNDERLINE}{len(scapy_packet)-3}{utils.colors.RESET}{utils.colors.BLUE} bytes -> {utils.colors.GREEN}{scapy_packet[IP].dst}{utils.colors.RESET}")
        scapy_packet = handler_func(scapy_packet)
    except Exception as e:
        print(e)
        pass
    packet.set_payload(bytes(scapy_packet))
    packet.accept()
    

def start_spoofing(handler_name):
    """ starts sniffing with custom handler """
    
    global handler_func
    
    try:
        module_name, function_name = handler_name.split('.')
        handler_module = importlib.import_module(module_name)
        handler_func = getattr(handler_module, function_name)
    except Exception as e:
        print(f"{utils.colors.FAIL}!{utils.colors.ITALIC} {e}{utils.colors.RESET}")
        pass
        
    print(f"{utils.colors.GREEN}*{utils.colors.ITALIC} sniffing with handler {utils.colors.WARNING}{handler_name}{utils.colors.RESET}")
    queue = NetfilterQueue()
    queue.bind(0, process_packet)
    queue.run()