#!/usr/bin/python
import sys
import threading

## Account for Python environment
try:
    from queue import Queue
except:
    from Queue import Queue

class Backgrounder(object):
    """Setup and hold the backgrounded thread"""
    def __init__(self, theThread = None):
        if theThread is not None:
            self.theThread = theThread


    def easyLaunch(self, args = None):
        """Kick off the thread"""
        if self.theThread is None:
            print('You need to create theThread() prior to launch')
            sys.exit(1)
        if args is not None:
            thread = threading.Thread(target = self.theThread, args = args)
        else:
            thread = threading.Thread(target = self.theThread)
        thread.daemon = True
        thread.start()


class EasyThread(object):
    """Setup and hold the threaded queue"""
    def __init__(self, theThread = None, jobList = range(10), nThread = 10):
        if type(jobList) is Queue:
            self.q = jobList
        else:
            self.q = Queue(maxsize = 0)
        if theThread is not None:
            self.theThread = theThread
        self.jobList = jobList
        self.nThread = nThread
        self.lock = threading.Lock()


    def workerAdd(self, q):
        """Add your workers to the Queue"""
        while True:
            worker = q.get()
            self.theThread(worker)
            q.task_done()


    def easyLaunch(self):
        """Kick off the threads with a pool"""
        if self.theThread is None:
            print('You need to create theThread() prior to launch')
            sys.exit(1)
        for i in range(self.nThread):
            worker = threading.Thread(target = self.workerAdd, args = (self.q,))
            worker.setDaemon(True)
            worker.start()
        if type(self.jobList) is not Queue:
            for job in self.jobList:
                self.q.put(job)
        self.q.join()


## Give a quick reminder of how to run
if __name__ == '__main__':

    """
    Example 1 -- Add our function as a method to EasyThread
    This has the benefit of allowing our function access to the Class via
    the function becoming a Method of the Class
    """

    ## Create a function defining what you want your jobs to do
    ## Use of the work object is not required, but is provided if wanted
    def exampleThread1(self, work):
        print (work)
        print (self.nThread)

    ## Add our function to EasyThread
    EasyThread.theThread = exampleThread1

    ## Instantiate using #s other than defaults
    et = EasyThread(jobList = [1,2,3,4,5], nThread = 5)

    ## Start the work
    et.easyLaunch()


    """
    Example 2 -- Pass our function as a parameter to EasyThread
    Does not allow our function access to the Class
    """

    ## Create a function defining what you want your jobs to do
    ## Use of the work object is not required, but is provided if wanted
    def exampleThread2(work):
        print (work)

    ## Instantiate with our function using the default parameters
    et = EasyThread(exampleThread2)

    ## Start the work
    et.easyLaunch()


    """
    Example 3 -- Add our function as a method to Backgrounder
    This has the benefit of allowing our function access to the Class via
    the function becoming a Method of the Class
    """

    ## Create a function defining what you want your jobs to do
    ## Use of the work object is not required, but is provided if wanted
    def exampleThread3(self):
        print ('hello world')

    ## Add our function to Backgrounder
    Backgrounder.theThread = exampleThread3

    ## Instantiate using #s other than defaults
    bg = Backgrounder()

    ## Start the work
    bg.easyLaunch()


    """
    Example 4 -- Combine Backgrounder and EasyThread with a Class and using a
    queue as the input to jobList
    """
    import time
    from easyThread import Backgrounder
    from easyThread import EasyThread
    from queue import Queue

    class OurClass(object):
        def foo(self, work):
            while True:
                print(self.q.get())
                self.q.task_done()

    ## Instantiate and create a FIFO queue
    oc = OurClass()
    oc.q = Queue()

    ## Add our function to EasyThread
    EasyThread.theThread = oc.foo
    et = EasyThread(jobList = oc.q, nThread = 5)

    ## Start the work
    def foo(self):
        et.easyLaunch()
    Backgrounder.theThread = foo
    bg = Backgrounder()
    bg.easyLaunch()

    ## Sleep so it has time to run, or do something else, maybe fill the queue, etc.
    while True:
        for i in range(20):
            oc.q.put(i)
        time.sleep(1)
