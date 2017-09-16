# auto_course_select
A python program for selecting course automatically on http://grdms.bit.edu.cn , based on selenium

### Dependencies & Requirements
1. Windows 7/8/8.1/10, 32-bit or 64-bit
2. Python 2.7
3. Selenium python bindings (http://selenium-python.readthedocs.io/), can be installed with <p> pip install selenium </p>
4. Internet Explorer driver for Selenium (x64 binary (v3.5.1) and x86 binary (v3.5.0) are attached to this repo)

### Disclaimer
1. 我是在实验室的小伙伴换课的时候课被别人抢了，实在看不下去才写了这个
2. 在别人换课的间隙抢课不会违反校规，但是这种行为不太好
3. 为了避免选课出现奇怪的问题以及简化程序逻辑，这里使用了Web自动化测试工具Selenium，通过程序与页面的交互来模拟人的操作，不会直接向服务器发送数据包
4. 过度使用自动化工具会对服务器造成一定压力，请谨慎使用
5. 目前还没有进行完整的测试，在一些机器上可能会有很多问题
6. 因使用这个工具造成的一切后果与作者无关
