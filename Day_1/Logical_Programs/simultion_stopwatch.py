import time

def stopwatch_simulation():
    input("Press enter to  start the stopwatch...")
    start_time = time.time()
    input("Press Enter to stop the stopwatch...")
    end_time = time.time()
    
    elapse_time = end_time - start_time
    
    print(f"Elapsed time : {elapse_time: .2f} seconds")
    
    return elapse_time

stopwatch_simulation()