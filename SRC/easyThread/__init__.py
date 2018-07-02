#!/usr/bin/python

import threading
from queue import Queue

class EasyThread(object):
    """Setup and hold the threaded environment"""
    def __init__(self, jobList = list(range(10)), nThread = 10):
        self.q = Queue(maxsize = 0)
        self.jobList = jobList
        self.nThread = nThread


    def workerAdd(self, q):
        """Add your workers to the Queue"""
        while True:
            worker = q.get()
            self.theThread(worker)
            q.task_done()


    def easyLaunch(self):
        """Kick off the threads with a pool"""
        for i in range(self.nThread):
            worker = threading.Thread(target = self.workerAdd,
                                      args = (self.q,))
            worker.setDaemon(True)
            worker.start()
        for job in self.jobList:
            self.q.put(job)
        self.q.join()


## Give a quick reminder of how to run
if __name__ == '__main__':

    ## Create a function defining what you want your jobs to do
    def exampleThread(self, work):
        print(work)

    ## Add our function to EasyThread
    EasyThread.theThread = exampleThread
  
    ## Instantiate using #s other than defaults
    et = EasyThread([1,2,3,4,5], 5)
    
    ## Start the work
    et.easyLaunch()
