import sys
import pyautogui as pag
from time import sleep,time

pag.PAUSE = 0
def key():
    b = input('准备好后请按下回车（请先切换成美式键盘输入）：')
    print('你的发送键是:\n1. Ctrl Enter\n2. Enter')
    sendkey = int(input(''))
    if sendkey != 1 and sendkey != 2:
        print('错误的输入')
        sys.exit()
    c = input('请输入您需要多少次输入：')
    c = int(c)
    print('请注意，您需要在8秒内切换到需要输入的窗口。')
    sleep(8)
    print('开始工作！')
    e = time()
    for i in range(c):
        pag.hotkey('Ctrl', 'V')
        if sendkey == 1:
        	pag.hotkey('Ctrl', 'Enter')
        if sendkey == 2:
            pag.press('Enter')
    f = time() - e
    input('完成。用时%f秒。' % f)
key()
