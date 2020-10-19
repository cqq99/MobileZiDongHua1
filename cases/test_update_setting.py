import os,sys

import pytest

sys.path.append(os.getcwd())
from basetest.get_driver import GetDriver
from page.page_update_setting import UpdateSetting


class TestUpdateSetting:

    #初始化函数
    #def setup_method(self):

    #销毁函数
    def teardown_method(self):
        GetDriver().quit_driver()
    #测试函数
    @pytest.mark.skipif(True, reason="ok")
    def test_update_setting(self,version,devicename,port):
        self.devicename = devicename
        self.port = port
        self.update_setting = UpdateSetting(GetDriver().get_driver(version, port=self.port, deviceName=self.devicename))
        self.update_setting.page_update_setting()