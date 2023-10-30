In Python, data can be grouped in categories called Types.

| Name      | Example      |
| ---       | ---          |
| string    | "hello"      |
| list      | \[1, 2, 3, 4] |
| integers or `int` | 1  -10  23 |
| `float`     | 3.5  -3.5  1.0 |
| boolean or `bool` | `True` `False` |

An example of using these types of data:

```python
favourite_food = "tempura"
my_age = 16    # my_age is of type int or integer
```

## Type Conversion

In Python, there are some *special functions* that allow us to change the type of something.

```python
intro_string = "My age is "    # type string
my_age = 15                    # type int

# Aside
"My name is" + "Duck"          # "My name isDuck"

print(intro_string + my_age)   # THIS BREAKS
```

We can use the following *built in* functions to convert into different types:

```python
int()
float()
str()

list()
```

We can fix the example above in this way

```python
intro_string = "My name is"
my_age = 16

print(intro_string + str(my_age))
print(intro_string + " " + str(my_age))
print(f"{intro_string} {my_age}")
```
