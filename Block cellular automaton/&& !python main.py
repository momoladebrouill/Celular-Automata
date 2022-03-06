from pprint import pprint
import random
size=16,16
grid=[[0 for i in range(size[0])] for i in range(size[1])]
def rotate(gen):
    new=[[0 for i in range(size[0]+gen%2)] for i in range(size[1]+gen%2)]
    for y in range(gen%2,size[1],2):
        for x in range(gen%2,size[0],2):
            for miny in range(2):
                for minx in range(2):
                    if y+minx<size[0] and x+miny<size[1]:
                        new[y+miny][x+minx]=/
                        grid[y+1-minx][x+miny]
    return new
grid[0][0]="a"
grid[0][1]="b"
grid[1][0]="c"
grid[1][1]="d"

for y in range(size[1]):
    for x in range(size[0]):
        grid[y][x]=chr(65+x+y)#"*" if random.random()>.5 else " "
        print(grid[y][x],end=" ")
    print()

print("---")



a=rotate(1)
for x in a:
    for b in x:
        print(b,end=" ")
    print()





