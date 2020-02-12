# Automated_Powercycle_Test
基于树莓派+小米插座Wi-Fi版的自动化开关机测试脚本

## 这个项目是用来做什么的？
通过[python-miio](https://github.com/rytilahti/python-miio)，使得我们可以直接通过树莓派给小米插座下发指令，进行开关小米插座的操作，从而达到自动化开关机的目的

## 如何使用？
1.首先你需要一个树莓派(需要无线网卡)， 一个小米插座Wi-Fi版，以及一个用以配置小米插座的网关

2.配置好插座，并让树莓派与插座处于同一内网下

3.在你的树莓派上安装相关环境，并获取你的小米设备的Token，具体操作过程可以参考我的一篇Blog: [Directly control my XiaoMi Adapter(Wi-Fi Edition) without Mi Home App](https://github.com/yanqiaoyu/Sth-Worth-Recording/blob/master/directly-control-my-mi-plug-wi-fi-edition-without-mi-home-app.md)

4.下载此脚本至你的树莓派上
```shell
git clone https://github.com/yanqiaoyu/Automated_Powercycle_Test.git
```

5.根据需要修改脚本中配置
```python
#插座的IP
PlugIP = '192.168.xxx.xxx'
#你插座配置好之后的Token，注意如果重新配置了插座，会导致Token变化
PlugToken = 'YourToken'
#待测样机的IP，用以开机之后检查连通性
DutIP = 'xxx.xxx.xxx.xxx'
#开关机测试一共 需要的次数
TestCount = 100
```
6.运行脚本
```shell
python3 powercycle.py
```

## 待完成
- [ ] 目前还不能判读无线接口的连通性，后续会结合另一个项目进行尝试
- [ ] 测试日志可以保存( >>> x.txt也不是不可以)
- [ ] 针对日志中的数据进行可视化输出(可选,看心情)
