 # Plastic Preservation

 ```
 └──╼ $cat encrypted.txt | base64 -d
c40d1f1b7bdd6012
```
Analysing the python script there are 3 layers of encoding

first `UUID` with a `dateformat`, second is `hexadecimal` 

there is `XOR` bitwise operation in layer 2

and last is `base64`

we already cracked layer 3 but now we revert the uuid

in `.log` file we can see the dateformat as such

```
# 2020-05-21 18:03:15.122389 14696055806137376749 
# 2020-05-21 18:03:15.122520 14695963447160612969 
```
the script removes the `#`


