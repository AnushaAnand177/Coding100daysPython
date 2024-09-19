## 1. Python's Primitive Data Types
Python provides several primitive data types that serve as the foundation for more complex data structures. These include:

- **Integers (int)**: Whole numbers, positive or negative, without a decimal point. For example, 5, -10, and 42.

- **Floats (float)**: Numbers that include a decimal point. For example, 3.14, 0.001, and -2.5.

- **Strings (str)**: A sequence of characters enclosed in quotes. For example, "Hello, World!", 'Python', and "1234".

- **Booleans (bool)**: Represent logical values: True or False.

These data types are called "primitive" because they are the most basic and are not composed of other types.

## 2. Type Errors
In Python, a type error occurs when an operation or function is applied to an object of an inappropriate type. For example, trying to concatenate a string and an integer directly will result in a TypeError:

`name = "Alice"
age = 25
print(name + age)  # This will raise a TypeError`

The above code fails because Python doesn't know how to combine a string with an integer directly.

## 3. Type Checking
Type checking is the process of verifying the type of an object in Python. This is often necessary to prevent type errors. Python provides the type() function to check the type of any variable:


`x = 42
print(type(x))  # Output: <class 'int'>`
You can use type checking to ensure that the data is of the expected type before performing operations on it.

## 4. Type Conversion
To avoid type errors, you often need to perform type conversion (also known as type casting). This involves converting a value from one data type to another. Python provides several built-in functions for type conversion:

* int(): Converts a value to an integer.
* float(): Converts a value to a float.
* str(): Converts a value to a string.
* bool(): Converts a value to a boolean.
For example, to concatenate a string with an integer, you need to convert the integer to a string:

`name = "Alice"
age = 25
print(name + " is " + str(age) + " years old.")`

## 5. Mathematical Operators
Python supports a wide range of mathematical operators for performing arithmetic operations:

* **Addition (+)**: Adds two numbers. Example: 3 + 5 results in 8.
* **Subtraction (-)**: Subtracts the second number from the first. Example: 10 - 4 results in 6.
* **Multiplication (*)**: Multiplies two numbers. Example: 2 * 3 results in 6.
* **Division (/)**: Divides the first number by the second and returns a float. Example: 7 / 2 results in 3.5.
* **Floor Division (//)**: Divides the first number by the second and returns the integer part of the quotient. Example: 7 // 2 results in 3.
* **Modulus (%)**: Returns the remainder of the division. Example: 7 % 2 results in 1.
* **Exponentiation (**)**: Raises the first number to the power of the second. Example: 2 ** 3 results in 8.

These operators are fundamental for performing calculations and manipulating numeric data in Python.

## 6. Number Manipulation
Python provides various methods for number manipulation, allowing you to perform complex mathematical operations:

**Rounding Numbers**: Use the round() function to round a number to a specified number of decimal places:

`x = 3.14159
print(round(x, 2))  # Output: 3.14`

**Absolute Value**: The abs() function returns the absolute value of a number:

`y = -10
print(abs(y))  # Output: 10`

**Power Function**: Use pow(x, y) to raise x to the power of y:

`print(pow(2, 3))  # Output: 8`

**Square Root**: Use the sqrt() function to calculate the square root of a number:

`print(sqrt(9))  # Output: 3`

## 7. f-Strings
**f-Strings** _(formatted string literals)_ are a modern and powerful way to embed 
expressions inside string literals, introduced in Python 3.6. 
They offer a more readable and concise way to format strings compared to older methods 
like `str.format()` or concatenation.

To use f-strings, prefix the string with an f and include expressions inside curly braces {}:

`name = "Alice"
age = 25
print(f"{name} is {age} years old.")`

f-Strings can include any valid Python expression, not just variables:

`width = 10
height = 5
print(f"The area of the rectangle is {width * height}.")`

f-Strings simplify string formatting and make the code more readable and less error-prone.