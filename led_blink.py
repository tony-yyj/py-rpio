# coding: utf-8
import RPi.GPIO as GPIO

import time
# 选择引脚的模式为板载模式
GPIO.setmode(GPIO.BCM)
# 将18号引脚设置为输出模式
GPIO.setup(18, GPIO.OUT)

while True:
    # 将18号输出引脚设置为高电平
    GPIO.output(18, True)
    time.sleep(0.5)
    # 低电平
    GPIO.output(18, False)
    # 休眠500毫秒
    time.sleep(0.5)


