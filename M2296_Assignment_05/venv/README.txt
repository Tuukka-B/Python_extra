First of all, read SPEC_UPGRADE.txt for explanation of changed specifications.

Second, start the program M2296_assignment05.py and type "server" or "client" after the python command, for example "python3 M2296_assignment05.py server". This will give you argparse's help-page of the server arguments. 

Typing "python3 M2296_assignment05.py client" will give you client help.

Typing "python3 M2296_assignment05.py client download" will give you download help for the client.

Typing "python3 M2296_assignment05.py client upload" will give you upload help for the client.

Typing "python3 M2296_assignment05.py client list" does not have a separate help, instead the command will execute as is (it does need server's address and port though, but the error message will tell you that)

Do NOT change the location of any of the Python files. GFTP.py, M2296_assignment05.py and sha_struct.py need to be in the same folder.

Provided with the assignment are also "server-files" and "test-files" folder. "server-files" is the default folder the server uses for its operations (you can change that though - see server help page). It is provided for the ease of use.

"test-files" folder contains files to test the functionality of the server or the client. It has no other purpose.

Happy testing!
