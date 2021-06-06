nums = list(map(int, input().split()))

if nums[0] % nums[1] == 0 or nums[1] % nums[0] == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
