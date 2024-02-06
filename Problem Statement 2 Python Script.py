import psutil
import platform
import subprocess
import time

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
PROCESS_THRESHOLD = 100  

# Function to check CPU usage
def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        print(f"High CPU Usage: {cpu_usage}%")

# Function to check memory usage
def check_memory():
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > MEMORY_THRESHOLD:
        print(f"High Memory Usage: {memory_usage}%")

# Function to check disk space
def check_disk():
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > DISK_THRESHOLD:
        print(f"High Disk Usage: {disk_usage}%")

# Function to check running processes
def check_processes():
    process_count = len(list(psutil.process_iter()))
    if process_count > PROCESS_THRESHOLD:
        print(f"Too Many Processes Running: {process_count}")

while True:
    check_cpu()
    check_memory()
    check_disk()
    check_processes()
    time.sleep(60)  #Checking for every min


