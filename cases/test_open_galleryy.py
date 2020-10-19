import pytest
import os,sys

sys.path.append(os.getcwd())
from basetest.get_driver import GetDriver
from page.page_open_gallery import OpenGallery


class TestOpenGallery:

    #def setup_method(self):

    def teardown_method(self):
        GetDriver().quit_driver()

    @pytest.mark.skipif(True,reason="ok")
    def test_open_gallery(self,version, devicename, port, isNew):
        self.devicename = devicename
        self.port = port
        self.open_gallery = OpenGallery(
            GetDriver().get_driver(version, deviceName=self.devicename, port=self.port))
        self.open_gallery.page_open_gallery1()
