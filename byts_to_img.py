import base64


decodeImg = base64.b64decode(encodeImg)

with open("./app/images/decode/test2.png" , 'bw') as f3:
    f3.write(decodeImg)