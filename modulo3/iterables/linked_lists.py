from collections import deque

"""
FIFO queue implementation
"""
llist = deque()
print(llist)
llist.append('Mary')
llist.append('Harry')
llist.append('Sally')
print(llist)
llist.popleft()
print(llist)


"""
LIFO queue implementation
"""

# TODO: Cómo sería
llist.pop()
print(llist)


global l
l = [1, 2]
print(l)


def delete(lista):
    print(l[1])
    del l[1]

delete(l)

print(l)