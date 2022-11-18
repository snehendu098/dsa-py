# Approach 1: Bad Approach of using a queue

Open python in terminal

```
mylist = []
mylist.append("value 1")
mylist.append("value 2")

mylist.push(0)
```

In queue, insertion and deletion happens from 2 different ends. So `mylist.push(0)` removes the 1st element. Thus, insertion happens from the last and deletion happens from 1st

# Approach 2:

```
>>> from collections import deque
>>> mylist = deque()
>>> mylist.append("Superman")
>>> mylist.append("Flash")
>>> mylist.append("Iron Man")

>>> mylist.popleft()
```

# Approach 3:

```
>>> from queue import Queue
>>> mylist = Queue()
>>> mylist.put("mango")
>>> mylist.put("banana")
>>> mylist.put("apple")

>>> mylist.get()
```

`put` inserts data and `get` removes the data. Once every element is removed with `mylist.get()`, you will see that running `mylist.get` doesn't do anything. You have to press `Ctrl+C` to quit the process and run `mylist.get_nowait()`. Then, you can see the exact result.
