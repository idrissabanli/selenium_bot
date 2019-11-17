import time
from selenium import webdriver



class LikePost():
    search_user = 'Mark Zuckerberg'
    login_email = 'idris1996@bk.ru'
    login_pass = ''

    def __init__(self):
        profile = webdriver.FirefoxProfile()

        profile.set_preference("dom.webnotifications.enabled", False)
        self.browser_driver = webdriver.Firefox(firefox_profile=profile, executable_path='/home/idris/Desktop/geckodriver')
        self.facebook_login()
        self.browser_driver.close()

    def facebook_login(self):
        self.browser_driver.get('https://facebook.com/')
        self.browser_driver.find_element_by_name('email').send_keys(self.login_email)
        self.browser_driver.find_element_by_name('pass').send_keys(self.login_pass)
        try:
            self.browser_driver.find_element_by_name('login').click()
        except:
            self.browser_driver.find_element_by_id('u_0_2').click()
            
        self.search()

    def search(self):
        self.browser_driver.find_element_by_css_selector('[name="q"]').send_keys(self.search_user)
        self.browser_driver.find_element_by_css_selector('._4w98').click()
        self.browser_driver.implicitly_wait(20) # seconds
        self.browser_driver.find_element_by_css_selector('._6xu6').click()
        self.browser_driver.find_element_by_id('u_0_x')
        self.like_posts()
    
    def like_posts(self):
        self.browser_driver.execute_script("window.scrollTo(0, document.body.offsetHeight);")
        elements = self.browser_driver.find_elements_by_css_selector("._6a-y._3l2t._18vj")
        for element in elements:
            time.sleep(2)
            scroll_position = element.location
            self.browser_driver.execute_script("window.scrollTo(0,{});".format(scroll_position.get('y')-400))
            element.click()
            time.sleep(2)
        self.search_google()

    def search_google(self):
        self.browser_driver.get('https://google.com/')
        self.browser_driver.find_element_by_name('q').send_keys(self.search_user)
        time.sleep(2)
        self.browser_driver.find_element_by_name('btnK').click()
        self.browser_driver.find_element_by_css_selector('.q.qs').click()
        time.sleep(2)
        image_elements = self.browser_driver.find_elements_by_css_selector('.rg_i.Q4LuWd.tx8vtf:not([href="#"])')
        if not image_elements:
            image_elements = self.browser_driver.find_elements_by_css_selector('.rg_l:not([href="#"])')
        self.browser_driver.implicitly_wait(5) # seconds
        self.write_file(image_elements)
 

    def write_file(self, image_elements):
        for img_element in image_elements:
            img_element.click()
            try:
                image_url = self.browser_driver.find_element_by_css_selector('.n3VNCb[src]').get_attribute("src")
            except:
                image_url = self.browser_driver.find_element_by_css_selector('.irc_mi[src]').get_attribute("src")
            if not image_url:
                image_url = self.browser_driver.find_element_by_css_selector('.irc_mi[src]').get_attribute("src")
            print(image_url)
            with open('images.txt', 'a+') as f:
                f.write(image_url + '\n')

        

LikePost()
