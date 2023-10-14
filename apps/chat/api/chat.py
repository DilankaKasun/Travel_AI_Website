
from apps.chat.api.openAI import * 
import time

def run(data):
    start_time = time.time()
    api_con = AI_main()
    APIData=api_con.run(data=data)
    print(APIData)
    elapsed_time = time.time() - start_time
    print(f"Class1, method1 execution time: {elapsed_time} seconds")

