# my first app
github repo: myhello
app: hello.py
test: test_hello.py
env: base PY 3.11 on Windows 11
vscode: with Python & Jupyter extensions

# my first enhancements

##
this readme.md

## create venv
venv: code_louisville
env: base PY 3.11 on Windows 11

Powershell workflow & vscode activate:

### in root Python folder, open cmd & run
```
PS C:\Users\stevewatkins\AppData\Local\Programs\Python\Python311> python -m venv code_louisville
```
### cd to "\code_louisville\Scripts" and exe ps1 as admin
```
PS C:\Users\stevewatkins\AppData\Local\Programs\Python\Python311> cd code_louisville\Scripts
```
### to test activate (security people love this...maybe not)
```
PS C:\Users\stevewatkins\AppData\Local\Programs\Python\Python311\code_louisville\Scripts> Set-ExecutionPolicy Unrestricted
PS C:\Users\stevewatkins\AppData\Local\Programs\Python\Python311\code_louisville\Scripts> C:\Users\stevewatkins\AppData\Local\Programs\Python\Python311\code_louisville\Scripts\Activate.ps1
```

### vscode activate - Windows
with any PY file open in vscode, point vscode to your new venv: 
```
View > Command Palette > Python: Interpreter > "C:\Users\stevewatkins\AppData\Local\Programs\Python\Python311\code_louisville\Scripts\python.exe"
```

delete and restart any vscode terminal instances; doing so should trigger vscode to run activate.bat (on windows)

## install new packages

### CLI
```
python -m pip install pyodbc
python -m pip install pytz
python -m pip install pytest
```

### dockerfile for alpine linux container
```
RUN apk update && python -m pip install pyodbc
RUN apk update && python -m pip install pytz
RUN apk update && python -m pip install pytest
```

## requirements.txt
In our repo, to recreate our venv.

```
$ pip freeze > requirements.txt
```

To replicate someone else's venv
```
$ pip install -r C:\Users\stevewatkins\AppData\Local\Programs\Python\Python311\code_louisville\Scripts\requirements.txt
```