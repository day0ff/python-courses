# 🐍 Python Homework Course

This repository is designed for students to **practice Python programming** and **self-check their homework** using automatic tests.

---

## 📚 Course Structure
- `tasks/` → Python files with assignments.  
  Each file contains an unfinished function with `TODO` instructions.  
- `tests/` → Unit tests for each task.  
  Students run these tests to check if their solution is correct.

---

## ⚙️ Dependencies

To work with this repository, you need:

- **Python 3.8+** → The programming language.  
    Check your version:

    ```bash
    python --version
    ```


- pip → Python package manager (comes with Python).
    Check if installed:

    ```bash
    pip --version
    ```


pytest → Testing library used to check solutions.

All dependencies are listed in requirements.txt.

## 🚀 How to Use

1. Clone the Repository

```bash
git clone https://github.com/day0ff/python-courses.git
cd python-courses
```

2. Install Dependencies
- Option A: Install from requirements.txt (recommended)

    ```bash
    pip install -r requirements.txt
    ```

- Option B: Install manually

    ```bash
    pip install pytest
    ```

3. Do the Homework
Open the file in tasks/, for example:

```python
# tasks/task01_ifelse.py

def check_number(num: int) -> str:
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"
```
4. Run Tests
To check your solution: write pytest and a pass to you solution file tests/test_task01_ifelse.py

```bash
pytest tests/test_task01_ifelse.py
```

You should see output like:

```bash
===================== test session starts =====================
collected 9 items

tests/test_task01_ifelse.py .....                        [100%]

====================== 9 passed in 0.03s ======================
```

✅ All tests passed = task completed successfully!


## ▶️ Running Tests

You can run tests in different ways depending on what you want to check:

1. Run all tests in the repository
```bash
pytest
```

2. Run all tests in a specific folder

For example, run all tests in the tests/ folder:

```bash
pytest tests/
```

3. Run a single test file

For example, only test the first homework task:

```bash
pytest tests/test_task01_ifelse.py
```

4. Run a single test function inside a file

For example, only run the test_positive function:

```bash
pytest tests/test_task01_ifelse.py::test_positive
```

## ❓ About __init__.py Files

Both tasks/ and tests/ folders contain an __init__.py file.
These files are needed so that Python treats the folders as packages, which allows imports like:

from tasks.task01_ifelse import check_number


The __init__.py file can be empty — this is enough to mark the folder as a package.

Optionally, you can add imports or variables inside it. For example:

# tasks/__init__.py
from .task01_ifelse import check_number


Now you could simply do:

from tasks import check_number


For this course, the __init__.py files are kept empty.

## 📝 Example Task

Task 01: Implement the function check_number(num: int) -> str.

Return "positive" if the number is greater than 0.

Return "negative" if the number is less than 0.

Return "zero" if the number is 0.

Check your solution:

pytest tests/test_task01_ifelse.py

## 📌 Notes

Always write code inside the function body (don’t change function names).

If all tests pass → your solution is correct! 🎉

If some tests fail → read the error message and fix your code.

## 🛠 Recommended Tools

pytest → testing framework (already included).

VS Code or PyCharm → for writing Python code.