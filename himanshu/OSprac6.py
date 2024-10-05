from collections import deque
time_quantum = 2

class Process:
  def __init__(self, name, arrival_time, required_time):
    self.name = name
    self.arrival_time = arrival_time
    self.required_time = required_time
    self.time_processed = 0
  def __repr__(self):
    return self.name

p0 = Process('P1', 0, 4)
p1 = Process('P2', 1, 3)
p2 = Process('P3', 2, 2)
p3 = Process('P4', 3, 1)
processes = [p0, p1, p2, p3]

end_times = {process.name:0 for process in processes}
wait_times = {process.name:0 for process in processes}

queue = deque()
running_proc = None # Tracks running process in the CPU
running_proc_time = 0 # Tracks the time running process spent in the CPU
for t in range(11):

 print(end_times) # End times for each process
 print(wait_times) # Wait times for each process in the queue
