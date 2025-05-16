# Sample 4 Map Class

class Map:

    class Item:

        def __init__(self, k, v):
            self.__key = k
            self.__value = v

        def __eq__(self, other):
            return self.__value == other.__value

        def __lt__(self, other):
            return self.__key < other.__key

        def __gt__(self, other):
            return self.__key > other.__key

        def __str__(self):
            return f"{self.__key}:{self.__value}"

    

    def __getitem__(self, key):
        '''Returns item value associated with key'''
        for item in self.__map:
            if item._Item__key == key:
                return item._Item__value
        raise KeyError(f"Key {key} not found")

    def __str__(self):
        out = "{"
        for item in self.__map:
            out += f"{item}, "
        if len(out) > 1:
            out = out[:-2]
        out += "}"

        return out

    

    

    def __delitem__(self, key):
        '''Deletes item at given key from Map'''
        for i in range(len(self.__map)):

            
            if self.__map[i]._Item__key == key:
                del self.__map[i]



                return
        raise KeyError(f"Key {key} not found")
    
    def __len__(self):
        '''Returns the number of items in the Map'''
        return len(self.__map)

    def __iter__(self):
        '''Makes iterable Map object'''
        for item in self.__map:

            yield item._Item__key

    def keys(self):




        k = []
        for item in self.__map:
            k.append(item._Item__key)
        return self.__map

    def __contains__(self, key):
        '''Determines if a key is in the Map'''
        for item in self.__map:

            if item._Item__key == key:
                return True
        
        return False

    def __init__(self):
        self.__map = []

    def get(self, key, default=None):
        '''Retrieves item attached to given key'''
        for item in self.__map:
            if item._Item__key == key:



                return item._Item__value
        return default

    def setdefault(self, key, default):
        '''Adds item to Map with default value'''
        for item in self.__map:
            if item._Item__key == key:
                return item._Item__value
        self[key] = default
        return default











    def __setitem__(self, key, value):
        '''Adds new element or changes existing one'''
        for item in self.__map:
            if item._Item__key == key:
                item._Item__value = value
                return
        item = self.Item(key, value)
        self.__map.append(item)
    
    def pop(self, key, default=None):
        '''Remove and return an element with a given key'''
        for i in range(len(self.__map)):
            if self.__map[i]._Item__key == key:
                item = self.__map[i]
                del self.__map[i]
                return item._Item__value






        if default is not None:
            return default



        raise KeyError(f"Key {key} not found")





    def popitem(self):
        '''Remove item last added to Map'''
        if len(self) == 0:
            raise KeyError("Map is empty")

        item = self.__map[-1]
        del self.__map[-1]
        return item._Item__key, item._Item__value
    def clear(self):
        '''Removes all items from Map'''
        self.__map = []

    


    def values(self):
        '''Returns list of all values'''
        v = []
        for item in self.__map:
            v.append(item._Item__value)
        return v
    def update(self, other):
        '''Adds all elements of a Map to another'''
        if type(other) != type(self):
            raise TypeError("Map object cannot join to non-Map object")
        for k in other:
            if k not in self:
                v = other[k]
                self[k] = v



    def __eq__(self, other):
        '''Determines if two maps contain the same key:value pairs'''
        if len(self) != len(other):


            return False

        for k in other:

            if k in self:

                if other[k] != self[k]:



                    return False
            else:

                return False
                
        return True


    def __ne__(self, other):
        '''Determines if two maps do not contain the same key:value pairs'''




        return not(self == other)

    