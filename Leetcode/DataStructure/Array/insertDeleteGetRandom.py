# 380. Insert Delete GetRandom O(1)
# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.

class RandomizedSet:

    def __init__(self):
        self.arr_map = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.arr:
            return False
        self.arr_map[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if not val in self.arr_map:
            return False 
        last_elem_in_list = self.arr[-1]
        index_of_elem_to_remove = self.arr_map[val]

        self.arr_map[last_elem_in_list] = index_of_elem_to_remove
        self.arr[index_of_elem_to_remove] = last_elem_in_list

        self.arr[-1] = val

        self.arr.pop()

        self.arr_map.pop(val)

        return True 

    def getRandom(self) -> int:
        return random.choice(self.arr)
    

class RandomizedSet1:

    def __init__(self):
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.arr:
            return False
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.arr:
            self.arr.remove(val)
            return True
        else:
            return False   

    def getRandom(self) -> int:
        return random.choice(self.arr)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()