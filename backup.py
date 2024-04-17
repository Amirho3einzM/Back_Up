import os
import shutil
import schedule
import time
import datetime


source_file = r"C:\Users\ToosArax\Pictures\Screenshots"
backup_file = r"C:\Users\ToosArax\Pictures\backup"

def backup(source,backup):
    today=datetime.date.today()
    backup_real=os.path.join(backup,str(today))
    
    try:
        shutil.copytree(source,backup_real)
        print(f"Folder Backupped at : {backup_real}")
    except FileExistsError:
        print(f"Folder Already Exist at:{backup}")
        
schedule.every().day.at("15:53").do(lambda: backup(source_file,backup_file))

while True:
    schedule.run_pending()
    time.sleep(60)