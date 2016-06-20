#!/usr/bin/python2
#coding=utf8
#umq sdk python

import net
import urllib
import json
import websocket

Organization = 10000 #组织ID
QueueId = "umq-xxx" #队列ID
AddrIp="xxx.xxx.xxx.xxx"
HttpAddr = "http://xxxx:6318" #服务地址
PublisherId = "PID_XXX" #发布者ID
PubliserToken = "xxxxx" #发布者Token
ConsumerId = "CID_XXXXXXX" #消费者token
ConsumerToken = "xxxxx" #消费者Token
WsAddr = "http://xxxxxx:6318/" #Websocket服务IP
WsUrl = "ws://xxx:6318/ws" #Websocket服务IP

def AckMsg(MsgId):
	ack_req = {
			"Action": "AckMsg",
			"QueueId": QueueId,
			"ConsumerId": ConsumerId,
			"MsgId": MsgId
	}
	ack_res = net.sendHttpRequest(AddrIp, HttpAddr, ack_req, 10)
	return ack_res

def PublishMsg(content):
	pub_req = {
			"Action": "PublishMsg",
			"QueueId": QueueId,
			"OrganizationId": str(OrganizationId),
			"PublisherId": PublisherId,
			"PublisherToken": PublisherToken,
			"Content": content
	}
	pub_res = net.sendHttpRequest(AddrIp, HttpAddr, pub_req, 10)
	return pub_res

def GetMsg(Num):
	get_req = {
			"Action": "GetMsg",
			"QueueId": QueueId,
			"OrganizationId": str(OrganizationId),
			"ConsumerId": ConsumerId,
			"ConsumerToken": ConsumerToken,
			"Num": str(Num)
	}
	get_res = net.sendHttpRequest(AddrIp, HttpAddr, get_req, 10)
	return get_res

def SubscribeQueue(msg_handler):
	try:
		#websocket.enableTrace(True)
		ws = websocket.WebSocket()
		ws.connect("ws://192.168.153.41:6318/ws")
		StartConsumeReq = {
				"OrganizationId": OrganizationId,
				"QueueId": QueueId,
				"ConsumerId": ConsumerId,
				"ConsumerToken": ConsumerToken
		}
		sub_req = {
				"Action": "ConsumeMsg",
				"Data": StartConsumeReq
		}
		body_data = json.dumps(sub_req)
		ws.send(body_data)
		sub_res = ws.recv()
		while True:
			print "start receiving"
			msg = ws.recv()
			msg_id = msg_handler(msg)
			if msg_id == "":
				print("msg handler error")			
			else:
				AckMsg(msg_id)			
	except Exception, e:
		print("error",e)
		return ""
	finally:
		if ws:
			ws.close()

def GetOrganizationId(email, project_id):
	org_req = {
			"Action": "GetOrganizationId",
			"UserEmail": email,
			"OrganizationAlias": project_id
	}
	org_res = net.sendHttpRequest(AddrIp, HttpAddr, org_req, 10)
	return org_res
