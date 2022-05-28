
for i in range(1,11):   # ループ開始　１から１０
    with open(f'../Data/n{i}.txt', mode='r') as f:     # データの読み込み
        data = f.read()
