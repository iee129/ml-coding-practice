# -*- coding: utf-8 -*-
import urllib.request
import datetime
import json
import pandas as pd

ServiceKey = "자신의 Service Key"

"""### [CODE 0]"""

def main():
    jsonResult = []
    result = []

    print("<< 국내 입국한 외국인의 통계 데이터를 수집합니다.")