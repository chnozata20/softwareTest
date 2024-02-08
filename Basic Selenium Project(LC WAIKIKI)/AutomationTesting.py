import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

#LOCATORS
locatorAyakkabı = '.menu-nav__lists .menu-header-item:nth-of-type(5) .menu-header-item__title'
locatorTerlikAyakkabı = "div:nth-of-type(3) > div:nth-of-type(1) > a > img[alt='#']"
locatorKadınTerlik = "a[title='Deri Görünümlü Çift Bantlı Kadın Terlik']  .product-image__slider-button-container"
locatorBeden = ".hidden-mobile [key='1']"
locatorSepeteEkle = "a#pd_add_to_cart"
locatorSepetSayfası = 'div:nth-of-type(2) > .header-dropdown-toggle'
locatorAnaSayfa = ".main-header-logo"

s = Service('C:/Users/chnoz/Desktop/chromedriver')

driver = webdriver.Chrome(service=s)  # Optional argument, if not specified will search path.
driver.maximize_window()

#1. https://www.lcwaikiki.com/tr-TR/TR adresine gidin.
driver.get('https://www.lcwaikiki.com/tr-TR/TR')
assert driver.title == "LC Waikiki | İlk Alışverişte Kargo Bedava! - LC Waikiki"

#2. Herhangi bir kategori sayfasına gidin.
ayakkabı = driver.find_element(By.CSS_SELECTOR, locatorAyakkabı)
driver.execute_script("arguments[0].click();", ayakkabı)
assert driver.title == "kadın erkek cocuk bebek ayakkabı - LC Waikiki"

#3. Herhangi bir ürün sayfasına gidin.
terlikAyakkabı = driver.find_element(By.CSS_SELECTOR, locatorTerlikAyakkabı)
driver.execute_script("arguments[0].click();", terlikAyakkabı)
assert driver.title == "Şık Terlikler Ayakkabılar - LC Waikiki"

kadınTerlik = driver.find_element(By.CSS_SELECTOR, locatorKadınTerlik)
driver.execute_script("arguments[0].click();", kadınTerlik)
assert driver.title == "Siyah Deri Görünümlü Çift Bantlı Kadın Terlik - S1CI90Z8-HUC - LC Waikiki"

#4. Ürünü sepete ekleyin.
beden = driver.find_element(By.CSS_SELECTOR, locatorBeden)
driver.execute_script("arguments[0].click();", beden)
assert driver.title == "Siyah Deri Görünümlü Çift Bantlı Kadın Terlik - S1CI90Z8-HUC - LC Waikiki"

sepeteEkle = driver.find_element(By.CSS_SELECTOR, locatorSepeteEkle)
driver.execute_script("arguments[0].click();", sepeteEkle)
assert driver.title == "Siyah Deri Görünümlü Çift Bantlı Kadın Terlik - S1CI90Z8-HUC - LC Waikiki"

#5. Sepet sayfasına gidin.
sepetSayfası = driver.find_element(By.CSS_SELECTOR, locatorSepetSayfası)
driver.execute_script("arguments[0].click();", sepetSayfası)
assert driver.title == "Sepetim - LC Waikiki"

#6. Anasayfaya geri dönün.
anaSayfa = driver.find_element(By.CSS_SELECTOR, locatorAnaSayfa)
driver.execute_script("arguments[0].click();", anaSayfa)
assert driver.title == "LC Waikiki | İlk Alışverişte Kargo Bedava! - LC Waikiki"

print("TEST OK")

time.sleep(2)
driver.quit()
