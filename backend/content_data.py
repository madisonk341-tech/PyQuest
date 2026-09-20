"""Course content: module metadata, lesson content, practice pools, sandbox prompts."""

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

MODULES_WITH_CONTENT = {str(i) for i in range(1, 14)}

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
    "4": {
        "id": "4",
        "title": "Boolean Expressions, Conditionals",
        "intro": "Programs need to make decisions. This module covers Boolean values (True/False), "
                 "the comparison and logical operators that produce them, and if/elif/else statements "
                 "that let a program take different paths depending on the data.",
        "components": [
            {
                "id": "4.1",
                "title": "Boolean Expressions & Comparisons",
                "explanation": (
                    "A Boolean expression evaluates to exactly one of two values: True or False. "
                    "Comparison operators (==, !=, <, >, <=, >=) produce Booleans, and the logical "
                    "operators and, or, and not combine them.\n\n"
                    "Watch the difference between = (assignment) and == (comparison) — this is one "
                    "of the most common beginner mistakes in any language."
                ),
                "examples": [
                    {
                        "code": "temperature = 88\nis_hot = temperature > 85\nprint(is_hot)\nprint(temperature > 100)\nprint(temperature == 88 and is_hot)",
                        "output": "True\nFalse\nTrue",
                        "note": "is_hot stores a Boolean; and requires both sides to be True for the whole expression to be True.",
                    }
                ],
                "practice": [
                    {
                        "id": "4.1.p1",
                        "question": "What does the expression 5 == 5 evaluate to?",
                        "choices": ["5", "True", "False", "Error"],
                        "answer": 1,
                        "explanation": "== compares two values and produces a Boolean; 5 equals 5, so it's True.",
                    },
                    {
                        "id": "4.1.p2",
                        "question": "What does (4 > 2) and (4 > 10) evaluate to?",
                        "choices": ["True", "False", "4", "Error"],
                        "answer": 1,
                        "explanation": "and requires both sides True; 4 > 10 is False, so the whole expression is False.",
                    },
                ],
            },
            {
                "id": "4.2",
                "title": "if / elif / else",
                "explanation": (
                    "An if statement runs a block of code only when its condition is True. elif "
                    "(\"else if\") checks another condition if the previous ones were False, and "
                    "else catches everything else. Python only runs the FIRST branch whose condition "
                    "is True, then skips the rest — order matters."
                ),
                "examples": [
                    {
                        "code": 'score = 72\nif score >= 90:\n    print("Grade: A")\nelif score >= 80:\n    print("Grade: B")\nelif score >= 70:\n    print("Grade: C")\nelse:\n    print("Grade: F")',
                        "output": "Grade: C",
                        "note": "72 fails the first two conditions but passes score >= 70, so that branch runs and the rest are skipped.",
                    }
                ],
                "practice": [
                    {
                        "id": "4.2.p1",
                        "question": "In an if/elif/else chain, how many branches can run?",
                        "choices": ["All of them", "Only the first one whose condition is True", "Only the last one", "None unless else is first"],
                        "answer": 1,
                        "explanation": "Python stops checking after the first True condition and runs only that branch.",
                    },
                    {
                        "id": "4.2.p2",
                        "question": "What does the else branch require?",
                        "choices": ["A condition of its own", "Nothing — it always runs if no earlier condition was True", "To be written first", "elif to be absent"],
                        "answer": 1,
                        "explanation": "else has no condition; it's the catch-all for when every if/elif above was False.",
                    },
                ],
            },
            {
                "id": "4.3",
                "title": "Nested and Combined Conditions",
                "explanation": (
                    "Conditionals can be nested — an if statement inside another if statement — to "
                    "check conditions only when an outer condition is already satisfied. Often, a "
                    "nested if can also be written as one condition combined with and, which is "
                    "usually easier to read."
                ),
                "examples": [
                    {
                        "code": 'age = 20\nhas_ticket = True\nif age >= 18:\n    if has_ticket:\n        print("Welcome in!")\n    else:\n        print("Buy a ticket first.")\nelse:\n    print("Must be 18 or older.")',
                        "output": "Welcome in!",
                        "note": "The inner if only runs because the outer condition (age >= 18) was already True.",
                    }
                ],
                "practice": [
                    {
                        "id": "4.3.p1",
                        "question": "Why nest an if statement inside another if?",
                        "choices": [
                            "To make the code run twice",
                            "To check a second condition only when the first is already True",
                            "It's required by Python syntax",
                            "To avoid using elif",
                        ],
                        "answer": 1,
                        "explanation": "Nesting lets the inner check depend on the outer condition already being satisfied.",
                    },
                    {
                        "id": "4.3.p2",
                        "question": "if age >= 18 and has_ticket: is most similar to which structure?",
                        "choices": [
                            "Two separate unrelated if statements",
                            "An if nested inside another if checking the same two conditions",
                            "A while loop",
                            "A function definition",
                        ],
                        "answer": 1,
                        "explanation": "Combining conditions with and is often a cleaner way to write nested ifs.",
                    },
                ],
            },
        ],
        "quiz": [
            {"id": "4.q1", "question": "Which operator checks equality (not assignment)?", "choices": ["=", "==", "!=", ":="], "answer": 1, "explanation": "== compares two values; = assigns a value."},
            {"id": "4.q2", "question": "True and False evaluates to:", "choices": ["True", "False", "None", "Error"], "answer": 1, "explanation": "and requires both sides True; here one side is False."},
            {"id": "4.q3", "question": "In an if/elif/else chain, elif conditions are checked:", "choices": ["All at once", "Only if the previous conditions were False", "Only after else", "Never"], "answer": 1, "explanation": "Each elif is only evaluated if everything above it was False."},
            {"id": "4.q4", "question": "not (5 > 3) evaluates to:", "choices": ["True", "False", "5", "3"], "answer": 1, "explanation": "5 > 3 is True; not flips it to False."},
            {"id": "4.q5", "question": "A nested if statement is:", "choices": ["An if inside another if", "An if with two conditions joined by or", "A syntax error", "The same as elif"], "answer": 0, "explanation": "Nesting means placing one if block inside another."},
        ],
    },
    "5": {
        "id": "5",
        "title": "Creating & Testing Programs, Basic Debugging",
        "intro": "Writing a working program is a process: plan what it should do, write it in small "
                 "pieces, and test it against inputs where you already know the right answer. This "
                 "module also introduces how to read Python's error messages when something goes wrong.",
        "components": [
            {
                "id": "5.1",
                "title": "The Program Development Process",
                "explanation": (
                    "Before typing code, decide what the program's inputs, outputs, and steps are. "
                    "Writing this out — even as a comment or on paper — is called planning, and it "
                    "prevents you from getting lost once the code gets more complex.\n\n"
                    "Build programs incrementally: write a few lines, run them, confirm they work, "
                    "then add more. Trying to write an entire program at once makes it much harder "
                    "to find where something went wrong."
                ),
                "examples": [
                    {
                        "code": 'radius = 3\narea = 3.14159 * radius ** 2\nprint("Area:", area)',
                        "output": "Area: 28.27431",
                        "note": "Planned steps: get the radius, apply the area formula, then display the result.",
                    }
                ],
                "practice": [
                    {
                        "id": "5.1.p1",
                        "question": "Why plan a program's steps before writing code?",
                        "choices": [
                            "Python requires a written plan to run",
                            "It clarifies inputs, outputs, and logic before things get complex",
                            "It makes the program run faster",
                            "It's not useful for short programs",
                        ],
                        "answer": 1,
                        "explanation": "Planning clarifies the problem so the code that follows has a clear direction.",
                    },
                    {
                        "id": "5.1.p2",
                        "question": "What does building a program 'incrementally' mean?",
                        "choices": [
                            "Writing the whole thing then testing once",
                            "Writing and testing small pieces before adding more",
                            "Only using integers",
                            "Writing code backwards from the output",
                        ],
                        "answer": 1,
                        "explanation": "Small, tested steps make it much easier to catch problems early.",
                    },
                ],
            },
            {
                "id": "5.2",
                "title": "Reading Error Messages",
                "explanation": (
                    "When Python can't run your code, it raises an exception and prints a traceback: "
                    "the line where it happened and the type of error. Common ones include "
                    "SyntaxError (invalid Python grammar), NameError (using a variable that doesn't "
                    "exist yet), and TypeError (using a value in a way its type doesn't support, "
                    "like adding a string to a number).\n\n"
                    "Read the LAST line of a traceback first — it names the error type and gives a "
                    "short description, which is usually the fastest way to understand what went wrong."
                ),
                "examples": [
                    {
                        "code": 'print("Testing:")\nresult = 10 / 2\nprint(result)',
                        "output": "Testing:\n5.0",
                        "note": "This one runs cleanly — but if result had been 10 / \"2\" instead, Python would raise a TypeError on that line.",
                    }
                ],
                "practice": [
                    {
                        "id": "5.2.p1",
                        "question": "Which error occurs from using a variable that was never assigned?",
                        "choices": ["SyntaxError", "NameError", "TypeError", "IndexError"],
                        "answer": 1,
                        "explanation": "NameError means Python doesn't recognize that name at all."},
                    {
                        "id": "5.2.p2",
                        "question": "When reading a traceback, which line should you check first?",
                        "choices": ["The first line", "The last line", "The middle line", "It doesn't matter"],
                        "answer": 1,
                        "explanation": "The last line names the exception type and gives the most direct explanation.",
                    },
                ],
            },
            {
                "id": "5.3",
                "title": "Basic Debugging Techniques",
                "explanation": (
                    "Debugging is finding and fixing the difference between what a program does and "
                    "what it should do. The simplest and most effective technique is adding temporary "
                    "print() statements to show a variable's value at different points, so you can "
                    "see exactly where it stops matching your expectations.\n\n"
                    "Test with inputs where you already know the correct answer. If your program "
                    "gets a simple case wrong, that's much easier to investigate than a complex one."
                ),
                "examples": [
                    {
                        "code": 'width = 4\nheight = 5\nprint("width:", width)\nprint("height:", height)\narea = width * height\nprint("area:", area)',
                        "output": "width: 4\nheight: 5\narea: 20",
                        "note": "Printing each variable along the way confirms every step before trusting the final result.",
                    }
                ],
                "practice": [
                    {
                        "id": "5.3.p1",
                        "question": "What is the simplest way to see a variable's value while a program runs?",
                        "choices": ["Guessing", "Adding a temporary print() statement", "Rewriting the whole program", "Waiting for a crash"],
                        "answer": 1,
                        "explanation": "print() debugging is quick and requires no special tools.",
                    },
                    {
                        "id": "5.3.p2",
                        "question": "Why test with inputs where you already know the answer?",
                        "choices": [
                            "It's required by Python",
                            "It makes it obvious when the program's output is wrong",
                            "It runs faster",
                            "It avoids using variables",
                        ],
                        "answer": 1,
                        "explanation": "A known expected result makes incorrect output immediately obvious.",
                    },
                ],
            },
        ],
        "quiz": [
            {"id": "5.q1", "question": "What is the first step in the program development process?", "choices": ["Writing all the code", "Planning inputs, outputs, and steps", "Submitting the assignment", "Adding comments"], "answer": 1, "explanation": "Planning comes before writing code."},
            {"id": "5.q2", "question": "Using a variable before it's ever assigned raises a:", "choices": ["SyntaxError", "NameError", "TypeError", "IndexError"], "answer": 1, "explanation": "Python doesn't recognize the name, so it raises NameError."},
            {"id": "5.q3", "question": "The most useful line of a traceback to read first is the:", "choices": ["First line", "Last line", "A random line", "Line count"], "answer": 1, "explanation": "The last line states the exception type and message directly."},
            {"id": "5.q4", "question": "Adding temporary print() statements to inspect variables is called:", "choices": ["Compiling", "print() debugging", "Refactoring", "Linting"], "answer": 1, "explanation": "This simple technique is often called print-statement debugging."},
            {"id": "5.q5", "question": "Building a program 'incrementally' means:", "choices": ["Writing it all at once", "Testing small pieces as you go", "Only using while loops", "Avoiding functions"], "answer": 1, "explanation": "Incremental development catches errors earlier by testing small steps."},
        ],
    },
    "6": {
        "id": "6",
        "title": "Loops and Iteration",
        "intro": "Loops let a program repeat steps without rewriting them. This module covers the "
                 "while loop (repeat while a condition holds), the for loop (repeat a known number "
                 "of times), and ways to control a loop's flow.",
        "components": [
            {
                "id": "6.1",
                "title": "The while Loop",
                "explanation": (
                    "A while loop repeats its body as long as its condition stays True. You must "
                    "update something inside the loop that eventually makes the condition False — "
                    "forgetting to do this creates an infinite loop that never stops."
                ),
                "examples": [
                    {
                        "code": 'count = 1\nwhile count <= 5:\n    print(count)\n    count = count + 1',
                        "output": "1\n2\n3\n4\n5",
                        "note": "count increases by 1 each time through the loop until it exceeds 5, which makes the condition False.",
                    }
                ],
                "practice": [
                    {
                        "id": "6.1.p1",
                        "question": "A while loop keeps running as long as its condition is:",
                        "choices": ["False", "True", "Zero", "A string"],
                        "answer": 1,
                        "explanation": "The loop body repeats while the condition evaluates to True.",
                    },
                    {
                        "id": "6.1.p2",
                        "question": "What causes an infinite loop in a while statement?",
                        "choices": [
                            "Using print() inside it",
                            "Never changing anything that affects the condition",
                            "Starting count at 1",
                            "Using range()",
                        ],
                        "answer": 1,
                        "explanation": "If nothing updates the condition's variables, it never becomes False.",
                    },
                ],
            },
            {
                "id": "6.2",
                "title": "The for Loop and range()",
                "explanation": (
                    "A for loop repeats once for each item in a sequence. range(n) generates numbers "
                    "0 through n-1; range(start, stop) and range(start, stop, step) give more control "
                    "over where to begin, end, and how much to count by each time."
                ),
                "examples": [
                    {
                        "code": "for i in range(5):\n    print(i)",
                        "output": "0\n1\n2\n3\n4",
                        "note": "range(5) produces 0, 1, 2, 3, 4 — five values, starting at 0 and stopping before 5.",
                    },
                    {
                        "code": "for i in range(2, 10, 2):\n    print(i)",
                        "output": "2\n4\n6\n8",
                        "note": "range(2, 10, 2) starts at 2, stops before 10, counting by 2 each time.",
                    },
                ],
                "practice": [
                    {
                        "id": "6.2.p1",
                        "question": "What does range(4) produce?",
                        "choices": ["1, 2, 3, 4", "0, 1, 2, 3", "0, 1, 2, 3, 4", "4"],
                        "answer": 1,
                        "explanation": "range(4) starts at 0 and stops before 4: 0, 1, 2, 3.",
                    },
                    {
                        "id": "6.2.p2",
                        "question": "range(1, 10, 3) produces:",
                        "choices": ["1, 4, 7", "1, 3, 6, 9", "1, 2, 3", "1, 4, 7, 10"],
                        "answer": 0,
                        "explanation": "Starting at 1, stopping before 10, counting by 3: 1, 4, 7.",
                    },
                ],
            },
            {
                "id": "6.3",
                "title": "Loop Control: break, continue, and Accumulators",
                "explanation": (
                    "break exits a loop immediately, and continue skips the rest of the current "
                    "iteration and moves to the next one. A very common loop pattern is the "
                    "accumulator: a variable (often starting at 0) that gets updated on every pass "
                    "through the loop to build up a total, count, or combined result."
                ),
                "examples": [
                    {
                        "code": "total = 0\nfor n in range(1, 6):\n    if n == 4:\n        continue\n    total = total + n\nprint(total)",
                        "output": "11",
                        "note": "continue skips adding 4, so total accumulates 1+2+3+5 = 11.",
                    }
                ],
                "practice": [
                    {
                        "id": "6.3.p1",
                        "question": "What does break do inside a loop?",
                        "choices": ["Skips to the next iteration", "Exits the loop immediately", "Restarts the loop", "Causes an error"],
                        "answer": 1,
                        "explanation": "break stops the loop entirely, right where it's called.",
                    },
                    {
                        "id": "6.3.p2",
                        "question": "An 'accumulator' variable is typically used to:",
                        "choices": [
                            "Store a single unchanging value",
                            "Build up a running total or result across loop iterations",
                            "Exit a loop early",
                            "Define a function",
                        ],
                        "answer": 1,
                        "explanation": "Accumulators collect a result (like a sum or count) as the loop progresses.",
                    },
                ],
            },
        ],
        "quiz": [
            {"id": "6.q1", "question": "A while loop repeats as long as its condition is:", "choices": ["True", "False", "0", "Undefined"], "answer": 0, "explanation": "while loops continue while their condition remains True."},
            {"id": "6.q2", "question": "range(3) produces which values?", "choices": ["1, 2, 3", "0, 1, 2", "0, 1, 2, 3", "3"], "answer": 1, "explanation": "range(3) gives 0, 1, 2 — three values starting at 0."},
            {"id": "6.q3", "question": "Which keyword skips the rest of the current loop iteration only?", "choices": ["break", "continue", "pass", "return"], "answer": 1, "explanation": "continue jumps to the next iteration without exiting the loop."},
            {"id": "6.q4", "question": "What is required to avoid an infinite while loop?", "choices": ["A print() statement", "Something inside the loop that can make the condition False", "Using range()", "Nothing, while loops always stop"], "answer": 1, "explanation": "The loop needs its condition to eventually become False."},
            {"id": "6.q5", "question": "An accumulator variable is usually initialized:", "choices": ["Inside the loop, every iteration", "Before the loop starts", "After the loop ends", "It doesn't need initializing"], "answer": 1, "explanation": "It's set to a starting value (often 0) before the loop begins, then updated inside it."},
        ],
    },
    "7": {
        "id": "7",
        "title": "Lists of Data",
        "intro": "A list stores many values together under one name. This module covers creating and "
                 "indexing lists, common list operations, and looping over a list's contents.",
        "components": [
            {
                "id": "7.1",
                "title": "Creating and Indexing Lists",
                "explanation": (
                    "A list is written with square brackets and comma-separated values: "
                    '["apple", "banana", "cherry"]. Each item has an index starting at 0, so the '
                    "first item is fruits[0], not fruits[1]. len() gives the number of items in a list."
                ),
                "examples": [
                    {
                        "code": 'fruits = ["apple", "banana", "cherry"]\nprint(fruits[0])\nprint(fruits[2])\nprint(len(fruits))',
                        "output": "apple\ncherry\n3",
                        "note": "Indexing starts at 0, so fruits[2] is the third item, 'cherry'.",
                    }
                ],
                "practice": [
                    {
                        "id": "7.1.p1",
                        "question": 'For colors = ["red", "green", "blue"], what is colors[0]?',
                        "choices": ["red", "green", "blue", "Error"],
                        "answer": 0,
                        "explanation": "List indexing starts at 0, so colors[0] is the first item.",
                    },
                    {
                        "id": "7.1.p2",
                        "question": 'For nums = [10, 20, 30, 40], what does len(nums) return?',
                        "choices": ["3", "4", "5", "40"],
                        "answer": 1,
                        "explanation": "The list has 4 items, so len() returns 4.",
                    },
                ],
            },
            {
                "id": "7.2",
                "title": "List Operations",
                "explanation": (
                    ".append(x) adds x to the end of a list. The in operator checks whether a value "
                    "exists in a list, returning a Boolean. Slicing (list[start:stop]) pulls out a "
                    "sub-section of a list, stopping before the stop index — just like range()."
                ),
                "examples": [
                    {
                        "code": 'fruits = ["apple", "banana"]\nfruits.append("cherry")\nprint(fruits)\nprint("banana" in fruits)\nprint(fruits[1:3])',
                        "output": "['apple', 'banana', 'cherry']\nTrue\n['banana', 'cherry']",
                        "note": "append() modifies the list in place; the slice [1:3] grabs indexes 1 and 2, stopping before 3.",
                    }
                ],
                "practice": [
                    {
                        "id": "7.2.p1",
                        "question": 'What does nums.append(5) do if nums = [1, 2, 3]?',
                        "choices": [
                            "Replaces the list with [5]",
                            "Adds 5 to the end, making it [1, 2, 3, 5]",
                            "Adds 5 to the beginning",
                            "Raises an error",
                        ],
                        "answer": 1,
                        "explanation": "append() always adds the new item to the end of the list.",
                    },
                    {
                        "id": "7.2.p2",
                        "question": 'For nums = [10, 20, 30, 40, 50], what is nums[1:4]?',
                        "choices": ["[10, 20, 30]", "[20, 30, 40]", "[20, 30, 40, 50]", "[1, 2, 3, 4]"],
                        "answer": 1,
                        "explanation": "The slice starts at index 1 and stops before index 4: [20, 30, 40].",
                    },
                ],
            },
            {
                "id": "7.3",
                "title": "Iterating Over Lists",
                "explanation": (
                    "A for loop can walk through every item in a list directly: for item in my_list. "
                    "This is the most common way to process every value in a list, such as summing "
                    "them up or checking each one against a condition."
                ),
                "examples": [
                    {
                        "code": 'scores = [88, 92, 79, 95]\ntotal = 0\nfor s in scores:\n    total = total + s\nprint("Average:", total / len(scores))',
                        "output": "Average: 88.5",
                        "note": "The loop visits every score once, accumulating a sum that's then divided by the count.",
                    }
                ],
                "practice": [
                    {
                        "id": "7.3.p1",
                        "question": "for item in my_list: gives you access to:",
                        "choices": ["Each item's index only", "Each item's value, one at a time", "The whole list at once, every iteration", "Nothing until the loop ends"],
                        "answer": 1,
                        "explanation": "Each pass through the loop, item holds the next value from the list.",
                    },
                    {
                        "id": "7.3.p2",
                        "question": "Why divide by len(scores) when computing an average in a loop?",
                        "choices": [
                            "To find the total number of items",
                            "To convert the sum into an average by dividing by how many values were summed",
                            "It's not necessary",
                            "To reset the accumulator",
                        ],
                        "answer": 1,
                        "explanation": "Average = total divided by count, and len() gives that count.",
                    },
                ],
            },
        ],
        "quiz": [
            {"id": "7.q1", "question": 'For nums = [5, 10, 15], what is nums[1]?', "choices": ["5", "10", "15", "1"], "answer": 1, "explanation": "Index 1 is the second item: 10."},
            {"id": "7.q2", "question": "Which method adds an item to the end of a list?", "choices": ["add()", "append()", "insert()", "push()"], "answer": 1, "explanation": "append() adds an item at the end of the list."},
            {"id": "7.q3", "question": '"x" in my_list evaluates to:', "choices": ["The index of x", "A Boolean: whether x is in the list", "A copy of the list", "An error if x is missing"], "answer": 1, "explanation": "The in operator returns True or False."},
            {"id": "7.q4", "question": 'For nums = [1, 2, 3, 4, 5], what is nums[0:2]?', "choices": ["[1, 2]", "[1, 2, 3]", "[2, 3]", "[0, 1]"], "answer": 0, "explanation": "The slice starts at index 0 and stops before index 2: [1, 2]."},
            {"id": "7.q5", "question": "for x in my_list: loops:", "choices": ["Once total", "Once for every item in the list", "A fixed 10 times", "Zero times always"], "answer": 1, "explanation": "It iterates once per item in the list."},
        ],
    },
    "8": {
        "id": "8",
        "title": "Top-Down Design; Dictionaries",
        "intro": "This module introduces top-down design — breaking a big problem into smaller "
                 "subproblems — and dictionaries, which store data as key/value pairs instead of "
                 "numbered positions.",
        "components": [
            {
                "id": "8.1",
                "title": "Top-Down Design",
                "explanation": (
                    "Top-down design means breaking a large problem into smaller, more manageable "
                    "subproblems before writing any code — for example, splitting 'analyze this data' "
                    "into 'get the input', 'do the computation', and 'display the result'. Each "
                    "subproblem can later become its own function."
                ),
                "examples": [
                    {
                        "code": 'def get_input():\n    return 40, 6\n\ndef compute_average(a, b):\n    return (a + b) / 2\n\ndef display(avg):\n    print("Average:", avg)\n\nx, y = get_input()\navg = compute_average(x, y)\ndisplay(avg)',
                        "output": "Average: 23.0",
                        "note": "Each subproblem (getting input, computing, displaying) is handled by its own small function.",
                    }
                ],
                "practice": [
                    {
                        "id": "8.1.p1",
                        "question": "Top-down design means:",
                        "choices": [
                            "Writing code from the bottom of the file upward",
                            "Breaking a big problem into smaller subproblems first",
                            "Always using loops",
                            "Avoiding functions",
                        ],
                        "answer": 1,
                        "explanation": "It's a planning approach: divide the big problem before coding the details.",
                    },
                    {
                        "id": "8.1.p2",
                        "question": "Why split a program into subproblems like get_input(), compute(), display()?",
                        "choices": [
                            "It's required by Python syntax",
                            "Each piece is easier to write, test, and understand on its own",
                            "It makes the program run faster",
                            "It avoids using variables",
                        ],
                        "answer": 1,
                        "explanation": "Smaller, focused pieces are simpler to reason about and debug individually.",
                    },
                ],
            },
            {
                "id": "8.2",
                "title": "Dictionaries: Keys and Values",
                "explanation": (
                    "A dictionary stores data as key/value pairs instead of numbered positions: "
                    '{"name": "Sam", "gpa": 3.5}. Look up a value with its key in square brackets, '
                    "like a list but indexed by a meaningful name instead of a position."
                ),
                "examples": [
                    {
                        "code": 'student = {"name": "Sam", "major": "ENGR", "gpa": 3.5}\nprint(student["name"])\nprint(student["gpa"])',
                        "output": "Sam\n3.5",
                        "note": "Each value is looked up by its key ('name', 'gpa') rather than a numeric index.",
                    }
                ],
                "practice": [
                    {
                        "id": "8.2.p1",
                        "question": 'For d = {"a": 1, "b": 2}, what does d["b"] return?',
                        "choices": ["1", "2", "b", "Error"],
                        "answer": 1,
                        "explanation": "d[\"b\"] looks up the value stored under the key 'b', which is 2.",
                    },
                    {
                        "id": "8.2.p2",
                        "question": "How is a dictionary different from a list?",
                        "choices": [
                            "It cannot store numbers",
                            "It's accessed by meaningful keys instead of numeric positions",
                            "It can only hold one value",
                            "There is no difference",
                        ],
                        "answer": 1,
                        "explanation": "Dictionaries map keys to values, rather than ordering items by position.",
                    },
                ],
            },
            {
                "id": "8.3",
                "title": "Working with Dictionaries",
                "explanation": (
                    "You can add or update a key with dict[key] = value, and loop over a dictionary's "
                    "entries with .items(). The .get(key, default) method safely looks up a key, "
                    "returning a default value instead of an error if the key doesn't exist."
                ),
                "examples": [
                    {
                        "code": 'inventory = {"bolts": 120, "screws": 75}\ninventory["nails"] = 40\ninventory["bolts"] = inventory["bolts"] - 20\nfor item, count in inventory.items():\n    print(item, ":", count)\nprint(inventory.get("washers", 0))',
                        "output": "bolts : 100\nscrews : 75\nnails : 40\n0",
                        "note": "items() gives each key/value pair; .get() returns 0 instead of an error since 'washers' isn't a key.",
                    }
                ],
                "practice": [
                    {
                        "id": "8.3.p1",
                        "question": 'What does d.get("x", 0) return if "x" is not a key in d?',
                        "choices": ["An error", "None always", "0 (the given default)", "The key 'x' itself"],
                        "answer": 2,
                        "explanation": ".get() returns the provided default instead of raising an error for a missing key.",
                    },
                    {
                        "id": "8.3.p2",
                        "question": "for key, value in d.items(): lets you access:",
                        "choices": ["Only the keys", "Only the values", "Both the key and value together each iteration", "Nothing useful"],
                        "answer": 2,
                        "explanation": ".items() yields key/value pairs together, one per iteration.",
                    },
                ],
            },
        ],
        "quiz": [
            {"id": "8.q1", "question": "Top-down design means breaking a problem into:", "choices": ["Random pieces", "Smaller subproblems before coding", "One giant function", "Comments only"], "answer": 1, "explanation": "It's a planning strategy of dividing the big problem first."},
            {"id": "8.q2", "question": 'For d = {"x": 5}, how do you access the value 5?', "choices": ["d[0]", 'd["x"]', "d.x", "d.get(0)"], "answer": 1, "explanation": "Dictionary values are accessed with their key in square brackets."},
            {"id": "8.q3", "question": "Which method safely looks up a key with a fallback default?", "choices": [".items()", ".get()", ".append()", ".keys()"], "answer": 1, "explanation": ".get(key, default) avoids an error for a missing key."},
            {"id": "8.q4", "question": 'd["new_key"] = 10 on an existing dictionary d:', "choices": ["Raises an error", "Adds a new key or updates an existing one", "Deletes d", "Does nothing"], "answer": 1, "explanation": "Assigning to a dictionary key adds it if missing, or updates it if present."},
            {"id": "8.q5", "question": ".items() is used to:", "choices": ["Delete a dictionary", "Loop over key/value pairs together", "Convert a dictionary to a list of keys only", "Sort a dictionary"], "answer": 1, "explanation": "It yields (key, value) pairs for iteration."},
        ],
    },
    "9": {
        "id": "9",
        "title": "Advanced Functions, Scope",
        "intro": "This module goes deeper into writing your own functions: parameters, return values, "
                 "default arguments, and scope — the rules for where a variable can and can't be seen.",
        "components": [
            {
                "id": "9.1",
                "title": "Parameters and Return Values",
                "explanation": (
                    "A function is defined with def name(parameters):. Parameters are placeholders "
                    "for values passed in when the function is called; return sends a value back to "
                    "wherever the function was called from. A function without return sends back None."
                ),
                "examples": [
                    {
                        "code": "def rectangle_area(width, height):\n    return width * height\n\nresult = rectangle_area(4, 5)\nprint(result)",
                        "output": "20",
                        "note": "width and height are parameters; the function returns their product, which is stored in result.",
                    }
                ],
                "practice": [
                    {
                        "id": "9.1.p1",
                        "question": "What does return do in a function?",
                        "choices": ["Prints a value to the screen", "Sends a value back to the caller", "Ends the whole program", "Restarts the function"],
                        "answer": 1,
                        "explanation": "return hands a value back to wherever the function was called.",
                    },
                    {
                        "id": "9.1.p2",
                        "question": "What does a function return if it has no return statement?",
                        "choices": ["0", '""', "None", "An error"],
                        "answer": 2,
                        "explanation": "Without an explicit return, Python functions return None by default.",
                    },
                ],
            },
            {
                "id": "9.2",
                "title": "Local vs Global Scope",
                "explanation": (
                    "A variable created inside a function is local — it only exists while that "
                    "function runs and is invisible outside it. A variable created outside all "
                    "functions is global. A local variable with the same name as a global one is a "
                    "completely separate variable; changing one doesn't affect the other."
                ),
                "examples": [
                    {
                        "code": 'def add_bonus():\n    points = 10\n    print("Inside function:", points)\n\npoints = 100\nadd_bonus()\nprint("Outside function:", points)',
                        "output": "Inside function: 10\nOutside function: 100",
                        "note": "The points inside add_bonus() is a separate local variable from the global points — changing one doesn't touch the other.",
                    }
                ],
                "practice": [
                    {
                        "id": "9.2.p1",
                        "question": "A variable created inside a function is:",
                        "choices": ["Global, visible everywhere", "Local, only visible inside that function", "Deleted immediately", "Automatically printed"],
                        "answer": 1,
                        "explanation": "Local variables exist only within the function where they're created.",
                    },
                    {
                        "id": "9.2.p2",
                        "question": "If a function has a local variable with the same name as a global one, they are:",
                        "choices": ["The exact same variable", "Two separate variables that don't affect each other", "A syntax error", "Automatically merged"],
                        "answer": 1,
                        "explanation": "The local name shadows the global one inside the function, but they remain independent.",
                    },
                ],
            },
            {
                "id": "9.3",
                "title": "Default Arguments and Multiple Return Values",
                "explanation": (
                    "A parameter can have a default value (def greet(name, title=\"Student\"):), used "
                    "only when the caller doesn't provide that argument. A function can also return "
                    "multiple values separated by commas, which the caller can unpack into separate "
                    "variables."
                ),
                "examples": [
                    {
                        "code": 'def describe(name, title="Student"):\n    return name + " is a " + title\n\nprint(describe("Sam"))\nprint(describe("Sam", "Freshman"))\n\ndef min_max(numbers):\n    return min(numbers), max(numbers)\n\nlo, hi = min_max([4, 9, 2, 7])\nprint(lo, hi)',
                        "output": "Sam is a Student\nSam is a Freshman\n2 9",
                        "note": "title defaults to 'Student' unless overridden; min_max returns two values at once, unpacked into lo and hi.",
                    }
                ],
                "practice": [
                    {
                        "id": "9.3.p1",
                        "question": "A default argument value is used when:",
                        "choices": ["Always, no matter what", "The caller doesn't provide a value for that parameter", "The function has no return", "Never"],
                        "answer": 1,
                        "explanation": "Defaults only kick in if the caller omits that argument."},
                    {
                        "id": "9.3.p2",
                        "question": "lo, hi = min_max([4, 9, 2, 7]) relies on the function:",
                        "choices": ["Printing two values", "Returning two values that get unpacked into lo and hi", "Taking two parameters", "Using a while loop"],
                        "answer": 1,
                        "explanation": "The function returns a pair of values, which Python unpacks into lo and hi.",
                    },
                ],
            },
        ],
        "quiz": [
            {"id": "9.q1", "question": "A function with no return statement returns:", "choices": ["0", "An empty string", "None", "An error"], "answer": 2, "explanation": "Python functions return None by default."},
            {"id": "9.q2", "question": "A variable defined inside a function is:", "choices": ["Global", "Local to that function", "Deleted on creation", "Always named 'x'"], "answer": 1, "explanation": "It exists only within that function's scope."},
            {"id": "9.q3", "question": "def greet(name, title=\"Student\"): — title is a:", "choices": ["Required argument", "Default argument", "Return value", "Global variable"], "answer": 1, "explanation": "It has a default value, making it optional for the caller."},
            {"id": "9.q4", "question": "return a, b from a function lets the caller:", "choices": ["Only use a", "Unpack both values into two variables", "Cause an error", "Only print the values"], "answer": 1, "explanation": "Multiple return values can be unpacked into separate variables."},
            {"id": "9.q5", "question": "A local variable with the same name as a global variable:", "choices": ["Overwrites the global permanently", "Is a separate variable inside the function", "Causes a NameError", "Is not allowed in Python"], "answer": 1, "explanation": "The local variable shadows the global one only within that function."},
        ],
    },
    "10": {
        "id": "10",
        "title": "Systematic Debugging",
        "intro": "This module builds a more structured approach to finding bugs: recognizing what "
                 "kind of error you're dealing with, tracing code by hand, and isolating the exact "
                 "line where behavior goes wrong.",
        "components": [
            {
                "id": "10.1",
                "title": "Types of Errors",
                "explanation": (
                    "Syntax errors mean Python can't even parse your code (like a missing colon) and "
                    "are caught before the program runs. Runtime errors happen while the program is "
                    "executing, like IndexError from accessing a position that doesn't exist. Logic "
                    "errors are the trickiest: the program runs fine but produces the wrong answer."
                ),
                "examples": [
                    {
                        "code": "values = [4, 8, 15, 16]\nprint(values[10])",
                        "output": "IndexError: list index out of range",
                        "note": "This is a runtime error: the code is valid Python, but index 10 doesn't exist in a 4-item list.",
                    }
                ],
                "practice": [
                    {
                        "id": "10.1.p1",
                        "question": "A program that runs without crashing but gives the wrong answer has a:",
                        "choices": ["Syntax error", "Runtime error", "Logic error", "No error at all"],
                        "answer": 2,
                        "explanation": "Logic errors don't crash the program — they just produce incorrect results."},
                    {
                        "id": "10.1.p2",
                        "question": "A missing colon after an if statement causes a:",
                        "choices": ["Logic error", "SyntaxError", "IndexError", "Nothing, it's optional"],
                        "answer": 1,
                        "explanation": "Invalid Python grammar is caught as a SyntaxError before the program runs.",
                    },
                ],
            },
            {
                "id": "10.2",
                "title": "Tracing Code by Hand",
                "explanation": (
                    "Tracing means walking through code line by line on paper (or in your head), "
                    "writing down each variable's value as it changes. This is especially useful for "
                    "loops, where it's easy to lose track of how a value evolves over each iteration."
                ),
                "examples": [
                    {
                        "code": 'total = 0\nfor n in [1, 2, 3]:\n    total += n\n    print("n =", n, "running total =", total)',
                        "output": "n = 1 running total = 1\nn = 2 running total = 3\nn = 3 running total = 6",
                        "note": "Printing the state at each step is exactly what hand-tracing captures on paper.",
                    }
                ],
                "practice": [
                    {
                        "id": "10.2.p1",
                        "question": "Tracing code by hand is most useful for understanding:",
                        "choices": ["How a program looks visually", "How variables change step by step, especially in loops", "How to write comments", "File names"],
                        "answer": 1,
                        "explanation": "Tracing tracks each variable's value across every step of execution.",
                    },
                    {
                        "id": "10.2.p2",
                        "question": "total += n is shorthand for:",
                        "choices": ["total = n", "total = total + n", "total = total - n", "n = total + n"],
                        "answer": 1,
                        "explanation": "+= adds the right-hand value to the variable and reassigns it.",
                    },
                ],
            },
            {
                "id": "10.3",
                "title": "Isolating Bugs with print() and assert",
                "explanation": (
                    "To find exactly where a bug happens, narrow it down: add print() statements at "
                    "different points until you find the first place a value is wrong. An assert "
                    "statement checks that a condition is True and stops the program immediately with "
                    "a message if it isn't — useful for catching bad values the moment they occur."
                ),
                "examples": [
                    {
                        "code": 'def half(n):\n    assert n >= 0, "n must be non-negative"\n    return n / 2\n\nprint(half(10))',
                        "output": "5.0",
                        "note": "The assert passes silently since 10 >= 0; had a negative number been passed, it would stop immediately with the given message.",
                    }
                ],
                "practice": [
                    {
                        "id": "10.3.p1",
                        "question": "What does an assert statement do when its condition is False?",
                        "choices": ["Nothing", "Stops the program with an error message", "Skips to the next line silently", "Fixes the bug automatically"],
                        "answer": 1,
                        "explanation": "A failed assert raises an AssertionError with the given message."},
                    {
                        "id": "10.3.p2",
                        "question": "Adding print() statements at different points to narrow down a bug is called:",
                        "choices": ["Compiling", "Isolating the bug", "Refactoring", "Importing"],
                        "answer": 1,
                        "explanation": "This process narrows down exactly where behavior first goes wrong."},
                ],
            },
        ],
        "quiz": [
            {"id": "10.q1", "question": "A program that crashes while running due to a bad index has a:", "choices": ["Syntax error", "Runtime error", "Logic error", "No error"], "answer": 1, "explanation": "This is a runtime error, caught as the program executes."},
            {"id": "10.q2", "question": "A program that runs fine but gives the wrong answer has a:", "choices": ["Syntax error", "Runtime error", "Logic error", "No error"], "answer": 2, "explanation": "Logic errors produce wrong results without crashing."},
            {"id": "10.q3", "question": "Tracing code by hand means:", "choices": ["Deleting code that doesn't work", "Following execution step by step, tracking variable values", "Writing comments", "Running the code faster"], "answer": 1, "explanation": "It's a manual walkthrough of how variables change over time."},
            {"id": "10.q4", "question": "assert x > 0, \"x must be positive\" does what if x is -1?", "choices": ["Nothing", "Prints x", "Stops the program with an AssertionError", "Sets x to 0"], "answer": 2, "explanation": "A failing assert raises an AssertionError immediately."},
            {"id": "10.q5", "question": "Adding print() statements to narrow down where a bug occurs is called:", "choices": ["Isolating the bug", "Compiling", "Looping", "Scoping"], "answer": 0, "explanation": "This narrows down the exact location of incorrect behavior."},
        ],
    },
    "11": {
        "id": "11",
        "title": "File Input and Output",
        "intro": "Programs often need to save data between runs or read data someone else prepared. "
                 "This module covers opening files for reading and writing, and safely closing them "
                 "with the with statement.",
        "components": [
            {
                "id": "11.1",
                "title": "Opening and Reading Files",
                "explanation": (
                    'open(filename, "w") opens a file for writing (creating it if needed, erasing '
                    'existing contents), and open(filename, "r") opens it for reading. Using with '
                    "open(...) as f: automatically closes the file when the block ends, even if an "
                    "error occurs — always prefer this over opening a file without with."
                ),
                "examples": [
                    {
                        "code": 'with open("scores.txt", "w") as f:\n    f.write("88\\n92\\n79\\n")\n\nwith open("scores.txt", "r") as f:\n    for line in f:\n        print(line.strip())',
                        "output": "88\n92\n79",
                        "note": ".strip() removes the trailing newline character each line ends with, so print() doesn't add an extra blank line.",
                    }
                ],
                "practice": [
                    {
                        "id": "11.1.p1",
                        "question": 'What does open("data.txt", "w") do if data.txt already exists with content?',
                        "choices": [
                            "Appends to the existing content",
                            "Erases the existing content and starts fresh",
                            "Refuses to open it",
                            "Reads it instead",
                        ],
                        "answer": 1,
                        "explanation": '"w" mode opens for writing and erases whatever was already in the file.',
                    },
                    {
                        "id": "11.1.p2",
                        "question": "Why use with open(...) as f: instead of just open(...)?",
                        "choices": [
                            "It's required syntax with no benefit",
                            "It automatically closes the file when done, even if an error happens",
                            "It reads faster",
                            "It only works for writing, not reading",
                        ],
                        "answer": 1,
                        "explanation": "with guarantees the file is properly closed once the block finishes.",
                    },
                ],
            },
            {
                "id": "11.2",
                "title": "Writing to Files",
                "explanation": (
                    "f.write(text) writes exactly the text given — it does not add a newline "
                    "automatically like print() does, so you usually add \\n yourself between lines. "
                    "f.read() reads an entire file's contents back as one string."
                ),
                "examples": [
                    {
                        "code": 'lines = ["Alice,90", "Bob,85"]\nwith open("students.txt", "w") as f:\n    for line in lines:\n        f.write(line + "\\n")\n\nwith open("students.txt", "r") as f:\n    contents = f.read()\nprint(contents)',
                        "output": "Alice,90\nBob,85\n",
                        "note": 'Each write() call adds its own "\\n" explicitly; f.read() then pulls the whole file back as a single string.',
                    }
                ],
                "practice": [
                    {
                        "id": "11.2.p1",
                        "question": "Does f.write() add a newline automatically like print() does?",
                        "choices": ["Yes, always", "No — you must add \\n yourself", "Only in write mode", "Only when reading"],
                        "answer": 1,
                        "explanation": "write() writes exactly what you give it, with no automatic newline.",
                    },
                    {
                        "id": "11.2.p2",
                        "question": "f.read() returns:",
                        "choices": ["Just the first line", "The entire file's contents as one string", "A list of lines", "Nothing, it's for writing only"],
                        "answer": 1,
                        "explanation": "read() with no arguments returns the whole file as a single string.",
                    },
                ],
            },
            {
                "id": "11.3",
                "title": "Working with File Data",
                "explanation": (
                    "Looping directly over an open file (for line in f:) gives one line at a time, "
                    "which is usually more memory-efficient than reading the whole file at once. Since "
                    "lines from a file include the trailing newline character, .strip() is commonly "
                    "used to remove it before using the text."
                ),
                "examples": [
                    {
                        "code": 'with open("scores.txt", "r") as f:\n    total = 0\n    count = 0\n    for line in f:\n        total = total + int(line.strip())\n        count = count + 1\nprint("Average:", total / count)',
                        "output": "Average: 86.33333333333333",
                        "note": "Each line is a string like '88\\n'; .strip() removes the newline and int() converts it to a number before adding it in.",
                    }
                ],
                "practice": [
                    {
                        "id": "11.3.p1",
                        "question": "for line in f: (where f is an open file) gives you:",
                        "choices": ["The whole file at once", "One line at a time", "Only the first line", "The file's name"],
                        "answer": 1,
                        "explanation": "Iterating over a file object yields one line per iteration.",
                    },
                    {
                        "id": "11.3.p2",
                        "question": "Why call .strip() on a line read from a file before converting it with int()?",
                        "choices": [
                            "It's not necessary",
                            "The line includes a trailing newline character that int() can't parse",
                            "strip() converts text to numbers",
                            "It closes the file",
                        ],
                        "answer": 1,
                        "explanation": "int() can't parse a string containing a newline, so strip() removes it first.",
                    },
                ],
            },
        ],
        "quiz": [
            {"id": "11.q1", "question": 'open(filename, "r") opens a file for:', "choices": ["Writing only", "Reading", "Deleting", "Renaming"], "answer": 1, "explanation": '"r" mode opens a file for reading.'},
            {"id": "11.q2", "question": "Why prefer with open(...) as f: over a plain open() call?", "choices": ["It reads faster", "It closes the file automatically, even on errors", "It's required to write files", "It prevents typos"], "answer": 1, "explanation": "The with block guarantees proper file closing."},
            {"id": "11.q3", "question": "Does f.write() add a newline automatically?", "choices": ["Yes", "No, you add \\n yourself", "Only for the first line", "Only in append mode"], "answer": 1, "explanation": "write() only writes exactly what's given."},
            {"id": "11.q4", "question": "for line in f: iterates:", "choices": ["Once for the whole file", "Once per line in the file", "Once per character", "Never"], "answer": 1, "explanation": "Each iteration yields the next line."},
            {"id": "11.q5", "question": "Why use .strip() on a line before int(line)?", "choices": ["To remove the trailing newline that would break int()", "To make the number bigger", "It's not needed", "To convert it to a list"], "answer": 0, "explanation": "int() can't parse a string with a trailing newline character."},
        ],
    },
    "12": {
        "id": "12",
        "title": "Using Engineering Modules in Python",
        "intro": "Python's standard library includes modules with ready-made functions for common "
                 "tasks. This module covers importing and using math and random, two modules "
                 "engineers use constantly.",
        "components": [
            {
                "id": "12.1",
                "title": "The math Module",
                "explanation": (
                    "import math gives access to mathematical functions and constants not built "
                    "into Python directly, like math.sqrt() (square root), math.pi, and math.ceil() "
                    "(round up to the next whole number). Access anything in the module with "
                    "math.name."
                ),
                "examples": [
                    {
                        "code": "import math\nprint(math.sqrt(64))\nprint(math.pi)\nprint(math.ceil(4.2))",
                        "output": "8.0\n3.141592653589793\n5",
                        "note": "math.pi is a precise constant; math.ceil() always rounds up to the next whole number.",
                    }
                ],
                "practice": [
                    {
                        "id": "12.1.p1",
                        "question": "What must you do before using math.sqrt()?",
                        "choices": ["Nothing, it's automatically available", "import math", "Define your own sqrt function", "Install Python again"],
                        "answer": 1,
                        "explanation": "Modules must be imported before their contents can be used.",
                    },
                    {
                        "id": "12.1.p2",
                        "question": "math.ceil(4.2) returns:",
                        "choices": ["4", "4.2", "5", "4.0"],
                        "answer": 2,
                        "explanation": "ceil() rounds up to the next whole number, regardless of the decimal portion.",
                    },
                ],
            },
            {
                "id": "12.2",
                "title": "The random Module",
                "explanation": (
                    "import random provides functions for generating randomness: random.randint(a, b) "
                    "gives a random whole number between a and b (inclusive), and random.choice(seq) "
                    "picks a random item from a sequence. random.seed(n) makes the sequence of "
                    "'random' values reproducible — useful for testing."
                ),
                "examples": [
                    {
                        "code": 'import random\nrandom.seed(42)\nprint(random.randint(1, 10))\nprint(random.choice(["rock", "paper", "scissors"]))',
                        "output": "2\nrock",
                        "note": "random.seed(42) makes this example's output reproducible every time — without a seed, values would differ each run.",
                    }
                ],
                "practice": [
                    {
                        "id": "12.2.p1",
                        "question": "random.randint(1, 6) simulates:",
                        "choices": ["A coin flip", "A single six-sided die roll", "A random word", "A fixed value of 1"],
                        "answer": 1,
                        "explanation": "It returns a random whole number from 1 to 6, inclusive — like a die roll.",
                    },
                    {
                        "id": "12.2.p2",
                        "question": "Why would a program call random.seed(42)?",
                        "choices": [
                            "To disable randomness completely",
                            "To make the 'random' sequence reproducible for testing",
                            "It's required before any random call",
                            "To generate bigger numbers",
                        ],
                        "answer": 1,
                        "explanation": "Seeding makes the same sequence of pseudo-random values repeat every run.",
                    },
                ],
            },
            {
                "id": "12.3",
                "title": "Importing Specific Names",
                "explanation": (
                    "Instead of importing a whole module, from module import name imports just the "
                    "specific functions or constants you need, letting you call them without the "
                    "module prefix. This is convenient but be careful: importing many names this way "
                    "can make it unclear where a function came from."
                ),
                "examples": [
                    {
                        "code": "from math import sqrt, pi\nprint(sqrt(25))\nprint(round(pi, 3))",
                        "output": "5.0\n3.142",
                        "note": "sqrt and pi are used directly, without the math. prefix, since they were imported by name.",
                    }
                ],
                "practice": [
                    {
                        "id": "12.3.p1",
                        "question": "After from math import sqrt, how do you call it?",
                        "choices": ["math.sqrt(x)", "sqrt(x)", "import.sqrt(x)", "sqrt.math(x)"],
                        "answer": 1,
                        "explanation": "Importing a specific name lets you call it directly, without the module prefix.",
                    },
                    {
                        "id": "12.3.p2",
                        "question": "One downside of from module import * (importing everything) is:",
                        "choices": [
                            "It's faster than normal import",
                            "It can make it unclear where a function came from",
                            "It doesn't work in Python",
                            "It only imports one function",
                        ],
                        "answer": 1,
                        "explanation": "Bringing in many names at once can create naming confusion or conflicts.",
                    },
                ],
            },
        ],
        "quiz": [
            {"id": "12.q1", "question": "Before using any function from the math module, you must:", "choices": ["Nothing special", "import math", "Restart Python", "Define it yourself"], "answer": 1, "explanation": "Modules require an import statement before use."},
            {"id": "12.q2", "question": "math.sqrt(81) returns:", "choices": ["8.0", "9.0", "81.0", "40.5"], "answer": 1, "explanation": "The square root of 81 is 9."},
            {"id": "12.q3", "question": "random.randint(1, 6) can return:", "choices": ["Only 1 or 6", "Any whole number from 1 to 6, inclusive", "Any decimal from 1 to 6", "Always the same number"], "answer": 1, "explanation": "randint is inclusive of both endpoints."},
            {"id": "12.q4", "question": "Why use random.seed()?", "choices": ["To stop the program", "To make random output reproducible", "To speed up the program", "It's required for every random call"], "answer": 1, "explanation": "Seeding fixes the sequence of pseudo-random values."},
            {"id": "12.q5", "question": "After from math import pi, which call works?", "choices": ["math.pi", "pi", "import.pi", "pi.math"], "answer": 1, "explanation": "Specific imports drop the module prefix."},
        ],
    },
    "13": {
        "id": "13",
        "title": "Functions in Top-Down / Bottom-Up Design",
        "intro": "This final module ties functions together with the design ideas from earlier in "
                 "the course: breaking a program into functions from the top down, building and "
                 "testing them from the bottom up, and combining them into a complete program.",
        "components": [
            {
                "id": "13.1",
                "title": "Top-Down Design with Functions",
                "explanation": (
                    "In top-down design, you start with the overall problem and break it into "
                    "functions before filling in their details. A main() function often calls "
                    "several helper functions in sequence, each handling one part of the problem — "
                    "making the overall structure readable at a glance."
                ),
                "examples": [
                    {
                        "code": 'def get_numbers():\n    return [3, 7, 2, 9]\n\ndef find_largest(numbers):\n    return max(numbers)\n\ndef main():\n    nums = get_numbers()\n    largest = find_largest(nums)\n    print("Largest:", largest)\n\nmain()',
                        "output": "Largest: 9",
                        "note": "main() reads like an outline of the whole program: get data, process it, show the result.",
                    }
                ],
                "practice": [
                    {
                        "id": "13.1.p1",
                        "question": "In top-down design, what typically calls the helper functions?",
                        "choices": ["Nothing, they call themselves", "A main() function that outlines the overall steps", "The Python interpreter automatically", "Only loops"],
                        "answer": 1,
                        "explanation": "main() usually ties the helper functions together in the right order.",
                    },
                    {
                        "id": "13.1.p2",
                        "question": "A benefit of splitting a program into functions like get_numbers() and find_largest() is:",
                        "choices": [
                            "The program runs in a random order",
                            "Each function can be understood, tested, and reused on its own",
                            "It's required syntax",
                            "It removes the need for variables",
                        ],
                        "answer": 1,
                        "explanation": "Small, focused functions are easier to read, test, and reuse.",
                    },
                ],
            },
            {
                "id": "13.2",
                "title": "Bottom-Up Design and Testing",
                "explanation": (
                    "Bottom-up design means building and testing small, individual functions first, "
                    "then combining them into a larger program once each piece works correctly. "
                    "Testing a function by itself — calling it directly with known inputs and "
                    "checking the output — catches problems before they get buried inside a bigger program."
                ),
                "examples": [
                    {
                        "code": "def celsius_to_fahrenheit(c):\n    return c * 9 / 5 + 32\n\nprint(celsius_to_fahrenheit(0))\nprint(celsius_to_fahrenheit(100))",
                        "output": "32.0\n212.0",
                        "note": "Testing the conversion function directly with known values (0°C = 32°F, 100°C = 212°F) confirms it works before using it elsewhere.",
                    }
                ],
                "practice": [
                    {
                        "id": "13.2.p1",
                        "question": "Bottom-up design means:",
                        "choices": [
                            "Writing the whole program before testing anything",
                            "Building and testing small functions individually before combining them",
                            "Only writing while loops",
                            "Skipping the planning stage",
                        ],
                        "answer": 1,
                        "explanation": "Each piece is verified on its own before being assembled into the full program.",
                    },
                    {
                        "id": "13.2.p2",
                        "question": "Why test celsius_to_fahrenheit(0) specifically?",
                        "choices": [
                            "It's a random choice",
                            "0°C has a well-known correct answer (32°F), making errors obvious",
                            "It's the only input Python allows",
                            "It avoids using functions",
                        ],
                        "answer": 1,
                        "explanation": "Known correct answers make it immediately obvious if a function is wrong.",
                    },
                ],
            },
            {
                "id": "13.3",
                "title": "Combining Functions into a Complete Program",
                "explanation": (
                    "Once individual functions are written and tested, top-down and bottom-up meet "
                    "in the middle: the tested functions are combined under a main() that calls them "
                    "in the right order, producing a complete, working program built from "
                    "well-understood pieces."
                ),
                "examples": [
                    {
                        "code": 'def celsius_to_fahrenheit(c):\n    return c * 9 / 5 + 32\n\ndef describe_temp(f):\n    if f >= 90:\n        return "hot"\n    elif f >= 60:\n        return "mild"\n    else:\n        return "cold"\n\ndef main():\n    c = 30\n    f = celsius_to_fahrenheit(c)\n    print(f, "degrees F is", describe_temp(f))\n\nmain()',
                        "output": "86.0 degrees F is mild",
                        "note": "Two independently-tested functions (conversion and classification) are combined inside main() to produce the final program.",
                    }
                ],
                "practice": [
                    {
                        "id": "13.3.p1",
                        "question": "Combining tested functions under a main() is an example of:",
                        "choices": ["A syntax error", "Bringing top-down structure and bottom-up tested pieces together", "Avoiding functions entirely", "Deleting unused code"],
                        "answer": 1,
                        "explanation": "The overall structure (top-down) is filled in with pieces already verified individually (bottom-up)."},
                    {
                        "id": "13.3.p2",
                        "question": "Why test each function individually before combining them?",
                        "choices": [
                            "It's not necessary if the final program works",
                            "Bugs are much easier to find in a small, isolated function than in a large combined program",
                            "Python requires it",
                            "It makes the program run faster",
                        ],
                        "answer": 1,
                        "explanation": "Isolated testing narrows down exactly where a bug could be, before complexity is added.",
                    },
                ],
            },
        ],
        "quiz": [
            {"id": "13.q1", "question": "In top-down design, main() typically:", "choices": ["Contains all the program's logic directly", "Calls helper functions in the right order", "Is never used", "Only holds variables"], "answer": 1, "explanation": "main() outlines the overall program by calling other functions."},
            {"id": "13.q2", "question": "Bottom-up design focuses on:", "choices": ["Writing the whole program at once", "Testing small functions individually before combining them", "Avoiding functions", "Writing comments only"], "answer": 1, "explanation": "Each function is verified on its own first."},
            {"id": "13.q3", "question": "Why test a function like celsius_to_fahrenheit(0) with a known answer?", "choices": ["It's required by Python", "A known correct answer makes bugs obvious", "It runs faster", "It replaces the need for main()"], "answer": 1, "explanation": "Known expected results make incorrect behavior immediately visible."},
            {"id": "13.q4", "question": "Combining top-down and bottom-up design means:", "choices": ["Picking only one approach", "Planning the overall structure while building/testing pieces individually", "Avoiding planning entirely", "Only using while loops"], "answer": 1, "explanation": "The two approaches meet: overall structure from top-down, verified pieces from bottom-up."},
            {"id": "13.q5", "question": "A key benefit of splitting a program into small, tested functions is:", "choices": ["It's required syntax", "Bugs are easier to isolate in small, focused pieces", "It removes the need for a main() function", "It disables error messages"], "answer": 1, "explanation": "Small, tested functions make debugging far more manageable."},
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
        {"id": "2.pool.5", "question": "x = 5\ny = x\nx = 9\nWhat is y?", "choices": ["9", "5", "None", "Error"], "answer": 1, "explanation": "y copied x's value (5) at assignment time; later changes to x don't affect y."},
        {"id": "2.pool.6", "question": "Which naming style does Python convention favor for variables?", "choices": ["snake_case", "camelCase", "PascalCase", "ALLCAPS"], "answer": 0, "explanation": "snake_case (lowercase_with_underscores) is the Python convention."},
        {"id": "2.pool.7", "question": "count = 1\ncount = count + 1\ncount = count + 1\nWhat is count?", "choices": ["1", "2", "3", "Error"], "answer": 2, "explanation": "count increases by 1 twice, from 1 to 3."},
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
    "4": [
        {"id": "4.pool.1", "question": "5 != 5 evaluates to:", "choices": ["True", "False", "5", "Error"], "answer": 1, "explanation": "!= means 'not equal'; 5 equals 5, so this is False."},
        {"id": "4.pool.2", "question": "(3 > 1) or (3 > 100) evaluates to:", "choices": ["True", "False", "3", "100"], "answer": 0, "explanation": "or only needs one side True; 3 > 1 is True."},
        {"id": "4.pool.3", "question": "In an if/elif chain, once one branch's condition is True:", "choices": ["Every remaining elif/else is skipped", "All branches still run", "The program stops entirely", "Python raises an error"], "answer": 0, "explanation": "Only the first matching branch runs; the rest are skipped."},
        {"id": "4.pool.4", "question": "Which symbol is used for 'not equal to' in Python?", "choices": ["<>", "!=", "=/=", "~="], "answer": 1, "explanation": "!= is Python's inequality operator."},
        {"id": "4.pool.5", "question": "An else clause runs when:", "choices": ["Its own condition is True", "No earlier if/elif condition was True", "It's placed first", "Never, it's optional syntax only"], "answer": 1, "explanation": "else has no condition of its own — it's the fallback."},
        {"id": "4.pool.6", "question": "not True evaluates to:", "choices": ["True", "False", "None", "1"], "answer": 1, "explanation": "not flips a Boolean value."},
        {"id": "4.pool.7", "question": "Nesting a conditional inside another if is useful when:", "choices": ["You want to check a second condition only after the first is satisfied", "You want to skip all conditions", "Python requires it for every if", "It replaces loops"], "answer": 0, "explanation": "Nested ifs check further conditions only within an already-true outer branch."},
        {"id": "4.pool.8", "question": "if 10 > 5: print(\"yes\") — what prints?", "choices": ["Nothing", "yes", "10 > 5", "An error"], "answer": 1, "explanation": "10 > 5 is True, so the if block runs and prints 'yes'."},
    ],
    "5": [
        {"id": "5.pool.1", "question": "Planning a program's inputs and outputs before coding is part of:", "choices": ["Debugging", "The development process", "Compiling", "Looping"], "answer": 1, "explanation": "Planning is an early step in developing a working program."},
        {"id": "5.pool.2", "question": "Which error type means Python's grammar rules were violated?", "choices": ["SyntaxError", "NameError", "TypeError", "Logic error"], "answer": 0, "explanation": "SyntaxError is raised before the program even runs, for invalid Python code."},
        {"id": "5.pool.3", "question": "Adding a string and a number directly (e.g. \"5\" + 3) raises a:", "choices": ["SyntaxError", "NameError", "TypeError", "IndexError"], "answer": 2, "explanation": "TypeError occurs when an operation isn't supported between those types."},
        {"id": "5.pool.4", "question": "Building a program in small, tested steps is called developing it:", "choices": ["Randomly", "Incrementally", "Backwards", "Silently"], "answer": 1, "explanation": "Incremental development tests small pieces before adding more."},
        {"id": "5.pool.5", "question": "The fastest way to inspect a variable's value while a program runs is to:", "choices": ["Guess based on the code", "Add a temporary print() statement", "Rewrite the function", "Wait for a crash"], "answer": 1, "explanation": "print() debugging shows a variable's actual value immediately."},
        {"id": "5.pool.6", "question": "A traceback's last line typically tells you:", "choices": ["The file's total line count", "The exception type and a short description", "The programmer's name", "Nothing useful"], "answer": 1, "explanation": "The final line names the error and briefly explains it."},
        {"id": "5.pool.7", "question": "Testing with an input where you already know the correct answer helps because:", "choices": ["It's required by Python", "Wrong output becomes immediately obvious", "It makes the program run faster", "It avoids using variables"], "answer": 1, "explanation": "A known expected result makes incorrect behavior easy to spot."},
        {"id": "5.pool.8", "question": "Which of these is a logic error, not a crash?", "choices": ["Using an undefined variable", "A program that runs but calculates the wrong average", "Missing a colon after if", "Indexing past the end of a list"], "answer": 1, "explanation": "Logic errors produce wrong results while still running successfully."},
    ],
    "6": [
        {"id": "6.pool.1", "question": "A while loop stops repeating when its condition becomes:", "choices": ["True", "False", "Zero", "Undefined"], "answer": 1, "explanation": "The loop exits once the condition evaluates to False."},
        {"id": "6.pool.2", "question": "range(0, 6, 2) produces:", "choices": ["0, 2, 4", "0, 2, 4, 6", "0, 1, 2, 3, 4, 5", "2, 4, 6"], "answer": 0, "explanation": "Starting at 0, stopping before 6, counting by 2: 0, 2, 4."},
        {"id": "6.pool.3", "question": "Which statement immediately exits the nearest enclosing loop?", "choices": ["continue", "break", "return", "pass"], "answer": 1, "explanation": "break stops the loop entirely."},
        {"id": "6.pool.4", "question": "An infinite loop happens when:", "choices": ["A for loop is used instead of while", "Nothing inside the loop ever makes the condition False", "print() is missing", "range() is used"], "answer": 1, "explanation": "The loop needs a path to eventually make its condition False."},
        {"id": "6.pool.5", "question": "total = total + n inside a loop is an example of:", "choices": ["A conditional", "An accumulator pattern", "A function definition", "A syntax error"], "answer": 1, "explanation": "This pattern builds up a running total across iterations."},
        {"id": "6.pool.6", "question": "for x in range(3): print(x) outputs:", "choices": ["1 2 3", "0 1 2", "0 1 2 3", "3"], "answer": 1, "explanation": "range(3) yields 0, 1, 2."},
        {"id": "6.pool.7", "question": "continue inside a loop:", "choices": ["Exits the loop completely", "Skips the rest of the current iteration and moves to the next", "Restarts the whole program", "Is identical to break"], "answer": 1, "explanation": "continue jumps ahead to the next iteration without leaving the loop."},
        {"id": "6.pool.8", "question": "A while loop is generally preferred over a for loop when:", "choices": ["The exact number of repetitions isn't known ahead of time", "You're looping over a list", "You never need a condition", "Python requires it for counting"], "answer": 0, "explanation": "while loops fit naturally when repetition depends on a condition rather than a fixed count."},
    ],
    "7": [
        {"id": "7.pool.1", "question": 'For letters = ["a", "b", "c", "d"], what is letters[3]?', "choices": ["c", "d", "3", "Error"], "answer": 1, "explanation": "Index 3 is the fourth item: 'd'."},
        {"id": "7.pool.2", "question": "Which operator checks whether a value exists in a list?", "choices": ["==", "in", "is", "has"], "answer": 1, "explanation": "in returns True or False depending on membership."},
        {"id": "7.pool.3", "question": 'For nums = [1, 2, 3], what does nums.append(4) change nums to?', "choices": ["[4, 1, 2, 3]", "[1, 2, 3, 4]", "[1, 2, 3]", "Error"], "answer": 1, "explanation": "append() adds the new value to the end of the list."},
        {"id": "7.pool.4", "question": 'For letters = ["a","b","c","d","e"], what is letters[2:4]?', "choices": ["['c', 'd']", "['b', 'c', 'd']", "['c', 'd', 'e']", "['a', 'b']"], "answer": 0, "explanation": "The slice starts at index 2 and stops before index 4."},
        {"id": "7.pool.5", "question": "for item in my_list: assigns item to:", "choices": ["The whole list every time", "One element per iteration", "Only the last element", "The list's length"], "answer": 1, "explanation": "Each iteration gives the next single element of the list."},
        {"id": "7.pool.6", "question": "len([]) (an empty list) returns:", "choices": ["0", "1", "None", "Error"], "answer": 0, "explanation": "An empty list has zero elements."},
        {"id": "7.pool.7", "question": "To compute an average of a list of numbers, you typically:", "choices": ["Multiply all the numbers together", "Sum them and divide by len() of the list", "Use only the first number", "Sort the list"], "answer": 1, "explanation": "Average = sum of values divided by how many there are."},
        {"id": "7.pool.8", "question": 'What does "z" in ["x", "y"] evaluate to?', "choices": ["True", "False", "z", "Error"], "answer": 1, "explanation": "'z' is not one of the list's elements, so in returns False."},
    ],
    "8": [
        {"id": "8.pool.1", "question": "Breaking a large problem into smaller subproblems before coding describes:", "choices": ["Bottom-up testing", "Top-down design", "Debugging", "Looping"], "answer": 1, "explanation": "Top-down design divides a big problem into manageable pieces first."},
        {"id": "8.pool.2", "question": 'For d = {"a": 1, "b": 2, "c": 3}, what does d["c"] return?', "choices": ["1", "2", "3", "c"], "answer": 2, "explanation": "The key 'c' maps to the value 3."},
        {"id": "8.pool.3", "question": "Which best describes a dictionary compared to a list?", "choices": ["Both are indexed only by position", "A dictionary is indexed by keys, not numeric position", "A dictionary can't store strings", "There's no difference"], "answer": 1, "explanation": "Dictionaries map keys to values rather than using positional indexing."},
        {"id": "8.pool.4", "question": 'd["new"] = 5 on a dictionary that has no "new" key:', "choices": ["Raises an error", "Adds a new key/value pair", "Deletes the dictionary", "Does nothing"], "answer": 1, "explanation": "Assigning to a new key adds it to the dictionary."},
        {"id": "8.pool.5", "question": 'd.get("missing", -1) if "missing" is not a key returns:', "choices": ["An error", "None", "-1", "missing"], "answer": 2, "explanation": ".get() returns the provided default instead of raising an error."},
        {"id": "8.pool.6", "question": "for k, v in d.items(): gives access to:", "choices": ["Only keys", "Only values", "Both key and value per iteration", "The dictionary's length"], "answer": 2, "explanation": ".items() yields key/value pairs together."},
        {"id": "8.pool.7", "question": "A function like get_input() that handles one small piece of a bigger problem reflects:", "choices": ["Bottom-up chaos", "Top-down design broken into subproblems", "A syntax requirement", "An error-handling technique"], "answer": 1, "explanation": "Each function tackles one subproblem identified during top-down design."},
        {"id": "8.pool.8", "question": 'Which syntax creates an empty dictionary?', "choices": ["[]", "()", "{}", "\"\""], "answer": 2, "explanation": "Curly braces with nothing inside create an empty dictionary."},
    ],
    "9": [
        {"id": "9.pool.1", "question": "A function with no explicit return statement returns:", "choices": ["0", "An empty string", "None", "The last variable used"], "answer": 2, "explanation": "Python functions return None by default."},
        {"id": "9.pool.2", "question": "A variable assigned inside a function, with no matching global name, is:", "choices": ["Visible everywhere in the program", "Local to that function only", "Automatically printed", "A syntax error"], "answer": 1, "explanation": "It only exists within that function's local scope."},
        {"id": "9.pool.3", "question": "def f(x, y=10): — calling f(5) uses which value for y?", "choices": ["5", "10", "None", "Error, y is required"], "answer": 1, "explanation": "y falls back to its default value of 10 since no second argument was given."},
        {"id": "9.pool.4", "question": "return a, b allows the caller to write:", "choices": ["x = a, b (with no unpacking possible)", "x, y = f(...) to get both values separately", "Only one variable can ever be used", "This causes a syntax error"], "answer": 1, "explanation": "Multiple return values can be unpacked into separate variables."},
        {"id": "9.pool.5", "question": "A parameter is best described as:", "choices": ["A global variable", "A placeholder for a value passed into a function", "The function's return value", "A type of loop"], "answer": 1, "explanation": "Parameters receive whatever values are passed in when the function is called."},
        {"id": "9.pool.6", "question": "Changing a local variable inside a function:", "choices": ["Always changes a global variable with the same name", "Only affects that local variable, unless declared global", "Is not allowed in Python", "Deletes the function"], "answer": 1, "explanation": "Local variables are independent from global ones unless explicitly declared global."},
        {"id": "9.pool.7", "question": "def greet(name, greeting=\"Hello\"): greeting is called a:", "choices": ["Required argument", "Default argument", "Global variable", "Return value"], "answer": 1, "explanation": "It has a default value used only if the caller omits it."},
        {"id": "9.pool.8", "question": "Why use functions with parameters instead of hardcoding values?", "choices": ["Parameters make code slower", "The same function can be reused with different inputs", "It's required by Python syntax", "It disables return values"], "answer": 1, "explanation": "Parameters let one function definition work for many different inputs."},
    ],
    "10": [
        {"id": "10.pool.1", "question": "A program that crashes because of invalid Python grammar has a:", "choices": ["Logic error", "Syntax error", "Runtime error", "No error"], "answer": 1, "explanation": "Syntax errors are caught before the program can even run."},
        {"id": "10.pool.2", "question": "A program that runs to completion but produces an incorrect result has a:", "choices": ["Syntax error", "Runtime error", "Logic error", "No error"], "answer": 2, "explanation": "Logic errors don't crash the program; they just give wrong output."},
        {"id": "10.pool.3", "question": "Tracing code by hand is especially useful for understanding:", "choices": ["File names", "How variable values evolve through a loop", "Comment formatting", "Import statements"], "answer": 1, "explanation": "It tracks each variable's value step by step, which is most valuable in loops."},
        {"id": "10.pool.4", "question": "assert x != 0, \"x cannot be zero\" does what if x is 0?", "choices": ["Nothing", "Prints a warning but continues", "Stops the program with an AssertionError", "Sets x to 1"], "answer": 2, "explanation": "A failing assert raises an AssertionError immediately, halting the program."},
        {"id": "10.pool.5", "question": "Adding print() statements at several points to find exactly where a bug starts is called:", "choices": ["Compiling", "Isolating the bug", "Importing", "Formatting"], "answer": 1, "explanation": "This narrows down the precise location where behavior first goes wrong."},
        {"id": "10.pool.6", "question": "Accessing index 5 of a 3-item list raises a(n):", "choices": ["SyntaxError", "IndexError", "Logic error only", "NameError"], "answer": 1, "explanation": "This is a runtime error: valid code, but an out-of-range index."},
        {"id": "10.pool.7", "question": "total += n is equivalent to:", "choices": ["total = n", "total = total + n", "n = total", "total == total + n"], "answer": 1, "explanation": "+= adds to the variable and reassigns the result to it."},
        {"id": "10.pool.8", "question": "Systematic debugging generally starts with:", "choices": ["Rewriting the entire program", "Identifying what type of error you're dealing with", "Ignoring the error message", "Deleting the code that failed"], "answer": 1, "explanation": "Knowing whether it's a syntax, runtime, or logic error shapes how you investigate it."},
    ],
    "11": [
        {"id": "11.pool.1", "question": 'open("log.txt", "w") on a file that already has content will:', "choices": ["Append new content to the end", "Erase the old content and start fresh", "Refuse to open", "Only allow reading"], "answer": 1, "explanation": '"w" mode always starts the file empty.'},
        {"id": "11.pool.2", "question": "The main benefit of with open(...) as f: is that it:", "choices": ["Reads files faster", "Closes the file automatically, even if an error occurs", "Is the only way to open a file", "Prevents typos in the filename"], "answer": 1, "explanation": "with guarantees proper cleanup of the file handle."},
        {"id": "11.pool.3", "question": "Does f.write(\"hello\") add a newline after 'hello'?", "choices": ["Yes, always", "No, you must add \\n yourself", "Only in read mode", "Only the first time"], "answer": 1, "explanation": "write() writes exactly the given text, with no automatic newline."},
        {"id": "11.pool.4", "question": "f.read() with no arguments returns:", "choices": ["Just the first character", "The entire file's contents as one string", "A list of lines", "Nothing"], "answer": 1, "explanation": "It reads the whole file into a single string."},
        {"id": "11.pool.5", "question": "for line in f: (f is an open file) yields:", "choices": ["The whole file at once", "One line per iteration", "Only the last line", "The file size"], "answer": 1, "explanation": "Iterating over a file gives one line per pass."},
        {"id": "11.pool.6", "question": "Why is .strip() commonly used on lines read from a file?", "choices": ["To make the text uppercase", "To remove the trailing newline character", "To convert it to a number automatically", "It's not commonly used"], "answer": 1, "explanation": "Lines from a file include a trailing \\n that strip() removes."},
        {"id": "11.pool.7", "question": 'open("data.txt", "r") on a file that does not exist will:', "choices": ["Create an empty file", "Raise an error (FileNotFoundError)", "Return None silently", "Open an unrelated file"], "answer": 1, "explanation": "Reading a nonexistent file raises FileNotFoundError."},
        {"id": "11.pool.8", "question": "What must you convert a line to before doing math with a number stored in a text file?", "choices": ["Nothing, it's already a number", "int() or float()", "list()", "dict()"], "answer": 1, "explanation": "Lines read from a file are strings and must be converted to a numeric type first."},
    ],
    "12": [
        {"id": "12.pool.1", "question": "Which statement makes math.sqrt() available for use?", "choices": ["No statement needed", "import math", "def math():", "from python import math"], "answer": 1, "explanation": "You must import a module before using its contents."},
        {"id": "12.pool.2", "question": "math.ceil(7.1) returns:", "choices": ["7", "7.1", "8", "7.0"], "answer": 2, "explanation": "ceil() always rounds up to the next whole number."},
        {"id": "12.pool.3", "question": "random.randint(5, 5) can return:", "choices": ["Only 5", "Any number from 0 to 5", "An error", "A random float"], "answer": 0, "explanation": "With matching bounds, the only possible value is 5."},
        {"id": "12.pool.4", "question": "random.seed(1) is typically used to:", "choices": ["Disable all randomness permanently", "Make random results reproducible across runs", "Generate larger random numbers", "Import the random module"], "answer": 1, "explanation": "Seeding fixes the sequence so the same 'random' values repeat."},
        {"id": "12.pool.5", "question": "After from math import pi, sqrt, which call is valid?", "choices": ["math.pi", "pi and sqrt(x) directly, without the math prefix", "import.pi", "pi.sqrt()"], "answer": 1, "explanation": "Names imported individually drop the module prefix."},
        {"id": "12.pool.6", "question": "random.choice([1, 2, 3]) returns:", "choices": ["Always 1", "A random element from the list", "The list's length", "None"], "answer": 1, "explanation": "choice() picks one random element from the given sequence."},
        {"id": "12.pool.7", "question": "math.pi is best described as:", "choices": ["A function you must call with ()", "A constant value you can use directly", "A random number generator", "A type of loop"], "answer": 1, "explanation": "pi is a constant attribute of the math module, not a function."},
        {"id": "12.pool.8", "question": "Why might a program import only specific names instead of the whole module?", "choices": ["It's the only way Python allows imports", "To use shorter names without the module prefix", "It disables the module", "It's required for math but not random"], "answer": 1, "explanation": "from module import name lets you skip the module prefix when calling it."},
    ],
    "13": [
        {"id": "13.pool.1", "question": "In top-down design, main() usually:", "choices": ["Does all the detailed work itself", "Calls helper functions in the right sequence", "Is never necessary", "Replaces all variables"], "answer": 1, "explanation": "main() typically outlines the program by calling other functions in order."},
        {"id": "13.pool.2", "question": "Bottom-up design emphasizes:", "choices": ["Writing the entire program before running any of it", "Testing individual functions before combining them", "Never using functions", "Skipping the planning stage"], "answer": 1, "explanation": "Each function is verified in isolation first."},
        {"id": "13.pool.3", "question": "Testing a function like celsius_to_fahrenheit(100) and expecting 212.0 is useful because:", "choices": ["100 is a random number", "It's a known correct answer, so wrong output is obvious", "It avoids using return", "Python requires this specific test"], "answer": 1, "explanation": "A known expected result makes bugs immediately visible."},
        {"id": "13.pool.4", "question": "Combining top-down and bottom-up approaches means:", "choices": ["Choosing one and ignoring the other", "Planning overall structure while testing pieces individually", "Never testing until the very end", "Avoiding functions entirely"], "answer": 1, "explanation": "The two approaches complement each other: structure from the top, verified pieces from the bottom."},
        {"id": "13.pool.5", "question": "A key reason to split a program into small functions is:", "choices": ["Python requires at least 3 functions", "Bugs are far easier to isolate in small, focused pieces", "It disables error messages", "It removes the need for a main() function"], "answer": 1, "explanation": "Smaller functions are simpler to test and debug individually."},
        {"id": "13.pool.6", "question": "Which function structure best reflects top-down thinking?", "choices": ["One giant function with everything inline", "main() calling get_data(), process(), and display()", "No functions at all", "A single while loop with no functions"], "answer": 1, "explanation": "Splitting responsibilities into named functions mirrors the top-down breakdown."},
        {"id": "13.pool.7", "question": "Why test find_largest([3, 7, 2]) and expect 7 before using it elsewhere?", "choices": ["It's not useful", "It confirms the function works correctly in isolation first", "Testing is only needed for main()", "It changes the function's return type"], "answer": 1, "explanation": "Isolated testing catches bugs before they're buried inside a larger program."},
        {"id": "13.pool.8", "question": "A complete program built from top-down and bottom-up design typically ends with:", "choices": ["No functions at all", "Tested functions combined under a main() that runs them in order", "A single print() statement", "Removing all functions before submission"], "answer": 1, "explanation": "The final program assembles verified functions into a coherent whole."},
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
    {
        "id": "4.sb.1",
        "module_id": "4",
        "title": "Classify an age",
        "prompt": "Set age = 15, then print exactly Minor if age is under 18, otherwise print Adult.",
        "starter_code": "",
        "expected_output": "Minor",
        "mode": "match_output",
    },
    {
        "id": "4.sb.2",
        "module_id": "4",
        "title": "Free play: conditionals",
        "prompt": "Experiment with if / elif / else and comparison operators.",
        "starter_code": 'x = 7\nif x > 5:\n    print("big")',
        "expected_output": None,
        "mode": "freeform",
    },
    {
        "id": "5.sb.1",
        "module_id": "5",
        "title": "Fix the bug: rectangle area",
        "prompt": "This should print the area of a 4x6 rectangle (24), but it has a bug — fix it.",
        "starter_code": "width = 4\nheight = 6\nprint(width + height)",
        "expected_output": "24",
        "mode": "match_output",
    },
    {
        "id": "5.sb.2",
        "module_id": "5",
        "title": "Free play: debugging",
        "prompt": "Practice reading output and error messages by experimenting freely.",
        "starter_code": "print(10 / 3)",
        "expected_output": None,
        "mode": "freeform",
    },
    {
        "id": "6.sb.1",
        "module_id": "6",
        "title": "Count from 1 to 5",
        "prompt": "Use a loop to print the numbers 1 through 5, each on its own line.",
        "starter_code": "",
        "expected_output": "1\n2\n3\n4\n5",
        "mode": "match_output",
    },
    {
        "id": "6.sb.2",
        "module_id": "6",
        "title": "Free play: loops",
        "prompt": "Experiment with while, for, range(), break, and continue.",
        "starter_code": "for i in range(3):\n    print(i * i)",
        "expected_output": None,
        "mode": "freeform",
    },
    {
        "id": "7.sb.1",
        "module_id": "7",
        "title": "Sum a list",
        "prompt": "Create a list containing 10, 20, and 30, then print their sum.",
        "starter_code": "",
        "expected_output": "60",
        "mode": "match_output",
    },
    {
        "id": "7.sb.2",
        "module_id": "7",
        "title": "Free play: lists",
        "prompt": "Experiment with append(), slicing, in, and looping over a list.",
        "starter_code": 'fruits = ["apple", "banana", "cherry"]\nprint(fruits)',
        "expected_output": None,
        "mode": "freeform",
    },
    {
        "id": "8.sb.1",
        "module_id": "8",
        "title": "Look up a dictionary value",
        "prompt": 'Create a dictionary with a "score" key set to 95, then print just that value.',
        "starter_code": "",
        "expected_output": "95",
        "mode": "match_output",
    },
    {
        "id": "8.sb.2",
        "module_id": "8",
        "title": "Free play: dictionaries",
        "prompt": "Experiment with creating, updating, and looping over a dictionary.",
        "starter_code": 'car = {"make": "Toyota", "year": 2020}\nprint(car)',
        "expected_output": None,
        "mode": "freeform",
    },
    {
        "id": "9.sb.1",
        "module_id": "9",
        "title": "Write a double() function",
        "prompt": "Write a function double(n) that returns n * 2, then print double(21).",
        "starter_code": "",
        "expected_output": "42",
        "mode": "match_output",
    },
    {
        "id": "9.sb.2",
        "module_id": "9",
        "title": "Free play: functions",
        "prompt": "Experiment with parameters, return values, and default arguments.",
        "starter_code": 'def greet(name):\n    return "Hi, " + name\n\nprint(greet("Sam"))',
        "expected_output": None,
        "mode": "freeform",
    },
    {
        "id": "10.sb.1",
        "module_id": "10",
        "title": "Fix the bug: sum a list",
        "prompt": "This should print 15 (3+5+7), but it has a bug — find and fix it.",
        "starter_code": "total = 0\nfor n in [3, 5, 7]:\n    total = n\nprint(total)",
        "expected_output": "15",
        "mode": "match_output",
    },
    {
        "id": "10.sb.2",
        "module_id": "10",
        "title": "Free play: debugging",
        "prompt": "Practice tracing values and spotting off-by-one mistakes.",
        "starter_code": "values = [4, 8, 15]\nprint(values[1])",
        "expected_output": None,
        "mode": "freeform",
    },
    {
        "id": "11.sb.1",
        "module_id": "11",
        "title": "Write then read a file",
        "prompt": 'Write the text "done" to a file, then read it back and print it.',
        "starter_code": "",
        "expected_output": "done",
        "mode": "match_output",
    },
    {
        "id": "11.sb.2",
        "module_id": "11",
        "title": "Free play: file I/O",
        "prompt": "Experiment with open(), write(), read(), and looping over a file's lines.",
        "starter_code": 'with open("notes.txt", "w") as f:\n    f.write("hello file\\n")\nwith open("notes.txt") as f:\n    print(f.read())',
        "expected_output": None,
        "mode": "freeform",
    },
    {
        "id": "12.sb.1",
        "module_id": "12",
        "title": "Square root with math",
        "prompt": "Use the math module to print the square root of 144.",
        "starter_code": "",
        "expected_output": "12.0",
        "mode": "match_output",
    },
    {
        "id": "12.sb.2",
        "module_id": "12",
        "title": "Free play: math and random",
        "prompt": "Experiment with math and random — try seeding random for reproducible results.",
        "starter_code": "import random\nrandom.seed(1)\nprint(random.randint(1, 100))",
        "expected_output": None,
        "mode": "freeform",
    },
    {
        "id": "13.sb.1",
        "module_id": "13",
        "title": "Build a main() function",
        "prompt": "Write a main() function that computes 6 * 7 using a helper function, prints the result, then call main().",
        "starter_code": "",
        "expected_output": "42",
        "mode": "match_output",
    },
    {
        "id": "13.sb.2",
        "module_id": "13",
        "title": "Free play: combining functions",
        "prompt": "Experiment with writing and combining several small, tested functions.",
        "starter_code": "def square(n):\n    return n * n\n\nfor i in range(1, 5):\n    print(square(i))",
        "expected_output": None,
        "mode": "freeform",
    },
]


def get_module_meta(module_id):
    for m in MODULES_META:
        if m["id"] == module_id:
            return m
    return None
