Strings are a Type of data.

# Format Strings
If we want to evaluate inside of a string, we use *f-strings*.
To create an f-string, we put an `f` before the open quote.

```python
fav_food = input("what's your favorite food? ")

print(f"Oooooo, {fav_food} sounds good!")
```


# String Methods
[[Methods]] are functions that we can use on [[objects]].

String methods allow us to modify strings.

Say for example, we want to make all the characters of a string lowercase.

```python
mr_ubial_yelling = "YOU SHOULD PUSH YOUR CHAIRS IN"

print(mr_ubial_yelling.lower())
```

We can use string methods to help solve [[Errors#Semantic Errors|semantic errors]].
## `.lower()`

The `.lower()` method takes a string and converts all uppercase characters to lowercase.

## `.upper()`

The `.upper()` method uppercases all the letters

## `.strip(chars)`

The `.strip()` method removes characters from both the beginning and the end of the string.

```python
user_feeling = input("How are you feeling today? ")

# "good!" "good." "Good!!!!!!!!"
if user_feeling.lower().strip("!.,") == "good":
	print("That's great!")
```

## `.split() -> List`

The `.split()` methods splits a string into a [[Lists|list]], separating the string based on the characters you give it.

```python
grocery_str = "eggs milk cheese hotwheels"

grocery_list = grocery_str.split(" ")
```
