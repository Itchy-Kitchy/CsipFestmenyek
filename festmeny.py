import festmenyek

samples = []

def inputFile(file, data):
    f = open(file, "r")
    for ln in f:
        ln = ln[:-1].split(",")
        data.append(festmenyek.Festmenyek(ln[0], ln[1], ln[2]))
    f.close()
    return

def writeToFile(file, data):
    f = open(file, "a")
    f.write(data)
    f.close()
    return

def newEntry(label):
    print(label)
    newdata = ""
    prompt = "\tKérem adja meg a festmény címét: "
    newtitle = str(input(prompt))
    newdata += str(newtitle)
    newdata += ","
    print("\tA megadott új cím: " + str(newdata))
    prompt = "\tKérem adja meg a festmény értékét: "
    newprice = int(input(prompt))
    newdata += str(newprice)
    newdata += ","
    print("\tA megadott új érték: " + str(newdata))
    prompt = "\tKérem adja meg a festmény pénznemét (HUF, EUR, USD, GBD): "
    newcurrency = str(input(prompt))
    if((newcurrency == "HUF") or (newcurrency == "EUR") or (newcurrency == "USD") or (newcurrency == "GBD")):
        newdata += str(newcurrency)
        newdata += "\n"
        print("\tA megadott új pénznem: " + str(newdata))
        writeToFile("festmenyek.txt", newdata)
    else:
        print("\tA megadott pénznem nem megfelelő!")
    return

def askAbout(label):
    print(label)
    prompt = "\tKérem adja meg a festmény címét: "
    inputtitle = str(input(prompt))
    prices = []
    sumprice = 0
    for i in range(len(samples)):
        if(samples[i].title == inputtitle):
            prices.append(samples[i].price)
        if(len(prices) == 0):
            print("\tA megadott címmel nem található festmény! " + str(prices))
            return
    for i in range(len(samples)):
        sumprice += samples[i].howMuchhuf()
    print("A(z) " + str(inputtitle) + " festmény adatai: ")
    print("\tA festmény " + str(len(prices)) + " alkalommal került rögzítésre.")
    print("\tAz festmény(ek) összértéke: " + str(sumprice) + " Ft")
    return

def f1(label):
    print(label)
    inputFile("festmenyek.txt", samples)
    print("\tA fájl beolvasása ... kész!")
    print("\tFestmenyek száma: " + str(len(samples)))
    for i in range(len(samples)):
        print("\t" + str(i+1) + ". Festmény: " + str(samples[i].title) + "\t" + str(samples[i].price) + " " + samples[i].whatCurrency())

def f2(label):
    print(label)
    prompt = "\tSzeretne új festményt rögzíteni? (y/n) "
    answer = str(input(prompt))
    if((answer == "y") or (answer == "Y")):
        newEntry("Új festmény rőgzítése:")
        return
    if((answer == "n") or (answer == "N")):
        askAbout("Festmény lekérdezés:")
        return
    else:
        print("\tÉrvénytelen válasz!")
        return

f1("Fájl beolvasás:")
f2("Fájl müvelet:")
    
