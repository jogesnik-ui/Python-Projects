import psutil
import csv
import time
from datetime import datetime
while True:


    
    ram_usage = psutil.virtual_memory().percent
    cpu_usage = psutil.cpu_percent(interval=1)

    header= ['DATE', 'CPU', 'RAM']
    data = [datetime.now(), cpu_usage, ram_usage]
    with open('Manager.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    time.sleep(60)

