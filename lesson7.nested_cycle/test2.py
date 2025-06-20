from math import log10, ceil, floor
depth = 100
dots = 0
floor_fulled_ranges = floor(log10(depth))
ceil_fulled_ranges = floor_fulled_ranges + 1
total_range = 0

for i in range(1, floor_fulled_ranges + 1):
    ten_coeff = 10 ** (i - 1)
    range_ = 9 * (ten_coeff or 1)
    dots += range_ * i
    total_range += range_

if floor_fulled_ranges < 1:
    dots = depth
    total_range = depth

dots += (depth - total_range) * ceil_fulled_ranges
dots -= ceil_fulled_ranges
dots *= 2
print(dots)
blocks_q = 1
for i in range(depth, 0, -1):
    for j in range(blocks_q):
        print(depth - j, end="")

    print("." * dots, end="")

    for j in range(1, blocks_q + 1):
        print(depth - blocks_q + j, end="")
    print()

    blocks_q += 1
    dots -= ceil(log10(i)) * 2
