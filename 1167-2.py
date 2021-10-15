while (amount_child := int(input())) != 0:
    child_name = []
    child_num = {}
    for n in range(amount_child):
        name, num = input().split()
        child_name.append(name)
        child_num[name] = int(num)
    index = 0
    removed = child_name[index]
    token = child_num[removed]
    while amount_child != 1:
        n = child_num[removed] % 2
        while token > 0:
            token -= 1
            index += (1 if n else -1)
            if index == amount_child or index == -1:
                index = (0 if n else amount_child - 1)
        removed = child_name.pop(index)
        amount_child -= 1
        rest = child_num[removed] % amount_child
        token = (rest if rest > 0 else child_num[removed])
        if child_num[removed] % 2 == 1:
            token -= 1
            if index == amount_child:
                index = 0
    print(f"Vencedor(a): {child_name[0]}")
