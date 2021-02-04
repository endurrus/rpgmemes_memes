import datetime
def time_until_end_of_day(dt=None):
    # type: (datetime.datetime) -> datetime.timedelta
    """
    Get timedelta until end of day on the datetime passed, or current time.
    """
    if dt is None:
        dt = datetime.datetime.now()
    tomorrow = dt + datetime.timedelta(days=1)
    return str(datetime.datetime.combine(tomorrow, datetime.time.min) - dt)

def time_until_salary_increment(dt=None):
    # type: (datetime.datetime) -> datetime.timedelta
    """
    Get timedelta until end of day on the datetime passed, or current time.
    """
    if dt is None:
        dt = datetime.datetime.now()
    tomorrow = dt + datetime.timedelta(days=7)
    return str(datetime.datetime.combine(tomorrow, datetime.time.min) - dt)

# timediff = time_until_end_of_day()
# print(timediff[:2], 'hrs', timediff[3:5], 'mins and', timediff[6:8], 'seconds to energy refill!' )

# timediff_salary = time_until_salary_increment()
# print(timediff_salary[0], 'days', timediff_salary[8:10], 'hrs', timediff_salary[11:13] ,'mins and', timediff_salary[14:16], 'seconds to next salary increment!')