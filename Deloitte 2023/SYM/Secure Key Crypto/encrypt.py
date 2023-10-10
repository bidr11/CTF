from key import key

def xor(a,key):
  return ''.join(chr(a[i] ^ key[i%len(key)]) for i in range(len(a)))

f = open('Symantec_Wise_Installer_log_file.log')
w = open('Symantec_Wise_Installer_log_file.enc', 'w')
w.write(xor(f.read(),key))
