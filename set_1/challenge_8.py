def validate():
    with open('8.txt', 'r') as f:
        results = []
        for line_no, line in enumerate(f):
            repeats = max([line.count(line[i * 16:(i * 16) + 16]) for i in range(len(line) // 16)])
            results.append((repeats, 'Line: {} Count: {}\n{}'.format(line_no, repeats, line)))

    print(max(results, key=lambda x: x[0])[1])
