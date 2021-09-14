from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import collections

global str_temp_name

class mainpage():
    title = "Find WW Studios & Meetings Near You | WW USA"

    #__init__() method
    def __init__(self,drv):
        self.drv = drv

    #Question 2
    #Assert loaded page title contains “Find WW Studios & Meetings Near You | WW USA”
    def test_title(self):
        print("Question 2 answer")
        print("-------------------")
        try:
            WebDriverWait(self.drv, 10).until(EC.title_contains("Find WW Studios & Meetings Near You | WW USA"))
            print(self.drv.title)
            print('Assertion test passed')
        except Exception as e:
            print("Assertion test failed")

    #Question 3
    # Under Find your Workshop, click on Studio
    def click_studio(self):
        print("Question 3 answer")
        print("-------------------")
        try:
            vg = self.drv.find_element_by_xpath("//span[contains(text(),'Studio')]")
            #print(vg.text)
            self.drv.implicitly_wait(15)
            vg.click()
            self.drv.implicitly_wait(15)
            print("Clicked on Studio")
        except Exception as e:
            print("Cannot click on Studio")

    #Question 4
    #In the search field, search for meetings for zip code: 10011
    def search_meetings(self):

        print("Question 4 answer")
        print("-------------------")
        try:
            self.drv.find_element_by_id("location-search").clear()
            self.drv.implicitly_wait(15)
            self.drv.find_element_by_id("location-search").send_keys("10011")
            self.drv.implicitly_wait(15)
            self.drv.find_element_by_id("location-search-cta").click()
            self.drv.implicitly_wait(15)
            print("Searching meetings")
        except Exception as e:
            print("Cannot search for meetings")

    #Question 5
    #Print the title of the first result and the distance (located on the right of location title/name)
    def print_firstResult_name_distance(self):
        global str_temp_name
        print("Question 5 answer")
        print("-------------------")
        try:
            print("TestCase: Name and distance for the first result are:")
            names_list = self.drv.find_element_by_id("search-results")
            list_temp = names_list.text
            str_temp_name = "\n".join(list_temp.splitlines()[0:1])
            print("\n".join(list_temp.splitlines()[0:2]))
        except Exception as e:
            print("No data")

    #Question 6
    #Click on the first search result and then verify displayed location name/title matches with
    #the name of the first searched result that was clicked
    def verify_first_search_result(self):
        global str_temp_name
        print("Question 6 answer")
        print("-------------------")
        try:
            self.drv.find_element_by_xpath("//*[@id='search-results']//div[1]//a[1]").click()
            self.drv.implicitly_wait(15)
            individual_place = self.drv.find_element_by_xpath("//*[@class='studioAddress-3O7LI']//div[1]//*//h1[1]").text
            if str_temp_name == individual_place:
                print("Matches with first result")
            else:
                print("Does not match with first result")
        except Exception as e:
            print("Exception")

    #Question 7
    #Click on Business Hours for first search result
    def click_Business_hours(self):
        print("Question 7 answer")
        print("-------------------")
        try:
            self.drv.find_element_by_xpath("//*[@class='studioAddress-3O7LI']//div[1]//*//*[contains(@class,'hours')]").click()
            self.drv.implicitly_wait(15)
            print("Clicked on business hours")
        except Exception as e:
            print("Cannot click on business hours")

    #Question 8
    #Create a method to print all the business hours for that studio
    def print_business_hours(self):
        list1 = []
        d = collections.defaultdict(list)
        print("Question 8 answer")
        print("-------------------")
        try:
            self.drv.implicitly_wait(15)
            operating_hours = self.drv.find_elements_by_xpath("//*[@class='studioAddress-3O7LI']//div[1]//*//*[contains(@class,'hours')]//div[2]//div")
            '''
            #saving the business hours to a tmp.txt file under POM/Pages folder
            my_path = os.path.abspath(os.path.dirname(__file__))
            tmp = "tmp.txt"
            path = os.path.join(my_path, tmp)
            with open(path, 'w+') as file:
                for i in operating_hours:
                    file.write(i.text)
                    #print(file.read(i.text))
    
            '''
            for i in operating_hours:
                list1.append(i.text)
            #print(list1)

            #We want to strip \n in all elements in this list
            stripped_list1 = [s.rstrip() for s in list1]

            #check if the list item contains "day" or hours and add them to dictionary
            for i in range(len(stripped_list1)):
                if "day" in stripped_list1[i]:
                    key_data = stripped_list1[i]
                else:
                    if "AM" or "PM" or "closed" in stripped_list1[i]:
                        d[key_data].append(stripped_list1[i])

            #print business hours
            for key in d.keys():
                print(key, *d[key], sep=' ')
        except Exception as e:
            print("Exception",e)

    # method to close and quit browser
    def tearDown(self):
        print("Closing the browser")
        self.drv.close()
        self.drv.quit()