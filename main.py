import psutil
import time
import pyodbc
import platform
import math
import gpustat
from datetime import datetime
import logging

# Logging
logging.basicConfig(filename='system_monitor.log', level=logging.INFO)

# Database connection
try:
    con = pyodbc.connect("DRIVER={ODBC Driver 18 for SQL Server};Server=Hiiragi;Database=master;Trusted_Connection=yes;TrustServerCertificate=yes;")
    cursor = con.cursor()
except pyodbc.Error as e:
    print("Error in database connection: ", e)
    exit(1)

while True:
    info_time = datetime.now()

    # Handle GPU availability
    gpu = gpustat.GPUStatCollection.new_query().gpus[0] if gpustat.is_available() else None
    gpu_name = gpu.name if gpu else None
    gpu_memory_total = gpu.memory_total if gpu else None
    gpu_memory_used = gpu.memory_used if gpu else None
    gpu_utilization = gpu.utilization if gpu else None

    # System performance stats
    cpu_name = platform.processor()
    cpu_usage = psutil.cpu_percent()
    cpu_freq = psutil.cpu_freq().current
    disk_total = round(psutil.disk_usage("/").total * math.pow(10, -9), 2)
    disk_usage = round(psutil.disk_usage("/").used * math.pow(10, -9), 2)
    ram_total = round(psutil.virtual_memory().total * math.pow(10, -9), 2)
    ram_used = round(psutil.virtual_memory().used * math.pow(10, -9), 2)
    net_sent = round(psutil.net_io_counters().bytes_sent * math.pow(10, -9), 2)
    net_received = round(psutil.net_io_counters().bytes_recv * math.pow(10, -9), 2)

    # Insert data into the database
    try:
        cursor.execute("USE system_information")
        cursor.execute(
            "INSERT INTO dbo.monitor (time, cpu_name, cpu_usage, cpu_freq, gpu_name, gpu_memory_total, gpu_memory_used, gpu_ultilization, disk_total, disk_used, ram_total, ram_used, net_sent, net_received) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                info_time,
                cpu_name,
                cpu_usage,
                cpu_freq,
                gpu_name,
                gpu_memory_total,
                gpu_memory_used,
                gpu_utilization,
                disk_total,
                disk_usage,
                ram_total,
                ram_used,
                net_sent,
                net_received,
            ),
        )
        con.commit()
    except pyodbc.Error as e:
        print(f"Error inserting data: {e}")

    # Log the output
    logging.info(f"Time: {info_time}, CPU Name: {cpu_name}, CPU Usage: {cpu_usage}, CPU Frequency: {cpu_freq}, GPU Name: {gpu_name}, GPU Memory Total: {gpu_memory_total}, GPU Memory Used: {gpu_memory_used}, GPU Utilization: {gpu_utilization}, Disk Total: {disk_total}, Disk Usage: {disk_usage}, RAM Total: {ram_total}, RAM Used: {ram_used}, Net Sent: {net_sent}, Net Received: {net_received}")
    print(f"Time: {info_time}, CPU Name: {cpu_name}, CPU Usage: {cpu_usage}, CPU Frequency: {cpu_freq}, GPU Name: {gpu.name}, GPU Memory Total: {gpu.memory_total}, GPU Memory Used: {gpu.memory_used}, GPU Utilization: {gpu.utilization}, Disk Total: {disk_total}, Disk Usage: {disk_usage}, RAM Total: {ram_total}, RAM Used: {ram_used}, Net Sent: {net_sent}, Net Received: {net_received}")

    time.sleep(1)
