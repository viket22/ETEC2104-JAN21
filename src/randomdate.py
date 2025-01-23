import datetime
import random

def gen_randomdate():
    x = datetime.timedelta(minutes=random.randrange(8000))
    hoursago = int( x.seconds / 3600 )
    minutesago = round(x.seconds - x.days*3600)/60
    return(f"{x.days} days, {hoursago} hours, and {minutesago:g} minutes ago")