import base64
import time
import cv2
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome()

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => false
    })
  """
})



url ='https://webvpn.lntu.edu.cn/http-8080/77726476706e69737468656265737421fae05988693c66446b468ca88d1b203b/eams/homeExt.action;jsessionid=8DBDEF1B2FE63A7DA440DD188543A3BE#'
driver.get(url)
driver.find_element_by_css_selector('#username').send_keys('账号')
driver.find_element_by_css_selector('#password').send_keys('密码')
driver.find_element_by_css_selector('#login_submit').click()

time.sleep(2)
full_js = driver.find_element_by_id('slider-img1')
full_js2 = driver.find_element_by_id('slider-img2')
# print(full_js)
image_url = full_js.get_attribute('src')
image_url2 = full_js2.get_attribute('src')
# print(image_url)
base64str = image_url.split('base64,')[1]
base64str2 = image_url2.split('base64,')[1]
imgdata = base64.b64decode(base64str)
imgdata2 = base64.b64decode(base64str2)

# full_image = driver.execute_script('image_url',)
# response = requests.get(image_url)
with open('bigimg.png', 'wb') as file:
        file.write(imgdata)
with open('smallimg.png', 'wb') as file:
    file.write(imgdata2)


img = cv2.imread('bigimg.png',0)
template = cv2.imread('smallimg.png',0)
res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED) #使用cv2平方差匹配来取值

value = cv2.minMaxLoc(res)[2][0]
print(value)
dis = (value * 280) /590
print(dis)





h = driver.find_element(By.XPATH, '//div[@class="slider"]')
action = ActionChains(driver)
action.click_and_hold(h).perform()
action.move_by_offset(dis,0)
action.release().perform()
#
# ame(f)
# driver.switch_to.fr
# time.sleep(3)
#
#
add = driver.find_element_by_xpath('//*[@id="main-nav"]/ul/li[2]/a').click()
time.sleep(1)

cdd = driver.find_element_by_xpath('//*[@id="main-nav"]/ul/li[2]/ul/li[5]/a').click()

driver.switch_to.frame('iframeMain')
ddd = driver.find_element_by_xpath('//*[@id="semesterGrade"]')
time.sleep(1)
fff = driver.page_source
print(fff)
with open('lntushuju.html','w',encoding='utf-8')as fp:
    fp.write(fff)


