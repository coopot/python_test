# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 19:53:50 2014
@author: duan
"""
import time
import paho.mqtt.client as mq
import datetime


def on_publish(msg, rc):   #成功发布消息的操作
    if rc == 0:
        print("publish success, msg = " + msg)


def on_connect(client, userdata, flags, rc):  #连接后的操作 0为成功
    print("Connection returned " + str(rc))

client = mq.Client(
    client_id="test_mqtt_sender_1", #client_id
    clean_session=True,
    userdata=None,
    protocol='MQTTv311'
)

trust =r"D:\python_work\baidu/root_cert.pem"#开启TLS时的认证文件目录
user = "parser_endpoint1478774398087/coopot"
pwd = "yMbg2oozB6twBzmgtDLcb1fkv4K0os3M3lqK6WRgXkg="
endpoint = "parser_endpoint1478774398087.mqtt.iot.gz.baidubce.com"
port = 1884
topic = "sub $baidu/iot/device/coopot"

client.tls_insecure_set(True) #检查hostname的cert认证
client.tls_set(trust) #设置认证文件
client.username_pw_set(user, pwd) #设置用户名，密码
client.connect(endpoint, port, 60) #连接服务 keepalive=60
client.on_connect = on_connect #连接后的操作
client.loop_start()
time.sleep(2)
count = 0
while count < 5: #发布五条消息
    count = count + 1
    msg = str(datetime.datetime.now())
    rc , mid = client.publish(topic, payload=msg, qos=1) #qos
    on_publish(msg, rc)
    time.sleep(2)