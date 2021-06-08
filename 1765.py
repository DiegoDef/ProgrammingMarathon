while (x := int(input())) != 0:
    for n in range(1, x+1):
        values = list(map(float, input().split()))
        total = round((values[0] * (values[1] * values[2])), 2)

        print(f"Size #{n}:")
        print(f"Ice Cream Used: {total:.2f} cm2")
    print()
