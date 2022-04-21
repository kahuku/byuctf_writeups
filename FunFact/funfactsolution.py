key = 'W'
encrypted = "g%4c$zc%dz4gg;"

s = []
for char in encrypted:
    s.append(ord(char))

l = []
for num in s:
    l.append(num ^ ord("W"))

s = ''
for num in l:
    char = chr(num)
    s += char
print(s)
