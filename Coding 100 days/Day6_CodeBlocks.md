### Code Blocks in Python

Code blocks are fundamental to writing and organizing code in Python. They define sections of code that should be executed together, typically within constructs like functions, loops, conditionals, or classes. Understanding how code blocks work is essential for writing clear, maintainable, and correctly functioning Python programs.

#### What is a Code Block?

A code block is a group of statements that are intended to be executed as a unit. In Python, code blocks are defined by their indentation level rather than by explicit delimiters like curly braces `{}` in languages such as C++ or Java.

#### Indentation

- **Indentation** is crucial in Python. It’s how Python determines which statements belong to the same code block.
- Consistent use of indentation (usually 4 spaces per level) is important. Mixing tabs and spaces, or inconsistent indentation, can lead to errors.

#### Example of a Code Block

```python
def greet(name):
    print("Hello, " + name + "!")
    print("Welcome aboard.")
```

In this example, the two `print` statements are part of the same code block. They will only be executed together when the `greet` function is called.

#### Code Blocks in Conditional Statements

When using `if`, `elif`, and `else` statements, the code block associated with each condition will only execute if the condition is met.

```python
age = 18

if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult!")
else:
    print("You are an adult.")
```

- The code block under `if` executes if the `if` condition is true.
- The code block under `elif` executes if the `if` condition is false and the `elif` condition is true.
- The `else` code block executes if none of the previous conditions are true.

#### Code Blocks in Loops

Loops like `for` and `while` also contain code blocks that execute repeatedly as long as the loop's condition is met.

```python
for i in range(3):
    print("Iteration", i)
    print("This is inside the loop")

print("This is outside the loop")
```

- The indented print statements are part of the loop’s code block, so they execute in each iteration of the loop.
- The last `print` statement is outside the loop’s code block, so it only executes once, after the loop completes.

#### Code Blocks in Functions

In functions, code blocks define the body of the function. All indented lines after the function declaration are part of the function’s code block.

```python
def calculate_area(radius):
    pi = 3.14159
    area = pi * (radius ** 2)
    return area
```

- The variables `pi` and `area`, along with the `return` statement, are part of the function’s code block. They execute together when the function is called.

#### Code Blocks in Classes

Classes in Python also contain code blocks. Each method within a class is a code block, as well as the code within those methods.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(self.name + " says woof!")
```

- The `__init__` and `bark` methods each have their own code blocks.
- Each method’s code block executes when the method is called on an instance of the class.

#### Nested Code Blocks

Code blocks can be nested inside other code blocks. For example, a function might contain an `if` statement, which in turn contains another code block.

```python
def check_number(num):
    if num > 0:
        print("The number is positive.")
        if num > 10:
            print("The number is greater than 10.")
    else:
        print("The number is not positive.")
```

- The outer `if` statement contains a code block.
- Inside this block, there is another `if` statement with its own code block.

#### The Importance of Proper Indentation

Python relies on indentation to define code blocks. Improper indentation can lead to errors or unexpected behavior.

```python
if True:
print("This will cause an IndentationError")
```

The above code will raise an `IndentationError` because the `print` statement is not indented properly under the `if` condition.

