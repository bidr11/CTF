
serial = [0]*16

serial[0] = 0x27;
serial[1] = 0x31;
serial[2] = 0x20;
serial[3] = 0x1c;
serial[4] = 0x1a;
serial[5] = 8;
serial[6] = 4;
serial[7] = 0x18;
serial[8] = 0x5c;
serial[9] = 0;
serial[10] = 0x31;
serial[11] = 0x18;
serial[12] = 0x44;
serial[13] = 3;
serial[14] = 0x17;
serial[15] = 0xe;

a=""
for counter in range(16):
	a+= chr(counter + 100 ^ serial[counter])

print(a)


#########################################
with open("encrypted_flag", "rb") as enc_file:
	enc=enc_file.read()

# print(len(key))

# key_test=key.copy()

# flag_test = "aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa"
# a = list(flag_test.encode("utf-8"))
# i=0
# enc_test=[]

# ##enc
# while (i<len(flag_test)):
# 	k = key_test[i]
# 	f = a[i]
# 	enc_test.append(k^f)
# 	key_test.append(k^f)
# 	i+=1

# ##dec
# i=0
# dec_test = []
# while (i<len(enc_test)):
# 	k = key_test[i]
# 	f = enc_test[i]
# 	dec_test.append(k^f)
# 	key_test.append(k^f)
# 	i+=1

# print("".join([chr(i) for i in dec_test]))

key = list(enc[:0x20])
enc = list(enc[0x20:])

flag=[]

i=0
while(enc):
	e = enc.pop(0)
	k = key[i]
	dec = e^k
	flag.append(dec)
	key[i] = e
	i = (i + 1) % 0x20 #correct




with open("decrypted", "wb") as dec_file:
	dec_file.write(bytes(flag))
# print(bytes(flag))
