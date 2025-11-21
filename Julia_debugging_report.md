
Setup Summary:

The virtual environment venv was set up ahead of time, along with the Python extension that was needed in order for the debugging to work.
The code needed for each of the files was copied from the assignment to ensure proper setup.

Bug list & Explanations:

Bug 1 - AttributeError 
The AttributeError was caused by the line: query = request.GET.get('q').strip()
It was missing the attribute  or " ", so instead the line should have read 
query = request.GET.get('q' or ' ').strip()
It was found through the use of a breakpoint in that line and then stepping over to get to the rest of the code. I would check back in forth to see what error would be produced on the server and then fixed it by adding the ' '

Bug 2 - Logic Error
The error was cause by the  if field_filter is not 'All': line, specifically with the is not. The is not operator checks for object identity - meaning it is checking if the objects are the exact same in memory. It focuses on the location of object in memory.
The =! operator checks for value equality - meaning it checks if object one contains the same thing as object 2.
In the line inside of the if statement you are comparing strings, meaning you want to check for the value as opposed to the location. Therefore the if field_filter is not 'All': led to a bug. To fix this, I set a break point in the if statement and then stepped into the if statement. I went back and forth with my code to the server to solve the issue. I then inserted != as opposed to is not.

Bug 3 - KeyError
The error resulted in the misspelling of the word description in the line 

return query.lower() in p['title'].lower() or query.lower() in p['descriptionn'].lower()

The issue was found by browsing through http://127.0.0.1:8000/buggy/?q=city. 
It provided an exception value at line 38. I fixed it by just adjusting the spelling.

