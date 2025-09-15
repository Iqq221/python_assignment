#Display the difference in dates
from datetime import datetime
dt1_str=input("\n enter date 1 in yyyy-mm-dd format")
dt2_str=input("\n enter date 2 in yyyy-mm-dd format")
dt1=datetime.strptime(dt1_str,"%Y-%m-%d")
dt2=datetime.strptime(dt2_str,"%Y-%m-%d")
new_date=dt2-dt1
print(f"difference in date is - {new_date.days}")