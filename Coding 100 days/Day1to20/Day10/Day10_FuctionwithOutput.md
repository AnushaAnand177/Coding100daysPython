### Functions in Python with Output: A Detailed Explanation

In Python, a **function** is a reusable block of code designed to perform a specific task. Functions can take inputs (known as **parameters**) and can return outputs. When a function **returns** a value, it provides an **output** that can be used later in the program.

---

### Components of a Function:
1. **Function Declaration (Definition)**:
    A function is defined using the `def` keyword.
2. **Function Name**:
    A unique name that describes what the function does.
3. **Parameters (Optional)**:
    Values passed into the function (inputs).
4. **Return Statement (Optional)**:
    This is how a function provides an output back to the caller.

---

### Basic Example of a Function with Output:

```python
def add_numbers(a, b):
    # Add two numbers and return the result
    result = a + b
    return result
```

- **`def`**: Keyword used to define the function.
- **`add_numbers`**: The function name, which suggests that it adds two numbers.
- **`a` and `b`**: Parameters that the function will accept when called.
- **`return result`**: The function outputs the sum of `a` and `b`.

---

### Calling the Function:

```python
output = add_numbers(5, 3)
print(output)  # Output: 8
```

When you call the function `add_numbers(5, 3)`, the two arguments `5` and `3` are passed to the function. The function processes them and returns their sum, which is stored in the variable `output` and then printed as `8`.

---

### How **Return** Works:
When you use a **`return`** statement in a function, it does two things:
1. **Outputs a Value**: The function sends back a result.
2. **Stops the Function Execution**: Once a `return` statement is hit, the function stops executing, and no further code in the function is run.

Example:

```python
def greet(name):
    return "Hello, " + name
    print("This line will never be executed")
```

Here, the `print` statement after the `return` will never be executed because the function stops as soon as it hits the `return` statement.

---

### Multiple Outputs:
A function can return multiple values by returning them as a **tuple**.

```python
def calculate(a, b):
    sum_ = a + b
    product = a * b
    return sum_, product

result_sum, result_product = calculate(10, 5)
print(result_sum)      # Output: 15
print(result_product)  # Output: 50
```

Here, the function `calculate()` returns both the sum and the product of the two inputs, and the results are unpacked into two variables.

---

### Function Without Return (No Output):

If a function doesn’t have a `return` statement, it implicitly returns `None`.

```python
def say_hello(name):
    print("Hello, " + name)

result = say_hello("Alice")  # This function does not return a value
print(result)  # Output: None
```

The function prints "Hello, Alice" to the console, but since it doesn’t return anything, the variable `result` will be `None`.

---

### Example: Function with Output Using Conditionals

Let's create a function that checks whether a number is even or odd and returns a message:

```python
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"

result = check_even_odd(7)
print(result)  # Output: 7 is odd
```

In this example:
- The function checks whether the number is divisible by 2.
- It returns a formatted string indicating whether the number is **even** or **odd**.

---

### Advanced: Using Function Output in Another Function

You can also use the result of one function as an input to another function:

```python
def square(number):
    return number ** 2

def double_square(x):
    return square(x) * 2

result = double_square(3)
print(result)  # Output: 18
```

- **`square(3)`** returns `9`.
- **`double_square(3)`** multiplies that result by `2`, giving `18`.

---

### Summary of Differences:

### Example 1: Basic Function with Return

```python
def add_numbers(a, b):
    result = a + b
    return result
```

### Explanation:
- **Input**: Takes two inputs (`a` and `b`).
- **Process**: Adds the two numbers.
- **Output**: Returns the sum of `a` and `b`.
- **Return Behavior**: The function outputs the result using the `return` statement and the function call gives back the output.

---

### Example 2: Function Without Return (Printing Inside Function)

```python
def say_hello(name):
    print("Hello, " + name)
```

### Explanation:
- **Input**: Takes a single input (`name`).
- **Process**: Combines a string with the input name and prints it.
- **Output**: There is no return statement; the output is displayed directly in the console using `print()`.
- **Return Behavior**: This function doesn't return a value, so any call to it would yield `None` if you try to store it in a variable.

---

### Comparison Between the Two Functions:

1. **Output Control**:
   - In the **first function** (`add_numbers`), the output is returned to the caller, meaning it can be stored, used later, or passed to other functions.
   - In the **second function** (`say_hello`), the result is directly printed inside the function, which means it’s displayed immediately but cannot be used elsewhere since it doesn’t return a value.

2. **Flexibility**:
   - **First function** (`add_numbers`): Since it returns the result, the caller can decide what to do with the result (store it, print it, or use it in another computation).
   - **Second function** (`say_hello`): Since it only prints the message, its usage is limited to direct output to the console, and the result cannot be reused elsewhere in the program.

3. **Reusability**:
   - **First function**: You can reuse the returned result in other parts of the code, making it more versatile.
   - **Second function**: Once the message is printed, it can’t be reused without calling the function again.

---

### Summary 

| Aspect                     | Function with Return (`add_numbers`) | Function without Return (`say_hello`) |
|-----------------------------|--------------------------------------|---------------------------------------|
| **Output**                  | Returns a value to the caller        | Prints directly, no return            |
| **Usage of Result**         | Can be stored, reused, or passed     | Cannot be stored or reused            |
| **Return Value**            | Can be anything (number, string, etc.) | Always returns `None`                |
| **Flexibility**             | More flexible; result can be used elsewhere | Limited to displaying information    |
| **Best Use Case**           | When you need the result later       | When you just need to print something |

---

In essence, a function with a return statement gives you control over what to do with the output, while a function that only prints is more limited to immediate console output.