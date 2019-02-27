# mpbatch
Mpbatch is a python library intends to make the multi-core processing of items which require repeated function evaluations more simple.

## Installation
Clone the repo. and run:

```bash
python setup.py
```

## Example Usage
```python
from mpbatch import batch_process

def test_func(L):
  return [el**2 for el in L]
  
test_list = [i+1 for i in range(10000)]  

num_cores = 4

output = batch_process(test_func,test_list,num_cores)
print(output)
```
