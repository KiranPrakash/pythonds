class BinaryHeap:
    """Implements Binary Heap"""

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size +=1

        self.percolate_up(self.current_size)

    def percolate_up(self, i):
        while i//2 > 0:
            if self.heap_list[i] < self.heap_list[i//2]:
                self.heap_list[i], self.heap_list[i//2] = self.heap_list[i//2], self.heap_list[i]

            i = i//2

    def delete_min(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.percolate_down(1)

        return retval

    def percolate_down(self, i):
        while 2 * i <= self.current_size:
            mc = self.min_cild(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]

            i = mc

    def min_child(self,i):
        #to return the least amongst a given children for a particular i th parent
        #if we have reached end of the list then just return the last index
        if 2*i +1 > self.current_size:
            return 2*i
        else:
            if self.heap_list[2*i] < self.heap_list[2*i +1]:
                return 2*i
            else:
                return 2*i+1


    def buildHeap(self, alist):
        i = len(alist)//2
        self.current_size = len(alist)
        self.heap_list = [0]+alist[:]
        while (i>0):
            self.percolate_down(i)
            i -=1






