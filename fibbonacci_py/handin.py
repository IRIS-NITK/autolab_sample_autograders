# Get number of testcases
T=int(input())

# Run the program T(num of test cases) times
for _ in range(T):
    n = int(input())
    prev_num = 1
    cur_num = 0
    next_num = 0
    for i in range(n):
        next_num = prev_num + cur_num
        prev_num = cur_num
        cur_num = next_num
    print(cur_num)

