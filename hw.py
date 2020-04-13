import numpy as np

def matrixPrint(Maze):  #建立二維矩陣
    for row in range(10):
        for column in range(12):
            if column == 11:
                print(Maze[row][column])
            else:
                print(Maze[row][column], end=' ')
                
def findPath(Maze, row, column): #矩陣顯示方式
  print ("=========================")
  print ("row=",row,"column=",column,) 
  matrixPrint(Maze)
  
  if row>=10 and column>=12: #當row大於等於10, column小於等於10，回傳失敗
       return False
  if Maze[row][column] == '1':  #碰到牆壁，回傳失敗
       return False
  if Maze[row][column] == '0':  #已走過
       return False
  if Maze[row][column] == ' ':  
      Maze[row][column]= '.'
  if Maze[row][column] == '.' and (row == 9 and column == 8): #終點
    print('已到終點!')
    return True
  if column<11 and Maze[row][column+1]==' ': #往右搜尋
    if findPath(Maze, row,column+1):
         return True
  if row<9 and Maze[row+1][column]==' ':  #往下搜尋
        if findPath(Maze, row+1,column):
            return True
  if column>0 and Maze[row][column-1]==' ': #往左搜尋
    if findPath(Maze, row,column-1):
         return True
  if row>0 or Maze[row-1][column]==' ': #網上搜尋
    if findPath(Maze, row-1,column):
         return True
  Maze[row][column]='0'
  return False

Maze =(['1','1','1','1','1','1','1','1','1','1','1','1']   #地圖
      ,[' ',' ',' ',' ','1','1','1','1','1','1','1','1']
      ,['1','1','1',' ','1',' ',' ',' ',' ','1','1','1']
      ,['1','1','1',' ','1',' ','1','1',' ','1','1','1']
      ,['1','1','1',' ',' ',' ','1','1',' ','1','1','1']
      ,['1','1','1',' ','1',' ','1','1',' ','1','1','1']
      ,['1','1','1',' ','1',' ','1','1',' ','1','1','1']
      ,['1','1','1','1','1',' ','1','1',' ','1','1','1']
      ,['1','1',' ',' ',' ',' ',' ','1',' ','1','1','1']
      ,['1','1','1','1','1','1','1','1',' ','1','1','1'])
      
findPath(Maze, 1, 0)   #設定起點
print ("=========================")
matrixPrint(Maze)