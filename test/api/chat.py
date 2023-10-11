import openAI 
import time

while (True):
  data = input("Enter Input :")
  start_time = time.time()
  x =openAI.AI_main()
  y,z=x.run(data=data)
  
  print(z)
  print(y)
  elapsed_time = time.time() - start_time
  print(f"Class1, method1 execution time: {elapsed_time} seconds")