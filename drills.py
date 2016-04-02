if __name__ == '__main__':
	import os
	import sys

	def pause():
		programPause = raw_input("Press the <ENTER> key to continue...")
	
	def drill():
		import random
		import time
		global score
		score=0
		correct=0
		global table 
		table=[]
		global input_time
		input_time=[]
		numbers=range(2,12)
		pause()
		for i in numbers:
			for j in numbers:
				if j > i:
					table.append((i,j))
		random.shuffle(table)
		size_of_table=len(table)
		for i in range(size_of_table-1):
			num1=table[i][0]
			num2=table[i][1]
			start = time.time()
			answer=input("%d * %d = " %(num1,num2))
			if answer == num1*num2:
				score+=1
				print("correct")
				correct=1
			end = time.time()	
			input_time.append((end - start,num1,num2,correct) )
			correct=0			
		print(score)
		print(input_time)
		f = open( 'drill.log', 'w' )
		f.write( repr(input_time) + '\n' )
		f.close()
	drill()
	
		

