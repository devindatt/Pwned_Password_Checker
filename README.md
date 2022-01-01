# Pwned_Password_Checker
Python (v3.8) script to securely check if any list of passwords have been part of a hack in the past, using k-anonymity methodology to securely check your password without transmitting the actual clear text password to the 'HaveIBeenPwned.com' API. 

**RUN IMPLEMENTATION**
1) Download single file
2) Run following python command from the CLI (below example is for mac):

**INPUT EXAMPLE:**
(venv) Username@Users-MacBook-Air % python3 checkmypass.py password1 password2 ewraedfdfgdgh

Output will show either the number of times that password has appeared in a previous security hack:

**OUTPUT EXAMPLE:**
Lets see is any of these passwords have been pwned: password1 password2 ewraedfdfgdgh

Checking password: password1
Which hashing into E38AD and 214943DAAD1D64C102FAEC29DE4AFE9DA3D
Hash to check is: 214943DAAD1D64C102FAEC29DE4AFE9DA3D
Holy crap!! password1 has been pwned a total of **3249873 times**, maybe you should change it!

Checking password: password2
Which hashing into 2AA60 and A8FF7FCD473D321E0146AFD9E26DF395147
Hash to check is: A8FF7FCD473D321E0146AFD9E26DF395147
Holy crap!! password2 has been pwned a total of **259930 times**, maybe you should change it!

Checking password: ewraedfdfgdgh
Which hashing into A80E2 and EF9F3CD4159A69882EA82CD39DE15A3C7C8
Hash to check is: EF9F3CD4159A69882EA82CD39DE15A3C7C8
Nice job!! ewraedfdfgdgh was found to be pwned a **total of 0 times**, carry on!
