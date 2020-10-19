import allure


import page
from basetest.basetest import Base
import os,sys

sys.path.append(os.getcwd())


class PageSearch(Base):
    #打开设置
    @allure.step(title="打开设置")
    def page_open_setting(self):
        self.base_open_app("com.android.settings", ".Settings")
    #点击搜索按钮
    @allure.step(title="点击搜索按钮")
    def page_click_search(self):
        self.base_click(page.search_button)
    #输入搜索内容
    @allure.step(title="输入搜索内容")
    def page_input_search(self,evalue):
        allure.attach("输入的内容为：",evalue,allure.attachment_type.TEXT)
        self.base_input(loc=page.search_input,value=evalue)
        allure.attach("执行结果截图：",self.base_get_screenshot(),allure.attachment_type.PNG)
    #组合方法
    def page_search(self,evalue):
        self.page_open_setting()
        self.page_click_search()
        self.page_input_search(evalue)