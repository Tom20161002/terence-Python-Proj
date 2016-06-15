# -*- coding: UTF-8 -*-

########################################################################
#   For more details, please visit
#   https://proj.org.cn/2016/06/14/第一个python-脚本-抓取下载链接.html
#   Or
#   http://wp.me/p7yURE-dy
########################################################################

import re
from urllib.request import urlopen

from bs4 import BeautifulSoup

req_id = '20142'
html_req_url = 'http://www.4567.tv/film/id' + req_id + '.html'

html_content = urlopen(html_req_url)

soup_content = BeautifulSoup(html_content, "lxml")

download_addr = re.findall('ed2k://.*\|/|ftp://.*\.mp4|ftp://.*\.rmvb|ftp://.*\.mkv', str(soup_content))

list_num = 0


def download_link_function_1(list_num):
    download_link_str_count_start = len(re.findall('ed2k://|ftp://', download_addr[list_num]))
    download_link_str_count = len(re.findall('ed2k://|ftp://', download_addr[list_num + 1]))
    if download_link_str_count_start >= download_link_str_count:
        download_link_str_count = 'true'
    else:
        download_link_str_count = 'false'
    return download_link_str_count


while list_num < len(download_addr):
    if list_num == len(download_addr) - 1:
        break
    else:
        if download_link_function_1(list_num) == 'true':
            break
        else:
            list_num += 1

download_addr = download_addr[list_num].replace('###', '\n')

html_title = soup_content.find('title')
media_title = html_title.get_text()
media_title = media_title[0:-24]
media_title = media_title.replace('/', '_')
media_title = media_title.replace(' ', '_')

download_addr_list_filename = media_title + '_' + req_id + '.txt'

html_write_to_file = open(download_addr_list_filename, 'wt')
html_write_to_file.write(media_title)
html_write_to_file.write('\n')

html_write_to_file.write(download_addr)
html_write_to_file.close()
