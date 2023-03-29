import dramatiq
import time

@dramatiq.actor
def wait(t,n):
   time.sleep(t)
   print("I am the actor %s and I will wait for %s secs" %(n,t))
   #return "I waited for {0} secs".format(t)


