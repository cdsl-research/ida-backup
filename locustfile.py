# selenium を使ってアクセス
# from locust import HttpUser, TaskSet, task, constant
# import string
# import random
# import time

# class UserBehavior(TaskSet):
#     def on_start(self):
#         """ on_start is called when a Locust start before any task is scheduled """
#         #self.comment()

#     @task(1)
#     def comment(self):
#         from selenium import webdriver

#         options = webdriver.ChromeOptions()
#         options.add_argument('--headless')

#         driver = webdriver.Chrome(options=options)
#         driver.get('http://192.168.100.61/')

# class WebsiteUser(HttpUser):
#     tasks = {UserBehavior:1}
#     wait_time = constant(0)

# spliter を使ってアクセス
# from locust import HttpUser, TaskSet, task, constant
# import string
# import random
# import time

# class UserBehavior(TaskSet):
#     def on_start(self):
#         """ on_start is called when a Locust start before any task is scheduled """
#         #self.comment()

#     @task(1)
#     def comment(self):
#         from splinter import Browser

#         with Browser('chrome', headless=True) as browser:
#             foo = ["36", "34", "45", "41", "32", "43"] # ガム，チョコ，ふがし，ポッキー，ポテチ，モナカ
#             browser.visit(WebsiteUser.host)
#             browser.visit(WebsiteUser.host + "shop/?add-to-cart=" + random.choice(foo))
#             # browser.visit(WebsiteUser.host + "checkout/")
#             # button = browser.find_by_name('woocommerce_checkout_place_order')
#             # button.click()
#             # browser.quit()

# class WebsiteUser(HttpUser):
#     host = 'http://192.168.100.61/'
#     tasks = {UserBehavior:1}
#     wait_time = constant(10)

# locust を使ってアクセス
# from locust import HttpUser, TaskSet, task, constant
# import string
# import random
# import time
# import re
# import os
# import json
# import traceback

# class CaseInsestiveDict(dict):
#     def __getitem__(self,key):
#         return super(CaseInsestiveDict,self).__getitem__(key.lower())

# class UserBehavior(TaskSet):

#     def on_start(self):
#         """ on_start is called when a Locust start before any task is scheduled """
#         #self.comment()

#     @task(1)
#     def comment(self):
#         self.client.get(WebsiteUser.host)
#         self.client.get(WebsiteUser.host + "shop/")
#         headers= {
#             "Content_Type": "application/x-www-form-urlencoded"
#         }
#         num_item = random.randint(1, 10)
#         foo = ["36", "34", "45", "41", "32", "43"] # ガム，チョコ，ふがし，ポッキー，ポテチ，モナカ
#         data = {
#             "product_sku": "",
#             "product_id": f"{random.choice(foo)}", 
#             "quantity": f"{num_item}"
#         }
#         try:
#             res = self.client.post(WebsiteUser.host + "?wc-ajax=add_to_cart", data, headers=headers)
#             res_dict = json.loads(res.text)
#             res_html = res_dict["fragments"]["div.widget_shopping_cart_content"]
#             res_simple_text = re.sub("<[^>]+>", " ", res_html)
#             print("")
#             print(f"res.status_code = {res.status_code}")
#             print("")
#             print(f"res.cookies = {res.cookies}")
#             print("")
#             print(f"res.text = {res_simple_text.split()}")
#             print("")
#         except Exception as e:
#             print(traceback.print_exc())
#             print("------------------------")
#             print("res1")
#             print("text",str(type(res.text)))
#             print("statusCode: ", str(res.status_code))
#             print("res-Json", res.text)
#             print("------------------------")

#         try:
#             res2 = self.client.get(WebsiteUser.host + "checkout/", cookies=res.cookies)
#             res2_nonce_list = re.findall("\"woocommerce-process-checkout-nonce\" value=\"\w+", res2.text)
#             res2_nonce = res2_nonce_list[0]
#             print(f"res2.status_code = {res2.status_code}")
#             print("")
#             print(f"res2.nonce = {res2_nonce[-10:]}, {type(res2_nonce)}, {res2_nonce_list}")
#             print("")
#         except Exception as e:
#             print(traceback.print_exc())
#             print("------------------------")
#             print("res2")
#             print("text",str(type(res2.text)))
#             print("statusCode: ", str(res2.status_code))
#             print("------------------------")

#         personal_data = {
#             "billing_last_name": "井田",
#             "billing_first_name": "尚樹",
#             "billing_company": "",
#             "billing_country": "JP",
#             "billing_postcode": "123-4567",
#             "billing_state": "JP13",
#             "billing_city": "a",
#             "billing_address_1": "11",
#             "billing_address_2": "",
#             "billing_phone": "1123456789",
#             "billing_email": "c0b2001930@edu.teu.ac.jp",
#             "shipping_last_name": "井田",
#             "shipping_first_name": "尚樹",
#             "shipping_company": "",
#             "shipping_country": "JP",
#             "shipping_postcode": "123-4567",
#             "shipping_state": "JP13",
#             "shipping_city": "a",
#             "shipping_address_1": "11",
#             "shipping_address_2": "",
#             "order_comments": "", 
#             "shipping_method[0]": "free_shipping:1",
#             "payment_method": "cod",
#             "mailpoet_woocommerce_checkout_optin_present": "1",
#             "woocommerce-process-checkout-nonce": f"{res2_nonce[-10:]}",
#             "wp_http_referer": "http://192.168.100.61/checkout/"
#         }
#         try:
#             res3 = self.client.post(WebsiteUser.host + "/?wc-ajax=checkout", personal_data, cookies=res.cookies)
#             # print(f"res3.status_code = {res3.status_code}")
#             # print("")
#             # print(f"res3.text = {res3.text}")
#             # print("")
#         except Exception as e:
#             print(traceback.print_exc())
#             print("------------------------")
#             print("res3")
#             print("text",str(type(res3.text)))
#             print("statusCode: ", str(res3.status_code))
#             print("res-Json", res3.text)
#             print("------------------------")
            
# class WebsiteUser(HttpUser):
#     host = 'http://192.168.100.61/'
#     tasks = {UserBehavior:1}
#     wait_time = constant(0)


from locust import HttpUser, TaskSet, task, constant
import string
import random
import time
import re
import os
import json
import traceback

class CaseInsestiveDict(dict):
    def __getitem__(self,key):
        return super(CaseInsestiveDict,self).__getitem__(key.lower())

class UserBehavior(TaskSet):
    headers= {
        "Content_Type": "application/x-www-form-urlencoded"
    }

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        #self.comment()

    @task(29)
    def index(self):
        self.client.get("/shop")
    
    @task(61)
    def addToCart(self):
        foo = ["36", "34", "45", "41", "32", "43"] # ガム，チョコ，ふがし，ポッキー，ポテチ，モナカ
        num_item = random.randint(1, 10)
        data = {
            "product_sku": "",
            "product_id": f"{random.choice(foo)}", 
            "quantity": f"{num_item}"
        }
        self.res = self.client.post("/?wc-ajax=add_to_cart", data, headers=self.headers)
    
    @task(10)
    def checkout(self):
        self.addToCart()
        self.res2 = self.client.get("/checkout/", cookies=self.res.cookies)
        self.res2_nonce_list = re.findall("\"woocommerce-process-checkout-nonce\" value=\"\w+", self.res2.text)
        self.res2_nonce = self.res2_nonce_list[0]
        personal_data = {
            "billing_last_name": "井田",
            "billing_first_name": "尚樹",
            "billing_company": "",
            "billing_country": "JP",
            "billing_postcode": "123-4567",
            "billing_state": "JP13",
            "billing_city": "a",
            "billing_address_1": "11",
            "billing_address_2": "",
            "billing_phone": "1123456789",
            "billing_email": "c0b2001930@edu.teu.ac.jp",
            "shipping_last_name": "井田",
            "shipping_first_name": "尚樹",
            "shipping_company": "",
            "shipping_country": "JP",
            "shipping_postcode": "123-4567",
            "shipping_state": "JP13",
            "shipping_city": "a",
            "shipping_address_1": "11",
            "shipping_address_2": "",
            "order_comments": "", 
            "shipping_method[0]": "free_shipping:1",
            "payment_method": "cod",
            "mailpoet_woocommerce_checkout_optin_present": "1",
            "woocommerce-process-checkout-nonce": f"{self.res2_nonce[-10:]}",
            "wp_http_referer": "http://192.168.100.61/checkout/"
        }
        self.client.post("/?wc-ajax=checkout", personal_data, cookies=self.res.cookies)
class WebsiteUser(HttpUser):
    host = 'http://192.168.100.61/'
    tasks = {UserBehavior}
    wait_time = constant(0)