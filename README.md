# mpbatch
Mpbatch is a python library intends to make the multi-core processing of items which require repeated function evaluations more simple.

## Installation
Install directly from git with:

```bash
sudo pip install git+https://github.com/coursekevin/mpbatch.git
```

or...

Clone the repository:

``` bash
git clone https://github.com/coursekevin/mpbatch.git
```
and install the package by running:

```bash
python setup.py
```
from the mpbatch/ directory

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
