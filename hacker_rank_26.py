# When users post an update on social media,such as 
# a URL, image, status update etc., other users in their network are able to 
# view this new post on their news feed. Users can also see exactly when the post was published, 
# i.e, how many hours, minutes or seconds ago.

# Since sometimes posts are published and viewed in different time zones, 
# this can be confusing. You are given two timestamps of one such post 
# that a user can see on his newsfeed in the following format:

# Day dd Mon yyyy hh:mm:ss +xxxx

# Here +xxxx represents the time zone. 
# Your task is to print the absolute difference (in seconds) between them.

# Sample Input 0
# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000

# Sample Output 0
# 25200

import math
import os
import random
import re
import sys
from datetime import date, time, datetime

def time_delta(t1, t2):
    
    # Define the datetime format
    date_format = "%a %d %b %Y %H:%M:%S %z"
    
    # Convert the datetime strings to datetime objects
    dt1 = datetime.strptime(t1, date_format)
    dt2 = datetime.strptime(t2, date_format)
    
    # Calculate the difference in seconds
    delta_seconds = int(abs(dt1-dt2).total_seconds())
    
    # # Return the difference as a string
    return str(delta_seconds)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()