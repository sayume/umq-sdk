#!/usr/lib/python2
#coding=utf8
#umq sdk python版
#http相关

import httplib
import urllib

def sendHttpRequest(ip, url_path, data, time_out):
	try:
		conn = httplib.HTTPConnection(ip, 6318, time_out)
		headers = {"Content-type": "application/x-www-form-urlencoded",
					"Accept": "text/plain"}
		body_data = urllib.urlencode(data)
		conn.request("POST", "/", body_data, headers)
		response = conn.getresponse()
		res = response.read()
		return res
	except Exception, e:
		print("send http request error:", e)
		return ""
	finally:
		if conn:
			conn.close()
