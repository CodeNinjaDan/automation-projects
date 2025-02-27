from scrape import GetHouseData
from data_manager import DataHandler

try:
    scraper = GetHouseData()
    house_addresses, house_prices, house_urls = scraper.scrape()

    data_handler = DataHandler()

    for address, price, url in zip(house_addresses, house_prices, house_urls):
        data_handler.enter_data(address, price, url)

finally:
    if data_handler.driver:
        data_handler.driver.quit()