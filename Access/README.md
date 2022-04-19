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

#### Solution
This challenge taught me that you can't always just take code off the internet and expect it to perfectly suit the needs of your situation. Who would've thought? 

The first thing I did was look through the log file with a simple `cat access.log`. I scrolled through the file for a minute just to get a feel for the data I was reading through. Here's an example line:
```
34.245.89.123 - - [09/Feb/2022:01:12:57 +0000] "GET /app-ads.txt HTTP/1.1" 200 473 "-" "TprAdsTxtCrawler/1.1"
```
This line contains a decent amount of information- an IP address, a timestamp, and details for a HTTP GET request. Fortunately, for this challenge, all we're looking for is a list of unique IP addresses. 

#### Real World Application

---

### Access 2 (Easy)
* 10 Points

#### Question
```
How many attempts were made to grab a .env file?
Flag format - byuctf{0000}
```

#### Solution

#### Real World Application

---

### Access 3 (Medium)
* 72 Points

#### Question
```
What IPs attempted to exploit log4j?
Flag format - byuctf{100.100.100.100_200.200.200.200}
```

#### Solution

#### Real World Application

---

### Access 4 (Medium)
* 76 Points

#### Question
```
What is the name of the exploit file that would be run in the obfuscated log4j attempt?
Flag format - byuctf{filename}
```

#### Solution

#### Real World Application

---

### Access 5 (Hard)
* 83 Points

#### Question
```
What IP addresses attempted to exploit CVE-2021-3129?
Flag format - byuctf{100.100.100.100_200.200.200.200}
```

#### Solution

#### Real World Application

---

### Access 6 (Hard)
* 86 Points

#### Question
```
What is the name of the ISP that hosts the Russian IP attempting to exploit CVE-2021-3129?
Flag format - byuctf{ispname}
```

#### Solution

#### Real World Application
