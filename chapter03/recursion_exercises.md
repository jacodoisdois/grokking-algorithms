1 - What information can you give me, just based on this call stack?

1. greet function called with name = maggie  
2. greet calls greet2 with name also maggie
3. greets pause and greet2 start
4. greet2 ends
5. greet resume

2 - Suppose you accidentally write a recursive function that runs forever. As you saw, your computer allocates memory on the stack for each function call. What happens to the stack when your recursive function runs forever?
The infinite recursion will crash the computer after overflow the memory. 
Wrong, the computer will not crash, but the program will exit with stack-overflow error.