enc = open("Symantec_Wise_Installer_log_file.enc", "rb").read()
key = b"***  Installation Started "

def xor(a,key):
  return ''.join(chr(a[i] ^ key[i%len(key)]) for i in range(len(a)))
  
a = xor(enc, key)
key2 = a[:len(key)]
key2 = list(key2)

flag=""
for i in range(len(enc)):
  flag += chr(ord(key2[i%len(key2)]) ^ enc[i])

print(flag)