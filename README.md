# CS6570
Assignments for the course CS6570 Secure Systems Engineering Jan - May 2021 

## Lab 1

You have 3 problems

*vegas1.c* (4 points)

Use a vulnerability in the program to win

*vegas2.c* (4 points)
Use a vulnerability in the program to win a million points

*vegas3.c* (2 points)
Similar to vegas1, win the game!!!
Hint1: Its not always about vulnerabilities.
Hint2: Using tools like pwn tools would help

*Rules*

* The executables for vegas1 and vegas3 are provided to you
in a shared folder. You would need give us an exploit input string, which
when executed will win.
* The string should be stored in the shared google folder with the same
name as the program.

## Lab 2
You have to do the following :

For : _t1_           (5 marks)
Find a way to execute the shell function using a vulnerality present in the program

For : _t2_           (5 marks)
Its not very easy to write malware. Very often the source code is not available
and malware coders need to work with assembly.

You are given an executable. You would need to (1) identify the vulnerability
(2) and exploit it to get a shell.

You can use the Return-to-libc attack that we did in class.

## Lab 3
This problem concerns the use of ROP gadgets to find 6! and print the results.
------------------------------------------------------------------------------------
1. Download and install ROP gadget from https://github.com/JonathanSalwan/ROPgadget. 
This may require you to also install capstone. Please see the readme file in the git hub.

2. Turn off ASLR for your Linux kernel (refer class slides).

3. Compile the C code given with the following options: 

$ gcc -m32 -O0 -fno-stack-protector -static tut3.c -o tut3. 

This will create a 32 bit executable with statically linked libraries.


4. Execute ROP gadget on tut2 using the command 

$ python ROPgadget.pY -binary tut3. 

Have a look at -help in ROPgadget.py for many more interesting options.

5. Pick your gadgets, stitch them together on the stack, so that 6! is printed on the screen. One way is to fill the result in the glb global variable, which gets printed in main

## Lab 4
This problem concerns format string vulnerabiltities
------------------------------------------------------------------------------------
1. Look at echo.c. There is a vulnerability. Use it to open a shell.


2. Submit the following:
(a) Label of exploit string: <<your folder name>>
    For  example if your folder is C17B104_CS17B042, then this should 
    be the name of your exploit file with extension .exp.
    in other words, the exploit file will be callled CS17B104_CS17B042.exp 
(b) Save the file in the folder for the assignment
(c) Submit the same exploit string on moodle.
(d) Write a document about how you went about doing the lab

## Lab 5
-- dream team --

This application lets you build your dream cricket team. The team
has 10 players and one secret player. Use a vulnerability in the
program to fill in and your name (or your partner's name) as the
secret player.

## Reading Project
https://drive.google.com/drive/folders/1IVsrwFeez5YKr1SSzyY0D8gKaF_8sc4I?usp=sharing
