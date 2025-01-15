# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium import webdriver
# from time import sleep
#
# PRODUCT_FIELD = "//button[contains(@name, 'backpack')]"
# CART_FIELD = "//div[@id='shopping_cart_container']/span"
# CART_INDEX_FIELD = "//div[@id='shopping_cart_container']/span/a"
#
# with webdriver.Chrome() as br:
#     br.get('https://www.saucedemo.com/')
#
#     br.find_element(By.XPATH, "//input[@id='user-name']").send_keys('standard_user')
#     br.find_element(By.XPATH, "//input[@id='password']").send_keys('secret_sauce')
#     br.find_element(By.XPATH, "//input[@id='login-button']").click()
#     br.find_element(By.XPATH, "//button[contains(@name, 'backpack')]").click()
#
#     assert br.find_element(By.XPATH, "//a[@class='shopping_cart_link']/span").text == '1', 'Товар не добавлен'
#
#     br.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
#
#     target = float(br.find_element(By.XPATH, "//div[@class='inventory_item_price']").text[1:])
#
#     br.find_element(By.XPATH, "//button[@name='checkout']").click()
#
#
#     br.find_element(By.XPATH, "//input[@name='firstName']").send_keys('1')
#     br.find_element(By.XPATH, "//input[@name='lastName']").send_keys('1')
#     br.find_element(By.XPATH, "//input[@name='postalCode']").send_keys('1')
#     br.find_element(By.XPATH, "//input[@name='continue']").click()
#     sleep(2)
#     """Сравнение цены"""
#     tax = float(br.find_element(By.XPATH, "//div[@class='summary_tax_label']").text.split().pop(1)[1:])
#     total = float(br.find_element(By.XPATH, "//div[@class='summary_total_label']").text.split().pop(1)[1:])
#     check_total = total*100 - tax*100
#     check_total /= 100
#     print(check_total)
#     assert total*100 - tax*100 == target*100, 'Цена товара другая'
