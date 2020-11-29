#Rajat Kumar Kushwaha
#Possible date input(2019-03-27,28,29,30,31)
import requests
import json
def fetch(date,choice):
    response = requests.get(
        "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22").json()
    if(choice==1):
        print("Weather update:-\n")
        for rt in response["list"]:
            if (rt["dt_txt"][0:10] ==date):
                for key, val in rt["main"].items():
                    if(key in ["temp","temp_min","temp_max"]):
                        print(key, ":-", val)
                for w in rt["weather"]:
                    for key,val in w.items():
                        print(key,":-",val)
                print("at",rt["dt_txt"][10:],"hrs\n----------------\n")
    if(choice==2):
        print("Wind Update:-\n")
        for rt in response["list"]:
            if (rt["dt_txt"][0:10] == date):
                for key, val in rt["wind"].items():
                    print(key, ":-", val)
                print("at", rt["dt_txt"][10:], "hrs\n----------------\n")

    if(choice==3):
        print("Pressure Update:-\n")
        for rt in response["list"]:
            if (rt["dt_txt"][0:10] == date):
                for key, val in rt["main"].items():
                    if(key in ["pressure","sea_level","grnd_level","humidity"]):
                        print(key, ":-", val)
                print("at", rt["dt_txt"][10:], "hrs\n----------------\n")




print("Welcome to weather")
choice=1
while(choice):
    print("Select from the below option:-\n"
          "1. Get weather\n"
          "2. Get wind Speed\n"
          "3. Get Pressure\n"
          "0. Exit\n"
          "Enter the corresponding number")
    choice = int(input())
    if(choice==0):
        print("thanks for visiting")
        break
    print("Enter the date (format- YYYY-MM-DD) :- ")
    date=input()
    fetch(date,choice)
