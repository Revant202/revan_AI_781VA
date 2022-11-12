import random


EMPTY = 0

class player:
    l_move = []
    ex_box = []
    inv={}
    def _init_(self):
        self.step=0
        self.l_move = []
        self.ex_box = []
        self.inv={(1,0):(-1,0),(0,1):(0,-1),(-1,0):(1,0),(0,-1):(0,1),2:1,1:2}
    def completed(self, B, N, cur_x, cur_y):
        done=True
        myVal=B[self.ex_box[0][0]][self.ex_box[0][1]]
        opVal=self.inv[myVal]
        for i in self.ex_box:
            if B[i[0]][i[1]] != myVal:
                done=False
        return done

    def blockage(self, B, N, cur_x, cur_y):
        interrupt=False
        myVal=B[self.ex_box[0][0]][self.ex_box[0][1]]
        opVal=self.inv[myVal]
        for i in self.ex_box:
            if B[i[0]][i[1]] == opVal:
                interrupt=True
        return interrupt

    def move(self,B,N,cur_x,cur_y):
        self.step+=1
        if len(self.l_move)==0:
            return self.findmove(B,N,cur_x,cur_y)
        else:
            move=self.l_move.pop(0)
            if(self.completed(B,N,cur_x,cur_y)):
                self.l_move.clear()
           
            elif(self.blockage(B,N,cur_x,cur_y)):
                self.l_move.clear()
                return self.findmove(B,N,cur_x,cur_y)
            return move


    def chk_corner(self, B, N, cur_x, cur_y):
            if cur_x + 7 < N and cur_y + 7 < N:
                available = True
                for i in range(random.randint(0, 10)):
                    for j in range(random.randint(0, 10)):
                        if B[cur_x + i][cur_y + j] !=0 and i!=0 and j!=0:
                            available = False

                if available :
                    self.ex_box=[(cur_x + i, cur_y + j) for i in range(random.randint(0, 10)) for j in range(random.randint(0, 10))]
                    self.l_move.extend([(1,0),(1,0),(1,0),(1,0),(0,1),(0,1),(0,1),(0,1),(-1,0),(-1,0),(-1,0),(-1,0),(0,-1),(0,-1),(0,-1),(0,-1)])
                    return [True,self.l_move.pop(0)]
                else:
                    return [False, (0,0)]
            else:
                    return [False, (0,0)]


    def chk_corner_again(self, B, N, cur_x, cur_y):
        if cur_x - 7 >= 0 and cur_y + 7 < N:
            available = True
            for i in range(random.randint(0, 10)):
                for j in range(random.randint(0, 10)):
                    if B[cur_x - i][cur_y + j] !=0 and i!=0 and j!=0:
                        available = False

            if available :
                self.ex_box=[(cur_x - i, cur_y + j) for i in range(random.randint(0, 10)) for j in range(random.randint(0, 10))]
                self.l_move.extend([(-1,0),(-1,0),(-1,0),(-1,0),(0,1),(0,1),(0,1),(0,1),(1,0),(1,0),(1,0),(1,0),(0,-1),(0,-1),(0,-1),(0,-1)])
                return [True,self.l_move.pop(0)]
            else:
                return [False, (0,0)]
        else:
                return [False, (0,0)]

    def chk_corner_thrice(self, B, N, cur_x, cur_y):
        if cur_x + 7 < N and cur_y - 7 >= 0:
            available = True
            for i in range(random.randint(0, 10)):
                for j in range(random.randint(0, 10)):
                    if B[cur_x + i][cur_y - j] !=0 and i!=0 and j!=0:
                        available = False

            if available :
                self.ex_box=[(cur_x + i, cur_y - j) for i in range(random.randint(0, 10)) for j in range(random.randint(0, 10))]
                self.l_move.extend([(1,0),(1,0),(1,0),(1,0),(0,-1),(0,-1),(0,-1),(0,-1),(-1,0),(-1,0),(-1,0),(-1,0),(0,1),(0,1),(0,1),(0,1)])
                return [True,self.l_move.pop(0)]
            else:
                return [False, (0,0)]
        else:
                return [False, (0,0)]

    def chk_corner_lasttime(self, B, N, cur_x, cur_y):
        if cur_x - 7>= 0 and cur_y - 7 >= 0:
            available = True
            for i in range(random.randint(0, 10)):
                for j in range(random.randint(0, 10)):
                    if B[cur_x - i][cur_y - j] !=0 and i!=0 and j!=0:
                        available = False

            if available :
                self.ex_box=[(cur_x - i, cur_y - j) for i in range(random.randint(0, 10)) for j in range(random.randint(0, 10))]
                self.l_move.extend([(-1,0),(-1,0),(-1,0),(-1,0),(0,-1),(0,-1),(0,-1),(0,-1),(1,0),(1,0),(1,0),(1,0),(0,1),(0,1),(0,1),(0,1)])
                return [True,self.l_move.pop(0)]
            else:
                return [False, (0,0)]
        else:
                return [False, (0,0)]
            


    def empty_close(self,B,N,cur_x,cur_y):
        dis=2*N+1
        best = {"x":cur_x,"y":cur_y}
        for i in range(N):
            for j in range(N):
                if B[i][j] == EMPTY:
                    dx = min ( abs(cur_x - i) , N - abs(cur_x - i) )
                    dy = min ( abs(cur_y - j) , N - abs(cur_y - j) )
                    cur_dis = dx+dy
                    if cur_dis < dis:
                        dis = cur_dis
                        best["x"] = i 
                        best["y"] = j 

       

        if best["y"] > cur_y:
            if best["y"]-cur_y < N/2:
                return (0,1)
            else:
                return (0,-1)


        if best["y"] < cur_y:
            if cur_y-best["y"] < N/2:
                return (0,-1)
            else:
                return (0,1)


        if best["x"] > cur_x:
            if best["x"]-cur_x < N/2:
                return (1,0)
            else:
                return (-1,0)

        if best["x"] < cur_x:
            if cur_x-best["x"] < N/2:
                return (-1,0)
            else:
                return (1,0)
        

        return (0,0)

    check_box=[chk_corner,chk_corner_again,chk_corner_thrice,chk_corner_lasttime]
    
   
   
    def findmove(self,B,N,cur_x,cur_y):
        
        for box in self.check_box:
            result = box(self,B,N,cur_x,cur_y)
            if result[0]:
                return result[1]
        
        
        return self.empty_close(B,N,cur_x,cur_y)