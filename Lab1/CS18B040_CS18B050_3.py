#run as python3 CS18B040_CS18B050_3.py
import pwn
payload = b'360\nRaghu_Aniswar\n'
for ii in range(0,5120):
        exploit = pwn.process(['./CS18B040_CS18B050_3'])
        exploit.sendline(payload)
        out = exploit.recv()
        if(b'Congrats' in out):
                break
print(out.decode('utf-8'))

