class sparseArray:
    def __init__(self, arr, n):
        self.n = n
        self._dict = {}
        for i, e in enumerate(arr):
            if e != 0:
                self._dict[i] = e
    
    def _checkBound(self, i):
        if i < 0 or i >= self.n:
            raise IndexError('Out of bounds')
    
    def set(self, i, val):
        self._checkBound(i)
        if val != 0:
            self._dict[i] = val
            return
        elif i in self._dict:
            del self._dict[i]
    
    def get(self, i):
        self._checkBound(i)
        return self._dict.get(i, 0)

obj = sparseArray([1, 0, 0, 0, 0, 55, 0, 0, 0, 111], 10)
print (obj.get(5))