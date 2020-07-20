from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.keys import Keys
import datetime
import time
from dotenv import load_dotenv
import os

class GTimeReportBot():
  def __init__(self):
    load_dotenv()
    self.driver = webdriver.Chrome(ChromeDriverManager().install())

  def login(self):
    # open website
    self.driver.get('https://gtimereport.com')

    sleep(2)

    # press Google button
    g_btn = self.driver.find_element_by_xpath('//*[@id="main"]/table/tbody/tr[1]/td[1]/div/div[3]/span/input')
    g_btn.click()

    sleep(2)

    # type in mail and send it
    email_in = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
    email_in.send_keys(os.getenv("NAME"))
    cont_btn = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
    cont_btn.click()

    sleep(2)

    # type in password and send it
    pw_in = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    pw_in.send_keys(os.getenv("PASSWORD"))
    pw_btn = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
    pw_btn.click()
  
  def clickOnBoxes(self):
    boxesToCheck = [2,4,7,9,10,11,12,13,14,15,16,17,18,19,20,22,26]
    for i in boxesToCheck:
      cb = self.driver.find_element_by_xpath('//*[@id="frmReport"]/table/tbody/tr/td[1]/table/tbody/tr[{}]/td/input'.format(i))
      cb.click()
  
  def calendarSelect(self, year, week):
    firstdate, lastdate =  self.getDateRangeFromWeek(year, week)
    firstdate = firstdate - datetime.timedelta(1)
    lastdate = lastdate - datetime.timedelta(1)
    cal_start_in = self.driver.find_element_by_xpath('//*[@id="PeriodStart"]')
    cal_start_in.send_keys(Keys.CONTROL + 'a')
    cal_start_in.send_keys(str(firstdate))

    cal_end_in = self.driver.find_element_by_xpath('//*[@id="PeriodEnd"]')
    cal_end_in.send_keys(Keys.CONTROL + 'a')
    cal_end_in.send_keys(str(lastdate))
  
  def download(self):
    dl_btn = self.driver.find_element_by_xpath('//*[@id="frmReport"]/div[2]/input[2]')
    dl_btn.click()

  def getDateRangeFromWeek(self,p_year,p_week):
    firstdayofweek = datetime.datetime.strptime(f'{p_year}-W{int(p_week )- 1}-1', "%Y-W%W-%w").date()
    lastdayofweek = firstdayofweek + datetime.timedelta(days=6.9)
    return firstdayofweek, lastdayofweek

  def autoBot(self, year, week):
    self.login()
    sleep(10)
    self.clickOnBoxes()
    self.calendarSelect(year, week)
    self.download()
  
