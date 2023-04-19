# set the initial value
num = 1
flag = True

# loop until we reach 10
while flag:
    # print the current number
    print(num)
    # increment the number by 1
    num += 1
    # check if we've reached 10
    if num > 10:
        # set the flag to False to exit the loop
        flag = False
