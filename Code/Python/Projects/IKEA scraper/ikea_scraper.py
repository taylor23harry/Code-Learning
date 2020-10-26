from selenium import webdriver

shop_choice = 'zaventem'
item = 'linnmon-plateau-brun-noir-80251358/'


class ScrapeKea:
    """A simple webscraper to return in_stock boolean for a IKEA item."""
    def __init__(self, item, shop):
        in_stock = False

    def _scrape(self, item, shop):
        """Does main webscraping."""    
        PATH = 'C:\\Program Files (x86)\\Selenium Webdriver'
        driver = webdriver.Firefox(PATH)
        driver.get("https://www.ikea.com/be/fr/p/" + item)
        # Opens shop list menu.
        stock_menu = driver.find_element_by_link_text("Vérifier le stock en magasin")
        stock_menu.click()
        shop_list = ["anderlecht", "arlon", "gent", "hasselt", "liege", "mons", "wilrijk", "zaventem"]

        shop = driver.find_element_by_xpath(f"/html/body/main/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div[{shop_list.index(shop)+1}]/div[2]/div/span[2]")
        shop_in_stock = shop.get_attribute("innerHTML").splitlines()
        if shop_in_stock == ['Rupture de stock']:
            in_stock = False
        elif shop_in_stock == ['Il en reste peu']:
            in_stock = True
        elif shop_in_stock == ['En stock']:
            in_stock = True
        else:
            print("ERROR")

        print(in_stock, "\n", shop_choice, shop_in_stock)

        driver.quit()

if __name__ == '__main__':
    ikea = ScrapeKea(item, shop_choice)
    ikea._scrape(item, shop_choice)
#/html/body/main/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div[7]/div[2]/div/span[2]
#/html/body/main/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div[7]/div[2]/div/span[2]