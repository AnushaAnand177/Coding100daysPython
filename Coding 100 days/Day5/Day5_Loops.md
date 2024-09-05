### Loops in Python

Loops are a fundamental concept in programming that allow you to repeat a block of code multiple times. Python provides two main types of loops: the `for` loop and the `while` loop.

#### 1. **`for` Loop**

The `for` loop in Python is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each item in the sequence.

**Basic `for` Loop Example:**

```python
# Looping through a list of numbers
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
```

Output:
```
1
2
3
4
5
```

In this example, the `for` loop iterates over each element in the `numbers` list and prints it.

**`for` Loop with `range()`:**

The `range()` function generates a sequence of numbers, which is commonly used with `for` loops.

```python
# Looping using range()
for i in range(5):
    print(i)
```

Output:
```
0
1
2
3
4
```

Here, `range(5)` generates numbers from 0 to 4, and the loop prints each number.

#### 2. **`while` Loop**

The `while` loop in Python continues to execute a block of code as long as a specified condition is `True`.

**Basic `while` Loop Example:**

```python
# Loop until a condition is met
count = 0

while count < 5:
    print(count)
    count += 1
```

Output:
```
0
1
2
3
4
```

In this example, the `while` loop keeps running as long as `count` is less than 5. After each iteration, `count` is incremented by 1.

### Loops with Lists

Loops are particularly powerful when working with lists, allowing you to iterate through elements, modify them, and perform various operations.

#### Iterating Over a List with `for` Loop

You can easily loop through each element in a list using a `for` loop:

```python
# Loop through a list of strings
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

Output:
```
apple
banana
cherry
```

This code loops through the `fruits` list and prints each fruit.

#### Modifying List Elements in a Loop

If you want to modify elements in a list, you can use a `for` loop along with indexing:

```python
# Multiply each element by 2
numbers = [1, 2, 3, 4, 5]

for i in range(len(numbers)):
    numbers[i] *= 2

print(numbers)
```

Output:
```
[2, 4, 6, 8, 10]
```

In this example, the `for` loop iterates through each index in the `numbers` list and doubles the value at each index.

#### Using `while` Loop with Lists

A `while` loop can also be used to iterate over a list, especially when the loop's condition depends on factors other than just the list’s elements.

```python
# Remove items from a list until it's empty
fruits = ["apple", "banana", "cherry"]

while fruits:
    print(fruits.pop())
```

Output:
```
cherry
banana
apple
```

Here, the `while` loop continues to run as long as the `fruits` list is not empty, removing and printing the last element each time.

