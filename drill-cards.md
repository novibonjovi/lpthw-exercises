# Drill Cards

## Command Line Basics

01. **`pwd`**
   print working directory

02. **`hostname`**
   my computer's network name

03. **`mkdir`**
   make directory

04. **`cd`**
   change directory

05. **`ls`**
   list directory

06. **`rmdir`**
   remove directory

07. **`pushd`**
   push directory
   "Save where I am, then go here."

08. **`popd`**
   pop directory

09. **`cp`**
   copy a file or directory
   overwrites existing files

10. **`mv`**
    move a file or directory
    rename a file or directory

11. **`less`**
    page through a file

12. **`cat`**
    print the whole file

13. **`xargs`**
    execute arguments
    construct argument list(s) and execute utility

14. **`find`**
    find files

15. **`grep`**
    find things inside files

16. **`man`**
    read a manual page

17. **`apropos`**
    find which man page is appropriate

18. **`env`**
    look at your environment

19. **`echo`**
    print some arguments

20. **`export`**
    export/set a new environment variable

21. **`exit`**
    exit the shell

22. **`sudo`**
    DANGER! become super user root DANGER!

23. **`mkdir -p`**
    create directory plus every parent directories needed

24. **`cp -r`**
    copy more directories with files in them

25. **`chmod`**
    change file modes or Access Control Lists

26. **`chown`**
    change file owner and group


    ## String Escape Sequences

01. **`\\`**
    Backslash (\)

02. **`\'`**
    Single-quote (')

03. **`\"`**
    Double-quote (")

04. **`\a`**
    ASCII bell (BEL)

05. **`\b`**
    ASCII backspace (BS)

06. **`\f`**
    ASCII formfeed (FF)

07. **`\n`**
    ASCII linefeed (LF)

08. **`\N{name}`**
    Character named name in the Unicode database (Unicode only)

09. **`\r`**
    Carriage Return (CR)

10. **`\t`**
    Horizontal Tab (TAB)

11. **`\uxxxx`**
    Character with 16-bit hex value xxxx

12. **`\Uxxxxxxxx`**
    Character with 32-bit hex value xxxxxxxx

13. **`\v`**
    ASCII vertical tab (VT)

14. **`\ooo`**
    Character with octal calue ooo

15. **`\xhh`**
    Character with hex value hh

    ## Data Typed

01. **`True` and `False`**
    Boolean values.
    `True or False == True`
    `False and True == False`

02. **`None`**
    Represents "nothing" or "no value".
    `x = None`

03. **`bytes`**
    Stores bytes, maybe of text, PNG, file, etc.
    `x = b"hello"`

04. **`strings`**
    Stores textual information.
    `x = "hello"`

05. **`numbers`**
    Stores integers.
    `i = 100`

06. **`floats`**
    Stores decimals.
    `i = 10.389`

07. **`lists`**
    Stores a list of things.
    `j = [1,2,3,4]`

08. **`dicts`**
    Stores a key=value mapping of things.
    `e = {'x': 1, 'y': 2}`


    ## Operators

01. **`+`**
    Addition
    `2 + 4 == 6`

02. **`-`**
    Subtraction
    `2 - 4 == -2`

03. **`*`**
    Multiplication
    `2 * 4 == 8`

04. **`**`**
    Power of
    `2 ** 4 == 16`

05. **`/`**
    Division
    `2 / 4 == 0.5`

06. **`//`**
    Floor Division
    `2// 4 == 0`

07. **`%`**
    Modulus or String interpolate
    `2 % 4 == 2`

08. **`<`**
    Less than
    `2 < 4 == True`

09. **`>`**
    Greater than
    `2 > 4 == False`

10. **`<=`**
    Less than equal
    `4 <= 4 == True`

11. **`>=`**
    Greater than equal
    `4 >= 4 == True`

12. **`==`**
    Equal
    `4 == 5 == False`

13. **`!=`**
    Not equal
    `4 != 5 == True`

14. **`( )`**
    Parenthesis
    `len('hi') == 2`

15. **`[ ]`**
    List brackets
    `[1,3,5]`

16. **`{ }`**
    Dict curly braces
    `{'x': 5, 'y': 10}`

17. **`@`**
    At (decorators)
    `@classmethod`

18. **`,`**
    Comma
    `range(0, 10)`

19. **`:`**
    Colon
    `def X(): pass`

20. **`.`**
    Dot
    `self.x = 10`

21. **`=`**
    Assign equal
    `x = 10`

22. **`;`**
    Semi-colon
    `print("hi"); print("there")`

23. **`+=`**
    Add and assign
    `x = 1; x += 2`

24. **`-=`**
    Subtract and assign
    `x = 1; x -= 2`

25. **`*=`**
    Multiply and assign
    `x = 1; x *= 2`

26. **`/=`**
    Divide and assign
    `x = 1; x /= 2`

27. **`//=`**
    Floor divide and assign
    `x = 1; x //= 2`

28. **`%=`**
    Modulus assign
    `x = 1; x %= 2`

29. **`**=`**
    Power assign
    `x = 1; x **= 2`


    ## Python Keywords

01. **`and`**
    Logical and
    `True and False == False`

02. **`as`**
    Part of the with-as statement.
    `with X as Y: pass`

03. **`assert`**
    Assert (ensure) that something is true.
    `assert False, "Error!"`

04. **`break`**
    Stop this loop right now.
    `while True: break`

05. **`class`**
    Define a class.
    `class Person(object)`

06. **`continue`**
    Don't process more of the loop, do it again.
    `while True: continue``

07. **`def`**
    Define a funtion.
    `def X(): pass``

08. **`del`**
    Delete from dictionary.
    `del X[Y]`

09. **`elif`**
    Else if condition.
    `if: X; elif: Y; else: J``

10. **`else`**
    Else condition.
    `if: X; else: Y``

11. **`except`**
    If an exception happens, do this.
    `except ValueError as e: print(e)``

12. **`exec`**
    Run a string as Python.
    `exec 'print("hello")'`

13. **`finally`**
    Exceptions or not, finally do this no matter what.
    `finally: pass`

14. **`for`**
    Loop over a collection of things.
    `for X in Y: pass`

15. **`from`**
    Importing specific parts of a module.
    `from x import Y`

16. **`global`**
    Declare that you want a global variable. (bad practice)
    `global X`

17. **`if`**
    If condition.
    `if: X; else: Y`

18. **`import`**
    Import a module into this one to use.
    `import os`

19. **`in`**
    Part of for-loops. Also a test of X in Y.
    `for X in Y: pass` also `1 in [1] == True`

20. **`is`**
    Like == to test equality.
    `1 is 1 == True`

21. **`lambda`**
    Create a short anonymous function.
    `s = lambda y: y ** y; s(3)`

22. **`not`**
    Logical not.
    `not True == False`

23. **`or`**
    Logical or.
    `True or False == True`

24. **`pass`**
    This block is empty.
    `def empty(): pass`

25. **`print`**
    Print this string.
    `print('this string')`

26. **`raise`**
    Raises an exception when things go wrong.
    `raise ValueError("No")`

27. **`return`**
    Exit the function with a return value.
    `def X(): return Y`

28. **`try`**
    Try this block, and if exception, go to `except`.
    `try: pass`

29. **`while`**
    While loop.
    `while X: pass`

30. **`with`**
    With an expression as a variable do.
    `with X as Y: pass`

31. **`yield`**
    Pause here and return to caller.
    `def X(): yield Y; X().next()`

    ## Python others

01. **`end=' '`**
    End line with space (default is new line)

02. **`close`**
    Closes the file. Like `File->Save..` in your editor

03. **`read`**
    Reads the contents of the file. You can assign the result to a variable

04. **`readline`**
    Reads just one line of a text file

05. **`truncate`**
    Empties the file. Watch out if you care about the file

06. **`write('stuff')`**
    Writes "stuff" to the file

07. **`seek(0)`**
    Move the read/write location to the beginning of the file
