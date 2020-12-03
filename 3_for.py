journal = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
{'school_class': '4b', 'scores': [5,3,4,4,1]},
{'school_class': '4d', 'scores': [2,4,3,4,5]}]

sum_scores = 0
sum_num_scores = 0

for i in journal:
    sum_scores += sum(i['scores'])
    sum_num_scores += len(i['scores'])
    print(f'Средний бал по {i["school_class"]} классу равен {int(sum_scores/sum_num_scores)}')

print(f'Средний бал по всей школе равен {int(sum_scores/sum_num_scores)}')
