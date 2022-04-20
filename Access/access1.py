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
