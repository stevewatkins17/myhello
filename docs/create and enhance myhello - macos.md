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
```
python -m venv code_louisville
```
## activate venv
```
source ./code_louisville/bin/activate
```

## install new packages

### CLI
```
python -m pip install pyodbc
python -m pip install pytz
python -m pip install pytest
python -m pip install ipykernel
python -m pip install notebook
python -m pip install pandas
python -m pip install requests

```
### 1 Big CMD
```
python -m pip install pyodbc pytz pytest ipykernel notebook pandas requests
```
## requirements.txt
In our repo, to recreate our venv.

```
pip freeze > requirements.txt
```

To replicate someone else's venv
```
$ pip install -r requirements.txt C:\Users\stevewatkins\AppData\Local\Programs\Python\Python311\code_louisville\Scripts\requirements.txt
```
## .gitignore
A .gitignore file is used by git to ignore files, filtered by pattern or explicit name. Pathing should be relative.

Templates abound: 
- https://www.toptal.com/developers/gitignore/  (Use tags "Python" & "VisualStudioCode")
- https://github.com/microsoft/vscode-python/blob/main/.gitignore
