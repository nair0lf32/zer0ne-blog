#!/usr/bin/env python3
def decrypt(msg):
	cd = []
	for char in msg:
		char = char - 18
		char = 179 * char % 256
		cd.append(char)
	return bytes(cd)
	
with open('msg.enc') as f:
	ct = bytes.fromhex(f.read())
	cd = decrypt(ct)
	print(cd)
	
    

    
    
    
    
    
    
    

     
