for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            if not(x or y or z) == (not x and not y and not z):
                result = True
            else:
                result = False
            print(f'X={x} Y={y} Z={z} ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z -> {result}')
