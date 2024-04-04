N = int(input())

num_set = set()

for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):

                    string = f"{a}{b}{c}{d}{e}"
                    for i in range(6):
                        ls = string[:i]
                        rs = string[i:]
                        
                        final = ls+str(666)+rs
                        num_set.add(int(final))

print(sorted(num_set)[N-1])
