import time, os

from helper import str_to_float
from webdriver import driver

from plyer import notification


def check_price(url:str, target_price:float):
    driver.get(url)
    target = driver.find_element_by_id("price_inside_buybox")
    str_price = target.text
    price = str_to_float(target.text)

    if target_price >= price:
        notification.notify(title= "Amazon price alert",
                    message= f"The price for your desired product just droped to {str_price}",
                    app_icon = os.path.dirname(os.path.realpath(__file__)) + "\icon.ico",
                    timeout= 15,
                    toast=False)
        driver.quit()
    else:
        time.sleep(60*10)
        check_price(url, target_price)



target_price = float(1000) # if user's desired product reaches this price range.

# url for the amazon product.
url = "https://www.amazon.com/ASUS-GeForce-i7-11370H-Windows-TUF516PE-AB73/dp/B08XPC3WFQ/ref=sr_1_4?dchild=1&keywords=The+Best+Gaming+Laptop&qid=1624881043&sr=8-4" 

check_price(url, target_price)
