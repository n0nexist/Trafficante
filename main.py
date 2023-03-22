# github.com/n0nexist/Trafficante

import modules.utils as utils
import modules.injector as inj
import modules.mitm as mitm
import modules.dns_spoof as dns
from threading import Thread as th

utils.checkroot()
utils.cls()
utils.logo()

target, gateway, attacktype, payloadfile = utils.args()

th(target=mitm.start_mitm,args=(target, gateway,)).start()
utils.enable_forwarding()

if attacktype == "js":
    print(f"{utils.colors.GREEN}*{utils.colors.ITALIC} starting javascript injection attack{utils.colors.RESET}")
    th(target=inj.start_injecting,args=(payloadfile,)).start()
elif attacktype == "dns":
    print(f"{utils.colors.GREEN}*{utils.colors.ITALIC} starting dns spoofing attack{utils.colors.RESET}")
    th(target=dns.start_spoofing,args=(payloadfile,)).start()