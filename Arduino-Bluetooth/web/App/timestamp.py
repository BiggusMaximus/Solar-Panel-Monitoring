import datetime

def get_time():
    dateTimeObj = datetime.datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y %H:%M:%S")
    return str(timestampStr)
