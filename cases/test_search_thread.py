import os, sys
import threading

import allure
import pytest

sys.path.append(os.getcwd())

from basetest.get_driver import GetDriver
from page.page_search import PageSearch
from tools.get_data import GetData


class TestSearch:
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("args",GetData().anylyze_file("search.yml"))
    def test_search_on(self,args):
        devices = GetData().anylyze_file(file_name="peizhi.yml")
        #value = "setting"
        value=args["value"]
        for device in devices:
            self.search = PageSearch(
                GetDriver().get_driver(version=device["platformVersion"], deviceName=device["deviceName"],
                                       port=device["port"]))
            threading.Thread(target=self.search.page_search, args=(value,)).start()
