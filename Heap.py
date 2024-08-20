class Heap:
    def __init__(self):
        self.__arr = []
    
    def _heapify(self, idx):
        l = idx * 2 + 1
        r = idx * 2 + 2
        center_element = idx
        if l < self.__sizeof__() and self.__arr[l] < self.__arr[center_element]:
            center_element = l
        if r < self.__sizeof__() and self.__arr[r] < self.__arr[center_element]:
            center_element = r

        if center_element != idx:
            self.__arr[idx], self.__arr[center_element] = self.__arr[center_element], self.__arr[idx]
            self._heapify(center_element)

    def _parent(self, idx):
        return (idx - 1) // 2
    
    def pop(self):
        root = self.__arr[0]
        self.delete(0)

        return root 
    
    def insert(self, value):
        self.__arr.append(value)
        idx = self.__sizeof__() - 1

        while idx != 0 and self.__arr[self._parent(idx)] > self.__arr[idx]:
            self.__arr[idx], self.__arr[self._parent(idx)] = self.__arr[self._parent(idx)], self.__arr[idx]
            idx = self._parent(idx)

    def delete(self, idx):
        last_element = self.__sizeof__() - 1
        self.__arr[idx], self.__arr[last_element] = self.__arr[last_element], self.__arr[idx]
        self.__arr.pop()
        self._heapify(0)

    def is_empty(self):
        return self.__sizeof__() == 0
    
    def __sizeof__(self) -> int:
        return len(self.__arr)
    
if __name__ == "__main__":
    mean_heap = Heap()
    mean_heap.insert(3); 
    mean_heap.insert(2); 
    # mean_heap.delete(1); 
    mean_heap.insert(15); 
    mean_heap.insert(5); 
    mean_heap.insert(4); 
    mean_heap.insert(45); 
    print(f'[HEAP]: {mean_heap.pop()}')
    print(f'[HEAP]: {mean_heap.pop()}')
    print(f'[HEAP]: {mean_heap.pop()}')
    print(f'[HEAP]: {mean_heap.pop()}')
    print(f'[HEAP]: {mean_heap.pop()}')
    print(f'[HEAP]: {mean_heap.pop()}')

