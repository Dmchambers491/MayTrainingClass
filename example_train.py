from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get('https://the-internet.herokuapp.com/')
driver.maximize_window()
driver.find_element_by_link_text('Dynamic Loading').click()
driver.find_element_by_xpath('//*[@id="content"]/div/a[2]').click()
driver.find_element_by_tag_name('button').click()

finished = (By.XPATH, '//*[@id="finish"]/h4')
wait = WebDriverWait(driver, 60)
wait.until(EC.visibility_of_element_located(finished))

try:
        assert driver.find_element(finished[0], finished[1]).is_displayed(), \
                "Hello World message did not appear"
except AssertionError as e:
        print(e)
finally:
        driver.close()

# assert driver.find_element_by_id('finish').is_displayed(), "%s was not displayed" % \
#                 (driver.find_element_by_id('finish'))
# driver.close()

# Code for wrong flash message
# name = driver.find_element_by_name('username')
# name.send_keys('Dchambers')
# password = driver.find_element_by_name('password')
# password.send_keys('Wrongpassword!')
# driver.find_element_by_class_name('radius').click()

# element = driver.find_element_by_class_name('error')
# assert element.is_displayed(), "Flash did not appear"
# assert "Your username is invalid!" in element.text
# driver.close()

# for link in links:
#         print(link.get_attribute('href'))
# driver.close()

# driver.get('https://www.Facebook.com')
# driver.maximize_window()
# element = driver.find_element_by_name('email')
# element.send_keys('darreal.chambers@yahoo.com')
# ele2 = driver.find_element_by_name('pass')
# ele2.send_keys('59d23m45c')
# log = driver.find_element_by_id('u_0_2').click()
# drop = driver.find_element_by_id('userNavigationLabel').click()
# log_out = driver.find_element_by_class_name('_54ni navSubmenu _6398 _64kz __MenuItem').click()


# tags = driver.find_element_by_tag_name('a')
#
# for tag in tags:
#         print(tag.text)
#         print(tag.get_attribute('a'))
# driver.close()


# example_list = []
# example_list.append(1)
# example_list.append("asdsad")
# example_list.append([])
# example_list.append({})
#
# for e in example_list:
#     print(e)
#
# dictionary_example = {}
# dictionary_example_1 = {'key_1': "value_1", 'key_2': 1, 'key_3': [1, 2, 3, 4]}
#
# value = dictionary_example['key_2']
#
# for key in dictionary_example.keys():
#     print (dictionary_example[key])
#
# example_string = "Hello World"
# example_string_2 = "HeLLo World"
# example_string_3 = "Hello_World"
#
# example_string.upper()
# example_string.lower()
# example_string.capitalize()
#
#
# print(example_string[0])
# example_string_3 = example_string_3.strip()
# example_string_3 = example_string_3.replace('_', ' ')

