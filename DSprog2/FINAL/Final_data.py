# %%
import requests
from bs4 import BeautifulSoup 
import re
import time

# %%
## まずは気象庁のWebサイトから、家から近い小田原市の気象情報を取得しDBに保存する

# DBファイルを保存するためのファイルパス

import sqlite3

# DBに接続する（指定したDBファイル存在しない場合は，新規に作成される）
con = sqlite3.connect("data.sqlite")
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

con = sqlite3.connect("data.sqlite")
cur = con.cursor()

for row in rows:
    time.sleep(1)
    data = row.findAll('td')
    rowData = []
    rowData.append(str(month) + "/" + str(data[0].string))
    rowData.append(str(data[1].string))
    rowData.append(str(data[4].string))
    rowData.append(str(data[5].string))
    rowData.append(str(data[6].string))
    rowData.append(str(data[7].string))
    rowData.append(str(data[8].string))
    rowData.append(str(data[15].string))

    cur.execute("INSERT INTO weather (date, precipitation,temp_avg, temp_high, temp_low, humidity_avg, humidity_min, sunshine) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", rowData)
    data_list.append(rowData)

if __name__ == "__main__":
    result = data_list
    print(result)

con.commit()
con.close()

# %%
# DBに接続する
con = sqlite3.connect("data.sqlite")
cur = con.cursor()

# SQLを用意
sql_select = "SELECT * FROM weather;"

# SQLを実行
cur.execute(sql_select)

for row in cur:
    print(row)

# DBへの接続を閉じる
con.close()

# %%
## ここからはローカルデータ(スクリーンタイム)の保存

# DBに接続する（指定したDBファイル存在しない場合は，新規に作成される）
con = sqlite3.connect("data.sqlite")
cur = con.cursor()

# テーブルが存在しない場合は作成
cur.execute('''CREATE TABLE IF NOT EXISTS screentime(
                date TEXT,
                game_time INTEGER,
                SNS_time INTEGER,
                entertainment_time INTEGER,
                utility_time INTEGER,
                others_time INTEGER,
                total_time INTEGER)
                ''')

# DBへの接続を閉じる
con.commit()
con.close()

# %%
def add_screentime(date, game_time, SNS_time, entertainment_time, utility_time, others_time, total_time):

    con = sqlite3.connect("data.sqlite")
    cur = con.cursor()

    cur.execute("INSERT INTO screentime (date, game_time, SNS_time, entertainment_time, utility_time, others_time, total_time) VALUES(?, ?, ?, ?, ?, ?, ?)", (date, game_time, SNS_time, entertainment_time, utility_time, others_time, total_time))

    con.commit()
    con.close()

add_screentime('12/17', 1188, 69, 60, 42, 8, 1367)
add_screentime('12/18', 462, 143, 57, 49, 8, 719)
add_screentime('12/19', 168, 183, 17, 9, 13, 390)
add_screentime('12/20', 332, 290, 44, 50, 15, 731)
add_screentime('12/21', 412, 374, 32, 81, 21, 920)
add_screentime('12/22', 174, 166, 12, 72, 34, 458)
add_screentime('12/23', 481, 147, 73, 191, 45, 937)
add_screentime('12/24', 180, 321, 82, 142, 7, 732)
add_screentime('12/25', 228, 328, 158, 68, 20, 802)
add_screentime('12/26', 16, 197, 27, 26, 57, 323)
add_screentime('12/27', 45, 28, 16, 8, 9, 106)
add_screentime('12/28', 40, 100, 30, 4, 20, 194)
add_screentime('12/29', 392, 126, 104, 17, 12, 651)
add_screentime('12/30', 672, 153, 14, 8, 21, 868)
add_screentime('12/31', 195, 244, 86, 163, 36, 724)

# %%
# DBに接続する
con = sqlite3.connect("data.sqlite")
cur = con.cursor()

# SQLを用意
sql_select = "SELECT * FROM screentime;"

# SQLを実行
cur.execute(sql_select)

for row in cur:
    print(row)

# DBへの接続を閉じる
con.close()


