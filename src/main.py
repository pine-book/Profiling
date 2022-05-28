data = []

for i in range(1,11):
    with open('../Data/n{i:>3d}.txt', mode='r') as f:     # データの読み込み 1から10
        data[i] = f.read()
