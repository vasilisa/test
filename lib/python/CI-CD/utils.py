import datetime


def process(row):
    
    # return the end of month for each date row
      
    current = datetime.datetime.strptime(row["line"],'%m/%d/%y')
    EndOfMonth = (datetime.datetime(current.year + int(current.month / 12), ((current.month % 12) + 1), 1) - datetime.timedelta(days=1))
    row["line"]= datetime.datetime.strftime(EndOfMonth,"%m/%d/%y")
    return row