
## Post Correspondence Problem

Author: **Ron Nathaniel**
 
 
 ### Usage
 
 The entry point for this program lives in `main.py`
 
 Invoke the application with 
 
    python3 main.py
    
or on Windows
 
    py main.py
    
You will be greated with a serious of questions to validate configuration.
    
    Max frontier size?  [5] 
    Max number of states?  [50] 
    Output flag? 0-1 [0] 
    How many dominoes?  [3] 
    List each domino with a space sep. ex: aa bb
    1?  DOM INO
    ...


 Answer Each question according to the type, and fill in each domino to start.
 
 The output, should a solution be found, may resemble
 
    Solution found in STAGE
    Solution Size (# of dominoes):  INT
    step # 1 :  AA - BB
    step # 2 :  DDDD - EEE
    step # 3 :  XX - YXXX
    step # 4 :  C - FF
    total sequence:  aabbbaabb - aabbbaabb

 
 
 ### Technology
    
This project runs natively on Python 3, and was developed specifically for Python 3.9.2

This code was written to be as backwards-compatible as possible, limiting use of 
- f-strings 
- the walrus operator
- type-hints

and more.

### Dependencies

None! This program was created solely with builtin functions.

### Copyright

Copyright Ron Nathaniel 2021

All rights reserved.