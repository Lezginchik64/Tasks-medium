print(all(map(lambda x: x.isdigit() and 0 <= int(x) <= 255, input().split("."))))
