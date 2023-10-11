# PART1: 50 points Find the serial number

We managed to obtain an evaluation copy of the new ransomware used. Unfortunately it requires a serial number before it can be used. Can you analyze the malware and identify this serial number? We obtained both the Windows and Linux version use whatever you feel most comfortable with :)

## Solution
check_serial

```python
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

flag=""
for counter in range(16):
	flag+= chr(counter + 100 ^ serial[counter])

print(flag)
```

## Flag
CTF{rans0m_w4re}

# PART2: 150 points Decrypt a file

We found a file that has been encrypted using the ransomware you analyzed before. Can you find a way to decrypt it?

## Solution
encrypt
```c
encrypted_buffer = fopen("encrypted.out","wb");
	if (encrypted_buffer != 0x0) {
	key = rand_string_alloc(0x20);
	fputs(key,encrypted_buffer);
	i = 0;
	while( true ) {
		read_bytes = fread(&buffer,1,1,input_file);
		if (read_bytes == 0) break;
		output = buffer ^ key[i];
		key[i] = output;
		fputc(output,encrypted_buffer);
		i = i + 1 & 0x1f;
	}
}
```

Decryption script:
```python
with open("encrypted_flag", "rb") as enc_file:
	enc=enc_file.read()

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
	i = (i + 1) % 20 # did this at first, sad

with open("decrypted", "wb") as dec_file:
	dec_file.write(bytes(flag))
```
oh man, big mistake
```python
i = (i + 1) % 0x20
```

## Flag
CTF{C4NT_BE_BROKEN}