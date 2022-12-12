row_data = []
total = 0


def main():

    for l in open('input.txt'):
        l = l.replace('\n', '')
        row_data.append(tuple(map(int, l)))

    col_data = list(zip(*row_data))
    size = len(row_data)

    for r in row_data:
        print(r)

    print()

    for c in col_data:
        print(c)

    total_visible = 0

    for x in range(size):
        for y in range(size):
            row_visible = is_visible(row_data[y], x)
            col_visible = is_visible(col_data[x], y)

            if row_visible or col_visible:
                total_visible += 1

    print(total_visible)


def is_visible(vector_data: list, index):
    front_visible = True
    back_visible = True
    index_val = vector_data[index]

    for d in vector_data[:index]:
        if d >= index_val:
            front_visible = False

    for d in vector_data[index+1:]:
        if d >= index_val:
            back_visible = False

    if front_visible or back_visible:
        return True
    else:
        return False


main()
