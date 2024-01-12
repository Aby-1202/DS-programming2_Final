# %%
import requests
from bs4 import BeautifulSoup 
import re
import time

place_name = ["小田原"]

# %%
# DBファイルを保存するためのファイルパス

import sqlite3

# DBに接続する（指定したDBファイル存在しない場合は，新規に作成される）
con = sqlite3.connect("weather.sqlite")
cur = con.cursor()

# テーブルが存在しない場合は作成
cur.execute('''CREATE TABLE IF NOT EXISTS weather(
                date TEXT,
                precipitation FLOAT,
                temp_avg FLOAT, 
                temp_high FLOAT, 
                temp_low FLOAT, 
                humidity_avg FLOAT, 
                humidity_min FLOAT, 
                sunshine FLOAT)
                ''')

# DBへの接続を閉じる
con.commit()
con.close()

# %%
url = "https://www.data.jma.go.jp/obd/stats/etrn/view/daily_a1.php?prec_no=46&block_no=1008&year=2023&month=12&day=&view=p1"

# 取ったデータをfloat型に変える(データが取れなかった場合、気象庁は"/"を埋め込んでいるため0に変える)
def str2float(str):
  try:
    return float(str)
  except:
    return 0.0

# %%
r = requests.get(url)
r.encoding = r.apparent_encoding

# %%
data_list = [['月日', '降水量', '気温_平均', '気温_最高', '気温_最低', '湿度_平均', '湿度_最小', '日照時間']]

month = 12
soup = BeautifulSoup(r.text, 'html.parser')
table = soup.find('table', {'id': 'tablefix1', 'class': 'data2_s'})
rows = table.findAll('tr', class_='mtx')
rows = rows[19:]

con = sqlite3.connect("weather.sqlite")
cur = con.cursor()


for row in rows:
    data = row.findAll('td')
    rowData = []
    rowData.append(str(month) + "/" + str(data[0].string))
    rowData.append(str(data[1].string) + "mm")
    rowData.append(str(data[4].string) + "°C")
    rowData.append(str(data[5].string) + "°C")
    rowData.append(str(data[6].string) + "°C")
    rowData.append(str(data[7].string) + "％")
    rowData.append(str(data[8].string) + "％")
    rowData.append(str(data[15].string) + "h")

    cur.execute("INSERT INTO weather (date, precipitation, temp_avg, temp_high, temp_low, humidity_avg, humidity_min, sunshine) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", rowData)
    data_list.append(rowData)

if __name__ == "__main__":
    result = data_list
    print(result)

con.commit()
con.close()

# %%
# DBに接続する
con = sqlite3.connect("weather.sqlite")
cur = con.cursor()

# SQLを用意
sql_select = "SELECT * FROM weather;"

# SQLを実行
cur.execute(sql_select)

for row in cur:
    print(row)

# DBへの接続を閉じる
con.close()


