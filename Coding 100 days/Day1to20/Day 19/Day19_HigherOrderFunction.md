In Python (and many other programming languages), the presence or absence of parentheses
after a function name has a significant impact on how the function behaves. It can
determine whether the function is **called (executed)** or simply **referred to**. Let’s
dive into the details of both scenarios:

# 1. **With Parentheses: Function Call**

When you include parentheses `()` after the function name, it means that you are **calling
** or **executing** the function immediately. The function runs its code, performs its
task, and returns its result (if any).

#### Syntax:

```python
function_name()  # Call the function immediately
```

#### Example:

```python
def greet():
    print("Hello!")


greet()  # This calls the function
```

Output:

```
Hello!
```

Explanation:

- The `greet()` function is called when you include the parentheses.
- The code inside `greet()` (`print("Hello!")`) is executed, and "Hello!" is printed to
  the console.

#### With Parameters:

If your function takes parameters, you also provide them inside the parentheses during the
function call.

```python
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")  # This calls the function and passes the argument "Alice"
```

Output:

```
Hello, Alice!
```

# 2. **Without Parentheses: Function Reference (No Call)**

When you **omit** the parentheses, you are not calling the function, but instead, you are
**referring** to the function object itself. The function is not executed; you are just
creating a reference to it.

#### Syntax:

```python
function_name  # Reference to the function (no parentheses, no call)
```

#### Example:

```python
def greet():
    print("Hello!")


greet  # This refers to the function, but does not call it
```

Explanation:

- In this case, `greet` is just a **reference to the function**. The function is not
  executed, so nothing happens in the output.

#### Using Function Reference:

This concept is very useful in scenarios where you need to **pass a function as an
argument** to another function or assign it to a variable, but don’t want to execute it
immediately.

Example:

```python
def greet():
    print("Hello!")


def execute_function(func):
    func()  # Calls the function passed as the argument


execute_function(greet)  # Pass the function reference without parentheses
```

Output:

```
Hello!
```

Explanation:

- `greet` is passed as an argument to `execute_function`, but it’s not executed right
  away.
- Inside `execute_function`, `func()` calls the passed function (`greet()`), and "Hello!"
  is printed.

### Summary of the Difference:

| **With Parentheses** (`greet()`)             | **Without Parentheses** (`greet`)                              |
|----------------------------------------------|----------------------------------------------------------------|
| Calls and executes the function.             | Refers to the function, no execution.                          |
| Runs the function code immediately.          | Can be passed around as a reference or assigned to a variable. |
| Returns the result of the function (if any). | Holds the function object, can be called later.                |

### Practical Use Cases of No Parentheses (Function Reference)

#### 1. **Passing a Function as a Callback:**

In event-driven programming, such as in GUI or web frameworks, you often pass functions as
**callbacks**. The callback function will be executed when an event occurs. For example,
in **Turtle** or **Tkinter**, you pass function references without parentheses to event
handlers like mouse clicks or key presses.

Example:

```python
import turtle


def move_forward():
    turtle.forward(100)


# Assign the function reference to the event (no parentheses)
turtle.onkey(move_forward, "Up")
turtle.listen()
turtle.mainloop()
```

- Here, `move_forward` is passed as a **reference** to the `onkey()` function, and it will
  be called when the "Up" key is pressed.

#### 2. **Storing Functions in Variables:**

You can store a function in a variable and call it later when needed.

```python
def say_hello():
    print("Hello!")


# Assign the function to a variable
greeting = say_hello

# Call the function later using the variable
greeting()  # Output: Hello!
```

# 3. **Higher-Order Functions:**

A **higher-order function (HOF)** is a function that either:

1. **Takes one or more functions as arguments**, or
2. **Returns a function as a result**.

This concept allows for flexible, reusable, and modular code in programming by making
functions more abstract and general.

### Key Characteristics of Higher-Order Functions:

1. **Accepting functions as arguments**:
   A higher-order function can take one or more functions as parameters. This allows a
   function to be more versatile and adaptable, depending on the behavior of the passed
   functions.

2. **Returning functions**:
   Higher-order functions can also return functions as output. This enables function
   composition, deferred execution, and the creation of function factories.

3. **Abstraction**:
   HOFs allow for abstracting repetitive code patterns. Instead of repeating logic, the
   behavior can be passed as a function, enabling code reuse.

### Example of Higher-Order Functions:

#### 1. Passing a function as an argument:

```python
def apply_twice(func, x):
    return func(func(x))


def add_two(n):
    return n + 2


result = apply_twice(add_two, 5)
print(result)  # Output: 9
```

In this example, `apply_twice` is a higher-order function because it takes the function
`add_two` as an argument and applies it twice to the input value.

#### 2. Returning a function:

```python
def multiply_by(factor):
    def multiply(n):
        return n * factor

    return multiply


double = multiply_by(2)
triple = multiply_by(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15
```

Here, `multiply_by` is a higher-order function because it returns a new function (
`multiply`) that multiplies by a given factor. This allows the creation of custom
multiplier functions (like `double` and `triple`).

### Built-in Higher-Order Functions in Python:

Python provides several built-in higher-order functions, such as:

- **`map()`**: Takes a function and an iterable, applies the function to each element of
  the iterable.

  ```python
  numbers = [1, 2, 3, 4]
  result = map(lambda x: x * 2, numbers)
  print(list(result))  # Output: [2, 4, 6, 8]
  ```

- **`filter()`**: Takes a function and an iterable, returns an iterable of items that
  satisfy the condition in the function.

  ```python
  numbers = [1, 2, 3, 4, 5]
  result = filter(lambda x: x % 2 == 0, numbers)
  print(list(result))  # Output: [2, 4]
  ```

- **`reduce()`** (from `functools` module): Takes a function and an iterable, reduces the
  iterable to a single value by applying the function cumulatively.

  ```python
  from functools import reduce
  numbers = [1, 2, 3, 4]
  result = reduce(lambda x, y: x + y, numbers)
  print(result)  # Output: 10
  ```

### Benefits of Higher-Order Functions:

1. **Modularity**: HOFs enable building small, modular functions that can be combined to
   perform complex tasks.
2. **Reusability**: Common patterns can be abstracted into functions that accept different
   behaviors (functions) as arguments.
3. **Clarity and Simplicity**: HOFs reduce repetitive code and make the purpose of the
   code clearer.

### Summary:

Higher-order functions increase flexibility in programming by making functions more
reusable and abstract. They can take functions as arguments or return new functions,
enabling complex behavior to be composed out of simpler parts.