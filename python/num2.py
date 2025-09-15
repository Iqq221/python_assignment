#Display time since epoch in hours and minutes
import time
from datetime import datetime
epoch_time=time.time()
print(epoch_time)
hrs=int(epoch_time//3600)
mins=int((epoch_time%3600)//60)

print(f"time since epoch is {hrs} hour and {mins} minutes")