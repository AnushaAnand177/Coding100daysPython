### Scope in Python

**Scope** refers to the region or area of a program where a particular variable or function is accessible. Python divides the scope of variables into four types:

1. **Local Scope**:
   - Variables created inside a function belong to the local scope of that function and can only be used within that function.
   - Once the function finishes execution, these variables are destroyed.
   
   ```python
   def my_function():
       x = 10  # Local variable
       print(x)  # Can access 'x' within this function
   
   my_function()  # 10
   print(x)  # Error! 'x' is not defined here
   ```

2. **Enclosing Scope (Nonlocal Scope)**:
   - This refers to variables in the local scope of enclosing functions, i.e., when one function is nested inside another.
   - Variables in the enclosing function are available to the inner function but are not local to it.

   ```python
   def outer_function():
       x = 5  # Enclosing variable
       
       def inner_function():
           print(x)  # Accessing the enclosing variable
       
       inner_function()  # Output: 5

   outer_function()
   ```

3. **Global Scope**:
   - Variables declared at the top-level of a script or module, outside of any function, are considered to have global scope.
   - They can be accessed throughout the code, even inside functions, unless shadowed by local variables.

   ```python
   x = 20  # Global variable
   
   def my_function():
       print(x)  # Can access global variable 'x'
   
   my_function()  # Output: 20
   ```

4. **Built-in Scope**:
   - This is the outermost scope that contains built-in objects and functions, like `print()`, `len()`, etc.
   
   ```python
   print("Hello!")  # 'print' is a built-in function
   ```

### Global Variables in Python

A **global variable** is one that is declared in the global scope, outside any function, and can be accessed by any function or code block in the program.

- You can declare a global variable like this:
  
  ```python
  x = 100  # Global variable
  
  def func():
      print(x)  # Accessing global variable inside the function
  
  func()  # Output: 100
  ```

- To modify a global variable inside a function, you need to use the `global` keyword:
  
  ```python
  x = 100
  
  def change_x():
      global x
      x = 50  # Modifies the global variable 'x'
  
  change_x()
  print(x)  # Output: 50
  ```

Without the `global` keyword, Python treats the variable as local to the function, even if a global variable with the same name exists.

### Constants in Python

In Python, **constants** are variables whose values should not change after being assigned. Although Python does not have built-in constant types, by convention, we write constants in **UPPERCASE** to signal that they should not be modified.

- For example:
  
  ```python
  PI = 3.14159  # PI is a constant (by convention)
  
  def calculate_circumference(radius):
      return 2 * PI * radius
  
  print(calculate_circumference(5))  # Output: 31.4159
  ```

However, unlike in other languages, there’s no language-enforced way to prevent a constant from being reassigned.

```python
PI = 3.14159
PI = 3  # Reassigning is allowed, but should be avoided by convention
```
