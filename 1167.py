while (amount_child := int(input())) != 0:
    child_name = []
    child_num = {}
    for n in range(amount_child):
        name, num = input().split()
        child_name.append(name)
        child_num[name] = int(num)
    removed = child_name[0]
    token = child_num[removed] % amount_child
    index = 0
    # ['Fernanda', 'Gabriel', 'Fernando', 'Gustavo']
    while amount_child != 1:
        if child_num[removed] % 2 == 1:
            while token > 0:
                token -= 1
                index += 1
                if index == amount_child:
                    index = 0
        else:
            while token > 0:
                token -= 1
                index -= 1
                if index == -1:
                    index = amount_child - 1
        removed = child_name.pop(index)
        amount_child -= 1
        rest = child_num[removed] % amount_child
        if rest != 0:
            token = rest
        else:
            token = child_num[removed]
        # print(removed, index, child_name)
        if child_num[removed] % 2 == 1:
            token -= 1
            if index == amount_child:
                index = 0
    print(f"Vencedor(a): {child_name[0]}")
