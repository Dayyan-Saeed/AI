# Min Max Algoritm
import math
def minMax(depth,Terminal_Values, Index, Turn, Max_depth):

  if(depth == Max_depth):
    return Terminal_Values[Index]
  
  if(Turn):
    return max(minMax(depth+1, Terminal_Values,Index*2, False,Max_depth),
               minMax(depth+1, Terminal_Values,Index*2+1, False,Max_depth))
  
  else:
    return min(minMax(depth+1, Terminal_Values,Index*2, True,Max_depth),
               minMax(depth+1, Terminal_Values,Index*2+1, True,Max_depth))

Terminal_Values =[4,6,2,8,-3,-1,2,4]

max_depth = int(math.log(len(Terminal_Values),2))

print("Answer: " ,minMax(0,Terminal_Values,0,True,max_depth))