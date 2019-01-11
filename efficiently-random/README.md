Design and implement a data structure which supports the following operations

1. `insert(x)`: Inserts the value x. If the value already exists, does nothing.
1. `delete(x)`: Deletes the value x from the data structure. Returns true if value was present and deleted else false if value was not present.
1. `search(x)`: Returns true or false depending on whether x is present or not.
1. `uniform_random()`: Returns a random value from the data structure with equal probability. By equal probability, it is meant that if called sufficient number of times, each value in the data structure is returned approximately equal number of times.


The input to the program will be input from the stdin in the following format:
```
INSERT x # insert(x)
DELETE x # delete(x)
SEARCH x # search(x)
RANDOM # uniform_random()
EXIT # closes the program.
```
Example Run:
```
> INSERT 1
> INSERT 5
> SEARCH 5
true
> INSERT 10
> RANDOM
1
> DELETE 1
true
> DELETE 18
false
```

As much as the implementation is important, we expect you to provide a short explanation of the following:
- Implementation of the data structure
- Time complexity of the four operations and explanation behind it.


Scoring Criteria:
- You will be judged on the worst time complexity among individual operations. Example,
If `insert(x), delete(x), search(x)` happen in `O(1)` (let's just say) and `uniform_random()` happens in `O(n)` then the time complexity of your solution will be considered to be `O(n)`.
