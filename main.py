import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.xe.gr/property/results?transaction_name=rent&item_type=re_residence&geo_place_ids[]=ChIJ7eAoFPQ4qBQRqXTVuBXnugk")

def wait():
	time.sleep(random.choice(range(5,10)))

wait()

all_houses=driver.find_elements(By.CSS_SELECTOR, '.common-ad-body')
for house in all_houses:
	wait()
	try:
		title=house.find_element(By.CSS_SELECTOR, 'h3[data-testid="property-ad-title"]').text
	except:
		title="N/A"
		print("error in title")
	wait()
	try:
		price=house.find_element(By.CSS_SELECTOR,value='span.property-ad-price').text
	except:
		price = "N/A"
		print("error in price")
	wait()
	try:
		price_per_sqm=house.find_element(By.CSS_SELECTOR,value="span.property-ad-price-per-sqm").text
	except:
		price_per_sqm="N/A"
		print("error in price_per_sqm")
	wait()
	try:
		level=house.find_element(By.CSS_SELECTOR,value="span.property-ad-level").text
	except:
		level = "N/A"
		print("error in level")

	wait()
	try:
		bedrooms=house.find_element(By.CSS_SELECTOR,value='span[data-testid="property-ad-bedrooms"]').text
	except:
		bedrooms="N/A"
		print("error in bedrooms")

	wait()
	try:
		bathrooms=house.find_element(By.CSS_SELECTOR,value='span[data-testid="property-ad-bathrooms"]').text
	except:
		bathrooms="N/A"
		print("error in bathrooms")


	wait()
	try:
		construction=house.find_element(By.CSS_SELECTOR,value='span[data-testid="property-ad-construction-year"]').text
	except:
		construction="N/A"
		print("error in construction")
	wait()
	try:
		region=house.find_element(By.CSS_SELECTOR,value="span.common-property-ad-address").text.split("|")[0]
	except:
		region="N/A"
		print("error in region")

	wait()

	try:
		home_info={
		"title":title,
		"price":price,
		"price_per_sqm":price_per_sqm,
		"level":level,
		"bedrooms":bedrooms,
		"bathrooms":bathrooms,
		"construction":construction,
		"region":region}
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

	wait()
	with open("houses.txt","a",encoding="utf-8") as file:
		file.write(f"{home_info}\n")
	wait()


