
for i in range(1,11):
    with open(f'../Data/n{i}.txt', mode='r') as f:     # データの読み込み 1から10
        data = f.read()
