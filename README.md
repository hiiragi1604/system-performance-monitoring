# System Performance Live Monitoring

## Overview

This project is designed for real-time monitoring of system performance metrics, including CPU, GPU, disk usage, RAM, and network I/O. The data is collected from the system, uploaded to a local SQL database, and visualized using Power BI for a comprehensive view of system health.

## Installing required python packages

```bash
pip install psutil pyodbc gpustat
```

**Note**: For `pyodbc` to work correctly, you may also need to install the ODBC driver for SQL Server. You can download it from [Microsoft’s website](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server).

## Project Workflow

1. **Data Collection**: System stats are collected in real-time using Python.
2. **Data Storage**: Data is uploaded to a local SQL database.
3. **Data Visualization**: Power BI is used to create a live monitoring dashboard.

## Power BI Visualization

The Power BI dashboard displays key metrics for live system performance, including:

- **Network Traffic**: Data sent and received over time.
- **Disk Usage**: Total and used disk space.
- **CPU Metrics**: Frequency and utilization percentage.
- **GPU Metrics**: Memory usage and utilization for Nvidia GPUs.
- **RAM Usage**: Total and used memory.
   
![Screenshot 2024-10-27 025029](https://github.com/user-attachments/assets/9319c62a-2e26-491e-8f8d-023dcc43ca96)

## Notes

- **Nvidia GPU Requirement**: GPU metrics are only available if an Nvidia GPU is present, as `gpustat` is Nvidia-specific.
- **Database Requirement**: Ensure the `system_information` database and `dbo.monitor` table are created in SQL Server.
