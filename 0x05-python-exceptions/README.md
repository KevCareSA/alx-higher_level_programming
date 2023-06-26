
# Python - Exceptions

## Function Prototypes :

Prototypes for functions written in this project:

| File                             | Prototype                                               |
| -------------------------------- | ------------------------------------------------------- |
| `0-safe_print_list.py`           | `def safe_print_list(my_list=[], x=0):`                 |
| `1-safe_print_integer.py`        | `def safe_print_integer(value):`                        |
| `2-safe_print_list_integers.py`  | `def safe_print_list_integers(my_list=[], x=0):`        |
| `3-safe_print_division.py`       | `def safe_print_division(a, b):`                        |
| `4-list_division.py`             | `def list_division(my_list_1, my_list_2, list_length):` |
| `5-raise_exception.py`           | `def raise_exception():`                                |
| `6-raise_exception_msg.py`       | `def raise_exception_msg(message=""):`                  |
| `100-safe_print_integer_err.py`  | `def safe_print_integer_err(value):`                    |
| `101-safe_function.py`           | `def safe_function(fct, *args):`                        |
| `102-magic_calculation.py`       | `def magic_calculation(a, b);`                          |
| `103-python.c`                   | `void print_python_list(PyObject *p);void print_python_bytes(PyObject *p);``void print_python_float(PyObject *p);`

## Tasks :

* **0. Safe list printing**
  * [0-safe_print_list.py: Python function that prints `x` elements
  of a list on the same line, followed by a new line.
  * The parameter `x` represents the number of elements to print - can be
  bigger than the length of `my_list`.
  * Returns the real number of elements printed.
  * Without importing modules or using `len()`.

* **1. Safe printing of an integers list**
  * 1-safe_print_integer.py: Python function that prints an integer in `"{:d}".format()` format.

* **2. Print and count integers**
  * 2-safe_print_list_integers.py: Python function that prints the first `x` elements of a list that are integers on the same line, followed by a new line.
  

* **3. Integers division with debug**
  * 3-safe_print_division.py: Python function that divides two integers and prints the result using `finally:`.

* **4. Divide a list**
  * 4-list_division.py: Python function that divides two lists element by element.


* **5. Raise exception**
  * 5-raise_exception.py: Python function that raises a type exception.


* **6. Raise a message**
  * 6-raise_exception_msg.py: Python function that raises a
  name exception with a message.
 

* **7. Safe integer print with error message**
  * 100-safe_print_integer_err.py: Python function that
  prints an integer with type-checking in `"{:d}".format())` format.

* **8. Safe function**
  *  101-safe_function.py: Python function that executes
  a function safely.

* **9. ByteCode -> Python #4**
  * 102-magic_calculation.py: Python function matching exactly a
  bytecode provided by ALX.
