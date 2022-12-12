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

    best_score = 0

    for x in range(size):
        for y in range(size):
            row_score = get_score(row_data[y], x)
            col_score = get_score(col_data[x], y)

            if (row_score * col_score) > best_score:
                best_score = row_score * col_score

    print(best_score)


def get_score(vector_data: list, index):
    front_distance = 0
    back_distance = 0
    index_val = vector_data[index]

    for d in reversed(vector_data[:index]):
        front_distance += 1
        if d >= index_val:
            break

    for d in vector_data[index+1:]:
        back_distance += 1
        if d >= index_val:
            break

    return front_distance * back_distance


main()
