import life


def read_data():
	print("Choose the type of reading your data:")
	print('\'1 input\' to read from std input')
	print('\'2 filename\' to read from file')

	s_input = input().split(' ')
	assert s_input[0] in ['1', '2'] and len(s_input) == 2, 'incorrect input'
	lines = []
	if s_input[0] == '1':
		assert s_input[1] == 'input', 'incorrect input'
		print("input osean_sizes and generation_count")
		m, n, n_gen = map(int, input().split(' '))
		for _ in range(n):
			lines.append(input())

	if s_input[0] == '2':
		with open(s_input[1], 'r') as f:
			m, n, n_gen = map(int, f.readline().split(' '))
			for line in f:
				lines.append(line.replace('\n', ''))
	# print(lines)
	return m, n, n_gen, lines

# read_data()
def write_data(ocean):
	print("Choose the type of writing your data:")
	print('\'1 output\' to write to std output')
	print('\'2 filename\' to write to file')

	s_output = input().split(' ')
	assert s_output[0] in ['1', '2'] and len(s_output) == 2, 'incorrect input'
	if s_output[0] == '1':
		assert s_output[1] == 'output', 'incorrect input'
		# print('current generation = {}'.format(gen))
		for line in ocean:
			for cell in line:
				print(cell, end=' ')
			print('')

	if s_output[0] == '2':
		with open(s_output[1], 'w+') as f:
			# f.write('current generation = {}'.format(gen))
			# f.write('\n')
			for line in ocean:
				for i, cell in enumerate(line):
					f.write(cell)
					if i < len(line):
						f.write(' ')
				f.write('\n')


# m, n, n_gen, lines = read_data()
# ocean = [[] for i in range(n)]
# for i in range(n):
# 	ocean[i] = list(map(str, lines[i].split()))
# print(ocean)
# write_data(ocean)



# with open("input.txt", 'r') as f:
# 	for line in f:
# 		pass
# 	print(line[-1])
# 	print(s0)
# 	print(str(s1))
# print(s1)
# print(len(s1.split('\n')))
# if(input() == "1"):
# 	f1 = input()
# else:
# 	print("Choose the name of input file")
# 	with open(input(), "r") as f1:
lines = []
n, m, n_gen, lines = read_data()
ocean = [[] for i in range(n)]
for i in range(n):
	ocean[i] = list(lines[i].split())
	assert len(ocean[i]) == m, 'incorrect input, try again'

for i in range(n_gen):
	ocean = life.next_gen(ocean);
	# print('current generation = {}'.format(n_gen))
	# for j in range(n):
		# print(*ocean[j])
write_data(ocean)
