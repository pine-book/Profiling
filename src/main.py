data = []

for i in range(10):
    with open('../Data/n%d.txt', i, mode='r') as f:     # データの読み込み
        data[i] = f.read()
