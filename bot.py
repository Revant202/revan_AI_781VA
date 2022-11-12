import random


EMPTY = 0

class player:
    l_move = []
    ex_box = []
    inv = {(1, 0): (-1, 0), (0, 1): (0, -1), (-1, 0): (1, 0), (0, -1): (0, 1), 2: 1, 1: 2}
    def _init_(self):
        pass

    def move(self, B, N, c_x, c_y):

        if len(self.l_move) == 0:
            return self.findmove(B, N, c_x, c_y)
        else:
            move = self.l_move.pop(0)
            if (self.completed(B, N, c_x, c_y)):
                self.l_move.clear()

            elif (self.blockage(B, N, c_x, c_y)):
                self.l_move.clear()
                return self.findmove(B, N, c_x, c_y)
            return move
    def completed(self, B, N, c_x, c_y):
        done=True
        myVal=B[self.ex_box[0][0]][self.ex_box[0][1]]
        for i in self.ex_box:
            if B[i[0]][i[1]] != myVal:
                done=False
        return done

    def blockage(self, B, N, c_x, c_y):
        interrupt=False
        myVal=B[self.ex_box[0][0]][self.ex_box[0][1]]
        opVal=self.inv[myVal]
        for i in self.ex_box:
            if B[i[0]][i[1]] == opVal:
                interrupt=True
        return interrupt



    def chk_corner(self, B, N, c_x, c_y):
            if c_x + 5 < N and c_y + 5 < N:
                available = True
                for i in range(5):
                    for j in range(5):
                        if B[c_x + i][c_y + j] !=0 and i!=0 and j!=0:
                            available = False

                if available :
                    self.ex_box=[(c_x + i, c_y + j) for i in range(5) for j in range(5)]
                    self.l_move.extend([(1,0),(1,0),(1,0),(1,0),(0,1),(0,1),(0,1),(0,1),(-1,0),(-1,0),(-1,0),(-1,0),(0,-1),(0,-1),(0,-1),(0,-1)])
                    return [True,self.l_move.pop(0)]
                else:
                    return [False, (0,0)]
            else:
                    return [False, (0,0)]


    def chk_corner_again(self, B, N, c_x, c_y):
        if c_x - 5 >= 0 and c_y + 5 < N:
            available = True
            for i in range(5):
                for j in range(5):
                    if B[c_x - i][c_y + j] !=0 and i!=0 and j!=0:
                        available = False

            if available :
                self.ex_box=[(c_x - i, c_y + j) for i in range(5) for j in range(5)]
                self.l_move.extend([(-1,0),(-1,0),(-1,0),(-1,0),(0,1),(0,1),(0,1),(0,1),(1,0),(1,0),(1,0),(1,0),(0,-1),(0,-1),(0,-1),(0,-1)])
                return [True,self.l_move.pop(0)]
            else:
                return [False, (0,0)]
        else:
                return [False, (0,0)]

    def chk_corner_thrice(self, B, N, c_x, c_y):
        if c_x + 5 < N and c_y - 5 >= 0:
            available = True
            for i in range(5):
                for j in range(5):
                    if B[c_x + i][c_y - j] !=0 and i!=0 and j!=0:
                        available = False

            if available :
                self.ex_box=[(c_x + i, c_y - j) for i in range(5) for j in range(5)]
                self.l_move.extend([(1,0),(1,0),(1,0),(1,0),(0,-1),(0,-1),(0,-1),(0,-1),(-1,0),(-1,0),(-1,0),(-1,0),(0,1),(0,1),(0,1),(0,1)])
                return [True,self.l_move.pop(0)]
            else:
                return [False, (0,0)]
        else:
                return [False, (0,0)]

    def chk_corner_lasttime(self, B, N, c_x, c_y):
        if c_x - 5>= 0 and c_y - 5 >= 0:
            available = True
            for i in range(5):
                for j in range(5):
                    if B[c_x - i][c_y - j] !=0 and i!=0 and j!=0:
                        available = False

            if available :
                self.ex_box=[(c_x - i, c_y - j) for i in range(5) for j in range(5)]
                self.l_move.extend([(-1,0),(-1,0),(-1,0),(-1,0),(0,-1),(0,-1),(0,-1),(0,-1),(1,0),(1,0),(1,0),(1,0),(0,1),(0,1),(0,1),(0,1)])
                return [True,self.l_move.pop(0)]
            else:
                return [False, (0,0)]
        else:
                return [False, (0,0)]
            


    def empty_close(self,B,N,c_x,c_y):
        dis=2*N+1
        final = {"x":c_x,"y":c_y}
        for i in range(N):
            for j in range(N):
                if B[i][j] == EMPTY:
                    dx = min ( abs(c_x - i) , N - abs(c_x - i) )
                    dy = min ( abs(c_y - j) , N - abs(c_y - j) )
                    c_dis = dx+dy
                    if c_dis < dis:
                        dis = c_dis
                        final["x"] = i 
                        final["y"] = j 

       

        if final["y"] > c_y:
            if final["y"]-c_y < N/2:
                return (0,1)
            else:
                return (0,-1)


        if final["y"] < c_y:
            if c_y-final["y"] < N/2:
                return (0,-1)
            else:
                return (0,1)


        if final["x"] > c_x:
            if final["x"]-c_x < N/2:
                return (1,0)
            else:
                return (-1,0)

        if final["x"] < c_x:
            if c_x-final["x"] < N/2:
                return (-1,0)
            else:
                return (1,0)
        

        return (0,0)

    check_box=[chk_corner,chk_corner_again,chk_corner_thrice,chk_corner_lasttime]
    
   
   
    def findmove(self,B,N,c_x,c_y):
        
        for box in self.check_box:
            result = box(self,B,N,c_x,c_y)
            if result[0]:
                return result[1]
        
        
        return self.empty_close(B,N,c_x,c_y)