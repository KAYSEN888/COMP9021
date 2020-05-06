# Randomly fills a grid with True and False, with width, height and density
# controlled by user input, and computes the number of all "good paths" that link
# a point of coordinates (x1, y1) to a point of coordinates (x2, y2)
# (x1 and x2 are horizontal coordinates, increasing from left to right,
# y1 and y2 are vertical coordinates, increasing from top to bottom,
# both starting from 0), that is:
# - paths that go through nothing but True values in the grid
# - paths that never go through a given point in the grid more than once;
# - paths that never keep the same direction (North, South, East, West) over
#   a distance greater than 2.
#
# Written by *** and Eric Martin for COMP9021


from collections import namedtuple
import numpy as np 
from random import seed, randrange
import sys
from collections import deque

Point = namedtuple('Point', 'x y')


def display_grid():
    for row in grid:
        print('   ', ' '.join(str(int(e)) for e in row))

def valid(pt):
    return 0 <= pt.x < width and 0 <= pt.y < height

new_path =deque()

def direc(up=0,down=0,left=0,right=0):#定义四个方向


    
    return direc

def direct(pt_1, pt_2, count_of_ways=0,up = 0, down = 0, left = 0, right = 0):#定义始末点，四个方向数目
    if grid[pt_1.y][pt_1.x]:#首先确定起始
        if grid[pt_2.y][pt_2.x]:
            if pt_1==pt_2:
                count_of_ways = count_of_ways+ 1

            elif pt_1!=pt_2:
                new_path.extend([pt_1])
                #向上走
                
                if pt_1.y!=0 and pt_1.y>0:#判断上层边界条件,注释以向上为例
                    if pt_1.y<height:#判断下层边界条件
                        new_one=Point(pt_1.x, pt_1.y - 1)#记录新的点
                        if new_one not in new_path :#如果不在路径内
                            if up < 2:#不能连续走三步在同一方向上(此时为up)
                                real_direct=direc(up+1,0,0,0)
                                new_path .extend([new_one])
                                count_of_ways = direct(new_one, pt_2, count_of_ways,up +1,  0,  0,  0)
                                new_path.pop()
                #向下走
                if pt_1.y==0 or pt_1.y>0:#判断上层边界条件
                    if pt_1.y<height-1:#判断下层边界条件
                        new_one=Point(pt_1.x, pt_1.y + 1)
                        if new_one not in new_path :
                            if down < 2:
                                real_direct=direc(0,down+1,0,0)
                                new_path .extend([new_one])
                                count_of_ways = direct(new_one, pt_2, count_of_ways, 0, down +1, 0,  0)
                                new_path.pop()
                #向左走
                if pt_1.x!=0 and pt_1.x>0:#判断左边界条件
                    if pt_1.x<width:#判断右边界条件
                        new_one=Point(pt_1.x-1, pt_1.y )
                        if new_one not in new_path :
                            if left < 2:
                                real_direct=direc(0,0,left+1,0)
                                new_path .extend([new_one])
                                count_of_ways = direct(new_one, pt_2, count_of_ways,0, 0, left+1,  0)
                                new_path.pop()

                #向右走
                if pt_1.y==0 or pt_1.y>0:#判断左边界条件
                    if pt_1.x<width-1:#判断右边界条件
                        new_one=Point(pt_1.x+1, pt_1.y)
                        if new_one not in new_path :
                            if right < 2:
                                real_direct=direc(0,0,0,right+1)
                                new_path .extend([new_one])
                                count_of_ways = direct(new_one, pt_2, count_of_ways,0, 0,  0, right+1)
                                new_path.pop()
                new_path.remove(pt_1)

    return count_of_ways
    return real_direct
    

def nb_of_good_paths(pt_1, pt_2):
    the_ways = direct(pt_1, pt_2)
    return the_ways
try:
    for_seed, density, height, width = (abs(int(i)) for i in
                                                  input('Enter four integers: ').split()
                                       )
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
if not density:
    density = 1
seed(for_seed)
grid = np.array([randrange(density) > 0
                              for _ in range(height * width)
                ]
               ).reshape((height, width))
print('Here is the grid that has been generated:')
display_grid()
try:
    i1, j1, i2, j2 = (int(i) for i in input('Enter four integers: ').split())
    pt_1 = Point(i1, j1)
    pt_2 = Point(i2, j2)
    if not valid(pt_1) or not valid(pt_2):
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
print('Will compute the number of good paths '
      f'from ({pt_1.x}, {pt_1.y}) to ({pt_2.x}, {pt_2.y})...'
     )
paths_nb = nb_of_good_paths(pt_1, pt_2)
if not paths_nb:
    print('There is no good path.')
elif paths_nb == 1:
    print('There is a unique good path.')
else:
    print('There are', paths_nb, 'good paths.')
