from life import Ocean


def from_input():
    lines = []
    print("input ocean_sizes and generation_count")
    try:
        n, m, count_of_generations = map(int, input().split(' '))
    except ValueError:
        print('incorrect input: not enough values\n')
        return False,

    for _ in range(n):
        try:
            lines.append(input())
            cells = lines[-1].split(' ')
            for i in range(m):
                cell = cells[i]
                assert cell in ('empty', 'stone', 'fish', 'shrimp')
        except IndexError:
            print('incorrect input: not enough values\n')
            return False,
        except AssertionError:
            print('incorrect input: unknown type of cell\n')
            return False,
    return (True, (n, m, count_of_generations, lines))


def from_file(filename):
    lines = []
    print("reading from file {}".format(filename))
    n, m, count_of_generations = 0, 0, 0
    try:
        f = open(filename, 'r')
        n, m, count_of_generations = map(int, f.readline().split(' '))
    except FileNotFoundError:
        print('file {} not found\n'.format(filename))
        return False,
    except ValueError:
        print('incorrect input: not enough values\n')
        return False,
    finally:
        for _ in range(n):
            try:
                lines.append(f.readline().replace('\n', ''))
                cells = lines[-1].split(' ')
                for i in range(m):
                    cell = cells[i]
                    assert cell in ('empty', 'stone', 'fish', 'shrimp')
            except IndexError:
                print('incorrect input: not enough cells in row\n')
                return False,
            except AssertionError:
                print('incorrect input: unknown type of cell\n')
                return False,
    f.close()
    return (True, (n, m, count_of_generations, lines))


def read_data():
    while True:
        all_fine = 1
        print("Choose the type of reading your data:")
        print('\'1\' to read from std input')
        print('\'2 filename\' to read from file')
        s_input = input().split(' ')
        try:
            if s_input[0] == '1':
                res = from_input()
            if s_input[0] == '2':
                res = from_file(s_input[1])
            if res[0]:
                global n, m, count_of_generations, lines
                n, m, count_of_generations, lines = res[1]
            else:
                continue
        except IndexError:
            print('incorrect input: lack of arguments\n')
            continue
        return m, n, count_of_generations, lines


def ocean_to_input(ocean):
    for line in ocean:
        for cell in line:
            print(cell, end=' ')
        print('')


def ocean_to_file(ocean, filename):
    with open(filename, 'w+') as f:
        for line in ocean:
            for i, cell in enumerate(line):
                f.write(cell)
                if i < len(line):
                    f.write(' ')
            f.write('\n')


def write_data(ocean):
    while True:
        print("Choose the type of writing your data:")
        print('\'1\' to write to std output')
        print('\'2 filename\' to write to file')
        s_output = input().split(' ')
        if s_output[0] == '1':
            ocean_to_input(ocean)
        if s_output[0] == '2':
            try:
                filename = s_output[1]
                ocean_to_file(ocean, filename)
            except IndexError:
                print('incorrect input: not enough values\n')
                continue
        break

lines = []
n, m, count_of_generations, lines = read_data()

ocean = Ocean(n, m, count_of_generations, lines)

for state in ocean:
    print("\n" + "~" * 20 + "\ngeneration_count = {}".format(ocean.generation_count))
    ocean_to_input(ocean.ocean)
    print("~" * 20)

write_data(ocean.ocean)
