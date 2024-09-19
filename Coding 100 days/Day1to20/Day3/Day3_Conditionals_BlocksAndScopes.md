# Python Conditional Statements, Logical Operators, Code Blocks, and Scopes

Understanding conditional statements, logical operators, code blocks, and scopes is fundamental for controlling the flow of your Python programs. This article provides an overview of these concepts and how they are used in Python.

## Conditional Statements

Conditional statements in Python allow you to execute specific blocks of code based on certain conditions. The most common conditional statements are `if`, `elif`, and `else`.

### `if` Statement

The `if` statement evaluates a condition. If the condition is `True`, the code block inside the `if` statement is executed.
```python
x = 10

if x > 5:
    print("x is greater than 5")
  ```


### `elif` Statement

The `elif `(short for "else if") statement allows you to check multiple conditions. 
If the `if` condition is False, Python checks the `elif` condition.

```python
x = 10

if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but less than or equal to 15")
  ```

### `else` Statement

The `else` statement is executed if all preceding conditions are False.

```python
x = 2

if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")
  ```

#### Nested Conditionals

Conditional statements can be nested, allowing for more complex decision-making processes.
#### Example of Nested Conditionals
```python
x = 10
if x > 5:
    if x > 15:
        print("x is greater than 15")
    else:
        print("x is greater than 5 but less than or equal to 15")
else:
    print("x is 5 or less") 
```
#### Logical Operators

Logical operators are used to combine conditions. The logical operators are `and`, `or`, and `not`.

#### Example of Logical Operators

```python
x = 10
y = 20

# Using 'and'
if x > 5 and y > 15:
    print("Both conditions are True")

# Using 'or'
if x > 15 or y > 15:
    print("At least one condition is True")

# Using 'not'
if not x < 5:
    print("x is not less than 5")

```

### Code Blocks

A code block is a group of statements that are executed together. 
In Python, code blocks are defined by their indentation level.

```python
x = 10

if x > 5:
    print("x is greater than 5")  # This line is part of the if code block
    y = x * 2                      # This line is also part of the if code block

print("This line is outside the if block")
```

### Scopes

Scope refers to the visibility and lifetime of variables. 
In Python, there are two main types of scopes:

* **Local Scope**: Variables declared inside a function or a code block are in the local
scope and can only be accessed within that function or block.
* **Global Scope**: Variables declared outside of all functions or blocks are in the 
global scope and can be accessed from anywhere in the code.
```python
def my_function():
    local_var = 10
    print(local_var)

my_function()
print(local_var)  # This will raise a NameError because local_var is not in the global scope
```
### Global Scope

```python
global_var = 20

def my_function():
    print(global_var)

my_function()  # This will print 20 because global_var is in the global scope
```

### Modifying Global Variables

To modify a global variable inside a function, you must use the global keyword.

```python
global_var = 20

def modify_global():
    global global_var
    global_var = 40

modify_global()
print(global_var)  # This will print 40
```

### Modulous Operator

The modulo operator in Python is represented by the `%` symbol and is used to find the remainder of the division of one number by another. It's a fundamental operator in many programming languages and is particularly useful for tasks like checking if a number is even or odd, determining divisibility, or cycling through a sequence.

### Syntax

```python
result = a % b
```

Here, `a` is the dividend, and `b` is the divisor. The expression `a % b` returns the remainder when `a` is divided by `b`.

### Examples

1. **Basic Example:**

```python
print(10 % 3)  # Output: 1
```
   
- **Explanation:** 10 divided by 3 equals 3 with a remainder of 1, so `10 % 3` is `1`.

2. **Even or Odd Check:**

   You can use the modulo operator to check if a number is even or odd.
 
```python
   number = 15
   if number % 2 == 0:
       print(f"{number} is even")
   else:
       print(f"{number} is odd")
       
```
   - **Explanation:** If the remainder when dividing by 2 is `0`, the number is even; otherwise, it's odd.

3. **Divisibility Check:**

   You can use the modulo operator to check if one number is divisible by another.
```python
   number = 25
   if number % 5 == 0:
       print(f"{number} is divisible by 5")
   else:
       print(f"{number} is not divisible by 5")
   ```
   - **Explanation:** If the remainder is `0`, the number is divisible by the divisor.

4. **Cyclic Patterns:**

   The modulo operator is also useful in cyclic patterns, like determining the day of the week.
   ```python
   days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
   day_number = 10
   print(days_of_week[day_number % 7])  # Output: "Wednesday"
   ```
   - **Explanation:** `10 % 7` equals `3`, so `days_of_week[3]` corresponds to `"Wednesday"`.

### Special Cases

- **Modulo with Zero:**
  - Dividing by zero is undefined, so attempting to use `a % 0` will result in a `ZeroDivisionError` in Python.
  
```python
print(10 % 0)  # This will raise ZeroDivisionError
  ```

- **Negative Numbers:**
  - The result of the modulo operation when involving negative numbers can be a bit tricky, as it depends on the language's implementation. In Python, the result has the same sign as the divisor.

 ```python
  print(-10 % 3)  # Output: 2
  print(10 % -3)  # Output: -2
 ```

### Conclusion

The modulo operator is a powerful tool in Python that allows you to 
determine the remainder of division operations. 
It has practical applications in various tasks such as checking 
for even or odd numbers, ensuring divisibility, 
creating cyclic patterns, and more. 
Understanding how to use the modulo operator effectively can help you 
solve many programming problems with ease.