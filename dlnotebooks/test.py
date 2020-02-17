from fastai2.text.all import *
from pathos.multiprocessing import ProcessingPool

class SleepyBatchFunc:
    def __init__(self): self.a=1
    def __call__(self, batch):
        for k in batch:
            time.sleep(random.random()/4)
            yield k+self.a

if __name__ == '__main__':
    x = np.linspace(0,0.99,20)
    
    results = ProcessingPool().map(SleepyBatchFunc, x)
