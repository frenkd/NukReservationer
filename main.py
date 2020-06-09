from selenium import webdriver
from time import sleep
from secrets import pw, username

class NukReservation:
  def __init__(self, username, pw):
    self.driver = webdriver.Chrome('./chromedriver')
    self.username = username

    self.driver.get("https://mreznik.nuk.uni-lj.si/rezervacija-citalnice")
    sleep(3)
    self.driver.find_element_by_xpath('//input[@name=\"login[cardnumber]\"]').click()
    sleep(2)
    self.driver.find_element_by_xpath('//input[@name=\"login[cardnumber]\"]')\
      .send_keys(username)
    print("USERNAME INPUT SUCCESFUL\n")
    sleep(2)
    self.driver.find_element_by_xpath('//input[@name=\"login[password]\"]').click()
    sleep(2)
    self.driver.find_element_by_xpath('//input[@name=\"login[password]\"]')\
      .send_keys(pw)
    print("PASSWORD INPUT SUCCESFUL\n")
    sleep(2)
    self.driver.find_element_by_xpath('//button[@type="submit"]').click()
    sleep(4)
    print("LOGGED IN!\n")
    
    

    # SELECT ALL
    self.driver.find_element_by_xpath('//label[@for="selectAllSwitch1"]').click()
    print("Selected all!\n")
    sleep(0.5)

    self.driver.execute_script("window.scrollTo(0, 50)") 
    print("SCROLLED\n")
    sleep(1)

    self.driver.find_element_by_xpath("//button[contains(text(), 'Rezerviraj')]").click()
    print("REZERVIRANO!")
    sleep(0.5)

    print("END\n") 
    sleep(4)



my_bot = NukReservation(username, pw)
