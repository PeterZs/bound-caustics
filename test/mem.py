# 内存监控（该脚本是公用设施，非必要不改动）

import sys
import time
import psutil
import threading

mem_max = 0
stop_flag = 0
proc_name = "mitsuba.exe"
th = 0

def get_mem_percent():
    global proc_name
    procs = psutil.process_iter()
    pid = list(i.pid for i in procs if i.name() == proc_name)
    if len(pid) == 0:
        return 0
    pid = pid[0]
    return psutil.Process(pid).memory_percent() * psutil.virtual_memory().total / 100 / 1024 / 1024

def get_mem_percent_auto():
    global mem_max
    global stop_flag
    while stop_flag == 0:
        tmp = get_mem_percent()
        print("mem", tmp)
        mem_max = max(mem_max, tmp)
        time.sleep(0.2)

def monitor_start():
    global th
    global mem_max
    global stop_flag
    th = threading.Thread(target = get_mem_percent_auto)
    stop_flag = 0
    mem_max = 0
    th.start()

def monitor_stop():
    global mem_max
    global stop_flag
    global th
    stop_flag = 1
    th.join()
    print("Memory monitor stopped, max mem used MB =", mem_max)
    return mem_max

if __name__ == "__main__":
    th = threading.Thread(target = get_mem_percent_auto)
    stop_flag = 0
    th.start()
    time.sleep(3)
    stop_flag = 1
    th.join()
    print(mem_max)