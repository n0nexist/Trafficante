<!-- <img align="center" src=""> -->

<h1 align="center">Trafficante</h1>

<p align="center">The man-in-the-middle toolkit</p><br>

<p align="center">
    <a href="https://github.com/n0nexist/Trafficante/blob/main/LICENSE.md">
      <img alt="MIT license" src="https://img.shields.io/badge/license-MIT-red?style=flat&logo=github" />
    </a>
    <a href="https://www.google.com/search?q=scapy+netfilterqueue">
      <img alt="Libraries" src="https://img.shields.io/badge/scapy-netfilterqueue-informational?style=flat&logo=python" />
    </a>
    <a href="https://github.com/n0nexist">
      <img src="https://img.shields.io/badge/python-pentesting-inactive?style=flat" />
    </a>
    <a href="https://github.com/n0nexist/Trafficante/issues">
      <img alt="Issues" src="https://img.shields.io/github/issues/n0nexist/Trafficante?color=0088ff" />
    </a>
</p>

<br>

<h2>:computer: Requirements</h2>
<b>1</b> -> <i>A ```linux``` computer with ```root``` permissions</i><br>
<b>2</b> -> <i>Python3 with ```scapy``` and ```netfilterqueue``` packages</i><br>
<b>3</b> -> <i>The package ```iptables``` installed on your linux distribution</i><br>

<h2>:arrow_down_small: Download & Usage</h2>

```
git clone https://github.com/n0nexist/Trafficante
cd Trafficante
pip3 install netfilterqueue scapy
sudo python3 main.py (target ip) (gateway ip) (attack type) my-payload.txt
```

<h2>:trident: Available attacks</h2>
<b><a href="https://github.com/n0nexist/Trafficante/blob/main/wiki/js-injection.md">arbitrary javascript injection</a></b> | <i>Injects ```javascript``` code into the target's ```http``` traffic</i><br>
<b><a href="https://github.com/n0nexist/Trafficante/blob/main/wiki/dns-spoofing.md">dns spoofing</a></b> | <i>Spoofs ```dns``` requests</i><br>
<b><a href="https://github.com/n0nexist/Trafficante/blob/main/wiki/email-hijacking.md">email hijacking</a> (to do)</b> | <i>Changes target's ```emails``` content</i><br>
<b><a href="https://github.com/n0nexist/Trafficante/blob/main/wiki/ssl-stripping.md">ssl stripping</a> (to do)</b> | <i>Sniffs target's ```https``` traffic by forcing a ```downgrade```</i><br>
