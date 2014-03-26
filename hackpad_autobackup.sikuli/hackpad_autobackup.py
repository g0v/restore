import time
import datetime
import threading


# 控制螢幕和鍵盤滑鼠，針對一個hackpad定時自動備份


# 這個程式使用Sikuli1，請先安裝Sikuli
# http://www.sikuli.org
# 運作時會搶你的螢幕和鍵盤滑鼠，可多利用閒置的電腦來備份
#
# 運作時會一直備份，要關掉的話只要把Java平台關掉即可
#
#
# 以CC0授權改作使用


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


def backup(target, browser, editor):
    
    App.open(browser)    
    
    type('t', KeyModifier.CMD)
    
    wait(1)
    
    click("1395819851429.png")
        
    
    type(target)
    
    type(Key.ENTER)
    
    wait(5)
    
    click(Pattern("1395819956912.png").exact().targetOffset(-227,82)) #此為hackpad的左上角，每個電腦不同，截圖可能需要自己重拍

    
    
    wait(2)
    type(Key.DOWN * 20, KeyModifier.CTRL); #如果文件很大 20 次往下還不夠到底，請自行增加
    
    wait(2)
    
    keyDown(Key.SHIFT)
    
    click(Pattern("1395821225790.png").exact())   #此為hackpad的右下角，每個電腦不同，截圖可能需要自己重拍
    
    keyUp(Key.SHIFT)
    
    
    
    type('c', KeyModifier.CMD)
    
    
    App.open(editor)
    
    wait(2)
    
    type('n', KeyModifier.CMD)
    
    wait(2)
    
    type('v', KeyModifier.CMD)
    
    wait(2)
    
    type('s', KeyModifier.CMD)
    
    wait(2)
    
    paste(target + '__' + datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))

    wait(1)

    type(Key.ENTER)

    
def myBackup():   
    backup('https://hackpad.com/kJ4yjP1uGvH', 'Safari', 'TextEdit')     #一個hackpad網址, 瀏覽器, 近端文字編輯器


myBackup()                         # 先備份一次
set_interval(myBackup, 60*5)       # 之後每五分鐘備份一次

