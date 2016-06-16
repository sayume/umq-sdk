package main

import (
	"fmt"
	httpclient "umq-sdk/go/http_v2"
)

func DoMsg(c chan string, Msg interface{}) {
	fmt.Println(Msg)
	c <- ""
	return
}

func main() {
	/*httpclient.OrganizationId = "org-xxx"
	httpclient.QueueId = "qid_1458720189|2"
	httpclient.HttpAddr = "http://192.168.153.41:6318"
	httpclient.PublisherToken = "9ffc96bbb62fd694298f2a90dc5df4c6"
	httpclient.ConsumerToken = "b49c4d7e09d29c762258f9860e69b7e3"
	httpclient.WsAddr = "http//192.168.153.41:6138/"
	httpclient.WsUrl = "ws://192.168.153.41:6318/ws"*/

	//发送消息
	//res, err := httpclient.PublishMsg("hello from xiaoding")
	//主动拉取消息
	//res, err := httpclient.GetMsg("10")
	//回执消息
	//res, err := httpclient.AckMsg("qid_1458720189|2-141381")
	err := httpclient.SubscribeQueue(DoMsg)
	if err != nil {
		fmt.Println(err)
		return
	}
	return
}
