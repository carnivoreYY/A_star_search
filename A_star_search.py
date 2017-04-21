class Gragh:
	def __init__(self):
		self.nodes = set()
		self.edges = {}
		self.distances = {}

	def add_node(self, value):
		self.nodes.add(value)

	def add_edge(self, from_node, to_node, distance):
		self.set_edge(from_node, to_node, distance)
		self.set_edge(to_node, from_node, distance)

	def set_edge(self, from_node, to_node, distance):
		self.edges.setdefault(from_node, [])
		self.edges[from_node].append(to_node)
		self.distances[(from_node, to_node)] = distance

def astar(gragh, start, goal, w1, w2):
	closed_set = set()
	nodes = set()
	nodes.add(start)
	visited = {}
	g = {}
	h = {}
	f = {}
	h = {'A': 366, 'B': 0, 'C': 160, 'D': 242, 'F': 178, 'L': 244, 
	'M': 241, 'O': 380, 'P': 98, 'R': 193,'S': 253, 'T': 329, 'Z': 374}
	g[start] = 0
	f[start] = w1*g[start] + w2*h[start]
	while nodes:
		x = None
		for node in nodes:
			if x is None:
				x = node
			elif f[node] < f[x]:
				x = node
		nodes.remove(x)
		if x == goal:
			return g, visited
		closed_set.add(x)
		for y in gragh.edges[x]:
			if y in closed_set:
				continue
			temp_f = w1*(g[x] + gragh.distances[(x, y)]) + w2*h[y]
			if y not in nodes or temp_f < f[y]:
				nodes.add(y)
				visited[y] = x
				f[y] = temp_f
				g[y] = g[x] + gragh.distances[(x, y)]
	return g, visited

def path(gragh, start, goal, w1, w2):
	costs ,paths = astar(gragh, start, goal, w1, w2)
	route = [goal]
	while goal != start:
		route.append(paths[goal])
		goal = paths[goal]
	route.reverse()
	return route, costs            

if __name__ == '__main__':
	g=Gragh()
	vertices = ['Z', 'A', 'T', 'L', 'M', 'D', 'C', 'P', 'R', 'O', 'S', 'F', 'B']
	for vertex in vertices:
		g.add_node(vertex)
	i = 0
	dist = [71, 140, 75, 118, 111, 70, 75, 120, 146, 138, 97, 151, 80, 99, 211, 101]
	edges = ['ZO', 'AS', 'ZA', 'AT', 'TL', 'LM', 'MD', 'DC', 'CR', 'CP', 'RP', 'OS', 'SR', 'SF', 'FB', 'PB']
	for edge in edges:
		g.add_edge(edge[:1], edge[1:], dist[i])
		i += 1

	city_abstract = {'Z':'Zerind', 'A':'Arad', 'T':'Timisoara', 'L':'Lugoj', 'M':'Mehadia', 'D':'Doreta', 'C':'Craiova', 'P':'Pitesti', 'R':'Rimnicu Vilcea', 'O':'Oradea', 'S':'Sibiu', 'F':'Fagaras', 'B':'Bucharest'}
	print(city_abstract)

	r,c = path(g, 'Z', 'B', 1, 1)
	print(r)
	print(len(r))
	print(c['B'])

	r,c = path(g, 'Z', 'B', 0.25, 0.75)
	print(r)
	print(len(r))
	print(c['B'])

	r,c = path(g, 'Z', 'B', 0.75, 0.25)
	print(r)
	print(len(r))
	print(c['B'])
	
