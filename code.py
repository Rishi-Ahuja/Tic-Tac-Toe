global grid
global win
global win1
global win2
grid = ['1','2','3','4','5','6','7','8','9']
win=[[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
win1=[]
win2=[]
def grid_making():
    print(grid[0],':',grid[1],':',grid[2])
    print(grid[3],':',grid[4],':',grid[5])
    print(grid[6],':',grid[7],':',grid[8])

grid_making()

user1=input('enter your name player 1')
user2=input('enter your name player 2')
no_win=True
turn=1

while no_win:
    while no_win and turn==1:
        choice=int(input('enter your choice %s'%user1))
        if grid[choice-1]=='0':
            print('%s already has choosen that, you loose your turn'%user2)
            turn=2
        else:
            grid[choice-1]='X'
            grid_making()
            turn=2
            win1.append(choice-1)
            win1.sort()
            for w in range(0,len(win)):
                if win1==win[w]:
                    no_win=False
                    print('%s wins'%user1)
    while no_win and turn==2:
        choice=int(input('enter your choice %s'%user2))
        if grid[choice-1]=='X':
            print('%s has already choose that, you loose your turn'%user1)
            turn=1
        else:
            grid[choice-1]='0'
            grid_making()
            turn=1
            win2.append(choice-1)
            win2.sort()
            for w in range(0,len(win)):
                if win2==win[w]:
                    no_win=False
                    print('%s wins'%user2)
