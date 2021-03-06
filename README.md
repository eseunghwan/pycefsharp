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
<br>
<br>

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

- V 0.2.0 [2020/07/23]
    - add properties of <b>url</b>, <b>title</b>, <b>icon</b>, <b>geometry</b>

- V 0.2.1 [2020/07/23]
    - make winform object private
    - form can be invoked by properties

- V 0.2.1.Rev2 [2020/07/23]
    - revoked changes and upgrade to <b>0.2.1.Rev2</b>

- V 0.2.1.Rev2 [2020/07/23]
    - bug fixed
        - find install dependencies properly
    - add <b>show</b>, <b>close</b> functions

- V 0.2.1.Rev3 [2020/07/23]
    - bug fixed
        - window moves to center when geometry's x and y are -1 properly

- V 0.2.1.Rev4 [2020/07/23]
    - window appears when page is loaded
