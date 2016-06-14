# -*- coding: UTF-8 -*-

########################################################################
#   For more details, please visit
#   https://proj.org.cn/2016/06/14/第一个python-脚本-抓取下载链接.html
#   Or
#   http://wp.me/p7yURE-dy
########################################################################

from urllib.request import urlopen

from bs4 import BeautifulSoup

req_id = 'id19654'
html_req_url = 'http://www.4567.tv/film/' + req_id + '.html'

html_content = urlopen(html_req_url)

soup_content = BeautifulSoup(html_content, "lxml")

html_title = soup_content.find('title')
html_title = html_title.get_text()
html_title = html_title.replace(' ', '-')
html_title_list = html_title.split('-')
html_title = html_title_list[0]
# print html_title

html_dowlload_content_list = soup_content.findAll(attrs={"class": "mox"})


def html_function_1(download_num):
    html_dowlload_list_content = str(html_dowlload_content_list[download_num])
    html_download_str = '下载地址2'
    download_current = html_dowlload_list_content.find(html_download_str)
    return download_current


download_num_str = 0
while html_function_1(download_num=download_num_str) < 0:
    download_num_str += 1

html_dowlload_content = str(html_dowlload_content_list[download_num_str])

soup_content = BeautifulSoup(html_dowlload_content, 'lxml')
html_dowlload_content_list = soup_content.findAll('script')
html_dowlload_addr = html_dowlload_content_list[1]
html_dowlload_addr = html_dowlload_addr.get_text()
html_dowlload_addr = html_dowlload_addr[16:-2]

html_dowlload_addr = html_dowlload_addr.replace('###', '\n')

html_title_2 = req_id + '.txt'

html_write_to_file = open(html_title_2, 'wt')
html_write_to_file.write(html_title)
html_write_to_file.write('\n')
html_write_to_file.write(html_dowlload_addr)
html_write_to_file.close()
