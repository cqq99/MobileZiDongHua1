import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait

KEYCODE_HOME = 3
KEYCODE_MENU = 82
KEYCODE_BACK = 4


Connection_None=0
Connection_Airplane_Mode=1
Connection_Wifi_only=2
Connection_Data_only=4
Connection_All_network_on=6

class Base:
    def __init__(self,driver):
        self.driver=driver
    #查找元素
    def base_find_element(self,loc,timeout=3,poll=0.2):
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))
    #输入
    def base_input(self,value,loc):
        el=self.base_find_element(loc)
        el.clear()
        el.send_keys(value)
    #点击
    def base_click(self,loc):
        self.base_find_element(loc).click()
    #截图
    def base_get_screenshot(self):
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))
    #获取元素内容
    def base_get_text(self,loc):
        return self.base_find_element(loc).text
    #滑动
    def base_drop_and_drag(self,el1,el2):
        self.driver.drop_and_drag(el1,el2)
    #打开APP
    def base_open_app(self,package,activity):
        self.driver.start_activity(package,activity)
    #下载APP
    def base_install(self,appname):
        directory="../app/"+appname
        self.driver.install(directory)
    #卸载APP
    def base_uninstall(self,package):
        self.driver.remove(package)
    #长按
    def base_long_press(self,loc):
        TouchAction(self.driver).long_press(loc)
    #发送键到设备
    def base_press_keycode(self,keycode):
        if keycode=='返回':
            self.driver.press_keycode(KEYCODE_BACK)
        if keycode=='菜单':
            self.driver.press_keycode(KEYCODE_MENU)
        if keycode=='HOME':
            self.driver.press_keycode(KEYCODE_HOME)
    #返回
    def base_click_back(self):
        self.driver.press_keycode(KEYCODE_BACK)
    #菜单
    def base_click_menu(self):
        self.driver.press_keycode(KEYCODE_MENU)
    #Home键
    def base_click_home(self):
        self.driver.press_keycode(KEYCODE_HOME)
    #设置手机网络
    def base_set_network(self,status):
        if status=='无':
            self.driver.set_network_connection(Connection_None)
        if status=='飞行模式':
            self.driver.set_network_connection(Connection_Airplane_Mode)
        if status=='所有':
            self.driver.set_network_connection(Connection_All_network_on)
        if status=='流量':
            self.driver.set_network_connection(Connection_Data_only)
        if status=='WIFI':
            self.driver.set_network_connection(Connection_Wifi_only)
    #获取手机网络
    def base_get_network(self):
        return self.driver.network_connection
    #打开通知栏
    def base_open_notification(self):
        self.driver.open_notification()
    #切换上下文
    def base_switch_to_context(self,context):
        self.driver.switch_to.context(context)