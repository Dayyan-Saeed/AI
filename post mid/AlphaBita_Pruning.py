def Alpha_Bita(depth, index, Terminal_values, Turn, A, B):

  if(depth == 3):
    return Terminal_values[index]
  
  if(Turn):
    best = beta
    for i in range(0,2):
      value = Alpha_Bita(depth+1,index*2+i, Terminal_values, False, A, B)
      best = max(best, value)
      A = max(A, best)
      if B<=A:
        break
    return best
  
  else:
    best = alpha
    for i in range(0,2):
      value = Alpha_Bita(depth+1,index*2+i, Terminal_values, True, A, B)
      best = min(best, value)
      A = min(A, best)
      if B<=A:
        break
    return best

alpha = 100
beta = -100
Terminal_Values =[4,5,2,7,9,2,6,4]
print("Answer: " ,Alpha_Bita(0,0,Terminal_Values,True,beta,alpha))