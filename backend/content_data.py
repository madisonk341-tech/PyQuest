"""Course content: module metadata, lesson content, practice pools, sandbox prompts.

Modules 1-3 are fully written (vertical slice). Modules 4-13 exist as metadata
only so they render on the learning map, but are marked hasContent=False until
written.
"""

MODULES_META = [
    {"id": "1", "title": "Intro to Course, Engineering & Programming", "week": 1, "icon": "🚀", "exam": None},
    {"id": "2", "title": "Sequential Steps, Variables, Assignment", "week": 2, "icon": "📦", "exam": "exam1"},
    {"id": "3", "title": "Data Types, Input/Output, Basic Functions", "week": 3, "icon": "🔤", "exam": "exam1"},
    {"id": "4", "title": "Boolean Expressions, Conditionals", "week": 4, "icon": "🔀", "exam": "exam1"},
    {"id": "5", "title": "Creating & Testing Programs, Basic Debugging", "week": 5, "icon": "🐞", "exam": "exam1"},
    {"id": "6", "title": "Loops and Iteration", "week": 6, "icon": "🔁", "exam": "exam1"},
    {"id": "7", "title": "Lists of Data", "week": 6, "icon": "📋", "exam": "exam1"},
    {"id": "8", "title": "Top-Down Design; Dictionaries", "week": 8, "icon": "🗂️", "exam": "exam2"},
    {"id": "9", "title": "Advanced Functions, Scope", "week": 9, "icon": "🧩", "exam": "exam2"},
    {"id": "10", "title": "Systematic Debugging", "week": 10, "icon": "🔍", "exam": "exam2"},
    {"id": "11", "title": "File Input and Output", "week": 11, "icon": "📁", "exam": "exam2"},
    {"id": "12", "title": "Using Engineering Modules in Python", "week": 12, "icon": "⚙️", "exam": "exam2"},
    {"id": "13", "title": "Functions in Top-Down / Bottom-Up Design", "week": 13, "icon": "🏗️", "exam": "exam2"},
]

MODULES_WITH_CONTENT = {"1", "2", "3"}

# ---------------------------------------------------------------------------
# Full lesson content for modules 1-3
# ---------------------------------------------------------------------------

MODULE_CONTENT = {
    "1": {
        "id": "1",
        "title": "Intro to Course, Engineering & Programming",
        "intro": "Before writing real programs, let's get oriented: what programming actually is, "
                 "how to make a program talk back to you with print(), and how to leave notes for "
                 "yourself (and your grader) with comments.",
        "components": [
            {
                "id": "1.1",
                "title": "What Is Programming?",
                "explanation": (
                    "A computer only does exactly what it's told, in exactly the order it's told. "
                    "Programming is the act of writing that exact list of instructions in a language "
                    "the computer can follow — for this course, that language is Python.\n\n"
                    "A Python **script** is just a text file full of instructions, executed top to "
                    "bottom by a program called an *interpreter*. When you 'run' a script, the "
                    "interpreter reads each line and carries it out immediately, which is different "
                    "from languages that must be fully compiled before anything happens."
                ),
                "examples": [
                    {
                        "code": 'print("Hello, world!")',
                        "output": "Hello, world!",
                        "note": "The classic first program: print() displays whatever is inside the parentheses.",
                    }
                ],
                "practice": [
                    {
                        "id": "1.1.p1",
                        "question": "What does a Python interpreter do?",
                        "choices": [
                            "Reads and executes your code line by line",
                            "Draws the icons for your desktop",
                            "Compiles your code into a Word document",
                            "Only runs after your whole computer restarts",
                        ],
                        "answer": 0,
                        "explanation": "The interpreter executes Python source line by line, top to bottom.",
                    },
                    {
                        "id": "1.1.p2",
                        "question": "A Python script is best described as:",
                        "choices": [
                            "A picture of your code",
                            "A text file containing instructions for the interpreter",
                            "A type of computer hardware",
                            "A compiled binary file only",
                        ],
                        "answer": 1,
                        "explanation": "Scripts are plain text files containing Python instructions.",
                    },
                ],
            },
            {
                "id": "1.2",
                "title": "The print() Function",
                "explanation": (
                    "print() is how a program communicates with the outside world. Anything placed "
                    "between its parentheses is displayed on the screen (the console).\n\n"
                    "You can print multiple pieces of information at once by separating them with "
                    "commas — print() automatically puts a space between them. You can also control "
                    "what goes between items (sep) and what's printed at the very end (end, which "
                    "defaults to a newline)."
                ),
                "examples": [
                    {
                        "code": 'print("Engineering", "is", "fun")',
                        "output": "Engineering is fun",
                        "note": "Commas between arguments insert a single space automatically.",
                    },
                    {
                        "code": 'print("A", "B", "C", sep="-")\nprint("No newline here", end="")\nprint(" ...continued")',
                        "output": "A-B-C\nNo newline here ...continued",
                        "note": "sep changes the separator between items; end changes what prints after the line (default is a newline).",
                    },
                ],
                "practice": [
                    {
                        "id": "1.2.p1",
                        "question": 'What is the output of print("x", "y", "z")?',
                        "choices": ["xyz", "x y z", "x, y, z", "Error"],
                        "answer": 1,
                        "explanation": "By default, print() separates arguments with a single space.",
                    },
                    {
                        "id": "1.2.p2",
                        "question": 'What does print("Hi", end="!") print, exactly?',
                        "choices": [
                            "Hi followed by a newline",
                            "Hi! with no newline afterward",
                            "!Hi",
                            "An error, end is not a valid argument",
                        ],
                        "answer": 1,
                        "explanation": "The end argument replaces the default trailing newline — here, with '!'.",
                    },
                ],
            },
            {
                "id": "1.3",
                "title": "Comments and Good Habits",
                "explanation": (
                    "A comment starts with # and is ignored entirely by the interpreter — it exists "
                    "only for humans reading the code. Use comments to explain *why* something is "
                    "done, not to restate what the code obviously does.\n\n"
                    "Good commenting habits matter for academic honesty too: in this course, your "
                    "comments and code should reflect your own understanding. Never copy code you "
                    "can't explain — if you can't describe what a line does in your own words, you're "
                    "not ready to turn it in."
                ),
                "examples": [
                    {
                        "code": "# Convert a temperature reading from Celsius to Fahrenheit\ncelsius = 20\nfahrenheit = celsius * 9 / 5 + 32\nprint(fahrenheit)",
                        "output": "68.0",
                        "note": "The comment explains the purpose of the calculation, not the mechanics of the math operator.",
                    }
                ],
                "practice": [
                    {
                        "id": "1.3.p1",
                        "question": "Which line is a comment in Python?",
                        "choices": [
                            '"# this explains the code"',
                            "// this explains the code",
                            "<!-- this explains the code -->",
                            "/* this explains the code */",
                        ],
                        "answer": 0,
                        "explanation": "Python comments start with a single # character.",
                    },
                    {
                        "id": "1.3.p2",
                        "question": "Why does this course care about comments and academic honesty together?",
                        "choices": [
                            "Comments are graded for length",
                            "Being able to explain your code in your own words shows genuine understanding",
                            "Comments make code run faster",
                            "They are unrelated topics",
                        ],
                        "answer": 1,
                        "explanation": "If you can explain every line yourself, your work is genuinely your own.",
                    },
                ],
            },
        ],
        "quiz": [
            {"id": "1.q1", "question": "What runs a Python script line by line?", "choices": ["A compiler", "The interpreter", "A web browser", "The file system"], "answer": 1, "explanation": "The Python interpreter executes code sequentially."},
            {"id": "1.q2", "question": 'print("A","B") outputs:', "choices": ["AB", "A B", "A, B", "A-B"], "answer": 1, "explanation": "Default separator between print() arguments is a space."},
            {"id": "1.q3", "question": "Comments in Python begin with which character?", "choices": ["//", "#", ";", "%"], "answer": 1, "explanation": "# marks the start of a comment."},
            {"id": "1.q4", "question": "What does the end= argument of print() control?", "choices": ["The separator between items", "What is printed after all arguments (default newline)", "Where the program stops", "Nothing, it's ignored"], "answer": 1, "explanation": "end= replaces the default trailing newline character."},
            {"id": "1.q5", "question": "A good reason to write a comment is to explain:", "choices": ["What print() does", "Why a non-obvious calculation is being done", "That a variable exists", "The file's size"], "answer": 1, "explanation": "Comments should clarify intent/reasoning, not restate obvious syntax."},
        ],
    },
    "2": {
        "id": "2",
        "title": "Sequential Steps, Variables, Assignment",
        "intro": "Programs run one instruction after another, in order. This module covers that "
                 "sequential flow, and how variables let a program remember values between steps.",
        "components": [
            {
                "id": "2.1",
                "title": "Sequential Execution",
                "explanation": (
                    "Unless told otherwise, Python executes statements strictly top to bottom, one "
                    "at a time. This means *order matters* — a value must exist before you use it, "
                    "and swapping the order of two lines can completely change a program's behavior."
                ),
                "examples": [
                    {
                        "code": 'print("Step 1: mixing ingredients")\nprint("Step 2: baking")\nprint("Step 3: cooling")',
                        "output": "Step 1: mixing ingredients\nStep 2: baking\nStep 3: cooling",
                        "note": "Each line runs only after the one before it finishes, in the order written.",
                    }
                ],
                "practice": [
                    {
                        "id": "2.1.p1",
                        "question": "In a normal Python script (no loops/conditionals yet), what determines execution order?",
                        "choices": ["Alphabetical order of variable names", "Top-to-bottom order in the file", "Random order", "Shortest line first"],
                        "answer": 1,
                        "explanation": "Statements execute in the order they appear, top to bottom.",
                    }
                ],
            },
            {
                "id": "2.2",
                "title": "Variables and the Assignment Operator",
                "explanation": (
                    "A variable is a name that refers to a value stored in memory. The = operator "
                    "assigns a value to a name: `x = 5` means 'store 5, and call it x'. Note this is "
                    "assignment, not mathematical equality — the right side is evaluated first, then "
                    "stored under the name on the left."
                ),
                "examples": [
                    {
                        "code": "width = 4\nheight = 6\narea = width * height\nprint(area)",
                        "output": "24",
                        "note": "width and height hold values; area is computed from them and stored under its own name.",
                    }
                ],
                "practice": [
                    {
                        "id": "2.2.p1",
                        "question": "In x = 5 + 3, what happens first?",
                        "choices": ["x is created empty", "5 + 3 is evaluated, then stored in x", "x is compared to 8", "Nothing, this is invalid syntax"],
                        "answer": 1,
                        "explanation": "The right-hand side is always evaluated before assignment happens.",
                    },
                    {
                        "id": "2.2.p2",
                        "question": "Which symbol is Python's assignment operator?",
                        "choices": ["==", ":=", "=", "<-"],
                        "answer": 2,
                        "explanation": "A single = assigns a value; == is used for comparison instead.",
                    },
                ],
            },
            {
                "id": "2.3",
                "title": "Naming Rules & Reassignment",
                "explanation": (
                    "Variable names may contain letters, digits, and underscores, but can't start "
                    "with a digit, and can't be a reserved word like `print` or `if`. Python "
                    "convention is snake_case (lowercase with underscores), e.g. `total_cost`.\n\n"
                    "Variables can be reassigned at any time — the old value is simply replaced, and "
                    "only the most recent assignment matters going forward."
                ),
                "examples": [
                    {
                        "code": "score = 10\nprint(score)\nscore = score + 5\nprint(score)",
                        "output": "10\n15",
                        "note": "score is reassigned to its old value plus 5; the old value of 10 is gone once reassigned.",
                    }
                ],
                "practice": [
                    {
                        "id": "2.3.p1",
                        "question": "Which of these is a valid Python variable name?",
                        "choices": ["2nd_place", "total-cost", "total_cost", "class"],
                        "answer": 2,
                        "explanation": "total_cost follows snake_case and doesn't start with a digit or use a reserved word.",
                    },
                    {
                        "id": "2.3.p2",
                        "question": "After x = 3 then x = x + 1, what is x?",
                        "choices": ["3", "4", "x + 1", "Error"],
                        "answer": 1,
                        "explanation": "x is reassigned to its previous value (3) plus 1, giving 4.",
                    },
                ],
            },
        ],
        "quiz": [
            {"id": "2.q1", "question": "Python statements execute:", "choices": ["Randomly", "Top to bottom, in order", "Bottom to top", "All at once"], "answer": 1, "explanation": "Sequential execution runs statements in file order."},
            {"id": "2.q2", "question": "What does total = 4 + 2 store in total?", "choices": ["The text '4 + 2'", "6", "4", "2"], "answer": 1, "explanation": "The expression is evaluated first, giving 6."},
            {"id": "2.q3", "question": "Which is NOT a valid variable name?", "choices": ["my_var", "_hidden", "3rd_try", "value2"], "answer": 2, "explanation": "Names cannot start with a digit."},
            {"id": "2.q4", "question": "If y = 10 and then y = 2, what is y afterward?", "choices": ["10", "2", "12", "Error, can't reassign"], "answer": 1, "explanation": "Reassignment replaces the old value entirely."},
            {"id": "2.q5", "question": "Python's recommended naming style (lowercase_with_underscores) is called:", "choices": ["camelCase", "PascalCase", "snake_case", "kebab-case"], "answer": 2, "explanation": "snake_case is the Python convention for variable names."},
        ],
    },
    "3": {
        "id": "3",
        "title": "Data Types, Input/Output, Basic Functions",
        "intro": "Every value in Python has a type. This module covers the core types, how to read "
                 "input from the user, and a handful of built-in functions you'll use constantly.",
        "components": [
            {
                "id": "3.1",
                "title": "Core Data Types",
                "explanation": (
                    "Python's basic built-in types include int (whole numbers), float (decimal "
                    "numbers), str (text, in quotes), and bool (True/False). Use the built-in "
                    "type() function to check what type a value is."
                ),
                "examples": [
                    {
                        "code": 'print(type(7))\nprint(type(3.14))\nprint(type("hello"))\nprint(type(True))',
                        "output": "<class 'int'>\n<class 'float'>\n<class 'str'>\n<class 'bool'>",
                        "note": "type() reports the underlying data type of any value.",
                    }
                ],
                "practice": [
                    {
                        "id": "3.1.p1",
                        "question": "What type is the value 3.0?",
                        "choices": ["int", "float", "str", "bool"],
                        "answer": 1,
                        "explanation": "Any number written with a decimal point is a float.",
                    },
                    {
                        "id": "3.1.p2",
                        "question": 'What type is "42" (with quotes)?',
                        "choices": ["int", "float", "str", "bool"],
                        "answer": 2,
                        "explanation": "Quotes make it text (a string), even though it looks numeric.",
                    },
                ],
            },
            {
                "id": "3.2",
                "title": "Getting Input from the User",
                "explanation": (
                    "The input() function pauses a program and waits for the user to type something "
                    "and press Enter. Critically, input() **always** returns a string — even if the "
                    "user types a number, you must convert it yourself using int() or float() before "
                    "doing math with it."
                ),
                "examples": [
                    {
                        "code": 'age_text = input("Enter your age: ")\nage = int(age_text)\nprint("Next year you will be", age + 1)',
                        "output": "Enter your age: 20\nNext year you will be 21",
                        "note": "The first line of output is the prompt with the simulated user typing 20; input() returned the string \"20\", which int() converted to the number 20.",
                    }
                ],
                "practice": [
                    {
                        "id": "3.2.p1",
                        "question": "What type does input() always return?",
                        "choices": ["int", "float", "str", "Whatever type the user typed"],
                        "answer": 2,
                        "explanation": "input() always returns a string, regardless of what was typed.",
                    },
                    {
                        "id": "3.2.p2",
                        "question": 'Why does age_text + 1 fail if age_text = input(...)?',
                        "choices": [
                            "input() is broken",
                            "age_text is a string, and you can't add an int directly to a string",
                            "1 is not allowed in Python",
                            "It doesn't fail",
                        ],
                        "answer": 1,
                        "explanation": "You must convert the string to a number first with int() or float().",
                    },
                ],
            },
            {
                "id": "3.3",
                "title": "Useful Built-in Functions",
                "explanation": (
                    "Python ships with many ready-to-use functions. A few you'll use right away: "
                    "len() (length of text), round() (round a number), abs() (absolute value), and "
                    "max()/min() (largest/smallest of a set of values)."
                ),
                "examples": [
                    {
                        "code": 'name = "Aggie"\nprint(len(name))\nprint(round(3.14159, 2))\nprint(abs(-7))\nprint(max(4, 9, 2))',
                        "output": "5\n3.14\n7\n9",
                        "note": "len() counts characters, round() takes an optional decimal-places argument, abs() removes the sign, max() returns the largest argument.",
                    }
                ],
                "practice": [
                    {
                        "id": "3.3.p1",
                        "question": 'What does len("python") return?',
                        "choices": ["5", "6", "7", "Error"],
                        "answer": 1,
                        "explanation": "'python' has 6 characters.",
                    },
                    {
                        "id": "3.3.p2",
                        "question": "round(2.567, 1) returns:",
                        "choices": ["2.5", "2.6", "3.0", "2.567"],
                        "answer": 1,
                        "explanation": "Rounded to 1 decimal place, 2.567 becomes 2.6.",
                    },
                ],
            },
        ],
        "quiz": [
            {"id": "3.q1", "question": "Which function tells you a value's data type?", "choices": ["kind()", "typeof()", "type()", "class()"], "answer": 2, "explanation": "type() returns a value's type."},
            {"id": "3.q2", "question": "input() always returns a:", "choices": ["int", "float", "str", "bool"], "answer": 2, "explanation": "input() returns text (a string) no matter what was typed."},
            {"id": "3.q3", "question": 'What is len("engineer")?', "choices": ["7", "8", "9", "10"], "answer": 2, "explanation": "'engineer' has 9 characters."},
            {"id": "3.q4", "question": "To use a number typed via input() in math, you should:", "choices": ["Use it directly", "Convert it with int() or float() first", "Wrap it in print()", "Nothing works, input can't be used in math"], "answer": 1, "explanation": "Convert the string to a numeric type before doing arithmetic."},
            {"id": "3.q5", "question": "abs(-12) returns:", "choices": ["-12", "12", "0", "Error"], "answer": 1, "explanation": "abs() strips the sign, returning the magnitude."},
        ],
    },
}

# ---------------------------------------------------------------------------
# Larger practice-tab question pools (distinct wording from the Learning tab)
# ---------------------------------------------------------------------------

PRACTICE_POOLS = {
    "1": [
        {"id": "1.pool.1", "question": "The Python interpreter processes a script:", "choices": ["All lines simultaneously", "One statement at a time, in order", "Starting from the last line", "Only the first line"], "answer": 1, "explanation": "Statements are executed sequentially."},
        {"id": "1.pool.2", "question": 'print("cat", "dog", sep=", ") outputs:', "choices": ["cat dog", "cat, dog", "catdog", "cat,dog"], "answer": 1, "explanation": "sep=', ' places a comma-space between arguments."},
        {"id": "1.pool.3", "question": "Which is ignored completely by the interpreter?", "choices": ["print statements", "Variable names", "Text after a # on a line", "Function calls"], "answer": 2, "explanation": "Comments (after #) are not executed."},
        {"id": "1.pool.4", "question": "What is the default value of print()'s end argument?", "choices": ["A space", "An empty string", "A newline character", "A comma"], "answer": 2, "explanation": "By default end='\\n', a newline."},
        {"id": "1.pool.5", "question": "Why should you be able to explain every line of code you submit?", "choices": ["It's required for the code to run", "It demonstrates the work is genuinely your own understanding", "Python requires explanatory comments", "It makes the code faster"], "answer": 1, "explanation": "Academic honesty means understanding, not just copying, your submitted code."},
        {"id": "1.pool.6", "question": 'How many arguments does print("a", "b", "c") receive?', "choices": ["1", "2", "3", "0"], "answer": 2, "explanation": "Three separate string arguments are passed."},
        {"id": "1.pool.7", "question": "A script that only contains comments, when run, will:", "choices": ["Print the comments", "Produce a syntax error", "Run and produce no output", "Not save"], "answer": 2, "explanation": "Comments do nothing at runtime, so no output is produced."},
        {"id": "1.pool.8", "question": "Which best defines 'programming'?", "choices": ["Designing computer hardware", "Writing exact instructions for a computer to follow", "Installing software", "Browsing the internet"], "answer": 1, "explanation": "Programming is writing precise instructions a computer executes."},
    ],
    "2": [
        {"id": "2.pool.1", "question": "total = 3; total = total * 2 leaves total as:", "choices": ["3", "6", "2", "Error"], "answer": 1, "explanation": "total is reassigned to 3*2 = 6."},
        {"id": "2.pool.2", "question": "Which statement about = in Python is true?", "choices": ["It checks equality", "It assigns the right-side value to the left-side name", "It only works with numbers", "It deletes a variable"], "answer": 1, "explanation": "= is the assignment operator."},
        {"id": "2.pool.3", "question": "Which variable name is invalid?", "choices": ["value_1", "1st_value", "_value", "value1"], "answer": 1, "explanation": "Names can't start with a digit."},
        {"id": "2.pool.4", "question": "If line 1 uses a variable defined on line 5, what happens?", "choices": ["Python looks ahead automatically", "An error occurs — the variable doesn't exist yet", "The variable defaults to 0", "Nothing, it's valid"], "answer": 1, "explanation": "Execution is sequential; a variable must be assigned before it's used."},
        {"id": "2.pool.5", "question": "x = 5\\ny = x\\nx = 9\\nWhat is y?", "choices": ["9", "5", "None", "Error"], "answer": 1, "explanation": "y copied x's value (5) at assignment time; later changes to x don't affect y."},
        {"id": "2.pool.6", "question": "Which naming style does Python convention favor for variables?", "choices": ["snake_case", "camelCase", "PascalCase", "ALLCAPS"], "answer": 0, "explanation": "snake_case (lowercase_with_underscores) is the Python convention."},
        {"id": "2.pool.7", "question": "count = 1\\ncount = count + 1\\ncount = count + 1\\nWhat is count?", "choices": ["1", "2", "3", "Error"], "answer": 2, "explanation": "count increases by 1 twice, from 1 to 3."},
        {"id": "2.pool.8", "question": "Reassigning a variable to a new value:", "choices": ["Creates a second variable with the same name", "Permanently deletes the variable", "Replaces its old value with the new one", "Causes an error"], "answer": 2, "explanation": "Assignment always overwrites the previous value."},
    ],
    "3": [
        {"id": "3.pool.1", "question": "type(10 / 2) in Python 3 is:", "choices": ["int", "float", "str", "bool"], "answer": 1, "explanation": "The / operator always produces a float, even for evenly divisible numbers."},
        {"id": "3.pool.2", "question": "What must you do before performing math on input() results?", "choices": ["Nothing", "Convert the string with int() or float()", "Wrap it in print()", "Use input() twice"], "answer": 1, "explanation": "input() returns a string; convert it to a number first."},
        {"id": "3.pool.3", "question": 'len("") returns:', "choices": ["0", "1", "None", "Error"], "answer": 0, "explanation": "An empty string has zero characters."},
        {"id": "3.pool.4", "question": "min(4, -2, 9, 0) returns:", "choices": ["4", "-2", "9", "0"], "answer": 1, "explanation": "-2 is the smallest of the given values."},
        {"id": "3.pool.5", "question": 'type(True) is:', "choices": ["int", "str", "bool", "float"], "answer": 2, "explanation": "True/False values are of type bool."},
        {"id": "3.pool.6", "question": "round(4.5) returns which type?", "choices": ["float", "int", "str", "bool"], "answer": 1, "explanation": "round() with no decimal-places argument returns an int."},
        {"id": "3.pool.7", "question": 'float("3.5") converts the string to:', "choices": ["The integer 3", "The float 3.5", "An error", "The string \"3.5\" unchanged"], "answer": 1, "explanation": "float() parses a numeric string into a float value."},
        {"id": "3.pool.8", "question": "Which function returns the absolute value of a number?", "choices": ["abs()", "len()", "round()", "type()"], "answer": 0, "explanation": "abs() strips the sign from a number."},
    ],
}

# ---------------------------------------------------------------------------
# Sandbox prompts (Pyodide runs these client-side)
# ---------------------------------------------------------------------------

SANDBOX_PROMPTS = [
    {
        "id": "1.sb.1",
        "module_id": "1",
        "title": "Print a greeting",
        "prompt": "Write code that prints exactly: Hello, PyQuest!",
        "starter_code": "",
        "expected_output": "Hello, PyQuest!",
        "mode": "match_output",
    },
    {
        "id": "1.sb.2",
        "module_id": "1",
        "title": "Free play: print() practice",
        "prompt": "Use print() however you like — try multiple arguments, sep, and end.",
        "starter_code": 'print("edit", "me")',
        "expected_output": None,
        "mode": "freeform",
    },
    {
        "id": "2.sb.1",
        "module_id": "2",
        "title": "Compute rectangle area",
        "prompt": "Create variables width = 5 and height = 3, then print their product.",
        "starter_code": "",
        "expected_output": "15",
        "mode": "match_output",
    },
    {
        "id": "2.sb.2",
        "module_id": "2",
        "title": "Free play: variables",
        "prompt": "Practice assigning and reassigning variables freely.",
        "starter_code": "x = 1\nx = x + 1\nprint(x)",
        "expected_output": None,
        "mode": "freeform",
    },
    {
        "id": "3.sb.1",
        "module_id": "3",
        "title": "Convert and greet",
        "prompt": 'Create name = "Sam" and age = "19" (as a string). Convert age to an int and print: '
                   'Sam will turn 20 next year',
        "starter_code": "",
        "expected_output": "Sam will turn 20 next year",
        "mode": "match_output",
    },
    {
        "id": "3.sb.2",
        "module_id": "3",
        "title": "Free play: built-ins",
        "prompt": "Experiment with len(), round(), abs(), max(), and min().",
        "starter_code": 'print(len("engineering"))',
        "expected_output": None,
        "mode": "freeform",
    },
]


def get_module_meta(module_id):
    for m in MODULES_META:
        if m["id"] == module_id:
            return m
    return None
