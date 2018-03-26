def get_neib(ocean, i, j):
	n = len(ocean)
	m = len(ocean[0])
	neib = {'fish': 0, 'shrimp': 0, 'stone': 0, 'empty': 0}
	def add_neib(value):
		neib[value] = neib.get(value, 0) + 1;
	if(i > 0):
		if(j > 0):
			add_neib(ocean[i-1][j-1])
		if(j < m - 1):
			add_neib(ocean[i-1][j+1])
		add_neib(ocean[i-1][j])
	if(i < n - 1):
		if(j > 0):
			add_neib(ocean[i+1][j-1])
		if(j < m - 1):
			add_neib(ocean[i+1][j+1])
		add_neib(ocean[i+1][j])
	if(j > 0):
		add_neib(ocean[i][j-1])
	if(j < m - 1):
		add_neib(ocean[i][j+1])
	return neib

def new_creature(x, neighbors):
	# print(neighbors)
	if(x == 'fish'):
		if (neighbors['fish']) <= 1 or (neighbors['fish']) >= 5:
			return "empty"
		return "fish"
	if(x == 'shrimp'):
		if (neighbors['shrimp']) <= 1 or (neighbors['shrimp']) >= 5:
			return "empty"
		return "shrimp"
	if(x == 'empty'): 
		if neighbors['fish'] == 3:
			return 'fish'
		if neighbors['shrimp'] == 3:
			return 'shrimp'
		return 'empty'
	return 'stone'

def next_gen(ocean):
	n = len(ocean)
	m = len(ocean[0])
	new_ocean = [[''] * m for i in range(n)]
	for i in range(n):
		for j in range(m):
			neighbors = get_neib(ocean, i, j)
			# print(i, j, 'Neighbors:', *neighbors)
			new_ocean[i][j] = new_creature(ocean[i][j], neighbors)
			# for k in range(n):
				# print(*new_ocean[i])
	return new_ocean


