import schedule
import time
import datetime


def Task_Minute():
    print("Task based on minutes gets scheduled at :",datetime.datetime.now())

def Task_Hour():
    print("Task based on hour gets scheduled at :",datetime.now())

def Task_Day():
    print("Task based on day gets scheduled at :",datetime.datetime.now())

def main():
    print("Inside task schedular")
    print("Current time is :",datetime.datetime.now())

    schedule.every(1).minutes.do(Task_Minute)

    schedule.every(1).hour.do(Task_Hour)
    schedulr.every().saturday.at("18:00").do(Tak_Day)

    while(True):
        schedule.run_pending()time.sleep(1)

    
    
    

if __name__ == "__main__":
    main()





if __name__ == "__main__":
    main()


