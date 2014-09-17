def draw_tree(n, base, leaves):
    for i in range(int(n/2) + 1):
        print('   ' + (int(n/2) - i)*' ' + str((2*i + 1)*leaves))
    print('   ' + (int(n/2) - 1)*' ' + str(3*base))

draw_tree(21, '#', '*')