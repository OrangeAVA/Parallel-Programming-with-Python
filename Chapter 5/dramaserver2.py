import dramatiq
import time

from dramatiq.brokers.redis import RedisBroker
#from dramatiq.brokers.rabbitmq import RabbitmqBroker
from dramatiq.results import Results
from dramatiq.results.backends import RedisBackend

broker = RedisBroker(host="localhost")
#broker = RabbitmqBroker(host="localhost")
dramatiq.set_broker(broker)
result_backend = RedisBackend(host="localhost")
broker.add_middleware(Results(backend=result_backend))

@dramatiq.actor(store_results=True)
def wait(t,n):
   time.sleep(t)
   print("I am the actor %s and I will wait for %s secs" %(n,t))
   return "I waited for {0} secs".format(t)


