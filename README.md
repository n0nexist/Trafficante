# Trafficante
![screenshot](https://user-images.githubusercontent.com/111337838/226925263-770a1ee7-eb7c-4c7f-ac84-68ad67fff76d.png)<br><br>
The man-in-the-middle toolkit

# Requirements
<b>1</b> -> <i>A ```linux``` computer with ```root``` permissions</i><br>
<b>2</b> -> <i>Python3 with ```scapy``` and ```netfilterqueue``` packages</i><br>
<b>3</b> -> <i>The package ```iptables``` installed on your linux distribution</i><br>

# Download & Usage
```
git clone https://github.com/n0nexist/Trafficante
cd Trafficante
pip3 install netfilterqueue scapy
sudo python3 main.py (target ip) (gateway ip) (attack type) my-payload.txt
```

# Available attacks
<b><a href="https://github.com/n0nexist/Trafficante/blob/main/wiki/js-injection.md">arbitrary javascript injection</a></b> | <i>Injects ```javascript``` code into the target's ```http``` traffic</i><br>
<b>dns spoofing</b> | <i>Spoofs ```dns``` requests</i><br>
<b>email hijacking (to do)</b> | <i>Changes target's ```emails``` content</i><br>
<b>ssl stripping (to do)</b> | <i>Sniffs target's ```https``` traffic by forcing a ```downgrade```</i><br>
