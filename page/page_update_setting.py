import page
from basetest.basetest import Base


class UpdateSetting(Base):
    #打开设置
    def page_open_setting(self):
        self.base_open_app("com.android.settings",".Settings")
    #点击Display
    def page_click_display(self):
        self.base_click(page.setting_click_display)
    #点击Sleep
    def page_click_sleep(self):
        self.base_click(page.setting_click_sleep)
    #选择30分钟
    def page_click_thirsty(self):
        self.base_click(page.setting_click_thirsty)
    #组合函数
    def page_update_setting(self):
        self.page_open_setting()
        self.page_click_display()
        self.page_click_sleep()
        self.page_click_thirsty()