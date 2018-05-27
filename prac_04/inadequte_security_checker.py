usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole',
'InterpreterInterface', 'StartServer', 'bob']

name_input = str(input("Enter your name: "))
if name_input in usernames:
    print("Access Granted")
else:
    print("Access Denied")