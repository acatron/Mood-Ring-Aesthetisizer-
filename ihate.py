import httplib, urllib, base64  

# Image to analyse (body of the request)

body = '{\'URL\': \'http://fordhamcss.me/img/team/elana.jpg\'}'

# API request for Emotion Detection

headers = {
   'Content-type': 'application/json',
}

params = urllib.urlencode({
   'subscription-key': 'a6b0ff316e2c427fb931f73fc7f1a106',  # Enter EMOTION API key
   #'faceRectangles': '',
})

try:
   conn = httplib.HTTPSConnection('api.projectoxford.ai')
   conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body , headers)
   response = conn.getresponse()
   print("Send request")

   data = response.read()
   print(data)
   conn.close()
except Exception as e:
   print("[Errno {0}] {1}".format(e.errno, e.strerror))

