#!/usr/bin/python2
#coding=utf8

import sys, os
sys.path.append(os.path.abspath(os.path.join(__file__, '../http')))
import client

def msg_handler(msg):
	print msg
	return  ""

if __name__ == '__main__':
	client.OrganizationId = 455
	client.QueueId = "umq-wmwhlk"
	client.AddrIp = "192.168.153.41"
	client.HttpAddr = "http://192.168.153.41:6318"
	client.PublisherId = "PID_e349dcbb67521fe082cf88d0892ef3f6"
	client.PublisherToken = "e349dcbb67521fe082cf88d0892ef3f6"
	client.ConsumerId = "CID_fafd13a67063ddd00d12a4c85664616d"
	client.ConsumerToken = "fafd13a67063ddd00d12a4c85664616d"
	client.WsAddr = "http://192.168.153.41:6138/"
	client.WsUrl = "ws://192.168.153.41:6318/ws"
	
	#发送消息 
	#pub_res = client.PublishMsg("hello")
	#print(pub_res)
	#回执消息
	#ack_res = client.AckMsg("umq-wmwhlk-16")
	#print(ack_res)
	#主动拉取消息 
	#get_res =client.GetMsg(2)
	#print(get_res)
	#订阅消息
	#sub_res = client.SubscribeQueue(msg_handler)
	#print(sub_res)
	#获取项目Id
	#org_res = client.GetOrganizationId("uhosttest@ucloud.cn", "org-23313")
	#print org_res
