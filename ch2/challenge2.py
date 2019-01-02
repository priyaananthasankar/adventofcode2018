# Part 1
with open("input.txt") as f:
    input = [int(x.strip()) for x in f.readlines()]
    final_answer = 0
    for i in input:
        final_answer += i
    print(final_answer)     

# Part 2
with open("input.txt") as f:
    input = [int(x.strip()) for x in f.readlines()]
    final_answer = 0
    freq = {}
    repeat = True
    while repeat:
        print("Going once...")
        for i in input:
            final_answer += i
            if final_answer in freq:
                print(final_answer)
                repeat = False
                break
            else:
                freq[final_answer] = 1
    