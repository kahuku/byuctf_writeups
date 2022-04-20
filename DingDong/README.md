# BYUCTF Winter 2022 - Ding Dong (Easy - Medium) Writeup
* Type - Forensics/Steganography
* Name - Ding Dong
* Points - 518

## Description
```
Here is a packet capture of Ian while on campus one afternoon. 
Can you figure out what he was doing?
```

---

### Ding Dong 1 (Easy)
* 76 Points

#### Question
```
What is Ian's IP and MAC address?
Flag format - byuctf{100.100.100.100_11:22:33:44:55:66}
```

#### Solution
Time to fire up trusty 'ol Wireshark! Opening DingDong.pcapng in Wireshark shows us a list of all the packets that were captured. Since Ian was on BYU campus, I knew the IP would start with `10.37`, as all student devices connected to eduroam campus Wi-Fi are on that subnet. Even without that prior knowledge, 97.9% of packets contained `10.37.131.2` (set the filter to `ip.addr == 10.37.131.2` and look at the lower right hand corner to see that even with that filter on, 4625/4722 packets are being displayed). After opening up any packet that contained `10.37.131.2` in the 'Destination' column in the packet inspector window, you can open the 'Ethernet II' dropdown and pull the MAC address out of the header for the 'Destination' sub-dropdown.

#### Real World Application
This challenge served as a good introduction to Wireshark. Wireshark is a packet capturing tool used to analyze network traffic. This challenge taught us how to set filters to look for specific IP addresses and how to analyze a packet in greater depth.

---

### Ding Dong 2 (Easy)
* 93 Points

#### Question
```
How many different DNS queries of type A were made?
Flag format - byuctf{0000}
```

#### Solution
The first thing I tried for this challenge was applying the `dns.a` filter and just entering the number of packets displayed (again, in the bottom right hand corner). That didn't give me the right answer. Turns out `dns.a` filters by address, not query type. So I had to find a different filter. Instead of just searching for a filter I thought might work, I found a packet that matched the description I was looking for. I filtered using the command
```
dns and (ip.dst==10.37.131.2 or ip.src==10.37.131.2)
``` 

and found 96 results. Later I found that all DNS queries in this capture included `10.37.131.2` somewhere in the source or destination, so I later simplified that filter to just `dns`. In those 96 results, I found a query. I selected the packet, opened it in the viewer, and under the 'Domain Name System (query)' subcategory, I right clicked on the 'Response: Message is a query' line, and selected 'Apply as Filter -> Selected' and went back to my main window. That automatically entered `dns.flags.response == 0` in the filter bar. When I prepended `dns &&`, my list was narrowed to 48 packets that were just DNS queries. Finally, I selected a packet with an 'A' in the info column, opened it in the packet viewer, under 'Queries -> <DNS query>: type A, class IN', right clicked the line that read 'Type: A', and applied that as a filter again. Finally, I added the `dns && dns.flags.response == 0` back into the search bar, so the final filter reads
```
dns && dns.flags.response == 0 && dns.qry.type == 1
``` 

Which gives the correct flag- byuctf{36}
  
#### Real World Application
Packets are sent across networks so fast, packet captures get very large very quickly. Any good analyst needs to be able to apply filters to narrow down the information they're sorting through to find the packets they need to analyze. 
  
---

### Ding Dong 3 (Medium)
* 86 Points

#### Question
```
How many packets have the ACK flag enabled?
Flag format - byuctf{0000}
```

#### Solution

#### Real World Application

---

### Ding Dong 4 (Medium)
* 91 Points

#### Question
```
What is the version number for the Linux server that sent a packet with redsonic as the user agent?
Flag format - byuctf{1.1.1}
```

#### Solution

#### Real World Application

---

### Ding Dong 5 (Medium)
* 83 Points

#### Question
```
What are the two IPs that function as DNS servers?
Flag format - byuctf{10.10.10.10_11.11.11.11}
```

#### Solution

#### Real World Application

---

### Ding Dong 6 (Medium)
* 89 Points

#### Question
```
What is the hidden flag?
```

#### Solution

#### Real World Application
