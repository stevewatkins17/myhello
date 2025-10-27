# my first app
github repo: myhello
app: hello.py
test: test_hello.py
env: base PY 3.12 on Windows 11
vscode: with Python & Jupyter extensions

# my first enhancements

##
this readme.md

## create venv
venv: cl_fall2025
env: base PY 3.12 on Windows 11

Windows Terminal workflow & vscode activate

### create project folder "C:\Users\stevewatkins\Downloads\repos\myhello", then switch into it
```
C:\Users\stevewatkins\Downloads\repos> mkdir myhello
C:\Users\stevewatkins\Downloads\repos> cd myhello
```

### where are my Python install paths?
```
where python
```

### in root project folder, create venv referencing your full python path executable path
```
C:\Users\stevewatkins\Downloads\repos\myhello> C:\Users\stevewatkins\AppData\Local\Programs\Python\Python312\python.exe -m venv cl_fall2025
```

### activate the new venv that you just created
```
C:\Users\stevewatkins\Downloads\repos\myhello>cl_fall2025\Scripts\activate.bat
```

## install new packages into your new venv

### CLI
```
python -m pip install pyodbc
python -m pip install pytz
python -m pip install pytest
python -m pip install pyodbc 
python -m pip install ipykernel 
python -m pip install notebook pandas

```

## requirements.txt
In our repo, to recreate our venv.

```
$ pip freeze > requirements.txt
```

To replicate someone else's venv
```
$ pip install -r requirements.txt
```
## .gitignore
A .gitignore file is used by git to ignore files, filtered by pattern or explicit name. Pathing should be relative.

Templates abound: 
- https://www.toptal.com/developers/gitignore/  (Use tags "Python" & "VisualStudioCode")
- https://github.com/microsoft/vscode-python/blob/main/.gitignore

If you created a venv inside your project folder, then you will want to exclude it from your github repo (large binary files will consume more space than your are probably allocated)

Add this line to your .gitignore file:
```
cl_fall2025/
```