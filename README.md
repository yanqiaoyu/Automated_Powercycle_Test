# Automated_Powercycle_Test
基于树莓派+小米插座Wi-Fi版的自动化开关机测试脚本

## 这个项目是用来做什么的？
通过[python-miio](https://github.com/rytilahti/python-miio)，使得我们可以直接通过树莓派给小米插座下发指令，进行开关小米插座的操作，从而达到自动化开关机的目的

## 如何使用？
1.首先你需要一个树莓派(需要无线网卡)， 一个小米插座Wi-Fi版，以及一个用以配置小米插座的网关

2.配置好插座，并让树莓派与插座处于同一内网下

3.在你的树莓派上安装相关环境，并获取你的小米设备的Token，具体操作过程可以参考我的一篇Blog: [Directly control my XiaoMi Adapter(Wi-Fi Edition) without Mi Home App](https://github.com/yanqiaoyu/Sth-Worth-Recording/blob/master/directly-control-my-mi-plug-wi-fi-edition-without-mi-home-app.md)

4.
