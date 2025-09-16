n, r = map(int, input().split())
nums = list(map(int, input().split()))
r_ = r  # 2
left_one_index = None  # None
signal = False
while r > 0:  # 2
    if nums[r - 1] == 1:
        if signal:
            pass
        else:
            left_one_index = r - 1
            signal = True
            pass
    elif nums[r - 1] == 0:
        if signal:
            signal = False
            left_one_index = None
        else:
            pass
        pass
    r -= 1
if left_one_index is None:
    left_one_index = 0
else:
    left_one_index += 1
sana = 0  #  2
for i in range(left_one_index, r_):  # 1 2
    if nums[i] == 0:
        sana += 1
        pass
    elif nums[i] == 1:
        sana += 2
    else:
        pass

right_one_index = None
signal_r = False
for i in range(r_, n):  # 3 4 5
    if nums[i] == 0:
        if signal_r:
            signal_r = False
            right_one_index = None
        else:
            pass
        pass
    elif nums[i] == 1:
        if signal_r:
            pass
        else:
            right_one_index = i
            signal_r = True
        pass
    else:
        pass

if right_one_index is None:
    right_one_index = n
for i in range(r_, right_one_index):
    if nums[i] == 0:
        sana += 1
        pass
    elif nums[i] == 1:
        sana += 2
    else:
        pass
print(sana)