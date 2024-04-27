from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.btkakademi.gov.tr")

if "BTK" in driver.title:
    print("BTK Akademi websitesine hoşgeldiniz")
else:
    print("Bir hata oluştu")

driver.quit()
