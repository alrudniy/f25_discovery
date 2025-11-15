Setup summary – how you created the virtual environment, installed dependencies, and added the .vscode/launch.json file for debugging.

    I had a pre existing virtual environment in my directory called "venv". I had installed the requirements.txt inside it, so I skipped this step. The only thing that I had to add was to create a .vscode folder and to add launch.json in my folder. After I added the .vscode to my directory, then I set the interpreter to the venv directory, so that It used python version and all the other interpreters that were installed in my venv folder.  

Bug list and explanation – for each bug:
    I had hart time at the beginning for debugging, but then I figured out how to do it. The bug that was the first one was because    .get('q') returns None when missing; None.strip() crashes. Therefore we would get a page in our browser that the page was crashed. The url in the browser should be ending in /buggy/ so that you view the output of the buggy. The fix for this one was to replace the query variable with the following line: query = (request.GET.get('q') or "").strip(). after this code is addded, the page actualy renders in the browser and you can actually see the page. 

    The second bug was easier to indicate and to fic too. The problematic line is  if field_filter is not 'All'. The problem here is "is not". This checks if the object of the field_filter is the same as the object of the string "All". However, we just have to check the value equality, which is done by writing !=. This chacks if the value is the same instead of checking the object equality. Symptom: Despite field_filter being "All", the condition may be True (object identity), so it filters when it shouldn’t. This can be achieved by adding the variable field_filter to the watch window at debugging stage and taking a look at it's content. In the browser you can check it by accessing the following url:  http://127.0.0.1:8000/buggy/?q=ai&field=All. Another way to identify it is to right klick on the break point and add the condition  "field_filter == "All"."


    The third bug was on the following line: return query.lower() in p['title'].lower() or query.lower() in p['descriptionn'].lower()
    The problem with this code is the spelling of the key of "p". It is saying descriptionn, while it should be saying "description". In this case if you ttry to access the page with the following url: http://127.0.0.1:8000/buggy/?q=city. The page will not render and it will say that the line number 36 has an issue. The way to indicate it is to  In the Run panel, enable “Break on raised exceptions” to stop exactly where it fails. if you fix it, the page will actually render and display: 
    Buggy Search
    Query: city • Field: All

Results: 1


