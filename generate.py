import life


def read_data():

    while(True):
        all_fine = 1
        print("Choose the type of reading your data:")
        print('\'1\' to read from std input')
        print('\'2 filename\' to read from file')
        s_input = input().split(' ')
        lines = []
        try:
            if s_input[0] == '1':
                print("input osean_sizes and generation_count")
                try:
                    n, m, n_gen = map(int, input().split(' '))
                except ValueError:
                    all_fine = 0
                    print('incorrect input: not enough values\n')
                    continue

                for _ in range(n):
                    try:
                        lines.append(input())
                        cells = lines[-1].split(' ')
                        for i in range(m):
                            cell = cells[i]
                            assert cell in ('empty', 'stone', 'fish', 'shrimp')
                    except IndexError:
                        all_fine = 0
                        print('incorrect input: not enough values\n')
                        break
                    except AssertionError:
                        all_fine = 0
                        print('incorrect input: unknown type of cell\n')
                        break

            if s_input[0] == '2':
                filename = s_input[1]
                print("reading from file {}".format(filename))
                n, m, n_gen = 0, 0, 0
                try:
                    f = open(filename, 'r')
                    n, m, n_gen = map(int, f.readline().split(' '))
                except FileNotFoundError:
                    print('file {} not found\n'.format(filename))

                except ValueError:
                    all_fine = 0
                    print('incorrect input: not enough values\n')
                    continue

                finally:
                    for _ in range(n):
                        try:
                            lines.append(f.readline().replace('\n', ''))
                            cells = lines[-1].split(' ')
                            for i in range(m):
                                cell = cells[i]
                                assert cell in ('empty', 'stone', 'fish', 'shrimp')
                        except IndexError:
                            all_fine = 0
                            print('incorrect input: not enough cells in row\n')
                            break
                        except AssertionError:
                            all_fine = 0
                            print('incorrect input: unknown type of cell\n')
                            break
                    f.close()
            elif s_input[0] == '2':
                with open(filename, 'r') as f:
                    n, m, n_gen = map(int, f.readline().split(' '))
                    for line in f:
                        lines.append(line.replace('\n', ''))
        except IndexError:
            all_fine = 0
            print('incorrect input: lack of arguments\n')
            continue
        if all_fine:
            break
    return m, n, n_gen, lines


def write_data(ocean):

    while(True):
        all_fine = 1

        print("Choose the type of writing your data:")
        print('\'1\' to write to std output')
        print('\'2 filename\' to write to file')

        s_output = input().split(' ')
        if s_output[0] == '1':
            for line in ocean:
                for cell in line:
                    print(cell, end=' ')
                print('')
        if s_output[0] == '2':
            try:
                filename = s_output[1]
                with open(filename, 'w+') as f:
                    for line in ocean:
                        for i, cell in enumerate(line):
                            f.write(cell)
                            if i < len(line):
                                f.write(' ')
                        f.write('\n')
            except IndexError:
                all_fine = 0
                print('incorrect input: not enough values\n')
                continue
        if all_fine:
            break3

lines = []
n, m, n_gen, lines = read_data()
ocean = [[] for i in range(n)]
for i in range(n):
    ocean[i] = list(lines[i].split())

for i in range(n_gen):
    ocean = life.next_gen(ocean)
    # print('current generation = {}'.format(n_gen))
    # for j in range(n):
    #     print(*ocean[j])
write_data(ocean)
