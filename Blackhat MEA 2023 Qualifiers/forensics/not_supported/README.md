![date](https://img.shields.io/badge/date-09.10.2023-brightgreen.svg)  
![solved](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Forensics-blueviolet.svg)   
![value](https://img.shields.io/badge/value-150-blue.svg)
## Description
Straight forward challenge, the flag is written on running notepad process. Flag is direct without BHFlagY{} tag.
## Challenge Files
- [url.txt](url.txt)

## Solution
We have a windows memory dump. We can use volatility3 to extract information out of it.
```
vol.py -f  windows.info
vol.py -f "memdump.mem" pslist
```
Upon executing pslist, we see a notepad executable in the dump. We can dump the process memory as follows:
```
vol.py -f "memdump.mem" -o "." windows.memmap ‑‑dump ‑‑pid <PID>
```
We get the [process memory dump](attachments/pid.1972.dmp)
Running strings on it, we get this result:
![](attachments/Pasted%20image%2020231011230227.png)

## Flag
BHflagY{d22a3eed050c23c0880cc912368905c9d2527a41c328f81ef115b9464b800f7425333edb71d57b440b94dc766a2d49611d46968477b09dfa1f246585d87d7b5a}