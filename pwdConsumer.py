import threading
import queue
import string
import random
from password import Password
class PWDConsumer(threading.Thread):

    def __init__(self,queue,condition):
        threading.Thread.__init__(self)
        self.queue=queue
        self.condition=condition

    def run(self):
        password = None
        while(True):
            self.condition.acquire()
            try:
                password=self.queue.get(block=False)
                self.condition.notify()
            except queue.Empty:
                self.condition.wait()
            self.condition.release()

            if not password is None:
                #print('Testing with 123: '+str(password.check('123'))
                testLen = 3
                tries = 0
                while(True):
                    randPwd = ''.join(random.choices(string.digits+string.ascii_lowercase+string.ascii_uppercase, k=testLen))
                    print('Checking pw: '+randPwd)
                    tries = tries+1

                    if password.check(randPwd):
                        print('Password found: '+randPwd+' by '+str(threading.get_ident())+'\n')
                        print('Tries: '+str(tries))
                        break




