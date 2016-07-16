# -*- coding: UTF-8 -*-

import getopt
import os
import sys

# ping包数,整数
ping_packet_count = 10

# 丢包率(%),请勿添加单位,浮点数
packetloss_percentage = 10.0

# 延迟(ms),请勿添加单位,浮点数
latency_max = 40.0


def main(argv):
    global server_ipaddr
    global server_name
    server_ipaddr = ''
    server_name = ''
    try:
        opts, args = getopt.getopt(argv, "hi:n:", ["iipaddr=", "nname="])
    except getopt.GetoptError:
        print('test.py -i <ipaddr> -n <name>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <ipaddr> -n <name>')
            sys.exit()
        elif opt in ("-i", "--ipaddr"):
            server_ipaddr = arg
        elif opt in ("-n", "--name"):
            server_name = arg


if __name__ == "__main__":
    main(sys.argv[1:])

ping_result = os.popen(
    'ping -c ' + str(ping_packet_count) + ' -t ' + str(ping_packet_count) + ' ' + server_ipaddr).readlines()

result_list_count = len(ping_result)
ping_packetloss_output_list = ping_result[-2].split(' ')
ping_packetloss_percentage = ping_packetloss_output_list[-3].strip('%')
ping_packetloss_percentage_output = 'packetloss = ' + str(ping_packetloss_percentage) + '%'
round_trip_list = ping_result[-1].split(' ')
round_trip_values = round_trip_list[3].split('/')
ping_max_value = float(round_trip_values[2])


def ping_result_output():
    ping_min = 'ping_min = ' + str(round_trip_values[0])
    ping_avg = 'ping_avg = ' + str(round_trip_values[1])
    ping_max = 'ping_max = ' + str(round_trip_values[2])
    ping_stddev = 'ping_stddev = ' + str(round_trip_values[3])
    date_now = str(os.popen('date').readline())
    print(
        '-' * 25 + server_name + '-' * 25 + '  ' + date_now + ping_min + '  ' + ping_avg + '  ' + ping_max + '  ' + ping_stddev + '  ' + ping_packetloss_percentage_output)
    return ping_result_output


if result_list_count <= 4:
    ping_result_output()
    print('server ' + server_name + ' is down!')
    os.popen('afplay /Users/terence/Music/QQ音乐/Austin\ Mahone\,Pitbull-Mmm\ Yeah.mp3')
elif float(ping_packetloss_percentage) >= float(packetloss_percentage):
    ping_result_output()
    print('The ' + server_name + ' network packet lossis is more then ' + str(packetloss_percentage) + '%! packetloss!')
    os.popen('afplay /Users/terence/Music/QQ音乐/Austin\ Mahone\,Pitbull-Mmm\ Yeah.mp3')
elif ping_max_value >= float(latency_max):
    ping_result_output()
    print('The ' + server_name + ' network latency is more then ' + str(latency_max) + 'ms! High network latency!')
    os.popen('afplay /Users/terence/Music/QQ音乐/Austin\ Mahone\,Pitbull-Mmm\ Yeah.mp3')
else:
    ping_result_output()
