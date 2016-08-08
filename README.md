# umq-sdk

## 操作queue

CreateQueue

Parameters

|   Name    |  Type   |               Description                | Required |
| :-------: | :-----: | :-------------------------------------- | :------: |
|  Region   | String  |                   地区Id                   |   Yes    |
| CouponId  | String  |                  优惠券Id                   |    No    |
|  Remark   | String  |                  域名组描述                   |    No    |
| QueueName | String  |                业务组信息/队列名                 |   Yes    |
| PushType  | Integer |      发送方式, e.g "Direct" or "Fanout"      |   Yes    |
|    QoS    | String  | 是否需要对消费进行服务质量管控。枚举值为: "Yes",表示消费消息时客户端需要确认消息已收到(Ack模式)；"No",表示消费消息时不需要确认(NoAck模式)。默认为"Yes"。 |    No    |

Return

|  Name   |  Type   |      Description       |
| :-----: | :-----: | :-------------------- |
| err  |  error |       错误消息            |
| QueueId |  String  |      生成的queue的ID       |

DeleteQueue

Parameters

|   Name    |  Type   | Description | Required |
| :-------: | :-----: | :--------- | :------: |
|   Zone    | String  |    可用区Id    |   Yes    |
|  Region   | String  |    地区Id     |   Yes    |
| QueueIdList |  Array  |    队列Id     |   Yes    |

Return

|  Name   |  Type   |      Description       |
| :-----: | :-----: | :-------------------- |
| err  |  error |       错误消息            |
| DeleteFailed |  Array  | 删除失败的queue的Id |


ListQueue

显示队列的基本信息，以及生产者和消费者信息

Parameters

|   Name    |  Type   | Description | Required |
| :-------: | :-----: | :--------- | :------: |
|  Region   | String  |    地区Id     |   Yes    |
|   Limit   | Integer |   获取的数据量    |   Yes    |
|  Offset   | Integer |    数据偏移量    |   Yes    |

Return

|    Name    |  Type   |           Description           |
| :--------: | :-----: | :----------------------------- |
| err  |  error |       错误消息            |
| TotalCount | Integer |             返回的数据总量             |
|  QueueInfo   |  Array  | 对应用户某个region内的所有队列 |

QueueInfo

|    Name     |  Type   |          Description          |
| :---------: | :-----: | :--------------------------- |
|   QueueId   | String  |             队列ID              |
|  QueueName  | String  |           队列名/业务组信息           |
|  PushType   | String  | 发送方式,e.g "Direct" or "Fanout" |
|   MsgTTL    | Integer |            消息存活时间             |
| CreateTime  | Integer |            队列创建时间             |
| HttpAddr    | String  |            访问队列的http域名       |
|    QoS      | String  | 是否需要对消费进行服务质量管控。枚举值为: "Yes",表示消费消息时客户端需要确认消息已收到(Ack模式)；"No",表示消费消息时不需要确认(NoAck模式)。 |
| PublisherList    | Array  |            对列注册的publisher       |
| ConsumerList   | Array  |            队列注册的consumer       |

Publisher, Consumer

|    Name    |  Type   | Description |
| :--------: | :-----: | :--------- |
|     Id     | String  |   对应角色Id    |
|   Token    | String  | 对应角色授权Token |
| CreateTime | Integer |  对应角色产生时间   |

SetRole

Params

|   Name    |  Type   |         Description          | Required |
| :-------: | :-----: | :-------------------------- | :------: |
|  Region   | String  |             地区Id             |   Yes    |
|  QueueId  | String  |             队列Id             |   Yes    |
|    Num    | Integer |             角色个数             |   Yes    |
|   Role    | String  | 角色标签，e.g : "Pub"发布者，"Sub"消费者 |   Yes    |

Return

|  Name   |  Type   |      Description       |
| :-----: | :-----: | :-------------------- |
| err  |  error |       错误消息            |
| RoleInfo |  Array  | 对应授权角色信息, 具体参考RoleInfo  |

RoleInfo

| Name  |  Type  | Description |
| :---: | :----: | :---------: |
|  Id   | String |   对应角色Id    |
| Token | String | 对应角色授权Token |

DeleteRole

|   Name    |  Type   | Description | Required |
| :-------: | :-----: | :--------- | :------: |
|  Region   | String  |    地区Id     |   Yes    |
|  QueueId  | String  |    队列Id     |   Yes    |
|  RoleIdList   |  Array  |    角色Id     |   Yes    |
|   Role    | String  |    角色标签     |   Yes    |

Return

|  Name   |  Type   |      Description       |
| :-----: | :-----: | :-------------------- |
| err  |  error |       错误消息            |
| DeleteFailed |  Array  |    对应ID, 执行成功与否，0表示成功，其他值则为错误代码 |

## 消息操作

CreateClient

Parameters (UMQClient)

|      Name      |  Type   | Description | Required |
| :------------: | :-----: | :--------- | :------: |
|   OrganizationId     | Integer  |    组织ID     |   Yes    |
|    QueueId     | String  |    队列Id     |   Yes    |
|  ConsumerToken   | String  |    消费者Token    |   No    |
| PublisherToken | String  |  发布者Token   |   No    |
|    HttpAddr     | String  |   httpAPI地址   |   Yes    |
|    WsAddr     | String  |   ws地址   |   Yes    |
|    WsUrl     | String  |   ws url  |   Yes    |

Return
client instance

PublishMsg

Parameters

|      Name      |  Type   | Description | Required |
| :------------: | :-----: | :--------- | :------: |
|    Content     | String  |   发布的消息内容   |   Yes    |

Return

|      Name      |  Type   | Description | Required |
| :------------: | :-----: | :--------- | :------: |
|    success    | Bool  |      |   Yes    |
|    err    | String  |   错误消息   |   Yes    |

GetMsg

|      Name      |  Type   | Description | Required |
| :------------: | :-----: | :--------- | :------: |
|    Num     | Integer  |   消息条数   |   Yes    |

Return

|      Name      |  Type   | Description | Required |
| :------------: | :-----: | :--------- | :------: |
|    MsgList     | Array  |   消息数组   |   Yes    |
| err  |  error |       错误消息            |

AckMsg

no params

SubscribeQueue

|      Name      |  Type   | Description | Required |
| :------------: | :-----: | :--------- | :------: |
|    method     | func  |   ack function   |   Yes    |

GetOrganizationId

|      Name      |  Type   | Description | Required |
| :------------: | :-----: | :--------- | :------: |
|    AccountId     | String  |   用户ID   |   Yes    |
|    OrgId    | String  |   项目ID   |   Yes    |
| err  |  error |       错误消息            |

