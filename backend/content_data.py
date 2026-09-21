"""Course content: module metadata, lesson content, practice pools, sandbox prompts.

Content is aligned to the actual ENGR 102 lecture slides for each module (terminology,
worked examples, and the order topics are introduced all follow the lectures).
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

MODULES_WITH_CONTENT = {str(i) for i in range(1, 14)}

# ---------------------------------------------------------------------------
# Full lesson content for all 13 modules
# ---------------------------------------------------------------------------

MODULE_CONTENT = {
    "1": {
        "id": "1",
        "title": "Intro to Course, Engineering & Programming",
        "intro": "A programmer writes instructions (a program) for a computer to follow; a compiler or "
                 "interpreter converts those instructions into something the computer can execute. This "
                 "module covers that basic process, your first Python program, arithmetic in Python, and "
                 "a general process for tackling any programming problem.",
        "components": [
            {
                "id": "1.1",
                "title": "The Programming Process",
                "explanation": (
                    "A program is just a text file containing commands, saved with the right extension "
                    "(.py for Python). A compiler or interpreter translates those commands into "
                    "instructions the computer can run. A compiler looks at the whole program at once "
                    "and produces a separate file of machine instructions; an interpreter translates and "
                    "runs a program line by line, with no separate file saved. Python is interpreted — "
                    "the original program is often called a script.\n\n"
                    "You can write a script in any text editor, but an IDE (Integrated Development "
                    "Environment) bundles an editor with helpful tools like syntax coloring and a way to "
                    "run your code, all in one place."
                ),
                "examples": [
                    {
                        "code": 'print("Howdy, World!")',
                        "output": "Howdy, World!",
                        "note": "The traditional first program, Aggie-style — one line is all it takes.",
                    }
                ],
                "practice": [
                    {
                        "id": "1.1.p1",
                        "question": "What is the key difference between a compiler and an interpreter?",
                        "choices": [
                            "A compiler translates the whole program before running it; an interpreter translates and runs it line by line",
                            "A compiler only works with Python",
                            "An interpreter is faster in every case",
                            "There is no real difference",
                        ],
                        "answer": 0,
                        "explanation": "A compiler processes the whole program up front; an interpreter translates line by line as it executes.",
                    },
                    {
                        "id": "1.1.p2",
                        "question": "What is a Python script?",
                        "choices": [
                            "A compiled binary file",
                            "A text file containing Python commands",
                            "A type of IDE",
                            "A picture of your code",
                        ],
                        "answer": 1,
                        "explanation": "A script is just a text file of instructions, run by the interpreter.",
                    },
                ],
            },
            {
                "id": "1.2",
                "title": "Arithmetic and the math Module",
                "explanation": (
                    "Python supports the basic arithmetic operators +, -, *, and / with the usual order "
                    "of operations (and parentheses override that order). Beyond those, Python has "
                    "** for exponentiation (2**10 is 1024), // for integer (floor) division with no "
                    "remainder (7//3 is 2), and % for modulus, the remainder from division (7%3 is 1).\n\n"
                    "For more advanced math — square roots, trig functions, logarithms — add the line "
                    "from math import * near the top of your program. This gives you functions like "
                    "sqrt(x), sin(x)/cos(x)/tan(x) (which use radians, not degrees), and constants like pi."
                ),
                "examples": [
                    {
                        "code": "print(2+3*4)\nprint((2+3)*4)\nprint(2**10)\nprint(7//3)\nprint(7%3)",
                        "output": "14\n20\n1024\n2\n1",
                        "note": "Order of operations applies (2+3*4 does the multiplication first); parentheses override it.",
                    },
                    {
                        "code": 'from math import *\nprint("ENGR")\nprint(((3**3)+4*5)*(sqrt(25)//2)+(28%10))',
                        "output": "ENGR\n102.0",
                        "note": "Working inside-out: 3**3=27, 27+20=47, sqrt(25)//2 = 5.0//2 = 2.0, 47*2.0=94.0, 28%10=8, 94.0+8=102.0.",
                    },
                ],
                "practice": [
                    {
                        "id": "1.2.p1",
                        "question": "What does 2**10 evaluate to?",
                        "choices": ["20", "100", "1024", "2"],
                        "answer": 2,
                        "explanation": "** is exponentiation: 2 to the 10th power is 1024.",
                    },
                    {
                        "id": "1.2.p2",
                        "question": "What must you add to your program to use sqrt() or pi?",
                        "choices": ["Nothing, they're always available", "from math import *", "import python", "print(math)"],
                        "answer": 1,
                        "explanation": "Extra math functions and constants come from the math module.",
                    },
                ],
            },
            {
                "id": "1.3",
                "title": "print(), Comments, and Multiple Values",
                "explanation": (
                    "print() displays whatever is in its parentheses. Text must be in quotation marks; "
                    "numbers can be placed directly. Each print() statement displays on its own line by "
                    "default.\n\n"
                    "Code can include comments, starting with a # character — everything after the # on "
                    "that line is ignored by the computer. Comments exist purely to help people reading "
                    "the code understand it."
                ),
                "examples": [
                    {
                        "code": 'print("Howdy, World!")\nprint(1)\n# The line below is a comment and does nothing\n# print(999)',
                        "output": "Howdy, World!\n1",
                        "note": "Text needs quotes; numbers don't. The commented-out print(999) never runs.",
                    }
                ],
                "practice": [
                    {
                        "id": "1.3.p1",
                        "question": 'Why does print("Howdy") need quotation marks but print(1) does not?',
                        "choices": [
                            "It's random which needs quotes",
                            "Text (a string) needs quotes; a number can be used directly",
                            "Quotes are always optional",
                            "Numbers always need quotes too",
                        ],
                        "answer": 1,
                        "explanation": "Quotation marks tell Python you mean literal text, not a variable name.",
                    },
                    {
                        "id": "1.3.p2",
                        "question": "What happens to the text after a # on a line?",
                        "choices": ["It causes an error", "It is ignored by the computer", "It is printed anyway", "It becomes a variable name"],
                        "answer": 1,
                        "explanation": "Everything after # on that line is a comment and is skipped entirely.",
                    },
                ],
            },
            {
                "id": "1.4",
                "title": "A Process for Solving Problems",
                "explanation": (
                    "Programming is fundamentally problem solving. A reliable process: (1) Understand "
                    "the problem — read it carefully, restate it in your own words; (2) Make a plan — "
                    "write pseudocode or comments as an outline, and create test cases to check your "
                    "answer against; (3) Execute the plan — write the code, run it, test it, debug it; "
                    "(4) Review your work — check your output against your test cases, and consider "
                    "whether there's a better way.\n\n"
                    "When in doubt, solve the problem by hand first, then translate that process into code."
                ),
                "examples": [
                    {
                        "code": "# Understand: convert a temperature from Celsius to Fahrenheit\n# Plan: F = C * 9/5 + 32; test case: 0C should give 32F\ncelsius = 0\nfahrenheit = celsius * 9 / 5 + 32\nprint(fahrenheit)",
                        "output": "32.0",
                        "note": "The comments record the plan before the code; the result matches the known test case (0C = 32F).",
                    }
                ],
                "practice": [
                    {
                        "id": "1.4.p1",
                        "question": "Why create test cases before writing code?",
                        "choices": [
                            "Python requires it",
                            "They give you a way to check whether your finished code produces the right answer",
                            "It makes the code run faster",
                            "It's not useful",
                        ],
                        "answer": 1,
                        "explanation": "A known expected answer lets you verify your code once it's written.",
                    },
                    {
                        "id": "1.4.p2",
                        "question": "What should you do when you're stuck on a problem?",
                        "choices": [
                            "Immediately start typing code",
                            "Try solving it by hand first, then translate that into code",
                            "Skip the understanding step",
                            "Give up on planning",
                        ],
                        "answer": 1,
                        "explanation": "Working it out by hand first often reveals the steps needed before any code is written.",
                    },
                ],
            },
        ],
        "quiz": [
            {"id": "1.q1", "question": "An interpreter, unlike a compiler, translates and runs a program:", "choices": ["All at once, ahead of time", "Line by line, as it executes", "Never — interpreters don't run programs", "Only after compiling first"], "answer": 1, "explanation": "Interpreters process and execute code line by line."},
            {"id": "1.q2", "question": "What does 7 // 3 evaluate to?", "choices": ["2.33", "2", "1", "3"], "answer": 1, "explanation": "// is floor division, dropping the remainder: 7 divided by 3 is 2 with remainder 1, so 7//3 is 2."},
            {"id": "1.q3", "question": "What line gives you access to sqrt() and pi?", "choices": ["import python", "from math import *", "print(math)", "Nothing needed"], "answer": 1, "explanation": "Extra math functions/constants come from the math module."},
            {"id": "1.q4", "question": "Text after a # on a line is:", "choices": ["Executed twice", "Ignored by the computer", "An error", "Printed automatically"], "answer": 1, "explanation": "Comments are skipped entirely by the interpreter."},
            {"id": "1.q5", "question": "In the problem-solving process, creating test cases happens during:", "choices": ["Understanding the problem", "Making a plan", "Reviewing your work only", "Never"], "answer": 1, "explanation": "Test cases are created as part of the planning step, before executing the plan."},
        ],
    },
    "2": {
        "id": "2",
        "title": "Sequential Steps, Variables, Assignment",
        "intro": "Programs run one instruction after another, in order. This module covers that "
                 "sequential flow, variables as named 'boxes' of computer memory, the rules for naming "
                 "them well, and how assignment actually works.",
        "components": [
            {
                "id": "2.1",
                "title": "Variables as Memory Boxes",
                "explanation": (
                    "Think of a computer's main memory as a bunch of boxes that hold information. A "
                    "variable is one of those boxes, holding a single unit of information (like the "
                    "number 19). Since there are many boxes, we need a way to tell them apart — that's "
                    "the variable name, like a label on the box.\n\n"
                    "Python variable names can start with a letter or underscore, and contain letters, "
                    "digits, and underscores after that — but a name can't be a reserved keyword (words "
                    "like if, for, and while that are reserved for the language itself)."
                ),
                "examples": [
                    {
                        "code": "age = 19\nprint(age)\nprint(age + 3)",
                        "output": "19\n22",
                        "note": "age is a labeled box holding 19; age + 3 reads that value and computes 22 without changing the box.",
                    }
                ],
                "practice": [
                    {
                        "id": "2.1.p1",
                        "question": "A variable is best thought of as:",
                        "choices": ["A comment", "A named box of memory holding a value", "A type of loop", "A function"],
                        "answer": 1,
                        "explanation": "Variables are labeled locations in memory that hold information."},
                    {
                        "id": "2.1.p2",
                        "question": "Which of these can NOT be used as a Python variable name?",
                        "choices": ["my_age", "_hidden", "for", "Age2"],
                        "answer": 2,
                        "explanation": "'for' is a reserved keyword, so it can't be used as a variable name.",
                    },
                ],
            },
            {
                "id": "2.2",
                "title": "Choosing Good Names",
                "explanation": (
                    "A name being valid doesn't mean it's good. Pick descriptive names — volume is "
                    "better than v — but not excessively long either. A few conventions: constants that "
                    "never change are often written in ALL_CAPS (like PI); the variables i, j, and k are "
                    "commonly used for counting; and most variable names start with a lowercase letter.\n\n"
                    "Good names matter because you're communicating — with anyone who reads your code, "
                    "and most importantly with your future self, once you've forgotten the details."
                ),
                "examples": [
                    {
                        "code": "PI = 3.14159\nradius = 5\narea = PI * radius ** 2\nprint(area)",
                        "output": "78.53975",
                        "note": "PI in all caps signals a constant; radius and area are clear, descriptive, lowercase names.",
                    }
                ],
                "practice": [
                    {
                        "id": "2.2.p1",
                        "question": "Which naming convention is commonly used for constants that never change?",
                        "choices": ["ALL_CAPS", "camelCase", "starting with a number", "single random letters"],
                        "answer": 0,
                        "explanation": "Constants are often written in ALL_CAPS, like PI or MAX_SPEED.",
                    },
                    {
                        "id": "2.2.p2",
                        "question": "Why does it matter if study_session_length is a better name than just t?",
                        "choices": [
                            "t is invalid syntax",
                            "A descriptive name communicates purpose to anyone reading the code later, including future you",
                            "Longer names always run faster",
                            "It doesn't matter at all",
                        ],
                        "answer": 1,
                        "explanation": "Good names are a form of communication with future readers of the code — including yourself.",
                    },
                ],
            },
            {
                "id": "2.3",
                "title": "Assignment and Sequential Execution",
                "explanation": (
                    "An assignment statement has the form <variable name> = <value to assign>. The = is "
                    "the assignment operator, not \"equals\" — it's often read aloud as \"gets\" or \"is "
                    "assigned.\" When an assignment runs, Python first evaluates the entire right-hand "
                    "side, then stores that result in the variable on the left. This means z = z + 1 "
                    "makes perfect sense: read the current value of z, add 1, then store the result back "
                    "into z.\n\n"
                    "Python statements execute sequentially, one after another in the order they're "
                    "written — a variable must be assigned before it's used, and reassigning a variable "
                    "replaces its old value entirely."
                ),
                "examples": [
                    {
                        "code": "x = 2\ny = 3\nx = x * x\ny = y + 2\nz = x * y\nz = z + 1\nprint(x, y, z)",
                        "output": "4 5 21",
                        "note": "Step by step: x becomes 4 (2*2), y becomes 5 (3+2), z becomes 20 (4*5), then z becomes 21 (20+1).",
                    }
                ],
                "practice": [
                    {
                        "id": "2.3.p1",
                        "question": "When Python executes z = z + 1, what happens first?",
                        "choices": [
                            "z is deleted",
                            "The current value of z is read and 1 is added, before the result is stored back in z",
                            "Python checks if z equals 1",
                            "An error occurs",
                        ],
                        "answer": 1,
                        "explanation": "The right-hand side is fully evaluated using the current value of z before the assignment happens.",
                    },
                    {
                        "id": "2.3.p2",
                        "question": "x=3; y=5; z=x; x=1 — what is the value of z at the end?",
                        "choices": ["1", "3", "5", "Error"],
                        "answer": 1,
                        "explanation": "z=x copied x's value (3) at that moment; changing x afterward doesn't affect z.",
                    },
                ],
            },
        ],
        "quiz": [
            {"id": "2.q1", "question": "A variable name may NOT:", "choices": ["Contain an underscore", "Be a reserved keyword like 'while'", "Start with a letter", "Contain digits after the first character"], "answer": 1, "explanation": "Reserved keywords can't be used as variable names."},
            {"id": "2.q2", "question": "The = operator in Python is best read aloud as:", "choices": ["'equals'", "'is assigned' or 'gets'", "'compares to'", "'greater than'"], "answer": 1, "explanation": "= assigns a value; it does not test equality (that's ==)."},
            {"id": "2.q3", "question": "x=3\\ny=5\\nz=x\\nx=1 — what is z?", "choices": ["1", "3", "5", "Undefined"], "answer": 1, "explanation": "z copied x's value (3) at assignment time, before x changed."},
            {"id": "2.q4", "question": "Which is a common convention for naming a constant like the value of pi?", "choices": ["pi_value_that_never_changes_ever", "PI", "p", "Pi123"], "answer": 1, "explanation": "ALL_CAPS is the common convention for constants."},
            {"id": "2.q5", "question": "Python statements execute:", "choices": ["In a random order", "Sequentially, top to bottom", "All simultaneously", "Bottom to top"], "answer": 1, "explanation": "Statements run one after another, in the order written."},
        ],
    },
    "3": {
        "id": "3",
        "title": "Data Types, Input/Output, Basic Functions",
        "intro": "Every variable has a type, which says how to interpret the 1s and 0s it stores. This "
                 "module covers Python's core types, strings and escape characters, converting between "
                 "types, and getting nicely-formatted input and output.",
        "components": [
            {
                "id": "3.1",
                "title": "Core Data Types",
                "explanation": (
                    "Python's basic built-in types include int (whole numbers), float (numbers with a "
                    "decimal point), bool (True or False), and str (text). In Python, a variable's type "
                    "is implied by how it was created or last assigned — you don't declare it up front "
                    "like in some other languages. Use type() to check what type a value currently is."
                ),
                "examples": [
                    {
                        "code": 'a = 5\nb = 5.0\nc = True\nd = "Five"\nprint(type(a))\nprint(type(b))\nprint(type(c))\nprint(type(d))',
                        "output": "<class 'int'>\n<class 'float'>\n<class 'bool'>\n<class 'str'>",
                        "note": "The type comes entirely from how each variable was assigned — 5 is an int, 5.0 is a float.",
                    }
                ],
                "practice": [
                    {
                        "id": "3.1.p1",
                        "question": "What type is x after x = 2 / 2?",
                        "choices": ["int", "float — dividing with / always gives a float", "str", "bool"],
                        "answer": 1,
                        "explanation": "The / operator always produces a float, even when the division comes out even.",
                    },
                    {
                        "id": "3.1.p2",
                        "question": "What type is x after x = 2 // 2?",
                        "choices": ["int — floor division with matching int operands stays an int", "float always", "str", "bool"],
                        "answer": 0,
                        "explanation": "// is floor division; with two ints it produces an int result.",
                    },
                ],
            },
            {
                "id": "3.2",
                "title": "Strings and Escape Characters",
                "explanation": (
                    "A string is text, written inside single or double quotes: \"like this\" or 'like "
                    "this'. To include an apostrophe, wrap the string in double quotes; to include a "
                    "quotation mark, use single quotes. For a string that needs both, use a backslash "
                    "\\ as an escape character before the character you want to include literally.\n\n"
                    "Other escape sequences: \\\\ prints one backslash, \\t is a tab, and \\n is a "
                    "newline. Triple-quoted strings ('''like this''' or \"\"\"like this\"\"\") can span "
                    "multiple lines."
                ),
                "examples": [
                    {
                        "code": "print('Backslash: \\\\1')\nprint('Tab: \\t2')\nprint('Newline: \\n3')\nprint('Quotes: \\'4\\' or \\\"5\\\"')",
                        "output": "Backslash: \\1\nTab: \t2\nNewline: \n3\nQuotes: '4' or \"5\"",
                        "note": "Each escape sequence produces one literal character in the output — \\n actually breaks the line.",
                    }
                ],
                "practice": [
                    {
                        "id": "3.2.p1",
                        "question": 'To include an apostrophe in a string, the simplest option is to:', "choices": [
                            "Wrap the string in double quotes",
                            "It's never possible",
                            "Always use triple quotes",
                            "Delete the apostrophe",
                        ],
                        "answer": 0,
                        "explanation": '"It\'s" works directly since double quotes don\'t conflict with the apostrophe.',
                    },
                    {
                        "id": "3.2.p2",
                        "question": "What does the escape sequence \\n represent?",
                        "choices": ["A literal backslash-n", "A newline character", "A tab character", "Nothing, it's ignored"],
                        "answer": 1,
                        "explanation": "\\n inserts a newline within a string.",
                    },
                ],
            },
            {
                "id": "3.3",
                "title": "Converting Between Types",
                "explanation": (
                    "Convert values with new_type(value): int(), float(), str(), and bool(). Converting "
                    "a float to an int truncates it — int(4.9) is 4, and int(-1.3) is -1 (it drops the "
                    "fractional part, it doesn't round). A string converts to a number only if it "
                    "clearly represents one: int('3') works, but int('2.5') is an error (it does NOT "
                    "convert to a float first).\n\n"
                    "Boolean conversions have their own rules: converting True/False to a number gives "
                    "1/0. Converting TO a bool, the number 0 is False and anything else is True — but "
                    "for strings, only the empty string '' is False; even '0' and 'False' count as True, "
                    "since they're non-empty strings."
                ),
                "examples": [
                    {
                        "code": "print(int(True))\nprint(float(False))\nprint(bool(0))\nprint(bool(3))\nprint(bool('0'))\nprint(bool(''))",
                        "output": "1\n0.0\nFalse\nTrue\nTrue\nFalse",
                        "note": "bool('0') is True because '0' is a non-empty string — only the truly empty string '' converts to False.",
                    }
                ],
                "practice": [
                    {
                        "id": "3.3.p1",
                        "question": "What does int(4.9) evaluate to?",
                        "choices": ["5 (it rounds)", "4 (it truncates)", "4.9", "Error"],
                        "answer": 1,
                        "explanation": "Converting float to int truncates the fractional part rather than rounding.",
                    },
                    {
                        "id": "3.3.p2",
                        "question": "What happens when you run int('2.5')?",
                        "choices": [
                            "It returns the integer 2",
                            "It raises an error — it does not first convert to float, then to int",
                            "It returns the float 2.5",
                            "It returns 0",
                        ],
                        "answer": 1,
                        "explanation": "int() on a string requires the string to clearly represent an integer; '2.5' does not.",
                    },
                ],
            },
            {
                "id": "3.4",
                "title": "Input, Output, and f-strings",
                "explanation": (
                    "input() reads what the user types, always as a string — convert it yourself with "
                    "int() or float() if you need a number. input(\"prompt\") prints the prompt (with no "
                    "newline after it) before waiting for input, which is usually cleaner than a separate "
                    "print() call.\n\n"
                    "print() separates multiple values with a space and ends with a newline by default; "
                    "override either with sep=\"...\" or end=\"...\". For full control over formatting, "
                    "use an f-string: write f'...' with {expression} placeholders inside. Add a format "
                    "specifier like {value:.2f} to control decimal places, or {value:>10} to right-align "
                    "text in a 10-character field (< for left, ^ for center)."
                ),
                "examples": [
                    {
                        "code": 'from math import pi\nflavor = "Apple"\nprint(f"{flavor} pie is tasty, and pi is {pi:.5f}")',
                        "output": "Apple pie is tasty, and pi is 3.14159",
                        "note": "{flavor} inserts the variable's value directly; {pi:.5f} formats pi to exactly 5 decimal places.",
                    },
                    {
                        "code": "r = float(input(\"Enter the radius of a circle: \"))\nfrom math import pi\narea = pi * r ** 2\nprint(f\"The area of the circle is {area:.4f}\")",
                        "output": "Enter the radius of a circle: 1\nThe area of the circle is 3.1416",
                        "note": "input() with a prompt string avoids a separate print() call; the f-string rounds to 4 decimal places for display.",
                    },
                ],
                "practice": [
                    {
                        "id": "3.4.p1",
                        "question": 'What does f"pi is {pi:.2f}" do differently from f"pi is {pi}"?',
                        "choices": [
                            "Nothing, they're identical",
                            "It rounds pi's displayed value to 2 decimal places",
                            "It converts pi to a string only",
                            "It causes an error",
                        ],
                        "answer": 1,
                        "explanation": "The :.2f format specifier controls how many decimal places are shown.",
                    },
                    {
                        "id": "3.4.p2",
                        "question": 'age = int(input("Enter age: ")) — why convert with int()?',
                        "choices": [
                            "input() always returns a string, so it must be converted to do math with it",
                            "It's not necessary",
                            "int() reads the keyboard directly",
                            "input() only works with int()",
                        ],
                        "answer": 0,
                        "explanation": "input() always returns a string, regardless of what the user typed.",
                    },
                ],
            },
        ],
        "quiz": [
            {"id": "3.q1", "question": "What type does x = 2 / 2 produce?", "choices": ["int", "float", "str", "bool"], "answer": 1, "explanation": "/ (true division) always produces a float."},
            {"id": "3.q2", "question": "To include a quotation mark inside a string, the simplest option is to:", "choices": ["Wrap the string in single quotes", "It's impossible", "Use only numbers", "Delete the quote"], "answer": 0, "explanation": "Single-quoting the string lets you include \" marks directly."},
            {"id": "3.q3", "question": "int('2.5') results in:", "choices": ["2", "2.5", "An error", "0"], "answer": 2, "explanation": "int() on a string needs a clear integer representation; '2.5' isn't one."},
            {"id": "3.q4", "question": "bool('') evaluates to:", "choices": ["True", "False", "Error", "0"], "answer": 1, "explanation": "Only the empty string converts to False; any non-empty string is True."},
            {"id": "3.q5", "question": 'f"{3.14159:.2f}" displays as:', "choices": ["3.14159", "3.14", "3.1", "3"], "answer": 1, "explanation": ":.2f rounds and displays exactly 2 decimal places."},
        ],
    },
    "4": {
        "id": "4",
        "title": "Boolean Expressions, Conditionals",
        "intro": "Programs need to make decisions. This module covers relational and Boolean operators "
                 "that produce True/False values, and the if/elif/else statements that branch a "
                 "program's flow based on them.",
        "components": [
            {
                "id": "4.1",
                "title": "Relational and Boolean Operators",
                "explanation": (
                    "Relational operators compare two values and produce a Boolean: == (equal — note "
                    "the two equal signs, since one = is assignment), != (not equal), <, >, <=, >=. "
                    "Boolean operators combine Booleans: A and B is True only if both are True; A or B "
                    "is True if either is True; not A flips A's value.\n\n"
                    "Order of operations: math operators run first, then relational operators, then "
                    "Boolean operators — and among Boolean operators, not runs before and, which runs "
                    "before or. Even so, use parentheses to make your intent clear and avoid bugs."
                ),
                "examples": [
                    {
                        "code": "a = 10\nb = 10\nc = 20\nd = ((a>b) and (b<=c)) or (not((((c<=a+b) and (a==10)) or ((b==10) and c!=10))))\nprint(d)",
                        "output": "False",
                        "note": "(a>b) is False, so the left side of or is False; inside the not(...), both inner conditions are True, so not(True) is False. False or False is False.",
                    }
                ],
                "practice": [
                    {
                        "id": "4.1.p1",
                        "question": "Which operator tests equality (not assignment)?",
                        "choices": ["=", "==", ":=", "!="],
                        "answer": 1,
                        "explanation": "== compares two values; = assigns a value.",
                    },
                    {
                        "id": "4.1.p2",
                        "question": "What is the Python order among not, and, or?",
                        "choices": ["or, then and, then not", "not, then and, then or", "They're all equal precedence", "and, then not, then or"],
                        "answer": 1,
                        "explanation": "not binds tightest, then and, then or."},
                ],
            },
            {
                "id": "4.2",
                "title": "if / elif / else",
                "explanation": (
                    "The if statement creates a branch: if <condition>: followed by an indented block "
                    "that runs only when the condition is True. Unlike most languages, Python requires "
                    "consistent indentation (commonly 4 spaces) to mark which lines belong to the block.\n\n"
                    "Use if/else when there are exactly two possibilities, and if/elif/else when there "
                    "are more. Conditions are checked top to bottom, and only the FIRST one that's True "
                    "runs — the rest are skipped, even if they'd also be True."
                ),
                "examples": [
                    {
                        "code": 'major = "ECEN"\nif major == "CSCE":\n    office = "HRBB 302"\nelif major == "ECEN":\n    office = "WEB 301"\nelif major == "MEEN":\n    office = "MEOB 100"\nelse:\n    office = "unknown"\nprint(office)',
                        "output": "WEB 301",
                        "note": "The first branch (CSCE) doesn't match, so Python checks the next; ECEN matches, so that branch runs and the rest are skipped.",
                    }
                ],
                "practice": [
                    {
                        "id": "4.2.p1",
                        "question": "In Python, what marks which lines belong to an if block?",
                        "choices": ["Curly braces {}", "Consistent indentation", "Semicolons", "Nothing — it's optional"],
                        "answer": 1,
                        "explanation": "Python uses indentation, not braces, to define blocks — and it's required, not optional."},
                    {
                        "id": "4.2.p2",
                        "question": "In an if/elif/elif/else chain where two conditions would both be True, how many branches run?",
                        "choices": ["Both", "Only the first one that's True", "Only the last one", "None"],
                        "answer": 1,
                        "explanation": "Python stops at the first True condition, regardless of whether a later one would also be True.",
                    },
                ],
            },
            {
                "id": "4.3",
                "title": "Combining and Nesting Conditions",
                "explanation": (
                    "You can nest an if statement inside another if to check a second condition only "
                    "once an outer one is already satisfied. Often, a nested check can also be written "
                    "as a single condition combined with and — which is usually easier to read.\n\n"
                    "A common pattern is testing whether a value falls in a range, like whether water at "
                    "a given Fahrenheit temperature is liquid: it needs to be both at least 32 and at "
                    "most 212."
                ),
                "examples": [
                    {
                        "code": "F = 75\nis_liquid = (F >= 32) and (F <= 212)\nprint(is_liquid)",
                        "output": "True",
                        "note": "Both conditions must hold for water to be liquid at that temperature; and requires both to be True.",
                    }
                ],
                "practice": [
                    {
                        "id": "4.3.p1",
                        "question": "To test if a variable is between 0 and 100 inclusive, you would write:",
                        "choices": [
                            "(variable >= 0) or (variable <= 100)",
                            "(variable >= 0) and (variable <= 100)",
                            "variable == 0 and 100",
                            "not (variable >= 0)",
                        ],
                        "answer": 1,
                        "explanation": "Both bounds must hold at once, so and is required (or would always be True)."},
                    {
                        "id": "4.3.p2",
                        "question": "A nested if inside another if is often equivalent to:",
                        "choices": [
                            "A single if with the conditions combined using and",
                            "A while loop",
                            "A function definition",
                            "Nothing — nesting is never equivalent to anything else",
                        ],
                        "answer": 0,
                        "explanation": "Nested ifs checking two conditions can usually be flattened into one if using and.",
                    },
                ],
            },
        ],
        "quiz": [
            {"id": "4.q1", "question": "Which comparison operator means 'equal to'?", "choices": ["=", "==", "<>", "eq"], "answer": 1, "explanation": "== tests equality; = is assignment."},
            {"id": "4.q2", "question": "True and False evaluates to:", "choices": ["True", "False", "None", "Error"], "answer": 1, "explanation": "and requires both sides True."},
            {"id": "4.q3", "question": "Python requires ___ to mark an if block's contents.", "choices": ["Curly braces", "Consistent indentation", "Line numbers", "Nothing"], "answer": 1, "explanation": "Indentation is mandatory in Python, unlike most other languages."},
            {"id": "4.q4", "question": "In an if/elif/else chain, once a condition is found True:", "choices": ["All remaining branches still run", "The remaining elif/else branches are skipped", "The program stops", "An error occurs"], "answer": 1, "explanation": "Only the first True branch executes."},
            {"id": "4.q5", "question": "not (5 > 3) evaluates to:", "choices": ["True", "False", "5", "3"], "answer": 1, "explanation": "5 > 3 is True; not flips it to False."},
        ],
    },
    "5": {
        "id": "5",
        "title": "Creating & Testing Programs, Basic Debugging",
        "intro": "As programs grow, planning and testing become essential. This module covers writing "
                 "good comments, designing a program before coding it, building it incrementally rather "
                 "than all at once, and writing tests that actually catch problems.",
        "components": [
            {
                "id": "5.1",
                "title": "Comments and Program Design",
                "explanation": (
                    "Comments should describe the purpose of code, clarify a non-obvious computation, or "
                    "separate sections — not restate what's already obvious from reading the code.\n\n"
                    "For designing a program: list out its major stages in order outside of any code "
                    "(e.g. get input -> calculate -> output result), turn those steps into comments, "
                    "then fill in the code between them one section at a time."
                ),
                "examples": [
                    {
                        "code": "# Get user's homework grade\nhomework = float(input(\"Enter your average homework grade: \"))\n# Get user's exam grade\nexam = float(input(\"Enter your average exam grade: \"))\n# Calculate grade as: 40% homework + 60% exam\ngrade = 0.4 * homework + 0.6 * exam\n# Determine letter grade\nif grade >= 90:\n    letter = \"A\"\nelif grade >= 80:\n    letter = \"B\"\nelse:\n    letter = \"C\"\nprint(f\"Your grade is: {letter}\")",
                        "output": "Enter your average homework grade: 95\nEnter your average exam grade: 88\nYour grade is: B",
                        "note": "Each comment states a design step first; the code beneath it fills that step in.",
                    }
                ],
                "practice": [
                    {
                        "id": "5.1.p1",
                        "question": "A good use of a comment is to:",
                        "choices": [
                            "Restate exactly what an obvious line of code does",
                            "Clarify the purpose of a non-obvious computation",
                            "Make the program run faster",
                            "Replace the need for variable names",
                        ],
                        "answer": 1,
                        "explanation": "Comments should add understanding, not just repeat what's already clear from the code."},
                    {
                        "id": "5.1.p2",
                        "question": "In the 'steps to comments to code' design process, what comes first?",
                        "choices": ["Writing all the code", "Listing the program's major steps in order, outside of any code", "Testing the finished program", "Picking variable names"],
                        "answer": 1,
                        "explanation": "You outline the steps first, before any code is written."},
                ],
            },
            {
                "id": "5.2",
                "title": "Incremental Development",
                "explanation": (
                    "Pyramids and arches are both stable ancient structures, but built very differently. "
                    "A pyramid can stop at any point and still be stable — you can test the lower levels "
                    "before adding more. An arch isn't stable until every stone is in place, so you can't "
                    "really test it partway through.\n\n"
                    "Some programmers build software the 'arch' way: write everything, then test at the "
                    "end — and if one piece is broken, the whole thing falls apart. Better is the "
                    "'pyramid' way: write a small piece, test it, confirm it works, then add more. You "
                    "always have a working piece of software, even before it's complete."
                ),
                "examples": [
                    {
                        "code": "# Step 1: read input and confirm it (test before continuing)\nstudy_time = float(input(\"How long will you study? \"))\nprint(\"Entered:\", study_time)",
                        "output": "How long will you study? 10\nEntered: 10.0",
                        "note": "Testing this small piece — confirming the input reads and converts correctly — before writing the next section is the 'pyramid' approach.",
                    }
                ],
                "practice": [
                    {
                        "id": "5.2.p1",
                        "question": "The 'pyramid' style of software development means:",
                        "choices": [
                            "Writing all the code, then testing once at the end",
                            "Writing and testing small pieces before adding more",
                            "Never testing your code",
                            "Writing code in alphabetical order",
                        ],
                        "answer": 1,
                        "explanation": "Pyramid-style development builds and verifies stable pieces incrementally."},
                    {
                        "id": "5.2.p2",
                        "question": "Why is the 'arch' style risky for software?",
                        "choices": [
                            "It's actually the safest approach",
                            "Nothing can be tested until every piece is written, so one broken piece breaks everything",
                            "It requires too many comments",
                            "It only works for small programs",
                        ],
                        "answer": 1,
                        "explanation": "Like an arch missing a stone, an incomplete 'arch-style' program can't be verified until it's entirely finished."},
                ],
            },
            {
                "id": "5.3",
                "title": "Writing Tests and Finding Bugs",
                "explanation": (
                    "Tests are inputs where you already know the correct output. Test the 'typical' case "
                    "first, then the 'edge' or 'corner' cases — the less common, boundary situations "
                    "(like the very first or last valid value). Debugging means using a failing test to "
                    "find, understand, and fix the underlying error.\n\n"
                    "A classic bug: reading input and forgetting to convert it. input() always returns a "
                    "string, so adding a number to it directly raises a TypeError — the fix is converting "
                    "with float() or int() right when you read it."
                ),
                "examples": [
                    {
                        "code": "study_time = float(input(\"How long will you study? \"))\nprint(\"Adding 1:\", study_time + 1)",
                        "output": "How long will you study? 10\nAdding 1: 11.0",
                        "note": "Converting with float() as soon as the value is read avoids a TypeError from trying to add 1 to a string.",
                    }
                ],
                "practice": [
                    {
                        "id": "5.3.p1",
                        "question": "What is an 'edge case' when testing a program?",
                        "choices": [
                            "A completely random input",
                            "A boundary or unusual situation, like the very first or last valid value",
                            "The most common, typical input",
                            "An input that's guaranteed to crash the program",
                        ],
                        "answer": 1,
                        "explanation": "Edge cases test boundaries and unusual situations, beyond the typical case."},
                    {
                        "id": "5.3.p2",
                        "question": "Why does study_time + 1 fail if study_time = input(\"...\") (with no conversion)?",
                        "choices": [
                            "input() is broken",
                            "study_time is a string, and you can't add a number directly to a string",
                            "1 is not a valid number in Python",
                            "It doesn't fail",
                        ],
                        "answer": 1,
                        "explanation": "input() returns a string; adding a number to it raises a TypeError unless it's converted first."},
                ],
            },
        ],
        "quiz": [
            {"id": "5.q1", "question": "A good comment should:", "choices": ["Restate obvious code", "Clarify a non-obvious purpose or computation", "Always be one word", "Be written in code, not English"], "answer": 1, "explanation": "Comments should add understanding beyond what the code already shows."},
            {"id": "5.q2", "question": "The 'pyramid' approach to building software means:", "choices": ["Writing everything before testing", "Testing small, stable pieces before adding more", "Skipping tests entirely", "Only testing at the very end"], "answer": 1, "explanation": "Like a pyramid, you can stop and verify stability at any point."},
            {"id": "5.q3", "question": "An 'edge case' test checks:", "choices": ["A typical, common input", "A boundary or unusual situation", "Nothing useful", "Only negative numbers"], "answer": 1, "explanation": "Edge cases probe boundaries, not the typical case."},
            {"id": "5.q4", "question": "Why convert input() results with float() or int() immediately?", "choices": ["It's optional styling", "input() always returns a string, and math operations need a number", "It makes the program run faster", "It's required by print()"], "answer": 1, "explanation": "Without conversion, using the result in math raises a TypeError."},
            {"id": "5.q5", "question": "Debugging means:", "choices": ["Writing new features", "Finding, understanding, and fixing an error using a failing test", "Deleting all comments", "Renaming variables"], "answer": 1, "explanation": "Debugging is the process of tracking down and correcting a bug."},
        ],
    },
    "6": {
        "id": "6",
        "title": "Loops and Iteration",
        "intro": "Loops let a program repeat steps without rewriting them. This module covers the while "
                 "loop, the for loop with range(), nesting loops inside each other, and controlling a "
                 "loop's flow with break and continue.",
        "components": [
            {
                "id": "6.1",
                "title": "The while Loop",
                "explanation": (
                    "Every loop has four parts: initializing a control variable, a continuation "
                    "condition, the things to repeat, and updating the control variable. A while loop "
                    "checks its condition, and if True, runs the indented block, then checks again — "
                    "repeating until the condition is False. If nothing inside the loop ever changes the "
                    "condition's outcome, you get an infinite loop.\n\n"
                    "A very common pattern counts iterations with a variable (often named i, j, or k), "
                    "usually starting at 0."
                ),
                "examples": [
                    {
                        "code": 'secret_number = 7\nuser_guess = 4\nwhile user_guess != secret_number:\n    print("No! Try again.")\n    user_guess = 7\nprint("You guessed it!")',
                        "output": "No! Try again.\nYou guessed it!",
                        "note": "The condition (guess != secret) is checked, found True once, the loop body runs, then the (now-matching) guess makes the condition False.",
                    }
                ],
                "practice": [
                    {
                        "id": "6.1.p1",
                        "question": "What are the four parts of a loop?",
                        "choices": [
                            "print(), input(), if, else",
                            "Initialize a control variable, a continuation condition, things to do, updating the control variable",
                            "Comments, variables, functions, loops",
                            "Only a condition is needed",
                        ],
                        "answer": 1,
                        "explanation": "Every loop needs these four components to work correctly."},
                    {
                        "id": "6.1.p2",
                        "question": "What causes an infinite while loop?",
                        "choices": [
                            "Using print() inside it",
                            "Nothing inside the loop ever changes what the condition depends on",
                            "Starting the counter at 0",
                            "Using an if statement inside it",
                        ],
                        "answer": 1,
                        "explanation": "If the condition's outcome never changes, the loop never stops."},
                ],
            },
            {
                "id": "6.2",
                "title": "The for Loop and range()",
                "explanation": (
                    "A for loop is built for the common case of running a known number of times. "
                    "for i in range(10): runs the body 10 times, with i taking values 0 through 9 (not "
                    "1 through 10 — the sequence starts at 0 and has 10 elements). i is called the "
                    "iterator.\n\n"
                    "range() can also take a start and step: range(start, stop, step) begins at start, "
                    "stops before stop, and counts by step each time."
                ),
                "examples": [
                    {
                        "code": "for i in range(3):\n    print(i, end='')\nprint()\nfor i in range(1, 5):\n    print(i, end='')\nprint()\nfor i in range(3, 9, 2):\n    print(i, end='')",
                        "output": "012\n1234\n357",
                        "note": "range(3) gives 0,1,2; range(1,5) gives 1,2,3,4; range(3,9,2) starts at 3, stops before 9, counting by 2.",
                    }
                ],
                "practice": [
                    {
                        "id": "6.2.p1",
                        "question": "for i in range(10): repeats the body:",
                        "choices": ["9 times, i from 1 to 9", "10 times, i from 0 to 9", "10 times, i from 1 to 10", "11 times"],
                        "answer": 1,
                        "explanation": "range(10) generates 10 values: 0 through 9."},
                    {
                        "id": "6.2.p2",
                        "question": "range(2, 10, 3) produces:",
                        "choices": ["2, 5, 8", "2, 3, 4", "2, 10", "2, 5, 8, 11"],
                        "answer": 0,
                        "explanation": "Starting at 2, stopping before 10, counting by 3: 2, 5, 8."},
                ],
            },
            {
                "id": "6.3",
                "title": "Nesting Loops",
                "explanation": (
                    "Just like if statements, loops can be nested — a loop written entirely inside "
                    "another loop's body. For each single pass of the outer loop, the entire inner loop "
                    "runs completely. This is useful for anything with two independent counters, like "
                    "generating every combination of two ranges of numbers."
                ),
                "examples": [
                    {
                        "code": "for i in range(3):\n    for j in range(3):\n        print(f'{i} times {j} equals {i*j}')",
                        "output": "0 times 0 equals 0\n0 times 1 equals 0\n0 times 2 equals 0\n1 times 0 equals 0\n1 times 1 equals 1\n1 times 2 equals 2\n2 times 0 equals 0\n2 times 1 equals 2\n2 times 2 equals 4",
                        "note": "For each value of i, the entire inner loop over j runs from start to finish before i advances.",
                    }
                ],
                "practice": [
                    {
                        "id": "6.3.p1",
                        "question": "In a nested loop, how many times does the inner loop run in total?",
                        "choices": [
                            "Once, no matter what",
                            "Its full range, once for every single iteration of the outer loop",
                            "The same number of times as the outer loop, combined",
                            "Never — inner loops don't actually run",
                        ],
                        "answer": 1,
                        "explanation": "The entire inner loop completes for each pass of the outer loop."},
                    {
                        "id": "6.3.p2",
                        "question": "for i in range(2):\\n    for j in range(4):\\n        print('x') — how many times does 'x' print?",
                        "choices": ["2", "4", "8", "6"],
                        "answer": 2,
                        "explanation": "2 outer iterations x 4 inner iterations each = 8 total prints."},
                ],
            },
            {
                "id": "6.4",
                "title": "break, continue, and Choosing a Loop",
                "explanation": (
                    "break immediately exits the loop it's in — the next line executed is the one after "
                    "the loop. continue immediately skips the rest of the current iteration and jumps "
                    "back to check the condition (while) or advance to the next value (for). Both are "
                    "best used sparingly, only when they make the code clearer.\n\n"
                    "Use a for loop when you know the number of iterations, or are iterating through a "
                    "known set of items. Use a while loop when you want to repeat indefinitely, until a "
                    "specific value shows up, or until some general condition is met."
                ),
                "examples": [
                    {
                        "code": "for i in range(10):\n    if i % 2 == 1:\n        continue\n    print(\"i is\", i)",
                        "output": "i is 0\ni is 2\ni is 4\ni is 6\ni is 8",
                        "note": "continue skips printing for every odd i, jumping straight to the next value in range(10).",
                    }
                ],
                "practice": [
                    {
                        "id": "6.4.p1",
                        "question": "What does break do inside a loop?",
                        "choices": ["Skips to the next iteration", "Immediately exits the loop entirely", "Pauses the program", "Restarts the loop from the beginning"],
                        "answer": 1,
                        "explanation": "break exits the loop right away; the next line is whatever comes after the loop."},
                    {
                        "id": "6.4.p2",
                        "question": "You should generally choose a for loop over a while loop when:",
                        "choices": [
                            "You want to repeat forever",
                            "You know the number of iterations or are iterating a known set of items",
                            "You never know when to stop",
                            "There's no difference, ever",
                        ],
                        "answer": 1,
                        "explanation": "for loops fit naturally when the number of repetitions (or the items to visit) is already known."},
                ],
            },
        ],
        "quiz": [
            {"id": "6.q1", "question": "A while loop's condition is checked:", "choices": ["Only once, before anything runs", "At the top of every potential repetition", "Only after the loop finishes", "Never"], "answer": 1, "explanation": "The condition is evaluated at the start of every possible iteration."},
            {"id": "6.q2", "question": "range(5) produces which values?", "choices": ["1,2,3,4,5", "0,1,2,3,4", "0,1,2,3,4,5", "5"], "answer": 1, "explanation": "range(5) starts at 0 and stops before 5."},
            {"id": "6.q3", "question": "In a nested loop, the inner loop runs its full range:", "choices": ["Once total", "Once per iteration of the outer loop", "Never", "Only on the last outer iteration"], "answer": 1, "explanation": "The complete inner loop executes for every single outer iteration."},
            {"id": "6.q4", "question": "continue inside a loop:", "choices": ["Exits the loop completely", "Skips the rest of the current iteration and moves to the next", "Is identical to break", "Causes an error"], "answer": 1, "explanation": "continue jumps ahead without leaving the loop."},
            {"id": "6.q5", "question": "Choose a for loop over a while loop when:", "choices": ["You don't know how many times to repeat", "You know the number of iterations or items in advance", "You want an infinite loop", "Never — while is always better"], "answer": 1, "explanation": "for loops are the natural choice for a known number of repetitions."},
        ],
    },
    "7": {
        "id": "7",
        "title": "Lists of Data",
        "intro": "When you have several related values, storing each in its own variable doesn't scale. "
                 "This module covers lists — a single named collection of values — indexing, slicing, "
                 "common list operations, and looping through a list's contents.",
        "components": [
            {
                "id": "7.1",
                "title": "Creating and Indexing Lists",
                "explanation": (
                    "A list groups similar values under one name, written with square brackets: "
                    "grades = [87, 93, 75, 100]. Each element has a position (index) starting at 0, so "
                    "the first element is grades[0]. Negative indices count backward from the end: "
                    "grades[-1] is the last element. Indexing past either end of the list — forward or "
                    "backward — raises an IndexError."
                ),
                "examples": [
                    {
                        "code": "grades = [87, 93, 75, 100, 82, 91, 85]\nprint(grades[0], grades[6])\nprint(grades[-1])",
                        "output": "87 85\n85",
                        "note": "grades[0] is the first element, grades[6] and grades[-1] both reach the same last element (7 items, indices 0-6 or -7 to -1).",
                    }
                ],
                "practice": [
                    {
                        "id": "7.1.p1",
                        "question": 'For colors = ["red", "green", "blue"], what is colors[0]?',
                        "choices": ["red", "green", "blue", "Error"],
                        "answer": 0,
                        "explanation": "Indexing starts at 0, so colors[0] is the first item."},
                    {
                        "id": "7.1.p2",
                        "question": 'For nums = [10, 20, 30], what is nums[-1]?',
                        "choices": ["10", "20", "30", "Error"],
                        "answer": 2,
                        "explanation": "Negative index -1 refers to the last element."},
                ],
            },
            {
                "id": "7.2",
                "title": "Slicing Lists",
                "explanation": (
                    "Slicing pulls out a sub-part of a list: list[a:b] gives elements from index a up "
                    "to (but not including) b. Leave off a to start at the beginning, or leave off b to "
                    "go to the end. Add a third value, list[a:b:c], to step by c between elements. "
                    "Unlike direct indexing, slicing never raises an out-of-range error — it just gives "
                    "you as much of the list as exists."
                ),
                "examples": [
                    {
                        "code": "grades = [87, 93, 75, 100, 82, 91, 85]\nprint(grades[0:3])\nprint(grades[4:])\nprint(grades[1:6:2])\nprint(grades[4:300])",
                        "output": "[87, 93, 75]\n[82, 91, 85]\n[93, 100, 91]\n[82, 91, 85]",
                        "note": "grades[1:6:2] steps by 2 starting at index 1; grades[4:300] just returns everything from index 4 to the end, with no error.",
                    }
                ],
                "practice": [
                    {
                        "id": "7.2.p1",
                        "question": "For nums = [10, 20, 30, 40, 50], what is nums[1:4]?",
                        "choices": ["[10, 20, 30]", "[20, 30, 40]", "[20, 30, 40, 50]", "[10, 20, 30, 40]"],
                        "answer": 1,
                        "explanation": "The slice starts at index 1 and stops before index 4."},
                    {
                        "id": "7.2.p2",
                        "question": "What happens with nums[2:1000] if nums only has 5 elements?",
                        "choices": [
                            "It raises an IndexError",
                            "It returns whatever elements exist from index 2 onward, no error",
                            "It returns an empty list always",
                            "It crashes the program",
                        ],
                        "answer": 1,
                        "explanation": "Slicing never raises an out-of-range error, unlike direct indexing."},
                ],
            },
            {
                "id": "7.3",
                "title": "List Operations",
                "explanation": (
                    "list.append(x) adds x to the end of a list. Two lists can be joined with + "
                    "(concatenation), producing a brand-new list; += works the same way, but you must "
                    "concatenate a list, not a bare value: grades += [80], not grades += 80. len() gives "
                    "the number of elements in a list."
                ),
                "examples": [
                    {
                        "code": "grades = [87, 93, 75]\ngrades.append(80)\nprint(grades)\ngrades += [95]\nprint(grades)\nprint(len(grades))",
                        "output": "[87, 93, 75, 80]\n[87, 93, 75, 80, 95]\n5",
                        "note": "append() adds one item in place; += needs the new item wrapped in its own list, [95], to concatenate correctly.",
                    }
                ],
                "practice": [
                    {
                        "id": "7.3.p1",
                        "question": "Which correctly adds the single value 80 to the end of the list grades?",
                        "choices": ["grades += 80", "grades.append(80)", "grades[80]", "grades = 80"],
                        "answer": 1,
                        "explanation": "append() adds one element directly; += would need [80], a one-item list, instead."},
                    {
                        "id": "7.3.p2",
                        "question": "list1 = [1,2]; list2 = [3,4]; list3 = list1 + list2 — what is list3?",
                        "choices": ["[1,2,3,4]", "[[1,2],[3,4]]", "Error", "[4,6]"],
                        "answer": 0,
                        "explanation": "+ concatenates two lists into one new combined list."},
                ],
            },
            {
                "id": "7.4",
                "title": "Iterating Over Lists",
                "explanation": (
                    "for i in range(len(mylist)): gives you the index i at each step, so mylist[i] can "
                    "be read AND changed. for i in mylist: is simpler and gives you each value directly "
                    "— but i is a separate variable, so changing i does NOT change the list itself. To "
                    "modify list elements in a loop, you need the index form.\n\n"
                    "enumerate(mylist) gives you both the index and the value together, which is handy "
                    "when you need both."
                ),
                "examples": [
                    {
                        "code": "grades = [87, 93, 75]\nfor i in grades:\n    i = 100\nprint(grades)\nfor i in range(len(grades)):\n    grades[i] = 100\nprint(grades)",
                        "output": "[87, 93, 75]\n[100, 100, 100]",
                        "note": "The first loop's i is a separate copy, so the list is untouched; the second loop uses the index to actually modify each element.",
                    }
                ],
                "practice": [
                    {
                        "id": "7.4.p1",
                        "question": "for i in mylist: i = 100 — what happens to mylist?",
                        "choices": [
                            "Every element becomes 100",
                            "mylist is unchanged — i is a separate variable, not a reference into the list",
                            "It raises an error",
                            "The list is deleted",
                        ],
                        "answer": 1,
                        "explanation": "This loop form gives i a copy of each value; reassigning i doesn't touch the list."},
                    {
                        "id": "7.4.p2",
                        "question": "enumerate(mylist) provides:",
                        "choices": ["Only the values", "Only the indices", "Both the index and value together", "The list's length"],
                        "answer": 2,
                        "explanation": "enumerate() yields (index, value) pairs as you loop."},
                ],
            },
        ],
        "quiz": [
            {"id": "7.q1", "question": "For nums = [5, 10, 15], what is nums[-1]?", "choices": ["5", "10", "15", "Error"], "answer": 2, "explanation": "Negative index -1 is the last element."},
            {"id": "7.q2", "question": "Slicing past the end of a list:", "choices": ["Raises an IndexError", "Just returns whatever elements exist, no error", "Deletes the list", "Is not allowed"], "answer": 1, "explanation": "Unlike direct indexing, slicing tolerates out-of-range bounds."},
            {"id": "7.q3", "question": "Which correctly adds 80 to the end of a list using concatenation?", "choices": ["grades += 80", "grades += [80]", "grades.add(80)", "grades[len(grades)] = 80 on an empty slot"], "answer": 1, "explanation": "+= needs a list on the right side, so [80] rather than a bare 80."},
            {"id": "7.q4", "question": "for i in mylist: i += 1 will:", "choices": ["Increase every element of mylist by 1", "Leave mylist unchanged", "Raise an error", "Double the list's length"], "answer": 1, "explanation": "i is a copy of each value in this loop form, so the list itself is never modified."},
            {"id": "7.q5", "question": "enumerate(mylist) is most useful when you need:", "choices": ["Only values", "Only indices", "Both index and value together", "Nothing from the list"], "answer": 2, "explanation": "enumerate() pairs each index with its corresponding value."},
        ],
    },
    "8": {
        "id": "8",
        "title": "Top-Down Design; Dictionaries",
        "intro": "This module introduces top-down design — organizing a complex problem as a hierarchy, "
                 "breaking it into smaller and smaller pieces — and dictionaries, which store data as "
                 "key-value pairs instead of numbered positions.",
        "components": [
            {
                "id": "8.1",
                "title": "Top-Down Design and Hierarchies",
                "explanation": (
                    "Top-down design starts with the most general idea and repeatedly divides it into "
                    "smaller, more specific pieces until each piece is simple enough to implement "
                    "directly. The result is a hierarchy — in computing, usually called a tree. A tree "
                    "has a root at the top; individual elements are nodes; a node's parent is the node "
                    "above it, its children are the nodes below it, and nodes with no children are "
                    "leaves.\n\n"
                    "Hierarchies show up everywhere — a university's org chart, a body's systems -> "
                    "organs -> cells, a sports league's conferences and divisions — because breaking a "
                    "big idea into a tree makes each piece easier to understand on its own."
                ),
                "examples": [
                    {
                        "code": "# Top-down design of a vacation plan (as comments = a design outline)\n# Vacation\n#   Transportation\n#   Hotel\n#   Activities\n#   Food\nprint(\"Design outlines don't need to run — they're a planning tool\")",
                        "output": "Design outlines don't need to run — they're a planning tool",
                        "note": "Turning a hierarchy into indented comments is a common first step before writing any real code.",
                    }
                ],
                "practice": [
                    {
                        "id": "8.1.p1",
                        "question": "In tree/hierarchy terminology, a node with no children is called a:",
                        "choices": ["Root", "Leaf", "Parent", "Branch only"],
                        "answer": 1,
                        "explanation": "Nodes without children are leaves."},
                    {
                        "id": "8.1.p2",
                        "question": "Top-down design means:",
                        "choices": [
                            "Writing code from the bottom of the file upward",
                            "Starting with the general problem and repeatedly breaking it into smaller pieces",
                            "Never planning ahead",
                            "Avoiding functions",
                        ],
                        "answer": 1,
                        "explanation": "It's a planning approach: divide the big problem into a hierarchy before coding details."},
                ],
            },
            {
                "id": "8.2",
                "title": "Dictionaries: Keys and Values",
                "explanation": (
                    "A dictionary stores key-value pairs instead of numbered positions: "
                    "age = {'John': 21, 'Jill': 21}. Create one with {}, or {} alone for an empty "
                    "dictionary. Both key and value can be any type. Look up a value with its key in "
                    "square brackets — age['John'] — and add or update an entry the same way a variable "
                    "is assigned: age['James'] = 20."
                ),
                "examples": [
                    {
                        "code": "age = {'John': 21, 'Jill': 21}\nprint(age['John'])\nage['James'] = 20\nprint(age)",
                        "output": "21\n{'John': 21, 'Jill': 21, 'James': 20}",
                        "note": "Looking up age['John'] uses the key directly; assigning to a new key adds it to the dictionary.",
                    }
                ],
                "practice": [
                    {
                        "id": "8.2.p1",
                        "question": "For d = {'a': 1, 'b': 2}, what does d['b'] return?",
                        "choices": ["1", "2", "'b'", "Error"],
                        "answer": 1,
                        "explanation": "d['b'] looks up the value stored under key 'b'."},
                    {
                        "id": "8.2.p2",
                        "question": "How is a dictionary different from a list?",
                        "choices": [
                            "It cannot store numbers",
                            "It's accessed by keys (which can be any type) instead of numeric position",
                            "It can only hold one value",
                            "There is no real difference",
                        ],
                        "answer": 1,
                        "explanation": "Dictionaries map keys to values rather than ordering items by numeric position."},
                ],
            },
            {
                "id": "8.3",
                "title": "Working with Dictionaries",
                "explanation": (
                    "Loop over a dictionary with a regular for loop — for key in my_dict: — and the "
                    "iterator takes on each KEY (not the value); use my_dict[key] inside the loop to get "
                    "the matching value. The in operator tests whether something is a key in the "
                    "dictionary: if 'James' in age:."
                ),
                "examples": [
                    {
                        "code": "age = {'John': 21, 'Jill': 21, 'James': 20}\nfor key in age:\n    print(f\"key {key}, value {age[key]}\")\nif 'James' in age:\n    print(\"Yes for James\")\nif 'Joe' in age:\n    print(\"Yes for Joe\")\nelse:\n    print(\"No for Joe\")",
                        "output": "key John, value 21\nkey Jill, value 21\nkey James, value 20\nYes for James\nNo for Joe",
                        "note": "The for loop's iterator takes each key in turn; age[key] then looks up the matching value.",
                    }
                ],
                "practice": [
                    {
                        "id": "8.3.p1",
                        "question": "for k in my_dict: — what does k take the value of, each time through the loop?",
                        "choices": ["Each value", "Each key", "Both key and value together", "Nothing useful"],
                        "answer": 1,
                        "explanation": "Looping directly over a dictionary iterates its keys."},
                    {
                        "id": "8.3.p2",
                        "question": "'x' in my_dict tests whether:",
                        "choices": ["'x' is a value in the dictionary", "'x' is a key in the dictionary", "The dictionary is empty", "'x' equals the dictionary"],
                        "answer": 1,
                        "explanation": "in checks dictionary keys, not values."},
                ],
            },
        ],
        "quiz": [
            {"id": "8.q1", "question": "In a tree hierarchy, the node at the very top is called the:", "choices": ["Leaf", "Root", "Child", "Branch"], "answer": 1, "explanation": "The topmost node is the root."},
            {"id": "8.q2", "question": "For d = {'x': 5}, how do you access the value 5?", "choices": ["d[0]", "d['x']", "d.x", "d.get(0)"], "answer": 1, "explanation": "Dictionary values are accessed with their key in square brackets."},
            {"id": "8.q3", "question": "for k in my_dict: iterates over:", "choices": ["The dictionary's values", "The dictionary's keys", "Nothing", "Key-value pairs directly as tuples"], "answer": 1, "explanation": "A plain for loop over a dictionary yields its keys."},
            {"id": "8.q4", "question": "d['new_key'] = 10 on an existing dictionary d:", "choices": ["Raises an error", "Adds a new key or updates an existing one", "Deletes d", "Does nothing"], "answer": 1, "explanation": "Assigning to a dictionary key adds it if missing, or updates it if present."},
            {"id": "8.q5", "question": "Top-down design produces what kind of structure?", "choices": ["A single flat list", "A hierarchy (tree)", "A random arrangement", "A dictionary only"], "answer": 1, "explanation": "Repeated breakdown from general to specific naturally produces a tree structure."},
        ],
    },
    "9": {
        "id": "9",
        "title": "Advanced Functions, Scope",
        "intro": "This module goes deeper into functions: how arguments and return values pass data in "
                 "and out, tuples for returning more than one value, the scope rules that keep a "
                 "function's variables separate from everything else, and how mutable data like lists "
                 "behaves differently when passed as an argument.",
        "components": [
            {
                "id": "9.1",
                "title": "Functions as Black Boxes",
                "explanation": (
                    "Think of a function as a black box: it takes input through arguments (also called "
                    "parameters), does something, and may return a value. def <name>(<parameters>): "
                    "starts a function definition; the indented body is its code. A function must be "
                    "defined before it's called — the interpreter just remembers the function's name and "
                    "body when it's defined, and only runs that body when the function is actually "
                    "called."
                ),
                "examples": [
                    {
                        "code": 'def warn():\n    print("********** WARNING! **********")\n    print("You are about to do something dangerous!")\n\ndef doublewarn():\n    warn()\n    warn()\n\ndoublewarn()',
                        "output": "********** WARNING! **********\nYou are about to do something dangerous!\n********** WARNING! **********\nYou are about to do something dangerous!",
                        "note": "doublewarn() calls warn() twice; each call jumps to warn()'s body, runs it fully, then returns to where it was called.",
                    }
                ],
                "practice": [
                    {
                        "id": "9.1.p1",
                        "question": "What must happen before a function can be called?",
                        "choices": ["Nothing special", "It must be defined earlier in the program", "It must return a value", "It must have no parameters"],
                        "answer": 1,
                        "explanation": "Calling an undefined function raises a NameError — definitions must come first."},
                    {
                        "id": "9.1.p2",
                        "question": "Thinking of a function as a 'black box' means:",
                        "choices": [
                            "You must know its exact internal code to use it",
                            "You only need to know its inputs and outputs, not how it works internally",
                            "It never returns anything",
                            "It can't take arguments",
                        ],
                        "answer": 1,
                        "explanation": "The black-box view focuses on inputs/outputs, hiding internal implementation details."},
                ],
            },
            {
                "id": "9.2",
                "title": "Tuples and Multiple Return Values",
                "explanation": (
                    "A function can only return one value — but that value can be a tuple, letting it "
                    "effectively return several values at once. A tuple looks like a list but uses "
                    "parentheses (or no brackets at all) and is immutable: once created, its values can't "
                    "be changed. You can 'unpack' a tuple's values directly into separate variables: "
                    "a, b = some_function()."
                ),
                "examples": [
                    {
                        "code": "def min_max(numbers):\n    return min(numbers), max(numbers)\n\nlo, hi = min_max([4, 9, 2, 7])\nprint(lo, hi)",
                        "output": "2 9",
                        "note": "min_max returns a tuple (2, 9); writing lo, hi = ... unpacks it into two separate variables in one step.",
                    }
                ],
                "practice": [
                    {
                        "id": "9.2.p1",
                        "question": "How many values can a Python function actually return?",
                        "choices": [
                            "As many separate values as it wants",
                            "Exactly one value — though that value can be a tuple holding several",
                            "Zero, always",
                            "It depends on the number of parameters",
                        ],
                        "answer": 1,
                        "explanation": "Multiple 'return values' are really one tuple, which the caller can unpack."},
                    {
                        "id": "9.2.p2",
                        "question": "What makes a tuple different from a list?",
                        "choices": [
                            "Tuples can't hold numbers",
                            "Tuples are immutable — their contents can't be changed after creation",
                            "Tuples can only have one element",
                            "There's no real difference",
                        ],
                        "answer": 1,
                        "explanation": "Lists can be modified after creation; tuples cannot."},
                ],
            },
            {
                "id": "9.3",
                "title": "Scope: Local vs Global",
                "explanation": (
                    "A local variable is defined inside a function and lives only in that function's own "
                    "area of memory — other functions (and the main program) can't see it. A global "
                    "variable is defined in the main program. A function CAN read a global variable if "
                    "it has no local variable of the same name — but relying on this is bad style. "
                    "Functions should stand on their own, understandable just by looking at their "
                    "parameters and return value, without needing to know about outside variables."
                ),
                "examples": [
                    {
                        "code": 'def my_function():\n    a = 3\n    print(a)\n\na = 5\nprint(a)\nmy_function()\nprint(a)',
                        "output": "5\n3\n5",
                        "note": "The a inside my_function is a completely separate variable from the a in the main program — each has its own memory.",
                    }
                ],
                "practice": [
                    {
                        "id": "9.3.p1",
                        "question": "A variable created inside a function is:",
                        "choices": ["Global, visible everywhere", "Local, living only in that function's own memory", "Deleted immediately", "Automatically printed"],
                        "answer": 1,
                        "explanation": "Local variables exist only within the function that creates them."},
                    {
                        "id": "9.3.p2",
                        "question": "Why is it bad style for a function to read a global variable directly?",
                        "choices": [
                            "It's actually good style",
                            "The function then can't be understood or reused without knowing about outside code",
                            "It causes a syntax error",
                            "Python doesn't allow it at all",
                        ],
                        "answer": 1,
                        "explanation": "Functions should be understandable on their own, using only their parameters and return value."},
                ],
            },
            {
                "id": "9.4",
                "title": "Passing Arguments and Mutable Data",
                "explanation": (
                    "When a function is called, each argument's value is copied into the function's own "
                    "parameter variable — reassigning that parameter never affects the caller's variable. "
                    "Lists (and dictionaries) behave differently, though: they're mutable, so if a "
                    "function modifies an element of a list passed in, that change IS visible outside the "
                    "function — but assigning the parameter itself a brand-new list is not."
                ),
                "examples": [
                    {
                        "code": "def dosomething(a):\n    a = [10, 11, 12]\n\nx = [1, 2, 3]\ndosomething(x)\nprint(x)\n\ndef dosomething2(a):\n    a[0] = 10\n\ny = [1, 2, 3]\ndosomething2(y)\nprint(y)",
                        "output": "[1, 2, 3]\n[10, 2, 3]",
                        "note": "Reassigning a to a new list inside the function doesn't affect x — but changing a[0] does modify y, since lists are mutable.",
                    }
                ],
                "practice": [
                    {
                        "id": "9.4.p1",
                        "question": "def f(a): a = 99  ...  x = 5; f(x); print(x) — what prints?",
                        "choices": ["99", "5", "Error", "None"],
                        "answer": 1,
                        "explanation": "Reassigning the parameter a never changes the caller's variable x."},
                    {
                        "id": "9.4.p2",
                        "question": "def f(a): a[0] = 99  ...  y = [1,2,3]; f(y); print(y) — what prints?",
                        "choices": ["[1, 2, 3]", "[99, 2, 3]", "Error", "None"],
                        "answer": 1,
                        "explanation": "Since lists are mutable, modifying an element inside the function changes the same list the caller holds."},
                ],
            },
        ],
        "quiz": [
            {"id": "9.q1", "question": "A function must be ___ before it can be called.", "choices": ["Returned", "Defined", "Imported from math", "Printed"], "answer": 1, "explanation": "Definitions must appear before the corresponding call."},
            {"id": "9.q2", "question": "A Python function can actually return:", "choices": ["Multiple separate values directly", "Exactly one value (which can be a tuple)", "Nothing, ever", "Only integers"], "answer": 1, "explanation": "Multiple return values are packaged into one tuple."},
            {"id": "9.q3", "question": "A variable defined inside a function is:", "choices": ["Global", "Local to that function", "Deleted on creation", "Shared with all functions"], "answer": 1, "explanation": "It exists only within that function's own scope."},
            {"id": "9.q4", "question": "def f(a): a[0]=99 ... y=[1,2,3]; f(y); print(y) prints:", "choices": ["[1,2,3]", "[99,2,3]", "Error", "None"], "answer": 1, "explanation": "Modifying a mutable list's element inside a function affects the caller's list too."},
            {"id": "9.q5", "question": "def f(a): a=99 ... x=5; f(x); print(x) prints:", "choices": ["99", "5", "Error", "None"], "answer": 1, "explanation": "Reassigning a parameter doesn't change the argument passed in from the caller."},
        ],
    },
    "10": {
        "id": "10",
        "title": "Systematic Debugging",
        "intro": "Everyone writes bugs — good programmers just find and fix them faster. This module "
                 "covers the three types of errors, handling runtime errors gracefully with try/except, "
                 "and a systematic process (DRIFT) for tracking down and fixing bugs.",
        "components": [
            {
                "id": "10.1",
                "title": "Three Types of Errors",
                "explanation": (
                    "Syntax errors break Python's grammar rules (a misspelled keyword, using = instead "
                    "of ==) — the editor usually catches these before the program even runs. Run-time "
                    "errors (exceptions) happen while the program executes, like dividing by zero or "
                    "indexing past the end of a list — often not predictable ahead of time. Logic errors "
                    "are the toughest: the code runs fine, but produces the wrong answer, often because "
                    "of a typo or a misunderstanding about what the code actually does."
                ),
                "examples": [
                    {
                        "code": "my_list = [1, 2, 3]\nprint(my_list[10])",
                        "output": "IndexError: list index out of range",
                        "note": "This is a run-time error: the code is valid Python, but index 10 doesn't exist in a 3-item list.",
                    }
                ],
                "practice": [
                    {
                        "id": "10.1.p1",
                        "question": "A program that runs to completion but gives the wrong answer has a:",
                        "choices": ["Syntax error", "Run-time error", "Logic error", "No error at all"],
                        "answer": 2,
                        "explanation": "Logic errors don't crash the program — they just produce incorrect results."},
                    {
                        "id": "10.1.p2",
                        "question": "Dividing by zero at run time raises a:",
                        "choices": ["SyntaxError", "ZeroDivisionError (a run-time error)", "Logic error only", "Nothing — it's allowed"],
                        "answer": 1,
                        "explanation": "This is caught only while the program executes, since it depends on the actual values involved."},
                ],
            },
            {
                "id": "10.2",
                "title": "Handling Errors with try/except",
                "explanation": (
                    "try: wraps code that might fail; if no error occurs, the except block is skipped "
                    "entirely. If a run-time error DOES occur, Python jumps straight to a matching "
                    "except <exception_type>: block instead of crashing. Common exception types include "
                    "TypeError, IndexError, ZeroDivisionError, and NameError. Leaving off the type "
                    "(except:) catches any exception at all."
                ),
                "examples": [
                    {
                        "code": 'a = 10\nb = 0\ntry:\n    c = a / b\nexcept ZeroDivisionError:\n    print("You can\'t divide by 0!")\n    b = 2\n    c = a / b\nprint(c)',
                        "output": "You can't divide by 0!\n5.0",
                        "note": "Dividing by 0 raises ZeroDivisionError, so the except block runs, fixes b, and retries the division.",
                    }
                ],
                "practice": [
                    {
                        "id": "10.2.p1",
                        "question": "What happens to the except block if the try block runs with no error?",
                        "choices": ["It runs anyway", "It is skipped entirely", "It raises an error", "It runs twice"],
                        "answer": 1,
                        "explanation": "except only runs if a matching exception actually occurs in the try block."},
                    {
                        "id": "10.2.p2",
                        "question": "Which exception type matches trying to access index 20 of a 5-item list?",
                        "choices": ["TypeError", "IndexError", "ZeroDivisionError", "NameError"],
                        "answer": 1,
                        "explanation": "Accessing an out-of-range list position raises IndexError."},
                ],
            },
            {
                "id": "10.3",
                "title": "A Systematic Debugging Process: DRIFT",
                "explanation": (
                    "Rather than randomly changing code and hoping it works, follow DRIFT: Discover a "
                    "repeatable problem; Reproduce it with a reliable test case; Isolate the bug's "
                    "location by narrowing down where things go wrong (e.g. with print statements or a "
                    "debugger's breakpoints); Fix the bug; Test to confirm the original case now passes "
                    "and nothing else broke.\n\n"
                    "IDE debuggers (VS Code, Spyder, PyCharm) support breakpoints (pause execution at a "
                    "line), step/step-into (run one line at a time), and examining variable values — "
                    "useful tools for the Isolate step, though they don't fix bugs for you."
                ),
                "examples": [
                    {
                        "code": "total = 0\nfor n in [1, 2, 3]:\n    total += n\n    print(\"n =\", n, \"running total =\", total)",
                        "output": "n = 1 running total = 1\nn = 2 running total = 3\nn = 3 running total = 6",
                        "note": "Printing state at each step like this is exactly what the Isolate step of DRIFT looks like in practice.",
                    }
                ],
                "practice": [
                    {
                        "id": "10.3.p1",
                        "question": "In the DRIFT process, what comes right after Discover?",
                        "choices": ["Fix", "Reproduce — create a reliable test case", "Test", "Isolate"],
                        "answer": 1,
                        "explanation": "D-R-I-F-T: Discover, Reproduce, Isolate, Fix, Test."},
                    {
                        "id": "10.3.p2",
                        "question": "What does a breakpoint do in an IDE debugger?",
                        "choices": ["Deletes that line of code", "Pauses execution at that line so you can examine memory", "Fixes the bug automatically", "Comments out the line"],
                        "answer": 1,
                        "explanation": "A breakpoint pauses the program at a chosen line for inspection."},
                ],
            },
        ],
        "quiz": [
            {"id": "10.q1", "question": "A program that crashes because of invalid Python grammar has a:", "choices": ["Logic error", "Syntax error", "Run-time error", "No error"], "answer": 1, "explanation": "Grammar violations are syntax errors, usually caught before running."},
            {"id": "10.q2", "question": "except ZeroDivisionError: runs when:", "choices": ["The try block succeeds", "A division by zero occurs inside the matching try block", "The program starts", "Never"], "answer": 1, "explanation": "except only runs for a matching exception raised in try."},
            {"id": "10.q3", "question": "In DRIFT, the 'I' stands for:", "choices": ["Ignore", "Isolate — narrow down where the bug is", "Import", "Interpret"], "answer": 1, "explanation": "Isolate means narrowing down the bug's exact location."},
            {"id": "10.q4", "question": "A program that runs fine but gives the wrong answer has a:", "choices": ["Syntax error", "Run-time error", "Logic error", "No error"], "answer": 2, "explanation": "Logic errors produce wrong results without crashing."},
            {"id": "10.q5", "question": "A breakpoint in a debugger:", "choices": ["Automatically fixes bugs", "Pauses execution at a chosen line for inspection", "Deletes the program", "Only works with syntax errors"], "answer": 1, "explanation": "Breakpoints pause a running program so you can examine its state."},
        ],
    },
    "11": {
        "id": "11",
        "title": "File Input and Output",
        "intro": "Programs often need to save data between runs or read data someone else prepared. This "
                 "module covers opening, reading from, and writing to files, and processing strings — "
                 "especially the lines read from a file — with split(), strip(), and join().",
        "components": [
            {
                "id": "11.1",
                "title": "Opening, Writing, and Closing Files",
                "explanation": (
                    "fileID = open(\"filename\", \"mode\") opens a file and assigns it to a variable. "
                    "Common modes: \"r\" reads an existing file, \"w\" writes (creating the file, or "
                    "erasing it if it already exists), and \"a\" appends to the end. Use fileID.write(text) "
                    "to write — unlike print(), write() only accepts one string, never adds a space "
                    "between calls, and never adds a newline automatically (add \\n yourself).\n\n"
                    "Always close a file with fileID.close() when done, or use with open(...) as "
                    "fileID: — which closes the file automatically once its indented block ends, even if "
                    "an error occurs partway through."
                ),
                "examples": [
                    {
                        "code": 'with open("scores.txt", "w") as f:\n    f.write("Testing the write command.\\n")\n    x = 987\n    f.write("Here\'s a number: " + str(x) + "\\n")',
                        "output": "",
                        "note": "Nothing prints here — this writes two lines to scores.txt. write() needs \\n explicitly, and only accepts strings (str(x) converts the number first).",
                    }
                ],
                "practice": [
                    {
                        "id": "11.1.p1",
                        "question": 'open("data.txt", "w") on a file that already has content will:', "choices": [
                            "Append to the existing content",
                            "Erase the existing content and start fresh",
                            "Refuse to open it",
                            "Read it instead",
                        ],
                        "answer": 1,
                        "explanation": '"w" mode opens for writing and erases whatever was already in the file.',
                    },
                    {
                        "id": "11.1.p2",
                        "question": "Does fileID.write() add a newline automatically, like print() does?",
                        "choices": ["Yes, always", "No — you must add \\n yourself", "Only in 'a' mode", "Only for the first write"],
                        "answer": 1,
                        "explanation": "write() writes exactly the string given, with no automatic separator or newline.",
                    },
                ],
            },
            {
                "id": "11.2",
                "title": "Reading From Files",
                "explanation": (
                    "fileID.readline() reads one line at a time as a string, returning '' once the file "
                    "is exhausted. fileID.read() reads the ENTIRE file into one (possibly huge) string. "
                    "fileID.readlines() reads every line into a list of strings. Most often, though, "
                    "you'll loop directly over the file: for line in fileID: gives you one line per "
                    "iteration, just like looping through a list."
                ),
                "examples": [
                    {
                        "code": 'with open("scores.txt", "r") as f:\n    for line in f:\n        print(line, end=\'\')',
                        "output": "Testing the write command.\nHere's a number: 987",
                        "note": "end='' avoids doubling up newlines, since each line already ends with its own \\n from the file.",
                    }
                ],
                "practice": [
                    {
                        "id": "11.2.p1",
                        "question": "for line in fileID: (fileID is an open file) gives you:",
                        "choices": ["The whole file at once", "One line per iteration", "Only the first line", "The file's name"],
                        "answer": 1,
                        "explanation": "Iterating directly over a file object yields one line per pass, like iterating a list."},
                    {
                        "id": "11.2.p2",
                        "question": "fileID.readlines() returns:",
                        "choices": ["A single string with the whole file", "A list of strings, one per line", "Just the first line", "Nothing — it's write-only"],
                        "answer": 1,
                        "explanation": "readlines() converts the file's lines into a list of strings."},
                ],
            },
            {
                "id": "11.3",
                "title": "String Processing: split, strip, join",
                "explanation": (
                    "mystring.split(separator) breaks a string into a list of strings wherever the "
                    "separator appears — useful for pulling apart a line read from a file, like "
                    "\"11/01/2023\".split('/'). mystring.strip() removes leading and trailing whitespace "
                    "(including the trailing \\n a file line usually has). separator.join(list_of_strings) "
                    "does the reverse, gluing a list of strings back together with a separator between "
                    "them. These methods are often chained together in one line."
                ),
                "examples": [
                    {
                        "code": "date = \"11/01/2023\"\nmonth, day, year = date.split('/')\nprint(f\"Day: {day} Month: {month} Year: {year}\")\n\nmystr = \"  1,2,3,4,5  \\n\"\nprint(mystr.strip().split(','))\nprint('.'.join(mystr.strip().split(',')))",
                        "output": "Day: 01 Month: 11 Year: 2023\n['1', '2', '3', '4', '5']\n1.2.3.4.5",
                        "note": "split('/') on the date gives a 3-item list unpacked directly into month/day/year; strip() then split() then join() are chained in one line.",
                    }
                ],
                "practice": [
                    {
                        "id": "11.3.p1",
                        "question": '"a,b,c".split(\',\') returns:', "choices": ["'a,b,c'", "['a', 'b', 'c']", "('a', 'b', 'c')", "Error"],
                        "answer": 1,
                        "explanation": "split() always returns a list of strings.",
                    },
                    {
                        "id": "11.3.p2",
                        "question": "Why call .strip() on a line read from a file before splitting or converting it?",
                        "choices": [
                            "It's not necessary",
                            "The line includes a trailing newline character that would otherwise cause problems",
                            "strip() converts text to numbers",
                            "It closes the file",
                        ],
                        "answer": 1,
                        "explanation": "Lines from a file end in \\n; strip() removes it before further processing.",
                    },
                ],
            },
        ],
        "quiz": [
            {"id": "11.q1", "question": 'open(filename, "r") opens a file for:', "choices": ["Writing only", "Reading", "Deleting", "Renaming"], "answer": 1, "explanation": '"r" mode opens a file for reading.'},
            {"id": "11.q2", "question": "Why prefer with open(...) as f: over a plain open() call?", "choices": ["It reads faster", "It closes the file automatically, even if an error occurs", "It's required to write files", "It prevents typos"], "answer": 1, "explanation": "The with block guarantees proper file closing."},
            {"id": "11.q3", "question": "Does fileID.write() add a newline automatically?", "choices": ["Yes", "No, you add \\n yourself", "Only for the first line", "Only in append mode"], "answer": 1, "explanation": "write() only writes exactly what's given."},
            {"id": "11.q4", "question": "for line in fileID: iterates:", "choices": ["Once for the whole file", "Once per line in the file", "Once per character", "Never"], "answer": 1, "explanation": "Each iteration yields the next line."},
            {"id": "11.q5", "question": '"11/01/2023".split(\'/\') returns:', "choices": ["'11/01/2023'", "['11', '01', '2023']", "('11','01','2023',)", "Error"], "answer": 1, "explanation": "split() breaks the string apart at every '/' into a list of strings."},
        ],
    },
    "12": {
        "id": "12",
        "title": "Using Engineering Modules in Python",
        "intro": "Python's standard library — and thousands of external packages — provide ready-made "
                 "functions you don't have to write yourself. This module covers what modules and "
                 "packages are, the different ways to import them, and how to get more of them.",
        "components": [
            {
                "id": "12.1",
                "title": "What Are Modules and Packages?",
                "explanation": (
                    "A module is a file of Python code someone else wrote — typically defining "
                    "functions, and sometimes constants. You've already used one: the math module "
                    "defines functions like sqrt() and sin(), plus the constant pi. A package is a "
                    "collection of related modules bundled together; you access a module inside a "
                    "package with package_name.module_name, like matplotlib.pyplot.\n\n"
                    "Using modules means you don't need to write (or even fully understand) everything "
                    "yourself — you get access to code many other people have already built and tested."
                ),
                "examples": [
                    {
                        "code": "import math\nprint(math.sqrt(2.0))",
                        "output": "1.4142135623730951",
                        "note": "Once imported, every function in the math module is available through the math. prefix.",
                    }
                ],
                "practice": [
                    {
                        "id": "12.1.p1",
                        "question": "A Python module is best described as:",
                        "choices": [
                            "A file of code someone else wrote, usually defining functions",
                            "A type of loop",
                            "A syntax error",
                            "A single variable",
                        ],
                        "answer": 0,
                        "explanation": "Modules are files of pre-written code you can import and reuse.",
                    },
                    {
                        "id": "12.1.p2",
                        "question": "matplotlib.pyplot refers to:",
                        "choices": [
                            "A variable named pyplot",
                            "The pyplot module inside the matplotlib package",
                            "An error in Python",
                            "A function with two names",
                        ],
                        "answer": 1,
                        "explanation": "package_name.module_name accesses a module inside a package.",
                    },
                ],
            },
            {
                "id": "12.2",
                "title": "Ways to Import",
                "explanation": (
                    "import module_name brings in the whole module; call its functions with "
                    "module_name.function_name(). from module_name import name1, name2 imports just "
                    "those specific names, so you can call them directly without the module prefix. "
                    "from module_name import * imports everything — convenient, but risky, since a new "
                    "name could silently override one you already had. You can also rename something as "
                    "you import it: from math import sqrt as sr lets you call sr(2.0) instead."
                ),
                "examples": [
                    {
                        "code": "from math import sin, sqrt, pi\na = sqrt(2.0)\nb = sin(pi / 4)\nprint(a, b)",
                        "output": "1.4142135623730951 0.7071067811865476",
                        "note": "Since sqrt, sin, and pi were imported by name, they're called directly with no math. prefix needed.",
                    }
                ],
                "practice": [
                    {
                        "id": "12.2.p1",
                        "question": "After from math import sqrt, how do you call it?",
                        "choices": ["math.sqrt(x)", "sqrt(x)", "import.sqrt(x)", "sqrt.math(x)"],
                        "answer": 1,
                        "explanation": "Importing a specific name lets you call it directly, without the module prefix.",
                    },
                    {
                        "id": "12.2.p2",
                        "question": "Why is from module import * generally discouraged?",
                        "choices": [
                            "It's slower than other imports",
                            "You may not know everything you're bringing in, and it could silently override an existing name",
                            "It only works with the math module",
                            "It doesn't actually work in Python",
                        ],
                        "answer": 1,
                        "explanation": "Importing everything makes it unclear what names you now have, risking accidental conflicts.",
                    },
                ],
            },
            {
                "id": "12.3",
                "title": "Getting More Modules",
                "explanation": (
                    "Python ships with many built-in modules (math, random, statistics, and 200+ more) "
                    "— you still have to import them, but nothing extra to install. Beyond that, "
                    "external packages (like numpy for vector/matrix math, matplotlib for plotting, or "
                    "pandas for data processing) can be installed with pip: pip install package_name, "
                    "run from your IDE's terminal. Once installed, they're imported exactly like any "
                    "built-in module."
                ),
                "examples": [
                    {
                        "code": "import random\nrandom.seed(42)\nprint(random.randint(1, 10))",
                        "output": "2",
                        "note": "random is a built-in module — no installation needed, just import it; seed(42) makes the 'random' result reproducible here.",
                    }
                ],
                "practice": [
                    {
                        "id": "12.3.p1",
                        "question": "Which of these is a built-in Python module, needing no separate install?",
                        "choices": ["random", "numpy", "pandas", "matplotlib"],
                        "answer": 0,
                        "explanation": "random ships with Python; numpy, pandas, and matplotlib are external packages you'd install with pip.",
                    },
                    {
                        "id": "12.3.p2",
                        "question": "How do you install an external package like numpy?",
                        "choices": ["import numpy install", "pip install numpy, from a terminal", "It's automatic", "Rewrite it yourself"],
                        "answer": 1,
                        "explanation": "pip is the standard tool for installing external Python packages.",
                    },
                ],
            },
        ],
        "quiz": [
            {"id": "12.q1", "question": "A module is best described as:", "choices": ["A syntax error", "A file of pre-written code you can import", "A type of variable", "A comment"], "answer": 1, "explanation": "Modules bundle reusable, pre-written code."},
            {"id": "12.q2", "question": "After import math, how do you call sqrt()?", "choices": ["sqrt(x)", "math.sqrt(x)", "math->sqrt(x)", "import.sqrt(x)"], "answer": 1, "explanation": "A whole-module import requires the module_name. prefix."},
            {"id": "12.q3", "question": "from math import sqrt as sr lets you call:", "choices": ["math.sqrt(x)", "sr(x)", "sqrt.sr(x)", "as(x)"], "answer": 1, "explanation": "The as keyword renames the imported function for use in your code."},
            {"id": "12.q4", "question": "Which of these needs pip install before you can import it?", "choices": ["math", "random", "numpy", "None of them do"], "answer": 2, "explanation": "numpy is an external package; math and random are built into Python."},
            {"id": "12.q5", "question": "A key risk of from module import * is:", "choices": ["It's not valid Python", "It can silently override names you already have, without you noticing", "It only imports one function", "It disables the module"], "answer": 1, "explanation": "Bringing in everything makes accidental name conflicts more likely."},
        ],
    },
    "13": {
        "id": "13",
        "title": "Functions in Top-Down / Bottom-Up Design",
        "intro": "This final module ties functions together with the design ideas from earlier in the "
                 "course: building a program's structure from the top down, building and combining "
                 "small tested pieces from the bottom up, documenting functions with docstrings, and "
                 "the idea of abstraction that ties it all together.",
        "components": [
            {
                "id": "13.1",
                "title": "Top-Down Design With Functions",
                "explanation": (
                    "Each node of a top-down hierarchy can become its own function — the smallest nodes "
                    "are functions that don't call anything else, while higher-level functions call "
                    "several others to do their work. When writing the code, define child functions "
                    "BEFORE the parent functions that call them, so those calls work; the main program's "
                    "code (the actual function calls, in order) goes at the bottom.\n\n"
                    "This separation makes changes easy: if you decide to read input from a file instead "
                    "of the console, you only change the implementation of that one function — nothing "
                    "that calls it needs to know how it works internally."
                ),
                "examples": [
                    {
                        "code": "def get_numbers():\n    return [3, 7, 2, 9]\n\ndef find_largest(numbers):\n    return max(numbers)\n\ndef main():\n    nums = get_numbers()\n    largest = find_largest(nums)\n    print(\"Largest:\", largest)\n\nmain()",
                        "output": "Largest: 9",
                        "note": "main() reads like an outline of the whole program's top-down design: get data, then process it, then show the result.",
                    }
                ],
                "practice": [
                    {
                        "id": "13.1.p1",
                        "question": "When converting a top-down hierarchy into functions, child functions should be defined:",
                        "choices": ["After their parent function", "Before the parent function that calls them", "It doesn't matter", "Only inside main()"],
                        "answer": 1,
                        "explanation": "A function must be defined before it's called, so children come first in the file."},
                    {
                        "id": "13.1.p2",
                        "question": "If you change how get_numbers() reads its data (console vs. file), what else must change?",
                        "choices": [
                            "Every function in the program",
                            "Nothing that calls get_numbers() needs to change, as long as it still returns the same thing",
                            "main() must be rewritten entirely",
                            "The program can no longer run",
                        ],
                        "answer": 1,
                        "explanation": "Separating functions by task means internal changes don't ripple outward, as long as the interface stays the same."},
                ],
            },
            {
                "id": "13.2",
                "title": "Bottom-Up Design",
                "explanation": (
                    "Bottom-up design starts from the other direction: build and test small, useful "
                    "functions for things you already know you'll need (like converting Celsius to "
                    "Fahrenheit), then combine them into bigger and bigger pieces until they form your "
                    "whole program. Create a new function whenever you spot something that will be done "
                    "repeatedly, or a key concept that can be built cleanly from what you already have.\n\n"
                    "In practice, most real design blends both directions: sketch the overall structure "
                    "top-down, while building and testing the small reusable pieces bottom-up."
                ),
                "examples": [
                    {
                        "code": "def celsius_to_fahrenheit(c):\n    return c * 9 / 5 + 32\n\nprint(celsius_to_fahrenheit(0))\nprint(celsius_to_fahrenheit(100))",
                        "output": "32.0\n212.0",
                        "note": "This is exactly the kind of small, independently useful function bottom-up design starts with — tested here against known values (0C=32F, 100C=212F).",
                    }
                ],
                "practice": [
                    {
                        "id": "13.2.p1",
                        "question": "Bottom-up design means:",
                        "choices": [
                            "Writing the whole program before testing anything",
                            "Building and testing small, useful functions first, then combining them into larger pieces",
                            "Never using functions",
                            "Skipping the planning stage entirely",
                        ],
                        "answer": 1,
                        "explanation": "Each small, reusable piece is built and verified before being combined into something larger."},
                    {
                        "id": "13.2.p2",
                        "question": "A good reason to create a new function is:",
                        "choices": [
                            "You'll only ever use the code once, in one place",
                            "You realize you'll need to do the same task repeatedly",
                            "The code is exactly one line",
                            "Never — functions should be avoided",
                        ],
                        "answer": 1,
                        "explanation": "Repeated tasks are a classic signal that a reusable function is worth writing."},
                ],
            },
            {
                "id": "13.3",
                "title": "Docstrings and Abstraction",
                "explanation": (
                    "A docstring documents a function: the first line right after def is a string "
                    "(usually triple-quoted) describing what the function does. Python's built-in "
                    "help(function_name) command displays it — handy for anyone using your function "
                    "without reading its internals.\n\n"
                    "That's really the whole point of top-down design, bottom-up design, and functions "
                    "in general: abstraction — the ability to use a well-documented piece of code "
                    "without worrying about exactly how it works inside. It's one of the most important "
                    "ideas in all of computing, letting you focus on one part of a problem at a time."
                ),
                "examples": [
                    {
                        "code": 'def drawsquare():\n    """Draw a square and return to original position and orientation"""\n    pass\n\nhelp(drawsquare)',
                        "output": "Help on function drawsquare in module __main__:\n\ndrawsquare()\n    Draw a square and return to original position and orientation",
                        "note": "help() reads the docstring directly — good documentation means anyone can use this function without reading its code.",
                    }
                ],
                "practice": [
                    {
                        "id": "13.3.p1",
                        "question": "Where does a function's docstring go?",
                        "choices": [
                            "In a comment before the def line",
                            "As the first line of the function body, usually a triple-quoted string",
                            "At the very end of the file",
                            "Nowhere — Python doesn't support this",
                        ],
                        "answer": 1,
                        "explanation": "A docstring is the string literal that appears first inside the function body."},
                    {
                        "id": "13.3.p2",
                        "question": "Abstraction, in the sense used throughout this course, means:",
                        "choices": [
                            "Making code deliberately confusing",
                            "Being able to use a piece of code by its documented behavior, without needing to know its internal details",
                            "Removing all comments",
                            "Writing only very short programs",
                        ],
                        "answer": 1,
                        "explanation": "Abstraction lets you rely on what something does without tracking exactly how it does it."},
                ],
            },
        ],
        "quiz": [
            {"id": "13.q1", "question": "When converting a hierarchy to functions, child functions must be defined:", "choices": ["After their parents", "Before the parent functions that call them", "Only in a separate file", "It never matters"], "answer": 1, "explanation": "A function must exist (be defined) before it can be called."},
            {"id": "13.q2", "question": "Bottom-up design focuses on:", "choices": ["Writing the whole program at once", "Building and testing small reusable functions, then combining them", "Avoiding functions", "Writing comments only"], "answer": 1, "explanation": "Small verified pieces are combined into progressively larger ones."},
            {"id": "13.q3", "question": "help(my_function) displays:", "choices": ["The function's entire source code", "The function's docstring", "Nothing unless you import help", "A syntax error"], "answer": 1, "explanation": "help() reads and displays the docstring."},
            {"id": "13.q4", "question": "A docstring is written as:", "choices": ["A comment above def", "The first statement inside the function body, typically a triple-quoted string", "A variable name", "A separate file"], "answer": 1, "explanation": "Docstrings are string literals placed as the function body's first line."},
            {"id": "13.q5", "question": "Abstraction, as used in this course, means being able to:", "choices": ["Use code without needing to know its internal implementation details", "Only write abstract math", "Avoid all documentation", "Write code with no functions"], "answer": 0, "explanation": "Abstraction hides implementation details behind a well-defined interface."},
        ],
    },
}

# ---------------------------------------------------------------------------
# Larger practice-tab question pools (distinct wording from the Learning tab)
# ---------------------------------------------------------------------------

PRACTICE_POOLS = {
    "1": [
        {"id": "1.pool.1", "question": "An interpreter differs from a compiler in that it:", "choices": ["Translates and runs code line by line", "Never produces any output", "Only works with binary files", "Is a type of variable"], "answer": 0, "explanation": "Interpreters process source code line by line as the program runs."},
        {"id": "1.pool.2", "question": "What does 100 % 10 evaluate to?", "choices": ["10", "0", "1", "100"], "answer": 1, "explanation": "% gives the remainder; 100 divides evenly by 10, leaving remainder 0."},
        {"id": "1.pool.3", "question": "Which line makes sqrt() and pi available in a program?", "choices": ["import python", "from math import *", "print(sqrt)", "Nothing needed"], "answer": 1, "explanation": "The math module must be imported to use its functions and constants."},
        {"id": "1.pool.4", "question": "print(3+2*2) outputs:", "choices": ["10", "7", "12", "5"], "answer": 1, "explanation": "Multiplication happens before addition: 2*2=4, then 3+4=7."},
        {"id": "1.pool.5", "question": "Text after a # on a line of Python code is:", "choices": ["Executed as normal code", "Completely ignored by the interpreter", "Highlighted in red only", "Required for every program"], "answer": 1, "explanation": "Everything after # on that line is a comment, skipped by the interpreter."},
        {"id": "1.pool.6", "question": "In the problem-solving process, what comes right after understanding the problem?", "choices": ["Reviewing your work", "Making a plan, including test cases", "Submitting the assignment", "Deleting your code"], "answer": 1, "explanation": "Planning (with test cases) follows understanding, before execution."},
        {"id": "1.pool.7", "question": "A .py file is:", "choices": ["A compiled binary", "A text file containing Python source code", "An image format", "A type of IDE"], "answer": 1, "explanation": "Python source files are plain text with a .py extension."},
        {"id": "1.pool.8", "question": "2**3 evaluates to:", "choices": ["6", "8", "9", "5"], "answer": 1, "explanation": "** is exponentiation: 2 to the power of 3 is 8."},
    ],
    "2": [
        {"id": "2.pool.1", "question": "A variable is best described as:", "choices": ["A comment", "A named location in memory holding a value", "A type of loop", "A function call"], "answer": 1, "explanation": "Variables are labeled boxes of memory."},
        {"id": "2.pool.2", "question": "Which is a reserved keyword and can't be a variable name?", "choices": ["total", "while", "my_var", "count2"], "answer": 1, "explanation": "'while' is reserved for the language itself."},
        {"id": "2.pool.3", "question": "x=5; y=x; x=9 — what is y afterward?", "choices": ["9", "5", "None", "Error"], "answer": 1, "explanation": "y copied x's value (5) at assignment time; later changes to x don't affect y."},
        {"id": "2.pool.4", "question": "Which naming convention is typically used for a constant like PI?", "choices": ["ALL_CAPS", "camelCase", "a single random letter", "starting with a digit"], "answer": 0, "explanation": "Constants are conventionally written in ALL_CAPS."},
        {"id": "2.pool.5", "question": "count = 1\ncount = count + 1\ncount = count + 1\nWhat is count?", "choices": ["1", "2", "3", "Error"], "answer": 2, "explanation": "count increases by 1 twice, from 1 to 3."},
        {"id": "2.pool.6", "question": "The = operator should be read aloud as:", "choices": ["'equals', exactly like in math", "'gets' or 'is assigned'", "'is greater than'", "'compares to'"], "answer": 1, "explanation": "= assigns a value; it is not a mathematical equality test."},
        {"id": "2.pool.7", "question": "Which variable name is invalid in Python?", "choices": ["value_1", "1st_value", "_value", "value1"], "answer": 1, "explanation": "Names can't start with a digit."},
        {"id": "2.pool.8", "question": "Python statements within a script execute:", "choices": ["In a random order", "Top to bottom, in the order written", "Bottom to top", "All at the same time"], "answer": 1, "explanation": "Sequential execution runs statements in file order."},
    ],
    "3": [
        {"id": "3.pool.1", "question": "type(10 / 2) in Python is:", "choices": ["int", "float", "str", "bool"], "answer": 1, "explanation": "The / operator always produces a float, even for evenly divisible numbers."},
        {"id": "3.pool.2", "question": "What must you do before doing math on an input() result?", "choices": ["Nothing", "Convert it with int() or float()", "Wrap it in print()", "Call input() twice"], "answer": 1, "explanation": "input() returns a string; convert it to a number first."},
        {"id": "3.pool.3", "question": "bool('False') (the string) evaluates to:", "choices": ["False", "True — any non-empty string is True", "0", "Error"], "answer": 1, "explanation": "Only the truly empty string '' converts to False; 'False' is a non-empty string."},
        {"id": "3.pool.4", "question": "int(-1.7) evaluates to:", "choices": ["-2", "-1", "-1.7", "2"], "answer": 1, "explanation": "Converting float to int truncates toward zero rather than rounding."},
        {"id": "3.pool.5", "question": 'f"{5:>6}" pads 5 to a width of 6 characters, aligned:', "choices": ["Left", "Right", "Center", "It doesn't pad at all"], "answer": 1, "explanation": "The > specifier right-aligns within the given width."},
        {"id": "3.pool.6", "question": "What does the escape sequence \\t produce inside a string?", "choices": ["A literal backslash-t", "A tab character", "A newline", "Nothing"], "answer": 1, "explanation": "\\t inserts a tab character."},
        {"id": "3.pool.7", "question": 'name = input("Enter name: ") — what does this print before waiting for input?', "choices": ["Nothing at all", "Enter name: (with no newline after it)", "Enter name: followed by a newline", "An error"], "answer": 1, "explanation": "input() with a string argument prints that prompt with no trailing newline."},
        {"id": "3.pool.8", "question": "Which correctly converts the string '3.14' to a float?", "choices": ["int('3.14')", "float('3.14')", "str(3.14)", "bool('3.14')"], "answer": 1, "explanation": "float() parses a numeric string, including decimals, into a float."},
    ],
    "4": [
        {"id": "4.pool.1", "question": "5 != 5 evaluates to:", "choices": ["True", "False", "5", "Error"], "answer": 1, "explanation": "!= means 'not equal'; 5 equals 5, so this is False."},
        {"id": "4.pool.2", "question": "(3 > 1) or (3 > 100) evaluates to:", "choices": ["True", "False", "3", "100"], "answer": 0, "explanation": "or only needs one side True; 3 > 1 is True."},
        {"id": "4.pool.3", "question": "In an if/elif chain, once one branch's condition is True:", "choices": ["Every remaining elif/else is skipped", "All branches still run", "The program stops entirely", "Python raises an error"], "answer": 0, "explanation": "Only the first matching branch runs; the rest are skipped."},
        {"id": "4.pool.4", "question": "What does Python require to mark the body of an if statement?", "choices": ["Curly braces {}", "Consistent indentation", "A semicolon at the end", "Nothing"], "answer": 1, "explanation": "Indentation (not braces) defines a block in Python, and it's mandatory."},
        {"id": "4.pool.5", "question": "Python's precedence order (highest to lowest) among these is:", "choices": ["Boolean operators, then relational, then math", "Math operators, then relational, then Boolean", "They're all equal", "Relational, then math, then Boolean"], "answer": 1, "explanation": "Math runs first, then comparisons, then and/or/not."},
        {"id": "4.pool.6", "question": "not True evaluates to:", "choices": ["True", "False", "None", "1"], "answer": 1, "explanation": "not flips a Boolean value."},
        {"id": "4.pool.7", "question": "To test if water (in F) is liquid, you need BOTH F>=32 and F<=212. Which operator combines them?", "choices": ["or", "and", "not", "=="], "answer": 1, "explanation": "Both conditions must hold simultaneously, so and is required."},
        {"id": "4.pool.8", "question": 'if 10 > 5: print("yes") — what prints?', "choices": ["Nothing", "yes", "10 > 5", "An error"], "answer": 1, "explanation": "10 > 5 is True, so the if block runs and prints 'yes'."},
    ],
    "5": [
        {"id": "5.pool.1", "question": "Turning a program's planned steps into comments, then filling in code below each, is an example of:", "choices": ["Debugging", "Program design", "Compiling", "Looping"], "answer": 1, "explanation": "This steps-to-comments-to-code approach is a basic design process."},
        {"id": "5.pool.2", "question": "In the pyramid vs. arch analogy, which represents safer software development?", "choices": ["Arch — build everything, then test once at the end", "Pyramid — build and test small stable pieces incrementally", "Neither matters", "Arch, because it's faster"], "answer": 1, "explanation": "The pyramid approach lets you verify each piece is stable before adding more."},
        {"id": "5.pool.3", "question": "Adding a number directly to a string (without converting first) raises a:", "choices": ["SyntaxError", "NameError", "TypeError", "IndexError"], "answer": 2, "explanation": "TypeError occurs when an operation isn't supported between those types."},
        {"id": "5.pool.4", "question": "A 'typical case' test checks:", "choices": ["An unusual boundary situation", "A common, everyday input", "Only invalid input", "Nothing useful"], "answer": 1, "explanation": "Typical cases confirm the program handles ordinary, expected input correctly."},
        {"id": "5.pool.5", "question": "Why write tests before writing the program, ideally?", "choices": ["It's required by Python", "It clarifies what the program should do and gives an immediate way to check your code", "It makes the program run faster", "It avoids using variables"], "answer": 1, "explanation": "Writing tests first forces you to think through expected behavior in advance."},
        {"id": "5.pool.6", "question": "A comment that just restates obvious code (like # add one to x above x = x + 1) is:", "choices": ["Best practice", "Not very useful — comments should add understanding, not repeat the obvious", "Required by Python", "The only correct kind of comment"], "answer": 1, "explanation": "Good comments explain non-obvious purpose or reasoning, not restate the code."},
        {"id": "5.pool.7", "question": "Which is a 'corner' or 'edge' case for a program processing calendar dates?", "choices": ["May 15", "February 29", "November 9", "Any random Tuesday"], "answer": 1, "explanation": "February 29 (leap day) is a special boundary case, unlike a typical mid-month date."},
        {"id": "5.pool.8", "question": "Debugging is best described as:", "choices": ["Deleting all your code and starting over", "Finding, understanding, and fixing an error", "Adding comments only", "Renaming variables"], "answer": 1, "explanation": "Debugging is the systematic process of finding and correcting a bug."},
    ],
    "6": [
        {"id": "6.pool.1", "question": "A while loop stops repeating once its condition becomes:", "choices": ["True", "False", "Zero", "Undefined"], "answer": 1, "explanation": "The loop exits once the condition evaluates to False."},
        {"id": "6.pool.2", "question": "range(0, 6, 2) produces:", "choices": ["0, 2, 4", "0, 2, 4, 6", "0, 1, 2, 3, 4, 5", "2, 4, 6"], "answer": 0, "explanation": "Starting at 0, stopping before 6, counting by 2: 0, 2, 4."},
        {"id": "6.pool.3", "question": "Which statement immediately exits the nearest enclosing loop?", "choices": ["continue", "break", "return", "pass"], "answer": 1, "explanation": "break stops the loop entirely."},
        {"id": "6.pool.4", "question": "An infinite loop happens when:", "choices": ["A for loop is used instead of while", "Nothing inside the loop ever makes the condition False", "print() is missing", "range() is used"], "answer": 1, "explanation": "The loop needs a path to eventually make its condition False."},
        {"id": "6.pool.5", "question": "In a loop, the variable names i, j, and k are conventionally used for:", "choices": ["Storing text", "Counting/indexing", "File names", "Boolean values"], "answer": 1, "explanation": "i, j, k are common counter variable names."},
        {"id": "6.pool.6", "question": "for i in range(4): print(i, end='') outputs:", "choices": ["1234", "0123", "01234", "4"], "answer": 1, "explanation": "range(4) yields 0,1,2,3, printed with no separator or newline."},
        {"id": "6.pool.7", "question": "For a nested loop (outer range(2), inner range(5)), how many total inner iterations occur?", "choices": ["2", "5", "7", "10"], "answer": 3, "explanation": "2 outer passes x 5 inner iterations each = 10 total."},
        {"id": "6.pool.8", "question": "Choose a while loop over a for loop when:", "choices": ["The number of iterations is known in advance", "You need to repeat until a general condition is met, with an unknown number of iterations", "You're looping through a fixed list", "Never — for is always better"], "answer": 1, "explanation": "while loops fit naturally when the stopping point isn't known ahead of time."},
    ],
    "7": [
        {"id": "7.pool.1", "question": 'For letters = ["a", "b", "c", "d"], what is letters[3]?', "choices": ["c", "d", "3", "Error"], "answer": 1, "explanation": "Index 3 is the fourth item: 'd'."},
        {"id": "7.pool.2", "question": 'For letters = ["a","b","c","d","e"], what is letters[-2]?', "choices": ["c", "d", "e", "b"], "answer": 1, "explanation": "-2 counts backward two from the end: 'd'."},
        {"id": "7.pool.3", "question": 'For nums = [1, 2, 3], what does nums.append(4) change nums to?', "choices": ["[4, 1, 2, 3]", "[1, 2, 3, 4]", "[1, 2, 3]", "Error"], "answer": 1, "explanation": "append() always adds the new value to the end of the list."},
        {"id": "7.pool.4", "question": 'For letters = ["a","b","c","d","e"], what is letters[2:4]?', "choices": ["['c', 'd']", "['b', 'c', 'd']", "['c', 'd', 'e']", "['a', 'b']"], "answer": 0, "explanation": "The slice starts at index 2 and stops before index 4."},
        {"id": "7.pool.5", "question": "for i in range(len(mylist)): mylist[i] = 0 — what does this do?", "choices": ["Raises an error", "Sets every element of mylist to 0", "Does nothing to mylist", "Deletes mylist"], "answer": 1, "explanation": "Using the index directly lets the loop actually modify each list element."},
        {"id": "7.pool.6", "question": "len([]) (an empty list) returns:", "choices": ["0", "1", "None", "Error"], "answer": 0, "explanation": "An empty list has zero elements."},
        {"id": "7.pool.7", "question": "grades += [90] on an existing list grades:", "choices": ["Raises an error", "Appends 90 to the end of grades", "Replaces grades with [90]", "Removes the last element"], "answer": 1, "explanation": "+= with a one-item list concatenates, effectively appending that item."},
        {"id": "7.pool.8", "question": "What does enumerate(mylist) give you access to, per iteration?", "choices": ["Only the value", "Only the index", "Both index and value together", "The list's length"], "answer": 2, "explanation": "enumerate() pairs each index with its value."},
    ],
    "8": [
        {"id": "8.pool.1", "question": "Breaking a large problem into smaller subproblems before coding describes:", "choices": ["Bottom-up testing", "Top-down design", "Debugging", "Looping"], "answer": 1, "explanation": "Top-down design divides a big problem into a hierarchy of smaller pieces first."},
        {"id": "8.pool.2", "question": "In tree terminology, the node directly above a given node is called its:", "choices": ["Child", "Parent", "Leaf", "Root always"], "answer": 1, "explanation": "The node above is the parent."},
        {"id": "8.pool.3", "question": 'For d = {"a": 1, "b": 2, "c": 3}, what does d["c"] return?', "choices": ["1", "2", "3", "c"], "answer": 2, "explanation": "The key 'c' maps to the value 3."},
        {"id": "8.pool.4", "question": "How is a dictionary's key different from a list's index?", "choices": ["A dictionary key must always be an integer, like an index", "A dictionary key can be almost any type, not just an integer position", "There's no difference", "Dictionaries don't have keys"], "answer": 1, "explanation": "Dictionary keys can be strings or other types, not just sequential integers."},
        {"id": "8.pool.5", "question": '"x" in my_dict tests whether:', "choices": ["'x' is a value in my_dict", "'x' is a key in my_dict", "my_dict is empty", "'x' equals my_dict"], "answer": 1, "explanation": "The in operator on a dictionary checks its keys."},
        {"id": "8.pool.6", "question": "for k in my_dict: print(my_dict[k]) will print:", "choices": ["Every key", "Every value, looked up by each key", "Nothing", "An error"], "answer": 1, "explanation": "k takes each key in turn, and my_dict[k] looks up its value."},
        {"id": "8.pool.7", "question": "A node in a hierarchy with no children is called a:", "choices": ["Root", "Leaf", "Parent", "Branch"], "answer": 1, "explanation": "Nodes without children are called leaves."},
        {"id": "8.pool.8", "question": "Which syntax creates an empty dictionary?", "choices": ["[]", "()", "{}", '""'], "answer": 2, "explanation": "Curly braces with nothing inside create an empty dictionary."},
    ],
    "9": [
        {"id": "9.pool.1", "question": "A function with no explicit return statement returns:", "choices": ["0", "An empty string", "None", "The last variable used"], "answer": 2, "explanation": "Python functions return None by default."},
        {"id": "9.pool.2", "question": "A tuple differs from a list mainly because a tuple is:", "choices": ["Always empty", "Immutable — its values can't change after creation", "Only for numbers", "Actually the same as a list"], "answer": 1, "explanation": "Tuples cannot be modified after creation, unlike lists."},
        {"id": "9.pool.3", "question": "def f(x, y=10): — calling f(5) uses which value for y?", "choices": ["5", "10", "None", "Error, y is required"], "answer": 1, "explanation": "y falls back to its default value of 10 since no second argument was given."},
        {"id": "9.pool.4", "question": "lo, hi = min_max(numbers) relies on min_max returning:", "choices": ["A single number", "A tuple of two values, which gets unpacked", "Nothing", "A dictionary"], "answer": 1, "explanation": "Multiple return values are packaged as a tuple and unpacked on assignment."},
        {"id": "9.pool.5", "question": "A variable is best considered 'local' when it is:", "choices": ["Defined in the main program", "Defined and used only inside one function", "Imported from a module", "A type of loop"], "answer": 1, "explanation": "Local variables live only within the function that creates them."},
        {"id": "9.pool.6", "question": "def f(a): a = [9,9,9] ... x=[1,2,3]; f(x); print(x) prints:", "choices": ["[9, 9, 9]", "[1, 2, 3]", "Error", "None"], "answer": 1, "explanation": "Reassigning the parameter to a brand-new list doesn't affect the caller's original list."},
        {"id": "9.pool.7", "question": "def f(a): a[1] = 9 ... x=[1,2,3]; f(x); print(x) prints:", "choices": ["[1, 2, 3]", "[1, 9, 3]", "Error", "None"], "answer": 1, "explanation": "Modifying an element of a mutable list inside the function changes the caller's list too."},
        {"id": "9.pool.8", "question": "Why should a function avoid reading a global variable directly, if possible?", "choices": ["Python forbids it", "It makes the function harder to understand and reuse on its own", "It always causes an error", "It's the only correct approach"], "answer": 1, "explanation": "Functions relying on outside globals are harder to understand in isolation."},
    ],
    "10": [
        {"id": "10.pool.1", "question": "A program that crashes because of invalid Python grammar has a:", "choices": ["Logic error", "Syntax error", "Runtime error", "No error"], "answer": 1, "explanation": "Syntax errors are caught before the program can even run."},
        {"id": "10.pool.2", "question": "A program that runs to completion but produces an incorrect result has a:", "choices": ["Syntax error", "Runtime error", "Logic error", "No error"], "answer": 2, "explanation": "Logic errors don't crash the program; they just give wrong output."},
        {"id": "10.pool.3", "question": "Which except clause would catch a division by zero?", "choices": ["except TypeError:", "except ZeroDivisionError:", "except IndexError:", "except NameError:"], "answer": 1, "explanation": "ZeroDivisionError is raised specifically for dividing by zero."},
        {"id": "10.pool.4", "question": "except: (with no exception type given) will catch:", "choices": ["Nothing", "Only TypeErrors", "Any exception at all", "Only syntax errors"], "answer": 2, "explanation": "A bare except catches every kind of exception."},
        {"id": "10.pool.5", "question": "In DRIFT, which step comes last?", "choices": ["Discover", "Fix", "Test — confirm the fix worked and nothing else broke", "Reproduce"], "answer": 2, "explanation": "D-R-I-F-T ends with Test."},
        {"id": "10.pool.6", "question": "Accessing index 5 of a 3-item list raises a(n):", "choices": ["SyntaxError", "IndexError", "Logic error only", "NameError"], "answer": 1, "explanation": "This is a runtime error: valid code, but an out-of-range index."},
        {"id": "10.pool.7", "question": "Using a debugger's 'step' command:", "choices": ["Deletes the current line", "Executes just the next line of code", "Fixes the bug automatically", "Restarts the whole program"], "answer": 1, "explanation": "Step runs one line at a time, letting you watch execution closely."},
        {"id": "10.pool.8", "question": "A try block with no matching except for the error that occurs:", "choices": ["Silently ignores the error", "Still lets the program crash with that error", "Automatically fixes it", "Runs the try block twice"], "answer": 1, "explanation": "Only a matching except handles the exception; otherwise it propagates as normal."},
    ],
    "11": [
        {"id": "11.pool.1", "question": 'open("log.txt", "w") on a file that already has content will:', "choices": ["Append new content to the end", "Erase the old content and start fresh", "Refuse to open", "Only allow reading"], "answer": 1, "explanation": '"w" mode always starts the file empty.'},
        {"id": "11.pool.2", "question": "The main benefit of with open(...) as f: is that it:", "choices": ["Reads files faster", "Closes the file automatically, even if an error occurs", "Is the only way to open a file", "Prevents typos in the filename"], "answer": 1, "explanation": "with guarantees proper cleanup of the file handle."},
        {"id": "11.pool.3", "question": "Which reads the entire file into a single list of line-strings?", "choices": ["read()", "readline()", "readlines()", "open()"], "answer": 2, "explanation": "readlines() returns a list with one string per line."},
        {"id": "11.pool.4", "question": '"a-b-c".split("-") returns:', "choices": ["'a-b-c'", "['a', 'b', 'c']", "('a','b','c')", "Error"], "answer": 1, "explanation": "split() breaks a string into a list wherever the separator appears."},
        {"id": "11.pool.5", "question": "for line in f: (f is an open file) yields:", "choices": ["The whole file at once", "One line per iteration", "Only the last line", "The file size"], "answer": 1, "explanation": "Iterating over a file gives one line per pass."},
        {"id": "11.pool.6", "question": "Why is .strip() commonly used on lines read from a file?", "choices": ["To make the text uppercase", "To remove the trailing newline character", "To convert it to a number automatically", "It's not commonly used"], "answer": 1, "explanation": "Lines from a file include a trailing \\n that strip() removes."},
        {"id": "11.pool.7", "question": "'-'.join(['a', 'b', 'c']) returns:", "choices": ["'a-b-c'", "['a', 'b', 'c']", "'abc'", "Error"], "answer": 0, "explanation": "join() glues the list's strings together, separated by '-'."},
        {"id": "11.pool.8", "question": "What must you convert a line read from a file to before doing math with the number in it?", "choices": ["Nothing, it's already a number", "int() or float()", "list()", "dict()"], "answer": 1, "explanation": "Lines read from a file are strings and must be converted to a numeric type first."},
    ],
    "12": [
        {"id": "12.pool.1", "question": "Which statement makes math.sqrt() available for use?", "choices": ["No statement needed", "import math", "def math():", "from python import math"], "answer": 1, "explanation": "You must import a module before using its contents."},
        {"id": "12.pool.2", "question": "A package, as opposed to a single module, is:", "choices": ["Exactly the same thing as a module", "A collection of related modules bundled together", "Only found in the math library", "A type of variable"], "answer": 1, "explanation": "Packages group multiple related modules together."},
        {"id": "12.pool.3", "question": "After from math import sqrt, pi, which call is valid?", "choices": ["math.sqrt(x)", "sqrt(x) and pi directly, without the math prefix", "import.sqrt(x)", "pi.sqrt()"], "answer": 1, "explanation": "Names imported individually drop the module prefix."},
        {"id": "12.pool.4", "question": "Which tool is used to install an external package like numpy?", "choices": ["print()", "pip", "import", "def"], "answer": 1, "explanation": "pip installs Python packages from the terminal."},
        {"id": "12.pool.5", "question": "from math import sqrt as sr allows you to call:", "choices": ["math.sqrt(x)", "sr(x)", "sqrt.sr(x)", "as(x)"], "answer": 1, "explanation": "The as keyword renames the imported function."},
        {"id": "12.pool.6", "question": "random is:", "choices": ["An external package requiring pip install", "A built-in Python module, ready to import with no extra install", "The same as the math module", "Not usable in this course"], "answer": 1, "explanation": "random ships with Python by default."},
        {"id": "12.pool.7", "question": "matplotlib.pyplot.plot(...) refers to a function inside:", "choices": ["A variable named pyplot", "The pyplot module, inside the matplotlib package", "An error", "The math module"], "answer": 1, "explanation": "This is a submodule access: package.module.function()."},
        {"id": "12.pool.8", "question": "Why might a program import only specific names instead of the whole module?", "choices": ["It's the only way Python allows imports", "To use shorter names without the module prefix", "It disables the module", "It's required for math but not random"], "answer": 1, "explanation": "from module import name lets you skip the module prefix when calling it."},
    ],
    "13": [
        {"id": "13.pool.1", "question": "In top-down design, main() usually:", "choices": ["Does all the detailed work itself", "Calls helper functions in the right sequence", "Is never used", "Only holds variables"], "answer": 1, "explanation": "main() typically outlines the program by calling other functions in order."},
        {"id": "13.pool.2", "question": "Bottom-up design emphasizes:", "choices": ["Writing the entire program before running any of it", "Building and testing small functions, then combining them", "Never using functions", "Skipping the planning stage"], "answer": 1, "explanation": "Each function is verified in isolation first, then combined."},
        {"id": "13.pool.3", "question": "help(my_function) reads information from a function's:", "choices": ["Variable names", "Docstring", "Return value only", "File size"], "answer": 1, "explanation": "help() displays the function's docstring."},
        {"id": "13.pool.4", "question": "Combining top-down and bottom-up approaches means:", "choices": ["Choosing one and ignoring the other", "Planning overall structure while testing pieces individually", "Never testing until the very end", "Avoiding functions entirely"], "answer": 1, "explanation": "The two approaches complement each other: structure from the top, verified pieces from the bottom."},
        {"id": "13.pool.5", "question": "Abstraction, as used throughout this course, refers to:", "choices": ["Making programs deliberately vague", "Using code by what it does, without needing its internal details", "Writing only mathematical code", "Removing all functions"], "answer": 1, "explanation": "Abstraction hides implementation details behind a clear interface."},
        {"id": "13.pool.6", "question": "Which function structure best reflects top-down thinking?", "choices": ["One giant function with everything inline", "main() calling get_data(), process(), and display()", "No functions at all", "A single while loop with no functions"], "answer": 1, "explanation": "Splitting responsibilities into named functions mirrors the top-down breakdown."},
        {"id": "13.pool.7", "question": "A docstring is typically written as:", "choices": ["A # comment above the function", "A triple-quoted string as the first line inside the function", "The function's name", "A separate text file"], "answer": 1, "explanation": "Docstrings are string literals placed as the first statement in the function body."},
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
        "title": "Howdy, World!",
        "prompt": "Write code that prints exactly: Howdy, World!",
        "starter_code": "",
        "expected_output": "Howdy, World!",
        "mode": "match_output",
    },
    {
        "id": "1.sb.2",
        "module_id": "1",
        "title": "Free play: math and print()",
        "prompt": "Try out +, -, *, /, **, //, %, and from math import * for extra functions.",
        "starter_code": 'from math import *\nprint(sqrt(16))',
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
        "title": "Format pi with an f-string",
        "prompt": "Using from math import pi, print pi rounded to exactly 3 decimal places using an f-string.",
        "starter_code": "",
        "expected_output": "3.142",
        "mode": "match_output",
    },
    {
        "id": "3.sb.2",
        "module_id": "3",
        "title": "Free play: types and f-strings",
        "prompt": "Experiment with type(), int(), float(), bool(), and f-string formatting.",
        "starter_code": 'x = "42"\nprint(type(x))\nprint(int(x) + 1)',
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
        "prompt": "Experiment with append(), slicing, negative indices, and enumerate().",
        "starter_code": 'fruits = ["apple", "banana", "cherry"]\nfor i, f in enumerate(fruits):\n    print(i, f)',
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
        "prompt": "Experiment with creating, updating, and looping over a dictionary's keys.",
        "starter_code": 'car = {"make": "Toyota", "year": 2020}\nfor k in car:\n    print(k, car[k])',
        "expected_output": None,
        "mode": "freeform",
    },
    {
        "id": "9.sb.1",
        "module_id": "9",
        "title": "Return a tuple",
        "prompt": "Write a function min_max(numbers) that returns both the min and max, then print min_max([4, 9, 2, 7]).",
        "starter_code": "",
        "expected_output": "2 9",
        "mode": "match_output",
    },
    {
        "id": "9.sb.2",
        "module_id": "9",
        "title": "Free play: functions and scope",
        "prompt": "Experiment with parameters, return values, tuples, and local vs. global variables.",
        "starter_code": 'def greet(name):\n    return "Hi, " + name\n\nprint(greet("Sam"))',
        "expected_output": None,
        "mode": "freeform",
    },
    {
        "id": "10.sb.1",
        "module_id": "10",
        "title": "Catch a division by zero",
        "prompt": "Use try/except to catch a ZeroDivisionError from 10/0, and print Caught it! instead of crashing.",
        "starter_code": "",
        "expected_output": "Caught it!",
        "mode": "match_output",
    },
    {
        "id": "10.sb.2",
        "module_id": "10",
        "title": "Free play: debugging",
        "prompt": "Practice tracing values, try/except, and spotting off-by-one mistakes.",
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
        "title": "Free play: file I/O and strings",
        "prompt": "Experiment with open(), write(), read(), and string methods like split() and strip().",
        "starter_code": 'with open("notes.txt", "w") as f:\n    f.write("hello file\\n")\nwith open("notes.txt") as f:\n    print(f.read().strip())',
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
        "title": "Free play: imports",
        "prompt": "Experiment with import, from...import, and renaming with as.",
        "starter_code": "from math import sqrt as sr\nprint(sr(9))",
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
        "title": "Free play: docstrings and design",
        "prompt": "Write a small function with a docstring, then call help() on it.",
        "starter_code": 'def square(n):\n    """Return n squared."""\n    return n * n\n\nhelp(square)\nprint(square(5))',
        "expected_output": None,
        "mode": "freeform",
    },

    # -- Lab-inspired prompts below: same concepts/tools as the real ENGR 102
    # -- labs, but original numbers and data so nothing is copied verbatim.

    {
        "id": "1.sb.3",
        "module_id": "1",
        "title": "Trig check",
        "prompt": "Using from math import *, print cos(0) then sin(0) on separate lines.",
        "starter_code": "",
        "expected_output": "1.0\n0.0",
        "mode": "match_output",
    },
    {
        "id": "2.sb.3",
        "module_id": "2",
        "title": "Interpolate a position",
        "prompt": "A car is at position 10 at time 0, and at position 35 at time 5. Using linear "
                  "interpolation (pos = pos1 + (pos2-pos1)*(t-t1)/(t2-t1)), compute and print its "
                  "position at time 2.",
        "starter_code": "",
        "expected_output": "20.0",
        "mode": "match_output",
    },
    {
        "id": "2.sb.4",
        "module_id": "2",
        "title": "Variable mutation puzzle",
        "prompt": "Trace this by hand first, then run it to check yourself: x=2, y=5, then x=y, then "
                  "y=x+1, then x=y-x. Print x and y at the end.",
        "starter_code": "x = 2\ny = 5\nx = y\ny = x + 1\nx = y - x\nprint(x, y)",
        "expected_output": "1 6",
        "mode": "match_output",
    },
    {
        "id": "3.sb.3",
        "module_id": "3",
        "title": "Unit conversion: Newtons to lbf",
        "prompt": "Convert 100 Newtons to pounds-force (divide by 4.44822) and print the result to "
                  "exactly 4 decimal places using an f-string.",
        "starter_code": "",
        "expected_output": "22.4809",
        "mode": "match_output",
    },
    {
        "id": "3.sb.4",
        "module_id": "3",
        "title": "3D vector magnitude",
        "prompt": "For a vector with components x=3, y=4, z=12, compute and print its magnitude "
                  "(sqrt(x**2 + y**2 + z**2)).",
        "starter_code": "",
        "expected_output": "13.0",
        "mode": "match_output",
    },
    {
        "id": "3.sb.5",
        "module_id": "3",
        "title": "Free play: mad-lib formatting",
        "prompt": "Write a 2-sentence mini mad-lib using at least one \\n escape and one f-string "
                  "placeholder holding a number.",
        "starter_code": 'name = "Reveille"\nnum = 12\nprint(f"{name} found {num} treats.\\nWhat a good dog!")',
        "expected_output": None,
        "mode": "freeform",
    },
    {
        "id": "4.sb.3",
        "module_id": "4",
        "title": "Floating point surprise",
        "prompt": "Print 0.1 + 0.2 == 0.3, then print whether abs(0.1 + 0.2 - 0.3) < 1e-9 — a "
                  "tolerance-based comparison instead of exact equality.",
        "starter_code": "",
        "expected_output": "False\nTrue",
        "mode": "match_output",
    },
    {
        "id": "4.sb.4",
        "module_id": "4",
        "title": "Compound Boolean expressions",
        "prompt": "Set p=True, q=False, r=True. Print (p and q) or (not r), then print "
                  "(p or q) and (not q or r).",
        "starter_code": "",
        "expected_output": "False\nTrue",
        "mode": "match_output",
    },
    {
        "id": "5.sb.3",
        "module_id": "5",
        "title": "Tiered pricing calculator",
        "prompt": "A shipping cost is $4.99 for packages up to 5 lbs, $8.99 up to 10 lbs, and $8.99 "
                  "plus $0.75 per pound over 10 for anything heavier. Print the cost for a 12 lb "
                  "package, to 2 decimal places.",
        "starter_code": "weight = 12\n",
        "expected_output": "10.49",
        "mode": "match_output",
    },
    {
        "id": "6.sb.3",
        "module_id": "6",
        "title": "Bisection root finder — Part 1: check the bracket",
        "prompt": "Define f(x) = x**3 - x - 2. Set x1=1 and x2=2. Print f(x1) then f(x2) to confirm "
                  "they have opposite signs — that's what guarantees a root lies between them.",
        "starter_code": "def f(x):\n    return x**3 - x - 2\n\nx1 = 1\nx2 = 2\n",
        "expected_output": "-2\n4",
        "mode": "match_output",
        "series": "bisection",
        "part": 1,
        "series_total": 3,
    },
    {
        "id": "6.sb.4",
        "module_id": "6",
        "title": "Bisection root finder — Part 2: one halving step",
        "prompt": "Using the same f, x1, and x2, compute the midpoint mid = (x1+x2)/2 and print f(mid). "
                  "This is the core step you'll repeat in a loop next.",
        "starter_code": "def f(x):\n    return x**3 - x - 2\n\nx1 = 1\nx2 = 2\n",
        "expected_output": "-0.125",
        "mode": "match_output",
        "series": "bisection",
        "part": 2,
        "series_total": 3,
    },
    {
        "id": "6.sb.5",
        "module_id": "6",
        "title": "Bisection root finder — Part 3: combine into a loop",
        "prompt": "Combine Parts 1 and 2 into a while loop: repeatedly halve [x1, x2] — keeping "
                  "whichever half still brackets the root — until x2 - x1 < 0.0001. Print the "
                  "midpoint rounded to 4 decimal places.",
        "starter_code": "def f(x):\n    return x**3 - x - 2\n\nx1 = 1\nx2 = 2\n",
        "expected_output": "1.5214",
        "mode": "match_output",
        "series": "bisection",
        "part": 3,
        "series_total": 3,
    },
    {
        "id": "6.sb.6",
        "module_id": "6",
        "title": "Collatz sequence length",
        "prompt": "Starting from n=19, repeatedly apply: if n is even, n = n // 2; if odd, "
                  "n = 3*n + 1. Count the steps until n reaches 1, and print the count.",
        "starter_code": "n = 19\nsteps = 0\n",
        "expected_output": "20",
        "mode": "match_output",
    },
    {
        "id": "6.sb.7",
        "module_id": "6",
        "title": "Count primes with a nested loop",
        "prompt": "Using a nested loop (no shortcuts), count how many prime numbers exist from 2 up "
                  "to and including 50, and print the count.",
        "starter_code": "",
        "expected_output": "15",
        "mode": "match_output",
    },
    {
        "id": "7.sb.3",
        "module_id": "7",
        "title": "Vector calculator — Part 1: magnitude",
        "prompt": "For vector a = [2, 3, 6] (stored as a list), compute its magnitude by summing the "
                  "squares of its components in a loop, then taking the square root. Print the result.",
        "starter_code": "from math import sqrt\na = [2, 3, 6]\n",
        "expected_output": "7.0",
        "mode": "match_output",
        "series": "vectors",
        "part": 1,
        "series_total": 3,
    },
    {
        "id": "7.sb.4",
        "module_id": "7",
        "title": "Vector calculator — Part 2: dot product",
        "prompt": "For a = [2, 3, 6] and b = [1, 0, 2], compute their dot product by looping over "
                  "matching indices and summing a[i]*b[i]. Print the result.",
        "starter_code": "a = [2, 3, 6]\nb = [1, 0, 2]\n",
        "expected_output": "14",
        "mode": "match_output",
        "series": "vectors",
        "part": 2,
        "series_total": 3,
    },
    {
        "id": "7.sb.5",
        "module_id": "7",
        "title": "Vector calculator — Part 3: angle between vectors",
        "prompt": "Combine Parts 1 and 2: using the magnitudes and dot product of a=[2,3,6] and "
                  "b=[1,0,2], compute the angle between them in degrees with "
                  "degrees(acos(dot / (mag_a * mag_b))). Print it rounded to 2 decimal places.",
        "starter_code": "from math import sqrt, acos, degrees\na = [2, 3, 6]\nb = [1, 0, 2]\n",
        "expected_output": "26.57",
        "mode": "match_output",
        "series": "vectors",
        "part": 3,
        "series_total": 3,
    },
    {
        "id": "7.sb.6",
        "module_id": "7",
        "title": "Pig Latin (one word)",
        "prompt": 'Convert the word "python" to Pig Latin: move the first letter to the end and add '
                  '"ay". Print the result.',
        "starter_code": 'word = "python"\n',
        "expected_output": "ythonpay",
        "mode": "match_output",
    },
    {
        "id": "7.sb.7",
        "module_id": "7",
        "title": "Free play: a 2D board",
        "prompt": "Build a 3x3 board as a list of lists, each cell holding \"-\", then print it row by row.",
        "starter_code": 'board = [["-" for _ in range(3)] for _ in range(3)]\nfor row in board:\n    print(row)',
        "expected_output": None,
        "mode": "freeform",
    },
    {
        "id": "8.sb.3",
        "module_id": "8",
        "title": "Build a lookup dictionary from two lists",
        "prompt": "Given parallel lists ids=[\"A101\",\"A102\",\"A103\"] and "
                  "names=[\"Priya\",\"Marcus\",\"Elena\"], build a dictionary mapping each id to its "
                  "name, then print directory[\"A102\"].",
        "starter_code": 'ids = ["A101", "A102", "A103"]\nnames = ["Priya", "Marcus", "Elena"]\ndirectory = {}\n',
        "expected_output": "Marcus",
        "mode": "match_output",
    },
    {
        "id": "8.sb.4",
        "module_id": "8",
        "title": "Free play: tally with a dictionary",
        "prompt": "Count how many times each word appears in a list using a dictionary and .get().",
        "starter_code": 'words = ["cat", "dog", "cat", "bird", "dog", "cat"]\ntally = {}\nfor w in words:\n    tally[w] = tally.get(w, 0) + 1\nprint(tally)',
        "expected_output": None,
        "mode": "freeform",
    },
    {
        "id": "9.sb.3",
        "module_id": "9",
        "title": "Return multiple stats as a tuple",
        "prompt": "Write a function stats(numbers) that returns both the sum and the average as a "
                  "tuple. Call it on [4, 8, 15, 16, 23] and print both values.",
        "starter_code": "",
        "expected_output": "66 13.2",
        "mode": "match_output",
    },
    {
        "id": "10.sb.3",
        "module_id": "10",
        "title": "Debug: the average that's always 0",
        "prompt": "This function should print the average of the scores (79.0), but a typo inside the "
                  "loop means the total never actually accumulates. Find it and fix it.",
        "starter_code": "def average(nums):\n    total = 0\n    for n in nums:\n        toal = total + n\n    return total / len(nums)\n\nscores = [72, 88, 91, 65]\nprint(average(scores))",
        "expected_output": "79.0",
        "mode": "match_output",
    },
    {
        "id": "10.sb.4",
        "module_id": "10",
        "title": "Debug: the max that misses the last value",
        "prompt": "This should print 42 (the largest value), but an off-by-one in the range() call "
                  "skips checking the last element of the list. Find it and fix it.",
        "starter_code": "def find_max(nums):\n    biggest = nums[0]\n    for i in range(1, len(nums) - 1):\n        if nums[i] > biggest:\n            biggest = nums[i]\n    return biggest\n\nvals = [3, 17, 9, 8, 42]\nprint(find_max(vals))",
        "expected_output": "42",
        "mode": "match_output",
    },
    {
        "id": "11.sb.3",
        "module_id": "11",
        "title": "Record parser — Part 1: split one record into fields",
        "prompt": 'Given the record string "name:Sam role:engineer id:104", split it on '
                  "whitespace, then split each piece on \":\" to build a dictionary of fields. "
                  'Print fields["role"].',
        "starter_code": 'record = "name:Sam role:engineer id:104"\nfields = {}\n',
        "expected_output": "engineer",
        "mode": "match_output",
        "series": "records",
        "part": 1,
        "series_total": 3,
    },
    {
        "id": "11.sb.4",
        "module_id": "11",
        "title": "Record parser — Part 2: check required fields",
        "prompt": 'Reuse Part 1\'s parsing. Check whether "name", "role", and "id" are all present as '
                  "keys in fields (use all(...) with a loop or generator), and print the result.",
        "starter_code": 'record = "name:Sam role:engineer id:104"\nfields = {}\nfor pair in record.split():\n    key, value = pair.split(":")\n    fields[key] = value\nrequired = ["name", "role", "id"]\n',
        "expected_output": "True",
        "mode": "match_output",
        "series": "records",
        "part": 2,
        "series_total": 3,
    },
    {
        "id": "11.sb.5",
        "module_id": "11",
        "title": "Record parser — Part 3: process multiple records",
        "prompt": "Combine Parts 1 and 2 into a full program: data holds 3 records separated by a "
                  'blank line ("\\n\\n"). Split it into records, parse each one\'s fields, and count '
                  "how many have all 3 required fields (one is missing \"role\"). Print the count.",
        "starter_code": 'data = "name:Sam role:engineer id:104\\n\\nname:Ana role:tech id:105\\n\\nname:Lee id:106"\nrequired = ["name", "role", "id"]\n',
        "expected_output": "2",
        "mode": "match_output",
        "series": "records",
        "part": 3,
        "series_total": 3,
    },
    {
        "id": "11.sb.6",
        "module_id": "11",
        "title": "Product code checksum",
        "prompt": 'For the 12-digit code "123456789012", compute a weighted checksum digit: sum '
                  "each digit times 3 if it's at an even index or 1 if odd (0-indexed), then the "
                  "check digit is (10 - (total % 10)) % 10. Print the check digit.",
        "starter_code": 'code = "123456789012"\ndigits = [int(d) for d in code]\n',
        "expected_output": "0",
        "mode": "match_output",
    },
    {
        "id": "11.sb.7",
        "module_id": "11",
        "title": "Free play: mini weather average",
        "prompt": "Given a week of temperature readings, compute and print the average to 2 decimal places.",
        "starter_code": 'temps = [61, 64, 70, 68, 72, 75, 66]\navg_temp = sum(temps) / len(temps)\nprint(f"{avg_temp:.2f}")',
        "expected_output": None,
        "mode": "freeform",
    },
    {
        "id": "12.sb.3",
        "module_id": "12",
        "title": "The statistics module",
        "prompt": "Import the built-in statistics module and print the mean, then the median, of "
                  "[88, 92, 79, 95, 84].",
        "starter_code": "import statistics\nscores = [88, 92, 79, 95, 84]\n",
        "expected_output": "87.6\n88",
        "mode": "match_output",
    },
    {
        "id": "13.sb.3",
        "module_id": "13",
        "title": "Numerical integration: the trapezoid rule",
        "prompt": "Write trapezoid_area(f, a, b, n) that estimates the area under f from a to b using "
                  "n trapezoids. Test it with f(x) = x**2 from 0 to 4 using n=1000 subintervals, "
                  "printed rounded to 3 decimal places.",
        "starter_code": "def f(x):\n    return x**2\n",
        "expected_output": "21.333",
        "mode": "match_output",
    },
    {
        "id": "13.sb.4",
        "module_id": "13",
        "title": "Free play: find a local maximum",
        "prompt": "Given a list of sampled y-values, loop through to find the index and value of the "
                  "largest one (a simple stand-in for spotting a curve's local max).",
        "starter_code": "ys = [3, 5, 9, 6, 4, 8, 2]\nbest_i = 0\nfor i in range(len(ys)):\n    if ys[i] > ys[best_i]:\n        best_i = i\nprint(best_i, ys[best_i])",
        "expected_output": None,
        "mode": "freeform",
    },
]


def get_module_meta(module_id):
    for m in MODULES_META:
        if m["id"] == module_id:
            return m
    return None
