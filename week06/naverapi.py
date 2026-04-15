# -*- coding: uft-8 -*-
import urllib.request
import datatime
import json

client_id = 'n506YF7IGfKX0YbK3Bie'
client_secret = 'KqZGEJRtqQ'

def main():

    node = 'news'                                             # 크롤링할 대상
    srcText = input('검색어를 입력하세요: ')

    cnt = 0
    jsonResult = []

    jsonResponse = getNaverSearch(node, srcTextm, 1, 100)      #