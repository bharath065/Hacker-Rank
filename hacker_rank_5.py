#You are given an integer,n . Your task is to print an alphabet rangoli of size n . 
#(Rangoli is a form of Indian folk art based on creation of patterns.)
#Different sizes of alphabet rangoli are shown below:

#size 3
#----c----
#--c-b-c--
#c-b-a-b-c
#--c-b-c--
#----c----

#size 5
#--------e--------
#------e-d-e------
#----e-d-c-d-e----
#--e-d-c-b-c-d-e--
#e-d-c-b-a-b-c-d-e
#--e-d-c-b-c-d-e--
#----e-d-c-d-e----
#------e-d-e------
#--------e--------

#size 10
#------------------j------------------
#----------------j-i-j----------------
#--------------j-i-h-i-j--------------
#------------j-i-h-g-h-i-j------------
#----------j-i-h-g-f-g-h-i-j----------
#--------j-i-h-g-f-e-f-g-h-i-j--------
#------j-i-h-g-f-e-d-e-f-g-h-i-j------
#----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
#--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
#j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
#--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
#----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
#------j-i-h-g-f-e-d-e-f-g-h-i-j------
#--------j-i-h-g-f-e-f-g-h-i-j--------
#----------j-i-h-g-f-g-h-i-j----------
#------------j-i-h-g-h-i-j------------
#--------------j-i-h-i-j--------------
#----------------j-i-j----------------
#------------------j------------------

#Sample Input:
# 5
#Sample Output:
#--------e--------
#------e-d-e------
#----e-d-c-d-e----
#--e-d-c-b-c-d-e--
#e-d-c-b-a-b-c-d-e
#--e-d-c-b-c-d-e--
#----e-d-c-d-e----
#------e-d-e------
#--------e--------


def print_rangoli(size):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lines = []
    for i in range(size):
        s = '-'.join(alphabet[size-1:i:-1] + alphabet[i:size])
        lines.append(s.center(4*size-3, '-'))
    full_pattern = lines[::-1] + lines[1:]
    print('\n'.join(full_pattern))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)