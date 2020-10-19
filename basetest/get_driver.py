from appium import webdriver


class GetDriver:
    driver=None
    def get_driver(self,version,deviceName,port):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': deviceName,  # adb devices查到的设备名
            'platformVersion': version,
            'appPackage': 'com.android.launcher3',  # 被测App的包名
            'appActivity': '.Launcher',  # 启动时的Activity
                # 'app':PATH('E:\yymobile_client-7.7.1.apk')
            }
        self.driver = webdriver.Remote('http://localhost:'+port+'/wd/hub', desired_caps)
        return self.driver
    def quit_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None