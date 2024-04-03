N = int(input())

bag_of_words = sorted(set([input() for _ in range(N)]), key=lambda x: (len(x), x))

for item in bag_of_words:
    print(item)