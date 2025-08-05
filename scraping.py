import random
import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Scrapper:
	def __init__(self):
		self.options = webdriver.ChromeOptions()
		self.options = webdriver.ChromeOptions()
		self.options.add_experimental_option("detach", True)
		self.driver = webdriver.Chrome(options=self.options)
		self.driver.get("https://www.xe.gr/property/results?transaction_name=rent&item_type=re_residence&geo_place_ids[]=ChIJ7eAoFPQ4qBQRqXTVuBXnugk")

	def wait_for_page(self):
		time.sleep(random.choice(range(15, 20)))
	def wait(self):
		time.sleep(random.choice(range(5, 10)))

		#takes all the visible houses on the page and scrap them and save it in houses.txt, it returns all_houses
	def scrapper(self):
			self.wait_for_page()
			all_houses = self.driver.find_elements(By.CSS_SELECTOR, '.common-ad-body')
			for house in all_houses:
				self.wait()
				try:
					title = house.find_element(By.CSS_SELECTOR, 'h3[data-testid="property-ad-title"]').text
				except:
					title = "N/A"
					print("error in title")
				self.wait()
				try:
					price = house.find_element(By.CSS_SELECTOR, value='span.property-ad-price').text
				except:
					price = "N/A"
					print("error in price")
				self.wait()
				try:
					price_per_sqm = house.find_element(By.CSS_SELECTOR, value="span.property-ad-price-per-sqm").text
				except:
					price_per_sqm = "N/A"
					print("error in price_per_sqm")
				self.wait()
				try:
					level = house.find_element(By.CSS_SELECTOR, value="span.property-ad-level").text
				except:
					level = "N/A"
					print("error in level")

				self.wait()
				try:
					bedrooms = house.find_element(By.CSS_SELECTOR,
												  value='span[data-testid="property-ad-bedrooms"]').text
				except:
					bedrooms = "N/A"
					print("error in bedrooms")

				self.wait()
				try:
					bathrooms = house.find_element(By.CSS_SELECTOR,
												   value='span[data-testid="property-ad-bathrooms"]').text
				except:
					bathrooms = "N/A"
					print("error in bathrooms")

				self.wait()
				try:
					construction = house.find_element(By.CSS_SELECTOR,
													  value='span[data-testid="property-ad-construction-year"]').text
				except:
					construction = "N/A"
					print("error in construction")
				self.wait()
				try:
					region = house.find_element(By.CSS_SELECTOR, value="span.common-property-ad-address").text.split("|")[0]
				except:
					region = "N/A"
					print("error in region")

				try:
					home_info = {
						"title": title,
						"price": price,
						"price_per_sqm": price_per_sqm,
						"level": level,
						"bedrooms": bedrooms,
						"bathrooms": bathrooms,
						"construction": construction,
						"region": region}
				except:
					home_info = {
						"title": "N/A",
						"price": "N/A",
						"price_per_sqm": "N/A",
						"level": "N/A",
						"bedrooms": "N/A",
						"bathrooms": "N/A",
						"construction": "N/A",
						"region": "N/A"}

				with open("houses.txt", "a", encoding="utf-8") as file:
					file.write(f"{home_info}\n")


	def scroll_half(self):
		screen_height = self.driver.execute_script("return window.screen.height;")
		i = 1.2
		self.driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))

	def scroll_full(self):
		screen_height = self.driver.execute_script("return window.screen.height;")
		i = 2.2
		self.driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))

	def next_page(self):
		self.driver.find_element(By.CSS_SELECTOR,value="a[rel='next']").click()

	def scrap_page(self):
		self.scroll_half()
		self.scrapper()
		self.scroll_full()
		self.next_page()


