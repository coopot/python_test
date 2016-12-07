#encoding:utf-8
import base64
import urllib, urllib2, sys ,json
import ssl
file=open(r'E:\1.jpg','rb')##填写你自己的图片路径
image= file.read()  ##读图片或者摄像头抓图
file.close()

host = 'https://dm-55.data.aliyun.com'
path = '/rest/160601/ocr/ocr_english.json'
method = 'POST'
appcode = '********6fbe9d61'#填写你自己的appcode
querys = ''
bodys = {}
url = host + path
###############以下是JSON组包
#数据
data = {}
data['dataType']=50
data['dataValue']=base64.b64encode(image)
#image标示
imagedata={}
imagedata['image']=data
#input标示
senddata={}
s=[imagedata]
senddata['inputs']=s
send_data=json.dumps(senddata)
#body
bodys[''] =send_data
post_data = bodys['']
###############JSON组包完成
#print post_data
request = urllib2.Request(url, post_data)
request.add_header('Authorization', 'APPCODE ' + appcode)
#根据API的要求，定义相对应的Content-Type
request.add_header('Content-Type', 'application/json; charset=UTF-8')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib2.urlopen(request, context=ctx)
content = response.read()
revout = json.loads(content)
###############JSON解包
rev=json.loads(revout['outputs'][0]['outputValue']['dataValue'])
if (content):
   #print content
    print rev['ret'][0]['result']
