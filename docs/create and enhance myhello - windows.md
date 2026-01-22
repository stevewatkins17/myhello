# my first app
github repo: myhello
app: hello.py
test: test_hello.py
env: base PY 3.12 on Windows 11
vscode: with Python & Jupyter extensions

# my first enhancements
- create local repo 
- create venv
- install packages

## create venv
venv: cl_jan2026
env: base PY 3.12 on Windows 11

Windows Terminal workflow & vscode activate

### clone existing, then switch into it
```
cd "C:\Users\stevewatkins\Downloads\repos"
git clone https://github.com/stevewatkins17/myhello.git
cd myhello
```

### Win terminal 
```terminal
python -m pip freeze > requirements_base.txt
```

### where are my Python install paths?
```GITbash
where python
py -V
which pip
which python
```

### in root project folder, create venv referencing your full python path executable path
```
C:\Users\stevewatkins\Downloads\repos\myhello>python.exe -m venv cl_aug2025
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
python -m pip install pyodbc pytz pytest ipykernel notebook pandas requests

```

## requirements.txt
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