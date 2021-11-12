class Festmenyek:
    def __init__(self, title, price, currency):
        self.title = str(title)
        self.price = int(price)
        self.currency = str(currency)

    def whatCurrency(self):
        txt = ""
        if(self.currency == "EUR"):
            txt = "€"
        if(self.currency == "HUF"):
            txt = "Ft"
        if(self.currency == "USD"):
            txt = "$"
        if(self.currency == "GBP"):
            txt == "£"
        return txt

    def howMuchhuf(self):
        huf = 0
        if(self.currency == "EUR"):
            huf = self.price * 365
        if(self.currency == "HUF"):
            huf = self.price
        if(self.currency == "USD"):
            huf = self.price * 310
        if(self.currency == "GBP"):
            huf = self.price * 420
        return huf
        
