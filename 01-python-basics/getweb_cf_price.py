import urllib.request
price = 99.99
while price >4.74:
    page = urllib.request.urlopen("https://markets.businessinsider.com/commodities/coffee-price")
    text = page.read().decode("utf8")
    
    where = text.find('price-section__current-value">')
    start_of_price = where + len('price-section__current-value">')
    end_of_price = start_of_price + 4

    
print(price) 
