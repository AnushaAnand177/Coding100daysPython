Functions in Python allow you to encapsulate code into reusable blocks. When a function is designed to accept inputs, these inputs are called **parameters** or **arguments**. Let’s break down how functions with inputs work, with examples.

### 1. **Function Definition with Parameters**

A function can be defined with parameters, which are placeholders for the values (arguments) that you will pass to the function when you call it.

```python
def greet(name):
    print(f"Hello, {name}!")
```

- **`def greet(name):`** - Here, `name` is a parameter. It’s a variable that will receive a value when the function is called.
- **`print(f"Hello, {name}!")`** - This line uses the `name` parameter to print a personalized greeting.

### 2. **Calling a Function with Arguments**

When you call a function and pass values to it, these values are called **arguments**. The function uses these arguments to execute its code.

```python
greet("Alice")
greet("Bob")
```

- **`greet("Alice")`** - Here, `"Alice"` is an argument passed to the `greet` function. The function prints "Hello, Alice!".
- **`greet("Bob")`** - Similarly, `"Bob"` is passed as an argument, and the function prints "Hello, Bob!".

### 3. **Multiple Parameters**

A function can accept more than one parameter. Here’s an example:

```python
def add_numbers(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is {result}")
```

- **`def add_numbers(a, b):`** - This function takes two parameters, `a` and `b`.
- **`result = a + b`** - The function adds the two numbers.
- **`print(f"The sum of {a} and {b} is {result}")`** - It then prints the result.

#### Calling the Function:

```python
add_numbers(5, 3)
add_numbers(10, 20)
```

- **`add_numbers(5, 3)`** - The function prints "The sum of 5 and 3 is 8".
- **`add_numbers(10, 20)`** - The function prints "The sum of 10 and 20 is 30".

### 4. **Return Values**

Often, you’ll want a function to return a value instead of just printing it. You can use the `return` statement to send a value back to the caller.

```python
def multiply_numbers(x, y):
    return x * y
```

- **`return x * y`** - This line returns the product of `x` and `y`.

#### Using the Return Value:

```python
result = multiply_numbers(4, 5)
print(result)  # Output: 20
```

- **`result = multiply_numbers(4, 5)`** - The function returns `20`, which is then stored in the variable `result`.
- **`print(result)`** - This prints the value stored in `result`, which is `20`.

### 5. **Default Parameters**

Sometimes, you might want to give a parameter a default value. This means that if no argument is passed, the function will use the default value.

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")
```

- **`name="Guest"`** - Here, `"Guest"` is the default value for the `name` parameter.

#### Calling the Function with or without an Argument:

```python
greet("Alice")  # Output: Hello, Alice!
greet()         # Output: Hello, Guest!
```

- **`greet("Alice")`** - Uses the argument `"Alice"`.
- **`greet()`** - Uses the default value `"Guest"` because no argument was provided.

### Summary

- **Parameters**: Variables defined in the function definition.
- **Arguments**: Values passed to the function when it’s called.
- **Return Statement**: Sends a value back to the caller.
- **Default Parameters**: Allows a function to have optional arguments with default values.