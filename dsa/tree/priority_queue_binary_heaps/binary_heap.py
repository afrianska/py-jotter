# Priority Queues with Binary Heaps
class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def percolate_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def percolate_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            # print(f"mc: {mc}, heap_list value: {self.heap_list[mc]} ----")
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        print("--current size: ", self.current_size)
        print("--before perlocate up: ", self.heap_list)
        self.percolate_up(self.current_size)
        print("after perlocate up: ", self.heap_list)

    def del_min(self):
        ret_val = self.heap_list[1]
        print(f" -- {self.heap_list[self.current_size]}")
        print("--before sweap: ", self.heap_list)
        self.heap_list[1] = self.heap_list[self.current_size]
        print("--after sweap: ", self.heap_list)
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        print("--after pop and before percolate down: ", self.heap_list)
        self.percolate_down(1)
        print("--after percolate down: ", self.heap_list)
        return ret_val

    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]
        while i > 0:
            self.percolate_down(i)
            i = i - 1


bh = BinaryHeap()
bh.insert(5)
bh.insert(7)
bh.insert(3)
bh.insert(11)

print(bh.heap_list)

print(bh.del_min())
print(bh.del_min())
print(bh.del_min())
print(bh.del_min())

a_list = [33, 17, 27, 14, 18, 9, 19, 11, 21]
print(f"a list : {a_list}")
bh.build_heap(a_list)
print(f"a list after heap-ing: {bh.heap_list}")
print(bh.del_min())
print(bh.del_min())
print(bh.del_min())
print(bh.del_min())
print(bh.del_min())
print(bh.del_min())
print(bh.del_min())
print(bh.del_min())
print(bh.del_min())


# STILL NEED EXPLORATION ABOUT THIS TOPIC
