# -*- coding: UTF-8 -*-

import os
import time

# 循环暂停时间
sleep_time = 60

# 线路以及ip地址
server_ipaddr = {'ChinaTelecom': '10.1.1.1', 'ChinaUnicom': '10.1.1.2'}

website_status_monitor_count = 1

while website_status_monitor_count == 1:
    for i in server_ipaddr:
        website_status_monitor_run = os.popen(
            'python3 /Users/terence/Documents/github/terence-Python-Proj/website_status_monitor/website_status_monitor.py -i ' +
            server_ipaddr[i] + ' -n ' + '%s' % i)
        website_status_monitor_run_output = website_status_monitor_run.readlines()
        for output_str in website_status_monitor_run_output:
            print(output_str.replace('  ', '\n'))
    print('+' * 100 + '\n')
    time.sleep(sleep_time)
