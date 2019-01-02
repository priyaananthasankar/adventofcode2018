with open("input.txt") as f:
    input = [int(x.strip()) for x in f.readlines()]
    final_answer = 0
    for i in input:
        final_answer += i
    print(final_answer)            