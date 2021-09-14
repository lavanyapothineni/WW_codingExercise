from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


from MainPage import mainpage

browserName = "chrome"

if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "safari":
    driver = webdriver.Safari()
else:
    print("Please pass the correct browser name")


#URL
base_URL = "https://www.weightwatchers.com/us/find-a-workshop/"

#Question:1
#Launch the browser (by default I am using chrome)
def set_up():
    driver.get(base_URL)
    print("Question 1 Answer")
    print("--------------------")
    print("Launched browser")

#Call MainPage methods
def test_mainPage():
    mp = mainpage(driver)
    mp.test_title()
    mp.click_studio()
    mp.search_meetings()
    mp.print_firstResult_name_distance()
    mp.verify_first_search_result()
    mp.click_Business_hours()
    mp.print_business_hours()
    mp.tearDown()


#calling methods
set_up()
test_mainPage()
