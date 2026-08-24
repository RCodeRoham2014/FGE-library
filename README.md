# FGE-library
**FGE**, or **Functional Graphic Engine**, is a Python library that allows Python developers to develop graphical applications quickly and easily.

This library is built on **PySide6**, which is why it offers high performance and powerful capabilities.

## Why FGE?

You may ask yourself: Why should I use this when other libraries already exist?

The answer is:

1. FGE requires very little code.
2. It also offers powerful capabilities.
3. It is very quick to learn! *(You can learn it in as little as one day!)*

## Getting Started

To use FGE, you must first install the **PySide6** library.

Then, you can download the `FGE.py` file, place it next to your project folder, and use it.
***

# FGE Library Tutorial

This tutorial will guide you through the process of creating graphical interfaces using the FGE library.

## 1. Prerequisites and Setup
Before you begin, ensure you have `PySide6` installed:

```bash
pip install PySide6
```

Next, import the necessary components into your script:
```python
from PySide6 import *
from FGE import *
```

## 2. Core Workflow
Creating an application with FGE follows these general steps:
1.  **Initialize the Screen:** This sets up the main window and provides a root container.
2.  **Add Elements:** Add elements like labels and buttons, passing the root container as their parent.
3.  **Run the Engine:** Start the main application loop.

---

## 3. Step-by-Step Implementation

### Step 1: Create the Screen
The `screen()` function is the foundation of your application. It creates the main window and sets its properties.

**Signature:**
```python
root = screen(size=(width, height), color=(r, g, b), title="Window Title")
```
*   **`size`**: A `(width, height)` tuple in pixels.
*   **`color`**: An RGB tuple for the background color.
*   **`title`**: The text displayed in the window's title bar.
*   **Important:** The return value of `screen()` *must* be stored in a variable (e.g., `root`) to be used as the parent for other elements.

### Step 2: Add a Label
Labels are used to display text.

**Signature:**
```python
label(parent, pos, text="Text", font_size=12, color=(0, 0, 0))
```
*   **`parent`**: The variable returned by `screen()` (e.g., `root`).
*   **`pos`**: A `(x, y)` tuple for the position. Note: FGE uses a bottom-left origin coordinate system.
*   **`font_size`**: The font size in points.
*   **`color`**: The text color as an RGB tuple.

### Step 3: Add a Button
Buttons allow user interaction.

**Signature:**
```python
button(parent, pos, size, text="Button", font_size=10, bg_color=(200, 200, 200), text_color=(0, 0, 0), action=None)
```
*   **`size`**: A `(width, height)` tuple for the button's dimensions.
*   **`action`**: The name of the function to be executed when the button is clicked.

### Step 4: Run the Application
After adding all elements, call `run()` to make the window visible and interactive. If `screen()` has not been called prior, this will raise a `RuntimeError`.

---

## 4. Coordinate System in FGE
FGE employs a coordinate system with its origin `(0,0)` at the **bottom-left** corner of the window.
*   The X-axis increases to the right.
*   The Y-axis increases upwards.
This differs from Qt's default top-left origin and is handled internally by FGE.

---

## 5. Complete Example
Here's a simple application demonstrating a button that prints a message:

```python
from PySide6 import *
from FGE import *

def my_action():
    print("Button was clicked!")

# 1. Initialize the screen
root = screen(size=(400, 400), color=(50, 50, 50), title="My First FGE App")

# 2. Add a label
label(root, pos=(150, 350), text="Hello, FGE!", font_size=24, color=(255, 255, 255))

# 3. Add a button
button(root, pos=(125, 100), size=(150, 50), text="Click Me", action=my_action)

# 4. Run the engine
run()
```

## 💡 Key Points
*   **Parenting:** Always pass the `root` object obtained from `screen()` as the `parent` argument to `label()` and `button()`.
*   **Coordinate System:** Remember that Y increases upwards in FGE's coordinate system.
***
##Creator : 
RCode ™