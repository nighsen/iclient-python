命令行工具
======================
这部分主要介绍iclientpy中所提供的命令行工具

没有你想要的工具的话，点 `这里 <https://github.com/SuperMap/iclient-python/issues>`_ 告诉开发人员。

这些命令行工具可以完成特定的任务。
安装iClient Python的时候这些命令行工具会一起安装。
如果只想使用这些命令行工具而不想安装iClient Python，或者是想在没有Python环境的机器上使用这些命令行工具，也可以下载独立运行包。

`点击下载win64命令行工具 <http://iclientpy.supermap.io/downloads/icpy-tools.zip>`_

`点击下载linux64命令行工具 <http://iclientpy.supermap.io/downloads/icpy-tools.tar>`_


* token工具_
* 缓存工具_
* iServer初始化工具_

token工具
******************
icpy-tokentool
生成token

示例：

对服务http://localhost:8090/iserver生成一个不做任何客户端验证的60分钟的token

    ::

        icpy-tokentool -l http://localhost:8090/iserver -u admin -p iserver -c NONE -e 60

详细参数：

-l ADDRESS, --uri ADDRESS          服务地址，如：http://localhost:8090/iserver
-u USERNAME, --user USERNAME       用户名
-p PASSWORD, --password PASSWORD   密码
-c CLIENT_TYPE, --client_type CLIENT_TYPE        发放令牌的方式。支持以下四个取值，分别对应四种发放令牌的方式：IP，即指定的 IP地址；Referer，即指定的 URL；RequestIP，即发送申请令牌请求的客户端IP；NONE，即不做任何验证。
-e EXPIRATION, --expiration EXPIRATION    申请令牌的有效期，默认单位为分钟，支持单位m(分)，h(小时)，d(天)，w(周)，M(月)，y(年)
--ip IP    clientType=IP 时，必选。 如果按照指定 IP 的方式申请令牌，则传递相应的 IP 地址。
--referer REFERER    clientType=Referer 时，必选。如果按照指定 URL 的方式申请令牌，则传递相应的 URL。
-h, --help    查看帮助


缓存工具
*****************
icpy-cachetool

recache
----------------------------
指定组件名称与地图名称，重新向存储id指明的存储位置增加新的切图

示例：

对服务map-World的World地图进行切图，且新的缓存存储在id是m的存储位置

    ::

        icpy-cachetool recache -l http://localhost:8090/iserver -t {tokenstr} -c map-World -m World -s m

**注：** {tokenstr}为占位字符串，生成token字符串请参考：token工具_

详细参数：

-l ADDRESS, --uri ADDRESS    服务地址，如：http://localhost:8090/iserver
-u USERNAME, --user USERNAME    用户名
-p PASSWORD, --password PASSWORD    密码
-t TOKEN, --token TOKEN    用于身份验证的token
-c COMPONENT_NAME, --component-name COMPONENT_NAME    待更新缓存服务名称
-m MAP_NAME, --map-name MAP_NAME    切图地图名称
-s STORAGEID, --storageid STORAGEID    存储的id
-h, --help    查看帮助

cache
----------------------
指明切图参数进行切图

示例：

从本地的工作空间zip压缩包对map-smtiles-World服务的World地图进行全图缓存更新

    ::

        icpy-cachetool cache -l http://localhost:8090/iserver -t {tokenstr} -c map-smtiles-World -w C:\World.zip -m World -o '-180,90' -b '-180,-90,180,90'

从map-World服务对对map-smtiles-World服务的World地图进行全图缓存更新

    ::

        icpy-cachetool cache -l http://localhost:8090/iserver -t {tokenstr} -c map-smtiles-World -m World -o '-180,90' -b '-180,-90,180,90' --source-component map-World --update

**注：** {tokenstr}为占位字符串，生成token字符串请参考：token工具_

详细参数：

-l ADDRESS, --uri ADDRESS   服务地址，如：http://localhost:8090/iserver
-u USERNAME, --user USERNAME    用户名
-p PASSWORD, --password PASSWORD    密码
-c COMPONENT_NAME, --component-name COMPONENT_NAME  待更新缓存服务名称
-w W_LOC, --w-loc W_LOC     工作空间路径
-m MAP_NAME, --map-name MAP_NAME    切图地图名称
-o ORIGINAL_POINT, --original-point ORIGINAL_POINT      切图原点，需以单引号开始和结束，如：'-180,90'
-b CACHE_BOUNDS, --bounds CACHE_BOUNDS  缓存范围，需以单引号开始和结束，如：'-180,-90,0,0'
-s SCALE, --scale SCALE     缓存比例尺分母，如：8000000,4000000,2000000
--service-type W_SERVICETYPE    工作空间服务类型
--tile-size TILE_SIZE   切片大小
--tile-type TILE_TYPE   切片类型
--format FORMAT     切片输出格式
--epsgcode EPSG_CODE    投影
--storageid STORAGEID   存储id
-rw     输入的工作空间地址是远程iServer所在服务器上的地址，不需要上传工作空间。
--quite     不需要确认，直接运行
--source-component SOURCE_COMPONENT_NAME    缓存更新数据来源服务
--update    更新服务缓存，与--source-component搭配使用
-h, --help    查看帮助



iServer初始化工具
***************************
对为进行初始化的iServer服务进行初始化

示例：

对地址是 http://localhost:8090/iserver 的iServer进行初始化，初始化用户名为supermap，密码为supermap

    ::

        icpy-initserver -l http://localhost:8090/iserver -u supermap -p supermap

详细参数：

-l ADDRESS, --uri ADDRESS   服务地址，如：http://localhost:8090/iserver
-u USERNAME, --user USERNAME    用户名
-p PASSWORD, --password PASSWORD    密码
-t TIMEOUT, --timeout TIMEOUT   超时时间，等待iServer启动的超时时间，单位为分钟







