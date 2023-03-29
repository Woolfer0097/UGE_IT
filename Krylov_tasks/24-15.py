nums = open("24/24var14-20.txt").read()
nums = nums.replace("11", "").replace("22", "").replace("00", "") \
    .replace("33", "").replace("44", "").replace("55", "").replace("66", "") \
    .replace("77", "").replace("88", "").replace("99", "")
print(len(nums))
