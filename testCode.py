from colorama import Fore

W = Fore.RESET
R = Fore.RED
G = Fore.GREEN
B = Fore.BLUE
C = Fore.CYAN
M = Fore.LIGHTMAGENTA_EX
Y = Fore.LIGHTYELLOW_EX

def result(passed):
	if passed:
		return f"{G}PASSED{W}"
	return f"{R}FAILED{W}"

def test_len(m, targetLen):
	if len(m) == targetLen:
		return True
	return False

def test_eq(m, m2):
	return m == m2

def test_ne(m, m2):
	return m != m2

def test_get(m, key):
	value = m.get(key)
	return value == None or m[key] == value

def test_setdefault(m, key, default):
	m.setdefault(key, default)
	return m[key] == default

def test_pop(m, key, default):
	try:
		if key in m:
			value = m[key]
		else:
			value = default
	
		returnVal = m.pop(key, default)
		if returnVal == value:
			return True
		return False
	except:
		return False

def pop_error(m, key):
	try:
		bool = test_pop(m, key, None)
		return False
	except:
		return True

def test_popitem(m):
	pair = m.popitem()
	if type(pair) == tuple and len(pair) == 2:
		return True
	return False

def popitem_error(m):
	try:
		bool = test_popitem(m)
		return False
	except:
		return True

def test_clear(m):
	m.clear()
	if len(m) == 0:
		return True
	return False

def test_keys(m, goal):
	keys = m.keys()
	try:
		return keys == goal
	except:
		return False

def test_values(m, goal):
	values = m.values()
	try:
		return values == goal
	except:
		return False

def test_update(m, m2):
	try:
		totalLen = len(m) + len(m2)
		m.update(m2)
		if totalLen == len(m):
			return True
		return False
	except:
		return False

def test_getitem(m, key, value):
	return m[key] == value

def getitem_error(m, key, value):
	try:
		m[key] == value
		return False
	except:
		return True

def test_setitem(m, key, value):
	try:
		m[key] = value
		return True
	except:
		return False

def test_delitem(m, key):
	value = m[key]
	del m[key]
	return getitem_error(m, key, value)

def delitem_error(m, key):
	try:
		bool = test_delitem(m, key)
		return False
	except:
		return True

def test_forLoop(m, goal):
	keyList = []
	for i in m:
		keyList.append(i)
	if goal == keyList:
		return True
	return False

### tests begin ###

def testMagic(m, m2):
	print(f'~{M}~{W}'*25)
	print(f"{B}TEST CATEGORY: Magic Methods{W}")
	print(f"Starting Map: {m}")

	print(f"\n{C}__setitem__ ( Map[key] = val ){W}")
	print(f"Item successfully added to Map: {result(test_setitem(m, 'Spain', 'Madrid'))}")
	
	print(f"\n{C}__getitem__ ( Map[key] ){W}")
	print(f"Successfully returns correct item: {result(test_getitem(m, 'Spain', 'Madrid'))}")
	print(f"Raises exception if key not in dictionary: {result(getitem_error(m, 'America', 'Freedom'))}")

	print(f"\n{C}__len__ ( len(Map) ){W}")
	print(f"Successfully returns the correct length of the Map: {result(test_len(m, 1))}")

	m2['Spain'] = 'Madrid'
	print(f"\n{C}__eq__ ( == ){W}")
	print(f"Identical Maps are recognized as equal: {result(test_eq(m, m2))}")

	print(f"\n{C}__delitem__ ( del Map[key] ){W}")
	print(f"Item successfully removed from Map: {result(test_delitem(m2, 'Spain'))}")
	print(f"Raises exception if key not in Map: {result(delitem_error(m2, 'Ethiopia'))}")

	print(f"\n{C}__ne__ ( != ){W}")
	print(f"Different Maps are portrayed as not equal: {result(test_ne(m, m2))}")

	m['Japan'] = 'Tokyo'
	m['Russia'] = 'Moscow'
	m['Mexico'] = 'Mexico City' # i just learned this, very original name

	print(f"{C}\n__iter__ & __contains__ ( for i in Map ){W}")
	print(f"Successfully yields all values of Map: {result(test_forLoop(m, ['Spain', 'Japan', 'Russia', 'Mexico']))}")

	print(f'{M}~{W}~'*25, '\n')
	return m

def testIndexing(m, m2):
	print(f'~{M}~{W}'*25)

	print(f"{B}TEST CATEGORY: Adding & Indexing{W}")
	print(f"Starting Map: {m}")
	
	print(f"\n{C}setdefault(){W}")
	print(f"Item successfully added to Map: {result(test_setdefault(m, 'France', 'Paris'))}")
	print(f"Item already in Map successfully referenced: {result(test_setdefault(m, 'France', 'Paris'))}")

	print(f"\n{C}get(){W}")
	print(f"Successfully returns value of key in Map: {result(test_get(m, 'France'))}")
	print(f"Returns None if key not in Map: {result(test_get(m, 'Venezuela'))}")

	m2['Germany'] = 'Berlin'
	m2['United Kingdom'] = 'London'
	m2['United States of America'] = 'Washington D.C.'
	m2['Canada'] = 'Ottawa'
	print(f"\n{C}update(){W}")
	print(f"Second map successfully added into first: {result(test_update(m, m2))}")
	
	print(f'{M}~{W}~'*25, '\n')
	return m

def testDeleting(m, m2):
	print(f'~{M}~{W}'*25)

	print(f"{B}TEST CATEGORY: Deleting{W}")
	print(f"Starting Map: {m}")

	print(f"\n{C}pop(){W}")
	print(f"Item successfully removed from Map: {result(test_pop(m, 'France', 'modulo'))}")
	print(f"Successfully returns default value if item not in Map: {result(test_pop(m, 'Madagascar', True))}")
	print(f"Raises exception if item not in map and default is None: {result(pop_error(m, 'Madagascar'))}")
	
	print(f"\n{C}popitem(){W}")
	print(f"Successfully returns (key, value) tuple: {result(test_popitem(m))}")
	print(f"Raises exception if given empty Map: {result(popitem_error(m2))}")
	
	m2['Egypt'] = 'Cairo'
	print(f"\n{C}clear(){W}")
	print(f"Successfully clears Map: {result(test_clear(m2))}")
	
	print(f'{M}~{W}~'*25, '\n')
	return m

def testKV(m):
	print(f'~{M}~{W}'*25)
	print(f"{B}TEST CATEGORY: Keys & Values{W}")
	print(f"Starting Map: {m}")

	print(f"\n{C}keys(){W}")
	print(f"Successfully returns list of keys: {result(test_keys(m, ['Spain', 'Japan', 'Russia', 'Mexico', 'Germany', 'United Kingdom', 'United States of America']))}")

	print(f"\n{C}values(){W}")
	print(f"Successfully returns list of values: {result(test_values(m, ['Madrid', 'Tokyo', 'Moscow', 'Mexico City', 'Berlin', 'London', 'Washington D.C.']))}")
	print(f'{M}~{W}~'*25, '\n')
	return m

def testDocstring(m):
	print(f'~{M}~{W}'*25)

	if m.__getitem__.__doc__ != None:
		print(f"{B}__getitem__() Documentation:{Y} {m.__getitem__.__doc__}\n")
	else:
		print(f"{R}__getitem__() Documentation Missing{W}\n")

	if m.__setitem__.__doc__ != None:
		print(f"{B}__setitem__() Documentation:{Y} {m.__setitem__.__doc__}\n")
	else:
		print(f"{R}__setitem__() Documentation Missing{W}\n")

	if m.__delitem__.__doc__ != None:
		print(f"{B}__delitem__() Documentation:{Y} {m.__delitem__.__doc__}\n")
	else:
		print(f"{R}__delitem__() Documentation Missing{W}\n")

	if m.__len__.__doc__ != None:
		print(f"{B}__len__() Documentation:{Y} {m.__len__.__doc__}\n")
	else:
		print(f"{R}__len__() Documentation Missing{W}\n")

	if m.__iter__.__doc__ != None:
		print(f"{B}__iter__() Documentation:{Y} {m.__iter__.__doc__}\n")
	else:
		print(f"{R}__iter__() Documentation Missing{W}\n")

	if m.__contains__.__doc__ != None:
		print(f"{B}__contains__() Documentation:{Y} {m.__contains__.__doc__}\n")
	else:
		print(f"{R}__contains__() Documentation Missing{W}\n")

	if m.get.__doc__ != None:
		print(f"{B}get() Documentation:{Y} {m.get.__doc__}\n")
	else:
		print(f"{R}get() Documentation Missing{W}\n")

	if m.setdefault.__doc__ != None:
		print(f"{B}setdefault() Documentation:{Y} {m.setdefault.__doc__}\n")
	else:
		print(f"{R}setdefault() Documentation Missing{W}\n")

	if m.pop.__doc__ != None:
		print(f"{B}pop() Documentation:{Y} {m.pop.__doc__}\n")
	else:
		print(f"{R}pop() Documentation Missing{W}\n")

	if m.popitem.__doc__ != None:
		print(f"{B}popitem() Documentation:{Y} {m.popitem.__doc__}\n")
	else:
		print(f"{R}popitem() Documentation Missing{W}\n")

	if m.clear.__doc__ != None:
		print(f"{B}clear() Documentation:{Y} {m.clear.__doc__}\n")
	else:
		print(f"{R}clear() Documentation Missing{W}\n")

	if m.keys.__doc__ != None:
		print(f"{B}keys() Documentation:{Y} {m.keys.__doc__}\n")
	else:
		print(f"{R}keys() Documentation Missing{W}\n")

	if m.values.__doc__ != None:
		print(f"{B}values() Documentation:{Y} {m.values.__doc__}\n")
	else:
		print(f"{R}values() Documentation Missing{W}\n")

	if m.update.__doc__ != None:
		print(f"{B}update() Documentation:{Y} {m.update.__doc__}\n")
	else:
		print(f"{R}update() Documentation Missing{W}\n")

	if m.__eq__.__doc__ != None:
		print(f"{B}__eq__() Documentation:{Y} {m.__eq__.__doc__}\n")
	else:
		print(f"{R}__eq__() Documentation Missing{W}\n")

	if m.__ne__.__doc__ != None:
		print(f"{B}__ne__() Documentation:{Y} {m.__ne__.__doc__}")
	else:
		print(f"{R}__ne__() Documentation Missing{W}")
	
	print(f'{M}~{W}~'*25, '\n')