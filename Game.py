import cv2  
import numpy as np  
from random import randint
import time

class Block() :
	def __init__(self,i,j) :
		self.value	= None
		self.pos	= (i,j)
	def setValue(self,value) :
		self.value	= value


class GUI() :
	def __init__(self,windowName) :
		self.windowName	= windowName
		self.width,self.height = 400,400
		
		self.menuHeight = 100
		self.image	= np.zeros((self.height+self.menuHeight,self.width,3),np.uint8)
		self.turn	= 1
		self.vsCom	= 0
		self.reset()
		
    #Reset Game
	def reset(self) :
		self.blocks	= []
		for i in range(3) :
			row  = []
			for j in range(3) :
				row.append([Block(i,j),(j*(self.width//3)+3,i*(self.height//3)+3),((j+1)*(self.width//3)-3,(i+1)*(self.height//3)-3)])
			self.blocks.append(row)

    #Drawing GUI and Game Screen
	def draw(self) :
		self.image = np.zeros((self.height+self.menuHeight,self.width,3),np.uint8)
		for i in range(3) :
			for j in range(3) :
				start_point = self.blocks[i][j][1]
				end_point = self.blocks[i][j][2]
				cv2.rectangle(self.image,start_point,end_point,(255,255,255),-1)
				value = " " if self.blocks[i][j][0].value is None else self.blocks[i][j][0].value
				cv2.putText(self.image,value,(j*(self.width//3)+25,(i*self.height//3)+100),cv2.FONT_HERSHEY_SIMPLEX,5,(0,0,0),5)
		# if self.checkWin() :
		# 	string = ("Player "+str(self.turn)+" Wins" if self.turn!=self.vsCom else "Computer Wins") if self.turn==1 else ("Player "+str(2)+" Win" if self.turn!=self.vsCom else "Computer Win")
		# else :
		# 	if not self.checkDraw() :
		# 		string = ("Player "+str(self.turn)+"'s Turn" if self.turn!=self.vsCom else "Computer's Turn") if self.turn==1 else ("Player "+str(2)+"'s Turn" if self.turn!=self.vsCom else "Computer's Turn")
		# 	else :
		# 		string = "Match Draw!!"
		cv2.putText(self.image,"hii",(self.width//2-70,self.height+30),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)
		cv2.putText(self.image,"R - Reset",(10,self.height+60),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)
		cv2.putText(self.image,"Esc - Exit",(10,self.height+80),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)
		string = "vs Computer" if self.vsCom==0 else "vs Human"
		cv2.putText(self.image,"Space - "+string,(self.width//2+10,self.height+80),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)

		# if self.selected and not(self.checkWin() or self.checkDraw()):
		# 	self.change   = True
		# 	self.selected = False
		# 	self.turn *= -1
			
    
# def checkWin(self) :
# 		self.win = False
# 		if (self.blocks[0][0][0].value is not None and self.blocks[0][0][0].value==self.blocks[0][1][0].value==self.blocks[0][2][0].value)or(self.blocks[1][0][0].value is not None and self.blocks[1][0][0].value==self.blocks[1][1][0].value==self.blocks[1][2][0].value)or(self.blocks[2][0][0].value is not None and self.blocks[2][0][0].value==self.blocks[2][1][0].value==self.blocks[2][2][0].value)or(self.blocks[0][0][0].value is not None and self.blocks[0][0][0].value==self.blocks[1][0][0].value==self.blocks[2][0][0].value)or(self.blocks[0][1][0].value is not None and self.blocks[0][1][0].value==self.blocks[1][1][0].value==self.blocks[2][1][0].value)or(self.blocks[0][2][0].value is not None and self.blocks[0][2][0].value==self.blocks[1][2][0].value==self.blocks[2][2][0].value)or(self.blocks[0][0][0].value is not None and self.blocks[0][0][0].value==self.blocks[1][1][0].value==self.blocks[2][2][0].value)or(self.blocks[2][0][0].value is not None and self.blocks[2][0][0].value==self.blocks[0][2][0].value==self.blocks[1][1][0].value) :
# 			self.win = True
# 		return self.win    

# def checkDraw(self) :
# 		flag = True
# 		for i in range(3) :
# 			for j in range(3) :
# 				if self.blocks[i][j][0].value == None :
# 					flag=False
# 		return flag   




g=GUI("game")
g.draw()

cv2.imshow(g.windowName, g.image)
cv2.waitKey(0)
cv2.destroyAllWindows()