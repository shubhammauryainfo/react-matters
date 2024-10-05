import threading

def fibonacci(n):
   fib = [0, 1]
   for i in range(2, n):
       fib.append(fib[-1] + fib[-2])
   return fib

if __name__ == '__main__':
   n = int(input('Enter the number of Fibonacci numbers to generate: '))

   def generate_fibonacci():
       sequence = fibonacci(n)
       print(sequence)

   thread = threading.Thread(target=generate_fibonacci)
   thread.start()
   thread.join()
