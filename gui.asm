format  PE GUI
entry   start
include 'include\win32a.inc'

 section '.data' data readable writeable

  text db  'Hello!', 0
  text2 db 'MessageComp', 0

 section '.code' code readable executable

 start:
         invoke  MessageBox,NULL,text,text2,MB_OK
         invoke  ExitProcess, 0

 section '.idata' import data readable writeable
         library kernel32,'kernel32.dll',\
                 user32,'user32.dll'
         import  kernel32,\
                 ExitProcess,'ExitProcess'
         import  user32,\
                 MessageBox,'MessageBoxA'
