import collections
with open("input.txt") as f:
    input = [x.strip() for x in f.readlines()]
    two_list = 0
    three_list = 0
    for item in input:
        d = collections.defaultdict(int)
        for c in item:
            d[c] += 1
        two_count_per_item = 0 
        three_count_per_item = 0
        for c in d:
            if d[c] == 2:
                two_count_per_item += 1
            if d[c] == 3:
                three_count_per_item += 1

        # count occurances just once
        if two_count_per_item >= 1:
            two_list +=1
        if three_count_per_item >= 1:
            three_list += 1

# checksum
print(two_list * three_list)
    
