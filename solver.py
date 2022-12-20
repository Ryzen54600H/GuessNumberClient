import numpy as np

class Location:
      def __init__(self, row, col):
            self.row = row
            self.col = col

class Solver():
	def __init__(self):
		self.VisitedLocation = None
		self.curGuessingMap = None
		self.curArraySize = None
		self.dx = [0, 1, -1, 0]
		self.dy = [1, 0, 0, -1]


	def SolveSuggestQuestion(self, curListLocation, ArraySize):
		ans = 0
		self.curArraySize = ArraySize
		self.VisitedLocation = np.zeros((self.curArraySize, self.curArraySize),dtype = np.int32)
		self.curGuessingMap = np.zeros((self.curArraySize, self.curArraySize),dtype = np.int32)
		for item in curListLocation:
				self.curGuessingMap[item.row][item.col] = 1
		for i in range(self.curArraySize):
				for j in range(self.curArraySize):
					print(self.curGuessingMap[i][j], end = "")
				print("")
		for i in range(self.curArraySize):
				for j in range(self.curArraySize):
					self.curLocation = Location(i, j)
					if(self.curGuessingMap[i][j] == 0 and self.VisitedLocation[i][j] == 0):
							ans = ans + 1
							print("i j:", i, j)
							self.DFS(i, j)
		return ans

	def DFS(self, i, j):
		self.VisitedLocation[i][j] = 1
		for t in range(4):
				x = i + self.dx[t]
				y = j + self.dy[t]
				if(x < 0 or x >= self.curArraySize):
					continue
				if(y < 0 or y >= self.curArraySize):
					continue
				self.curLocation = Location(x, y)
				if(self.curGuessingMap[x][y] == 0 and  self.VisitedLocation[x][y] == 0):
					print("x y:",x,y)
					self.DFS(x, y)