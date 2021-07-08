from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os
from datetime import datetime

timestamp = int(time.time())
dt_object = datetime.fromtimestamp(timestamp)

try:
	chrome_options = webdriver.ChromeOptions()
	chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--disable-dev-shm-usage")
	chrome_options.add_argument("--no-sandbox")
	driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
	#driver = webdriver.Chrome("D:\\Python\\Drivers\\chromedriver_win32\\chromedriver.exe")
	driver.get("https://charusat.edu.in:912/Uniexamresult")

	inst = Select(driver.find_element_by_xpath('/html/body/form/div[3]/table[2]/tbody/tr[1]/td[2]/select'))
	inst.select_by_value('21')

	degr = Select(driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[2]/td[2]/select"))
	degr.select_by_value('132')

	sem = Select(driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[3]/td[2]/select"))
	sem.select_by_value('4')

	exam = Select(driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[4]/td[2]/select"))
	# exam.select_by_index('1')

	if len(exam.options)>5:
		from pushbullet import Pushbullet
		APIKEY = "o.FfGgVikGfklDRxpLHGvAKPgFmtYgRSr4"
		pb = Pushbullet(APIKEY)
		push = pb.push_note(f"Results Available!", "")
	print(f"Last Update: {dt_object}")

except:
	print(f"Last Failed: {dt_object}")
