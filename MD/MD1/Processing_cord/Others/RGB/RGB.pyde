import csv

PHOTO_SIZE_X = 756
PHOTO_SIZE_Y = 1008
BLOCK_SIZE = 4

# csv格納用リスト
csv_data = []

# 読み込むデータを「f」という略称で扱う
with open('./RGB_data.csv') as f:
    # データを読み込み，readerに格納
    reader = csv.reader(f)
    # 格納したデータを1行ずつ取り出しリストに格納
    for row in reader:
        csv_data.append(row)

# 格納したデータの形状を確認＝2次元配列（文字列型）
print(csv_data)

size(756,1008)
x = 0
y = 0
