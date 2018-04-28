# Wechat-Alert-for-Zabbix
zabbix微信告警脚本
参考文档：https://work.weixin.qq.com/api/doc#10167

程序编写环境：
<br>
os:centos7
<br>
python:2.7.5

本文档通过“touser”和“toparty”参数控制向用户或部门发送告警微信。执行如下：
<br>
启用toparty参数，向部门发送微信：
<br>
![Image text](https://github.com/loong576/Wechat-Alert-for-Zabbix/blob/master/img/wechat01.jpg)

![Image text](https://github.com/loong576/Wechat-Alert-for-Zabbix/blob/master/img/wechat02.jpg)

zabbix运行此脚本时需修改脚本所在目录属主和执行权限：
```Shell
[root@zabbix-server alertscripts]# chown -R zabbix:zabbix /etc/zabbix/alertscripts/
[root@zabbix-server alertscripts]# chmod -R 755 /etc/zabbix/alertscripts/
```

详细搭建过程及测试：
<br>
http://blog.51cto.com/3241766/2108769
