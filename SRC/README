# easy-thread
An easy way to create a threaded queue for Python 2 or 3

By default easyThread will create 10 threads and 10 jobs to perform.  The default parameters easyThread will use are:
* jobList = range(10)
* nThread = 10

jobList - A list of things you want to pass the function which is threaded.  It could be anything.  As a silly example below, we use the jobList to print values in the range 0-9.  If you choose not to use the elements within jobList for use directly in EasyThread.theThread() that is okay as well.  The main thing to keep in mind is that jobList is the maxmimum amount of times your function is repeated.

nThread - This is an integer representing the threads available for your use.

#### EasyThread.theThread()
This is the function which you will create.  As there was no purpose to create this object in the file, the code itself does not contain it.  You the user must define what theThread() does.  An example of how to do so is below.

### Example Usage #1 -- Method moficiation
Add our function as a method to EasyThread.  This has the benefit of allowing our function access to the Class via the function becoming a Method of the Class.
~~~~
	from easyThread import EasyThread

    ## Create a function defining what you want your jobs to do
    ## Use of the work object is not required, but is provided if wanted
    def exampleThread1(self, work):
        print (work)
		print (self.nThread)

    ## Add our function to EasyThread
    EasyThread.theThread = exampleThread1
       
    ## Instantiate using #s other than defaults
    et = EasyThread([1,2,3,4,5], 5)
    
    ## Start the work
    et.easyLaunch()
~~~~

### Example Usage #2 -- Parameterization
Pass our function as a parameter to EasyThread.  Does not allow our function access to the Class:
~~~~
	from easyThread import EasyThread

    ## Create a function defining what you want your jobs to do
    ## Use of the work object is not required, but is provided if wanted
    def exampleThread2(work):
        print(work)    
    
    ## Instantiate with our function using the default parameters
    et = EasyThread(exampleThread2)
    
    ## Start the work
    et.easyLaunch()
~~~~

### Feedback
I would love any feedback from the community on this repo.  Threading has always been one of my slowpoints in Python, and I hope that by sharing this, others might find it useful.
