# API-password-handling

An API that checks if the password passed as argument is compliant to some constraints like

The API is accessible through  https://password-checking-33347.herokuapp.com/password/[password]/[complexity] , 
where:

[password] is the password

[complexity] is the complexity level selected and it can be 1, 2 or 3.

Obviously this is not the best way to check a password which should be encrypted, but the password is treated as a simple string, to give an idea of the API structure.
