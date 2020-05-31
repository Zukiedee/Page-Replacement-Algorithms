''' 
Zukiswa Lobola - LBLZUK002
OS Assigment 1: Memory Management
FIFO, LRU, Optimal Page Replacement Algorithms
2 June 2020
'''

import random
import sys

''' 
FIFO Page Replacement Algorithm
'''
def FIFO(size, pages):
    frame = []                                                                  # Creates a page frame
    page_faults = 0                                                             # Initialise number of page faults to zero
    
     #loop through each page
    for page in pages:                                    
        
        # Fills up the page frame if memory is not full yet.
        if (len(frame) < size):                            

            if (page not in frame): 
                frame.append(page)
                page_faults += 1    
           
           # Does nothing if page found    
            else: 
                continue     

        # If the memory is full, begin page replacements
        else: 
            
            if (page not in frame):   
                frame.pop(0)  
                frame.append(page)  
                page_faults += 1
    return page_faults

    
''' 
LRU Page Replacement Algorithm
'''
def LRU(size, pages):
    frame = []                                                                  # Creates a list (aka page frame)
    page_faults = 0                                                             # Initialise number of page faults to zero

    # loop through each page
    for page in pages:

        # Fills up the page frame if not full yet.
        if (len(frame) < size):

            if (page not in frame): 
                frame.insert(0, page)
                page_faults += 1    

            else:
                frame.remove(page)
                frame.insert(0,page)       
  
        # If the page frame is full, begin page replacements
        else:
            #If the page is not found, replace the last page with the current page
            if (page not in frame):
                frame.remove(frame[len(frame) - 1])                             # Removes the last element
                frame.insert(0,page)                                            # Add page to memory
                page_faults += 1  
            
            #If the page is found, shuffle the order in page frame
            else:
                frame.remove(page)
                frame.insert(0,page)
    return page_faults


''' 
Optimal Page Replacement Algorithm
'''
def OPT(size, pages):
    frame = []                                                                  # Creates a list 
    page_faults = 0                                                             # Initialise number of page faults
    
    # loop through each page
    for i in range(len(pages)):                                    
        
        # Fills up page frame if not yet full.
        if (len(frame)  < size):                            
            if (pages[i] not in frame):        
                frame.append(pages[i]) 
                page_faults += 1                
            else: 
                continue
        
        # If the page frame is full, begin page replacements             
        else:         
            # If the page is not already in the page frame 
            if (pages[i] not in frame): 
                farthest = -1
                for j in frame:
                    if pages[i:].count(j) == 0: 
                        replacedPage = j 
                        break 
                    else: 
                        tmp = pages[i:].index(j) 
                        if tmp > farthest:
                            farthest = tmp
                            replacedPage = j  
                            
                # Replace page in frame
                index = frame.index(replacedPage)
                frame.remove(replacedPage)
                frame.insert(index,pages[i])
                page_faults += 1
            
            # Does nothing if page found    
            else: 
                continue  
    return page_faults
    
    
''' 
Main method
'''
def main():
    size = int(sys.argv[1])                                                     # size of frame
    N = int(sys.argv[2]) 
    pages = list()                                                              # page reference string
    
    # Generates a random page-reference string
    for i in range (N):
        pages.insert(i, random.randint(0,9))
    
    print ('FIFO', FIFO(size, pages), 'page faults.')
    print ('LRU', LRU(size, pages), 'page faults.')                       
    print ('OPT', OPT(size, pages), 'page faults.')
    
if __name__ == "__main__":
    if len(sys.argv) !=3:
        print ('Usage: python paging.py [number of pages] [size of sequence]')
    else:
        main()