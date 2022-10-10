from weather import functions

myfile = "weather.dat"

mychoice = 0
while(True):
    print("     ***TUFFY TITAN WEATHER LOGGER MAIN MENU")
    print()
    print()
    print("1. Set data Filename")
    print("2. Add weather Data")
    print("3. Print Daily Report")
    print("4. Print Historical Data")
    print("9. Exit Program")

    print()

    mychoice = input("Enter Menu Choice: ")
    print()

    if mychoice == 1:
        myfile = input ("Enter Data Filename:")
        weather = functions.read_data(myfile) 
    elif mychoice == 2:
        dt = input("Enter date: ")
        tm = input("Enter time: ")
        t = int(input("Enter Temparture: "))
        h = int(input("Enter humidity: "))
        r = float(input("Enter the Rainfall: "))
        weather[dt+tm] = {'t': t, 'h' : h, 'r' : r}
        functions.write_data(weather, myfile)
    elif mychoice == 3:
        d = input("Enter date: ")
        display = functions.report_daily(weather,d)
        print(display)
    elif mychoice == 4:
        display = functions.report_historical(weather)
        print(display)
    elif mychoice == 9:
        break
    