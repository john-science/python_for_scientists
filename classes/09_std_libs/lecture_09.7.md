# Decorators

> TODO

## What is a Decorator?

A "decorator" is a wrapper you define around a function or classs in Python. A decorator might allow you to modify the inputs or outputs of a function. A decorator might allow you to wrap different functions with the same error / validity checking logic.

We will have to look at some examples, but decorators are a great way to write logic to "wrap around" other logic.  It's a useful and powerful idea, once you have used it a couple of times.

## Toy Examples

TODO

### Time a Method

TODO

```python
def time_it(func):
    def wrapper(*arg):
        t = time.time()
        res = func(*arg)
        print(time.time() - t)
        return res

    return wrapper


@time_it
def wait_one_sec():
    time.sleep(1)


wait_one_sec()
```


### Validate the Inputs

TODO


## Standard Library Examples

TODO


## Problem Sets

 * TODO

## Further Reading

 * [Geeks for Geeks](https://www.geeksforgeeks.org/decorators-in-python/)
 * [Python Basics](https://pythonbasics.org/decorators/)
 * [Programiz](https://www.programiz.com/python-programming/decorator)
 * [Python decorator list: std libs and found in the wild](https://github.com/lord63/awesome-python-decorator)

[Back to Syllabus](../../README.md)
