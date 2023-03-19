# Trafficante
Inject arbitrary javascript in other's http traffic

# Requirements
<b>1</b> -> <i>A ```linux``` computer with ```root``` permissions</i><br>
<b>2</b> -> <i>Python3 with ```scapy``` and ```netfilterqueue``` packages</i><br>
<b>3</b> -> <i>The package ```iptables``` installed on your linux distribution</i><br>

# Download & Usage
```
git clone https://github.com/n0nexist/Trafficante
cd Trafficante
pip3 install netfilterqueue scapy
sudo python3 main.py (target ip) (gateway ip) my-payload.txt
```
# Description
<b>1</b> -> <i>Write your javascript payload and save it on a file</i><br><br>
<b>2</b> -> <i>run: ```sudo python3 main.py 192.168.1.104 192.168.1.1 ciao.js```</i><br><br>
![alt-text](https://user-images.githubusercontent.com/111337838/226171334-b0fc2da0-4d50-41c6-8c97-574eb820bd2e.png)<br>
<i>(the output should be similar to <b>this</b>)</i><br><br>
<b>3</b> -> <i>if you now visit any http website as the target, you will se that the payload is injected</i><br>
![alt-text](https://user-images.githubusercontent.com/111337838/226171496-02efe3da-9a54-499e-90a0-2433c99ead1b.png)<br>
<i>(<b>attacker</b>'s screen)</i><br><br>
<b>4</b> -> <i>as we can see on the target's screen, the payload was injected succesfully</i><br>
![alt-text](https://user-images.githubusercontent.com/111337838/226171705-3dfa8f1c-c260-4afd-a06d-a9a8a21cd583.png)<br>
<i>(<b>target</b>'s screen)</i><br><br>
