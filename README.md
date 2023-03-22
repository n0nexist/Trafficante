<p align="center">
 <img width="100px" src="https://github.com/n0nexist/Trafficante/blob/main/logo.png?raw=true" align="center" alt="GitHub Readme Stats" />
 <h2 align="center">Trafficante</h2>
 <p align="center">The man-in-the-middle toolkit</p>
</p>

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
<ul>
 <li><i>A <code>linux</code> computer with <code>root</code> permissions</i></li>
 <li><i>Python3 with <code>scapy</code> and <code>netfilterqueue</code> packages</i></li>
 <li><i>The package <code>iptables</code> installed on your linux distribution</i></li>
</ul>

<h2>:arrow_down_small: Download & Usage</h2>

```
git clone https://github.com/n0nexist/Trafficante
cd Trafficante
pip3 install netfilterqueue scapy
sudo python3 main.py (target ip) (gateway ip) (attack type) my-payload.txt
```

<h2>:trident: Available attacks</h2>

| Title                          | Description                                                  |
|--------------------------------|--------------------------------------------------------------|
| <b><a href="https://github.com/n0nexist/Trafficante/blob/main/wiki/js-injection.md">arbitrary javascript injection</a></b> | Injects javascript code into the target's http traffic       |
| <b><a href="https://github.com/n0nexist/Trafficante/blob/main/wiki/dns-spoofing.md">dns spoofing</a></b>                   | Spoofs dns requests                                          |
| <b><a href="https://github.com/n0nexist/Trafficante/blob/main/wiki/custom-handlers.md">custom handlers</a></b>                | Applies custom scapy handlers to craft your own mitm attacks |

