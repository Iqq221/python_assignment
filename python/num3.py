from datetime import datetime
dt_str=input("\n enter birth date in yyyy-mm-dd format")
dt=datetime.strptime(dt_str,"%Y-%m-%d")

dt_now=datetime.now().date()
yr=dt_now.year-dt.year
mon=dt_now.month-dt.month
day=dt_now.day-dt.day
if(day<0):
    mon-=1
    from calendar import monthrange
    days_in_month=monthrange(dt_now.year,dt_now.month-1 if dt_now.month>1 else 12)[1]
    day+=days_in_month
if (mon<0):
    yr-=1
    mon+=12
print(f"you are {yr} year {mon} month {day} days old")