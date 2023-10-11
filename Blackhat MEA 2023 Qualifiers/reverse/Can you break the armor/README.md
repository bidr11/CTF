![date](https://img.shields.io/badge/date-09.10.2023-brightgreen.svg)  
![solved](https://img.shields.io/badge/solved-After%20the%20CTF-red.svg)   
![category](https://img.shields.io/badge/category-Reverse-blueviolet.svg)   
![value](https://img.shields.io/badge/value-180-blue.svg)
## Description
Can you beat this awesome armor?
## Challenge Files
- `run.py`
- `pyarmor_runtime_000000/__init__.py`
- `pyarmor_runtime_000000/pyarmor_runtime.so`

## Solution
```bash
$> gdb python3
gdb> b exit
gdb> run run.py
gdb> generate-core-file
```
![](attachments/Pasted%20image%2020231011231345.png)
![](attachments/Pasted%20image%2020231011231419.png)
![](attachments/Pasted%20image%2020231011231448.png)
Yes... That's literally it.
## Flag
BHFlagY{th4t_4rm0r_wasnt_v3ry_5tr0ng}