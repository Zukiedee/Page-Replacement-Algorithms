# Page-Replacement-Algorithms
This program is a simulation of 3 of the many OS Page Replacement Algorithms, namely FIFO, LRU &amp; Optimal.

It is designed to run using the command line terminal on a UNIX operating system. 

## How to run the program:
On the command line: paging.py [arg1] [arg2]
Where arg1 is the size of the frame and arg2 is the length of the page sequence

```
Example:
        input --> paging.py 4 32
        output --> FIFO 18 page faults.
                   LRU 17 page faults.
                   OPT 13 page faults.
```

### Explanation of program
The program generates a random string sequence of length [arg2] and passes the string and frame size through each page replacement algorithm in order to calcualte how many page faults occur from the algorithm and outputs it to the user.

## Author
> Zukiswa Lobola (LBLZUK002)
