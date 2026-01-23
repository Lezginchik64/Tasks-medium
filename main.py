with open('new_scores.txt', 'w', encoding='utf-8') as f, open('class_scores.txt', 'r', encoding='utf-8') as lines:
    for line in lines:
        surname, score = line.split()
        score = int(score) + 5
        if score > 100:
            score = 100
        print(surname, score, file=f)