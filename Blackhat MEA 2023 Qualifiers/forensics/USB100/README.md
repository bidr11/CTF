![date](https://img.shields.io/badge/date-09.10.2023-brightgreen.svg)  
![solved](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Forensics-blueviolet.svg)   
![value](https://img.shields.io/badge/value-50-blue.svg)
## Description
In a shocking turn of events, a malicious actor managed to gain physical access to our victim's computer by plugging in a rogue USB device. As a result, all critical data has been pilfered from the system. Flag is direct without BHFlagY{} tag.
## Initial Files
- [send.pcapng](send.pcapng)

## Solution
First looking at the capture, we can see the keywords USB, USBMS, and SCSI. After a quick google search it is obvious that the device is a USB Mass Storage device, so it is safe to assume that we need to extract a file from these transfers.
![](attachments/Pasted%20image%2020231011230330.png)
Just looking around I came upon this specific packet which starts with the keywords INDX. I thought that this would be most likely a list of files in a directory. I was right.
![](attachments/Pasted%20image%2020231011230813.png)
Extracting the data and putting it into a more readable format, I found the name of an executable called `blackhat.exe`
![](attachments/Pasted%20image%2020231011230943.png)
I then extracted the executable and ran it.
![](attachments/Pasted%20image%2020231011231024.png)

## Flag
BHflagy{1d3cbfa0e052b1729a00950e9fc0f61a3f393bc97c0c74c8ecab1b58cd0f95c32e4c970bdfa6e23371d50680ca0c37f61f7206974d20d5cbb2f00151f4735dde}