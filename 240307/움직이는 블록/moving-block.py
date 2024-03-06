import math 

n = int(input())

block_num = [int(input()) for _ in range(n)]
standard = int(sum(block_num)/n)

diff = [abs(block-standard) for block in block_num]

min_move = math.ceil(sum(diff)/2)
print(min_move)