# case

A module to allow python to have a 'case' statement (otherwise known
as 'switch')

## How to use it

###1. Importing
It is recommended to import the `case` module using the following code:
```python
from case import case
```
This is because there is only one external function in this module and therefore that is all you will need

###2. The Arguments to the function

The case function by itself has indefinitely many arguments, but each argument must follow this format:
```python
(bool_value, function, (function_argument1, function_argument2),{'keyword_argument': 3})
```

where:
`bool_value` is the result of a boolean expression such as `a == 1`;
`function` is a function, such as `print` (do not have brackets, that will call the function);
`(function_argument1,function_argument2)` are the arguments to the function (there can be as many or as few as you want and this can be omitted)
`{'keyword_argument': 3}` are the keyword arguments (these can be omitted, but if they are added, the 'normal' arguments must be in place)

**Note:**
If you want a keyword argument but not a 'normal' one, empty brackets `()` should be used in the 'normal' arguments

###3. Return values
The `case` function returns whatever value the executed function does

###Examples:
Code:
```python

from case import case

a = 2
case(
    (a == 1, print, ('a is 1')),
    (a == 2, print, ('a is 2','and not 3'), {'sep': ': '}),
    (a == 3, print)
)
```
Output:
`a is 2: and not 3`

Code:
```python
n = 1
n = case(
    (isinstance(n,string), int, (n,)),
    (isinstance(n,float), math.floor, (n,)),
    (True, print, (n,))
)
```
Output:
`1`

In this scenario, the `True` value in the final case acts as an `else` would in an if statement
