# debug mode

1. import `import pdb;`
2. put it `breakpoint()` where you want check.
3. write it `pdb.run("reverse2('hello')")` in where you want to check file.
4. debug mode excute in terminal.
```
python3 -m pdb reversestring.py
continue
```
if you want to check element 'str', 
just write 'str'.

if you want to check 'reversed',
just write 'reversed'.

5. If you want to leave debug mode,
`exit()`

6. `list` , if you want to check current excute code.