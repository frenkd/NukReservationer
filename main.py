import sys
from selenium import webdriver
from time import sleep
from secrets import pw, username, guser, gpass
import smtplib
from datetime import datetime


class NukReservation:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome('./chromedriver')
        self.username = username

        self.driver.get("https://mreznik.nuk.uni-lj.si/rezervacija-citalnice")
        sleep(3)
        self.driver.find_element_by_xpath(
            '//input[@name=\"login[cardnumber]\"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//input[@name=\"login[cardnumber]\"]')\
            .send_keys(username)
        print("USERNAME INPUT SUCCESFUL\n")
        sleep(2)
        self.driver.find_element_by_xpath(
            '//input[@name=\"login[password]\"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//input[@name=\"login[password]\"]')\
            .send_keys(pw)
        print("PASSWORD INPUT SUCCESFUL\n")
        sleep(2)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(4)
        print("LOGGED IN!\n")

        self.location = sys.argv[1] if len(sys.argv) > 1 else ""
        
        if (self.location == "vc" or not self.location):
            print("TRYING FOR VELIKA ČITALNICA!\n")
            # SELECT ALL
            self.driver.find_element_by_xpath(
                '//label[@for="selectAllSwitch1"]').click()
            print("Selected all!\n")
            sleep(0.5)

            self.driver.execute_script("window.scrollTo(0, 50)")
            print("SCROLLED\n")
            sleep(1)

            self.driver.find_element_by_xpath(
                "//button[contains(text(), 'Rezerviraj')]").click()
            print("REZERVIRANO!")
            sleep(0.5)
        elif (self.location == "cc"):
            print("TRYING FOR ČASOPISNA ČITALNICA!\n")
            # scroll into view
            element = self.driver.find_element_by_xpath(
                "//strong[contains(text(), 'Časopisna čitalnica')]")
            self.driver.execute_script(
                "arguments[0].scrollIntoView();", element)
            print("SCROLLED\n")
            sleep(1)

            # SELECT ALL
            self.driver.find_element_by_xpath(
                '//label[@for="selectAllSwitch2"]').click()
            print("Selected all!\n")
            sleep(0.5)

            self.driver.find_element_by_xpath(
                "/html/body/main/div/div[2]/div[3]/div[2]/div/div[3]/button").click()
            print("REZERVIRANO!")
            sleep(0.5)
        else:
            print("Wrong argument!")

        if (guser):
          gmail_user = guser
          gmail_password = gpass

          # datetime object containing current date and time
          now = datetime.now()


          # dd/mm/YY H:M:S
          dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
          #print("date and time =", dt_string)

          sent_from = gmail_user
          to = [gmail_user]
          subject = 'NUK REZERVACIJA: {t}'.format(t=dt_string)
          body = 'Rezervacija za citalnico uspesna!'

          email_text = "From: {fromS}\nTo: {toS}\nSubject: {subjectS}\n\n{bodyS}".format(fromS = sent_from, toS = to, subjectS = subject, bodyS = body)

          # email_text = """\
          # From: %s
          # To: %s
          # Subject: %s

          # %s
          # """ % (sent_from, ", ".join(to), subject, body)

          try:
              server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
              server.ehlo()
              server.login(gmail_user, gmail_password)
              server.sendmail(sent_from, to, email_text)
              server.close()

              print ('Email sent!')
          except:
              print ('Something went wrong...')

        sleep(4)
        print("END\n")
        self.driver.quit()


my_bot = NukReservation(username, pw)
