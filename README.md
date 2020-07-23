# pycefsharp
<p align="center">

<a href="https://pypi.python.org/pypi/pycefsharp">
<img src="https://img.shields.io/pypi/v/pycefsharp.svg" /></a>
<a href="https://travis-ci.org/eseunghwan/pycefsharp"><img src="https://travis-ci.org/eseunghwan/pycefsharp.svg?branch=master" /></a>
</p>
<br>
<br>

# Install
### using pip
```powershell
pip install pycefsharp
```
### from git
```powershell
git clone https://github.com/eseunghwan/pycefsharp.git
cd pycefsharp
python setup.py install
```

# Usage
### open url from cli
```powershell
python -m pycefsharp "http://www.google.com" --title="hey, google!" --icon="[iconFile]" --geometry=[x],[y],[width],[height]
```

### use in script
```python
from pycefsharp.cef import CefApp, CefView

CefApp().Run(CefView("https://github.com/eseunghwan/pycefsharp", "simple_test"))
```
<br>
<br>

# License
pycefsharp is MIT license
<br>
<br>

# Release History
- V 0.1.0 [2020/07/23]
    - initial version