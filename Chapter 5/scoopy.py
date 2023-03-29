from scoop import futures

def worker(value):
    print("I am the Worker %s" %value)

if __name__ == "__main__":
    list(futures.map(worker, range(4)))
    