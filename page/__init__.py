#以下为设置的配置信息
from selenium.webdriver.common.by import By

setting_click_display=By.XPATH,"//*[contains(@text,'Display')]"
setting_click_sleep=By.XPATH,"//*[contains(@text,'Sleep')]"
setting_click_thirsty=By.XPATH,"//*[contains(@text,'30 minutes')]"
#以下为gallery的配置信息
gallery_click_camera=By.XPATH,"//*[contains(@text,'Camera')]"
#以下为搜索的配置信息
search_button=By.ID,"com.android.settings:id/search"
search_input=By.ID,"android:id/search_src_text"