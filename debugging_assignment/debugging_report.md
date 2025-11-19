# Debugging Report – Django Buggy View Assignment
Yifeng Peng
CSCI 340 – Software Development  
Debugging Practice with VS Code  


## 1. Setup Summary


### **Virtual Environment**
created and activated a virtual environment inside the project folder:

python -m venv .venv
source .venv/bin/activate 

Then installed all dependencies:

pip install -r requirements.txt


### **VS Code Debug Configuration**
created `.vscode/launch.json` with two debugging configurations:

1. **Django: runserver** – used to debug the buggy view  
2. **Django: manage.py test (debug)** – used for test debugging

The server was launched using the debug launcher, not the terminal, so breakpoints properly attached to Django’s execution.

### **Routing + Template Setup**
- Added `buggy_view.py` to the `pages/` app  
- Wired the route:

```python
path('buggy/', buggy_view.buggy_search, name='buggy_search')
Created template: templates/pages/buggy_search.html

Everything above ensured I could reproduce all three bugs using Django’s debug mode.

2. Bug list and explanation
Bug 1:
Location
query = request.GET.get('q').strip()

Cause:
When visiting /buggy/ with no q parameter, the expression:
request.GET.get('q')
returns None, and calling .strip() on None raises:
AttributeError: 'NoneType' object has no attribute 'strip'


How I Found It:
Set a breakpoint on the query = ... line.
Started debugging using Django: runserver.
Opened the browser
visit:
http://127.0.0.1:8000/buggy/

When stepping over the line (F10), VS Code showed the exception.

Fix:
query = (request.GET.get('q') or "").strip()


Bug 2
Location:
if field_filter is not 'All':


Cause:
The code incorrectly uses is (object identity) instead of == (value equality).
Python compares string identity unpredictably because "All" literals are not guaranteed to be the same object.
Django also emitted this warning:
SyntaxWarning: "is not" with 'str' literal. Did you mean "!="?


How I Found It:
Added a breakpoint on the if field_filter is not 'All': line.

visit:
http://127.0.0.1:8000/buggy/?q=ai&field=All
In the VARIABLES window:

field_filter = "All"
but VS Code showed that is not evaluated to True.

Fix:
if field_filter != 'All':
Screenshot
(Insert screenshot showing the breakpoint + variable inspection)

 
Bug 3
Location
query.lower() in p['descriptionn'].lower()

Cause
The key 'descriptionn' is misspelled.
The actual dictionary key is 'description'.

This results in a runtime crash:
KeyError: 'descriptionn'


How I Found It
Set a breakpoint inside the predicate(p) function.
visit:
http://127.0.0.1:8000/buggy/?q=city
Stepped into the function (F11).
The exception was thrown at the misspelled key.

Fix
query.lower() in p['description'].lower()
Screenshot
(Insert screenshot showing KeyError: 'descriptionn')
