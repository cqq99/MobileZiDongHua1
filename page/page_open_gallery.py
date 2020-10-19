import page
from basetest.basetest import Base


class OpenGallery(Base):
    #打开相册
    def page_open_gallery(self):
        self.base_open_app("com.android.gallery3d",".app.GalleryActivity")
    #点击进入相机
    def page_click_camera(self):
        self.base_click(page.gallery_click_camera)
    def page_open_gallery1(self):
        self.page_open_gallery()
        self.page_click_camera()
