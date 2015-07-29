import math,random

def undo_lists(lists):
    # takes lists of lists and returns a single list
    while type(lists[0]) == list:
        temp = []
        for item in lists:
            temp += item
        lists = temp
    return lists


def perm_helper(string,char):
    # given a string a char, permute char through string
    # returning list of all permutations of string and single char
    string = undo_lists(string)
    permut = []
    for item in string:
        for index in range(0,len(item)+1):
            permut.append(item[:index]+char+item[index:])
    return permut


def perm(string):
    # given string, return list of all permutations of same length
    if len(string) <= 1:
        return l
    elif len(string) == 2:
        return [string,string[1]+string[0]]
    else:
        char = string[-1]
        rest = string[:-1]
        return perm_helper(perm(rest),char)



class Node():
	'''
	linked lists
	'''
	def __init__(self,data = None):
		self.data = data
		self.next = None

	def add_node(self,data):

		if self.data == None:
			self.data = data

		else:
			while self.next != None:
				self = self.next
			self.next = Node(data)


	def del_node(self,data):
		if self.data == None:
			print "ERROR: Null list"
			return self
		elif self.data == data:
			if self.next == None:
				self.data = None
				return self
			else:
				return self.next
		start = self
		prev = self
		self = self.next
		while self.next != None:
			if self.data == data:
				prev.next = self.next
				return start
			prev = self
			self = self.next
		if self.data == data:
			prev.next = None
			return start
		else:
			print "ERROR: value not in list"
			return start

	def get_len(self):
		length = 0
		if self.data == None:
			return length
        
		while self.next != None:
			length += 1
			self = self.next
		return length + 1

	def __str__(self):

		string = ''

		while self.next != None:
			string += str(self.data) + ' -> '
			self = self.next
		return string + str(self.data)

class ordered_list():
	'''
	creates a linked list stores ints in order 
	'''
	def __init__(self,value = None):
		self.value = value
		self.next = None
		self.head = None

	def add_node(self,value):
		if self.value == None:
			#list is empty
			self.value = value
			self.next = None
			self.head = self
		else:
			while self.next != None:
				if value < self.value:
					#new value < first node
					new_head = ordered_list(value)
					new_head.next = self
					return new_head
                
				elif value < self.next.value:
					temp = self.next
					self.next = ordered_list(value)
					self.next.next = temp
					return
				self = self.next
			self.next = ordered_list(value)

	def __str__(self):
		string = ''
		while self.next != None:
			string += str(self.value) + ' - > '
			self = self.next
		string += str(self.value)
		return string


def remove_dup(l):
	'''
	given a linked list, remove all duplicate nodes 
	'''
	new_list = Node(l.data)
	have_seen = [l.data]
	l = l.next
	for i in range(0,l.get_len()):
		if l.data not in have_seen:
			new_list.add_node(l.data)
			have_seen.append(l.data)
		l = l.next
	return new_list        

class Stack():
	'''
	create a stack 
	'''
	def __init__(self):
		self.stack = []

	def push(self,data):
		self.stack.append(data)

	def pop(self):
		if len(self.stack) > 0:
			self.stack = self.stack[:-1]

	def get_len(self):
		print len(self.stack)

	def __str__(self):

		string = ''
		for index in range(len(self.stack)-1,0,-1):
			string += str(self.stack[index]) + ' -> '
		return string + str(self.stack[0])    


class tree():
	def __init__(self,value=None):
		self.value = value
		self.left = None
		self.right = None
		self.height = 0
		self.parent = None
                
	def add_node(self,value):
		if self.value == None:
			self.value = value
			self.height = 1
		else:
			if value < self.value:
				if self.left == None:
					self.left = tree(value)
					self.height += 1
					self.left.parent = self
				else:
					self.left.add_node(value)
			else:
				if self.right == None:
					self.right = tree(value)
					self.height += 1
					self.right.parent = self
				else:
					self.right.add_node(value)
                        
	def nodes_at(self,depth):
		if depth > self.height:
			print "depth exeeded tree height"
		elif depth == 0:
			return self.value
		else:
			nodes = []
			if self.left != None:
				nodes.append(self.left.nodes_at(depth-1))
			if self.right != None:
				nodes.append(self.right.nodes_at(depth-1))
			return nodes

	def __str__(self):
		if self.height == 0:
			return
		else:
			p = ''
			for i in range(0,self.height):
				p += str(self.nodes_at(i)) + '\n'
			return p

def min_height_tree(sorted_list):
	'''
	given a sorted list make a binary tree with min height
	'''
	if len(sorted_list) == 0:
		return 
	else:
		midway = len(sorted_list)/2
		mid = sorted_list[midway]
		left = sorted_list[:midway]
		right = sorted_list[midway+1:]

		root = Tree(mid)
		root.left = min_height_tree(left)
		root.right = min_height_tree(right)

		return root     

'''
bfs and dfs will use get_path() and rev_list() to 
solve.
'''
def rev_list(l):
	'''
	reverses a given list
	'''
	last = -1
	for i in range(0,len(l)/2):
		temp = l[i]
		l[i] = l[last]
		l[last] = temp
		last -= 1
	return l

def get_path(node):
	'''
	walks up all parents of a given node until root is found
	returning the path generated
	'''
	path = []
	while node.parent != None:
		path.append(node.value)
		node = node.parent
	path.append(node.value)
	return rev_list(path)      

def bfs(tree,value):
	'''
	breath first search of tree
	'''
	to_check = []
	if tree.height == 0:
		return (False,[])
	else:
		to_check.append(tree)
		while len(to_check) > 0:
			current = to_check.pop(0)
			if current.value == value:
				return (True,get_path(current))
			else:
				if current.left != None:
					to_check.append(current.left)
				if current.right != None:
					to_check.append(current.right)
	return (False,[])

def dfs(tree,value):
	'''
	depth first search of tree
	'''
	to_check = []
	if tree.height == 0:
		return False
	else:
		to_check.append(tree)
		while len(to_check) > 0:
			current = to_check.pop(0)
			print current.value
			if current.value == value:
				return (True,get_path(current))
			else:
				if current.left != None:
					to_check.insert(0,current.left)
				if current.right != None:
					to_check.insert(1,current.right)
		return False
t = tree()
t.add_node(5)
t.add_node(1)
t.add_node(3)
t.add_node(10)
t.add_node(0)
t.add_node(7)
t.add_node(11)

def qsort(l):
	'''
	quicksort on list
	'''
	if len(l) == 0:
		return l
	else:
		smaller = []
		bigger = []
		mid = l[len(l)/2]
		for index in l:
			if index < mid:
				smaller.append(index)
			elif index > mid:
				bigger.append(index)

		smaller = qsort(smaller)
		bigger = qsort(bigger)
		return smaller + [mid] + bigger      

def merg(l):
	'''
	merg sort
	'''
	if len(l) < 2:
		return l
	else:
		result = []
		mid = len(l)/2
		left = merg(l[:mid])
		right = merg(l[mid:])
		while len(left) > 0 or len(right) > 0:
			if len(left) > 0 and len(right) > 0:
				if left[0] < right[0]:
					result.append(left.pop(0))
				else:
					result.append(right.pop(0))
			else:
				return result + left + right        

def bi(l,value):
	'''
	binary search
	'''
	if len(l) == 0:
		return False
	else:
		mid = len(l) / 2
		if value == l[mid]:
			return True
		elif value < l[mid]:
			return bi(l[:mid],value)
		else:
			return bi(l[mid+1:],value)

def is_prime(n):
	'''
	given an int, return bool is prime
	'''
	if n == 2:
		return True
	elif n % 2 == 0:
		return False
	else:
		for i in range(3,int(math.sqrt(n))+2,2):
			if n % i == 0:
				return False
		return True          

def sieve(max_num):
	'''
	sieve of eratosthenes
	(calls quicksort and is_prime functions)
	'''
	primes = []
	numbers = []
	for i in range(2,max_num+1):
		numbers.append(i)

	while len(numbers) > 0:
		p = numbers[0]
		if is_prime(p):
			primes.append(p)
			for num in numbers:
				if num % p == 0:
					numbers.remove(num)
	return qsort(primes)    


'''
bottom up fib.
memo will store our already found fib numbers starting with the first two
numbers (eg 1,1) which we will initialize upon calling the function.

using an index to go from 0 to n , calculating the new fib on each step,
then storing it in memo.  If memo has more than two elements, we can disregard
all but the last two.

Once index = n, we simply return the last thing in memo.

This will run in O(n), since each fib will be calculated only once.
Also its space complexity is O(1), since memo doesn't grow beyond 3,
and the the stack isn't filling with recursive calls
(as in return fib(n-1)+fib(n-2) would be).
'''

def fib(index,memo,n):
	if index == n:
		return memo[-1]
	if len(memo) > 2:
		memo = memo[-2:]
	memo.append(memo[-2] + memo[-1])
	return fib(index+1,memo,n)


'''
reverse string keeping spacing in tacked & reverse words
so every word is in reverse order but readable (with original spacing)
'''
def rev_word(word):
	rword = ''
	for i in range(-1,-len(word)-1,-1):
		rword += word[i]
	return rword


def rev_string(string):
	rev_string = ''
	for i in range(-1,-len(string)-1,-1):
		rev_string += string[i]

	start = 999
	started = False
	for i in range(0,len(string)):
		if rev_string[i] != ' ' and started == False:
			start = i
			started = True
	        
		if i == len(string)-1 and rev_string[i] != ' ':
			word = rev_word(rev_string[start:i+1])
			rev_string = rev_string[:start] + word 
			return rev_string
	    
		if started == True and rev_string[i] == ' ':
			word = rev_word(rev_string[start:i])
			rev_string = rev_string[:start] + word + rev_string[i:]
			started = False
	        
	return rev_string

def dijstra(g,start):
	'''
	#Dijstra example problem
	'''
	'''
	example of graph used in dijstra
	(g['b'] = [('f',10)] means node b is connected to f with value 10)

	g = {}
	g['a'] = [('b',20),('g',90),('d',80)]
	g['b'] = [('f',10)]
	g['c'] = [('h',20),('d',10),('f',50)]
	g['d'] = [('g',20)]
	g['e'] = [('g',30),('b',50)]
	g['f'] = [('c',10),('d',40)]
	g['g'] = [('a',20)]
	g['h'] = []
	'''
	if start not in g.keys():
		print "starting postion not in graph"
		return
	else:
		shortest_path = {}
		finished = [start]
		for key in g.keys():
			shortest_path[key] = (999,'')

		todo = []
		for path in g[start]:
			todo.append(path[0])  #holds all connections from start node
		key = start #current postion
        
		while len(todo) > 0:
			for path in g[key]:
                #path := (to_node,cost)
                #shortest_path[key] = (cost,from_node)

				if shortest_path[path[0]][0] == 999:
                    #print key, path
					if shortest_path[key][0] == 999:
						shortest_path[path[0]] = (path[1],key)
					else:
						path_cost = path[1] + shortest_path[key][0]
						if path_cost < shortest_path[path[0]][0]:
							shortest_path[path[0]] = (path_cost,key)
				else:
					path_cost = path[1] + shortest_path[key][0]
					if path_cost < shortest_path[path[0]][0]:
						shortest_path[path[0]] = (path_cost,key)
						todo.append(path[0])
			if key not in finished:
				finished.append(key)
			key = todo.pop(0)
			for path in g[key]:
				if path[0] not in finished:
					todo.append(path[0])
                    
		return shortest_path
                
                    
def is_pal(string):
	'''
	checks if a string in a palandrome returns bool
	'''
	if len(string) == 0:
		return True
	else:
		alpha = 'abcdefghijklmnopqrstuvwxyz'
		string = string.lower()
		for index in range(0,len(string)):
			if string[index] not in alpha:
				string = string.replace(string[index],' ')
		string = string.replace(' ','')
		for index in range(0,len(string)):
			if string[index] != string[-index-1]:
				return False
		return True


def rotate_string(string):
	'''
	To rotate string by K characters means to cut these characters from
	the beginning and transfer them to the end. If K is negative, characters,
	on contrary should be transferred from the end to the beginning.
	'''
	if len(string) == 0:
		return
	else:
		pivot = ''
		for index in range(0,len(string)):
			if string[index] == ' ':
				pivot = int(string[:index])
				string = string[index+1:]
				break
        
		if pivot > 0:
			return string[pivot:] + string[:pivot]
		else:
			return string[pivot:] + string[:pivot]        


def pascal(n):
	'''
	takes in a natural number, returns
	that level of pascal's triangle
	'''
	r1 = [1]
	r2 = [1,1]
	rc = []
	print "0:",r1
	print "1:",r2
	count = 2
	for i in range(0,n-1):
		rc.append(1)
		for j in range(1,len(r2)):
			new = r2[j-1]+r2[j]
			rc.append(new)
		rc.append(1)
		temp = rc
		r2 = temp
		rc = []        
		print count,r2
		count += 1 
        
	return r2     

'''
balanced takes in a string and returns if the different types of paran "({[" are balanced
balanced uses lr(),lr_index(),middle(),parse() as helper functions
'''

def balanced(s):
	left = 0
	right = 0
	for i in s:
		if i == '(':
			left += 1
		elif i == ')':
			right += 1
	return left == right

def lr(s):
	left = 0
	right = 0
	for i in s:
		if i == '(':
			left += 1
		elif i == ')':
			right += 1
	return left,right

def lr_index(s):
	left = []
	right = []
	for i in range(0,len(s)):
		if s[i] == '(':
			left.append(i)
		elif s[i] == ')':
			right.append(i)
	return left,right
            

def middle(s):
	if not balanced(s):
		return None
	else:
		left,right = lr(s)
		middle = ''
		for i in s:
			if left == 0:
				if i != ')':
					middle += i
				else:
					return middle
			if i == '(':
				left -= 1

def parse(s):
	if not balanced(s):
		return None
	elif len(s) == 0:
		return None
	else:
		left,right = lr_index(s)
		front = s[:left[-1]]
		mid = middle(s)
		found = False
		i = 0
		while not found:
			if right[i] > left[-1]:
				end = s[right[i]+1:]
				found = True
			else:
				i += 1
		new_s = front + end
		#print front
		print mid
		#print end
		parse(new_s)

'''
power set returns power set of a list of objects:
uses rev(),add_zeros(),bi()
'''

def rev(s):
	#reverses a list
	temp = []
	answer = ''
	s = list(s)
	while len(s) > 0:
		temp.append(s.pop())
	for i in temp:
		answer += i
	return answer

def add_zeros(biggest,current):
	current = rev(current)
	while len(biggest) > len(current):
		current += '0'
	return rev(current)
        


def bi(n):
	answer = ''
	if n == 0:
		return '0'
	while n > 0:
		if n % 2 == 1:
			answer += '1'
		else:
			answer += '0'
		n /= 2
	return rev(answer)

def convert_to_str(s):
	for i in range(0,len(s)):
		s[i] = str(s[i])
	return s


def power_set(s):
	if type(s[0]) != 'str':
		s = convert_to_str(s)
	p_set = []
	bi_list = []
	biggest = bi(2**len(s)-1)
	for i in range(0,2**len(s)):
		bi_list.append(add_zeros(biggest,bi(i)))
	for element in bi_list:
		temp = ''
		for index in range(0,len(element)):
			if element[index] == '1':
				temp += s[index]
		p_set.append(temp)

	return p_set
 