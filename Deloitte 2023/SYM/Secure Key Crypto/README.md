#### 100 points Secure key crypto

We need to store the output log files for all our software installations. Since we cannot store data in plaintext, we need to encrypt all log files and we share the key file on a need to know basis. Can you decrypt this log file?  
26 bytes should be a safe key length right?

```python
from key import key

def xor(a,key):
  return ''.join(chr(a[i] ^ key[i%len(key)]) for i in range(len(a)))

f = open('Symantec_Wise_Installer_log_file.log')
w = open('Symantec_Wise_Installer_log_file.enc', 'w')
w.write(xor(f.read(),key))
```

## Solution
[File Signatures](https://kali-km.tistory.com/entry/File-Signature)
![](attachments/Pasted%20image%2020230516173623.png)

```python
enc = open("Symantec_Wise_Installer_log_file.enc", "rb").read()
key = b"***  Installation Started "

a = xor(enc, key)
key2 = a[:len(key)]
key2 = list(key2)

flag=""
for i in range(len(enc)):
  flag += chr(ord(key2[i%len(key2)]) ^ enc[i])

print(flag)
```

## Flag
CTF{5e159a313bb41e221419ca629496f084}