import os, sys

import pytest

sys.path.append(os.getcwd())

from basetest.get_driver import GetDriver
from page.page_search import PageSearch
from tools.get_data import GetData


class TestSearch:
    #@pytest.mark.parametrize()
    @pytest.mark.skipif(True, reason="ok")
    def test_search_on(self):
        devices = GetData().anylyze_file(file_name="peizhi.yml")
        for device in devices:
            self.search = PageSearch(
                GetDriver().get_driver(version=device["platformVersion"], deviceName=device["deviceName"],
                                       port=device["port"]))
            self.search.page_search(evalue="112")
