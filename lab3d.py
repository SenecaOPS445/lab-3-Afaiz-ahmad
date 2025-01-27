#!/usr/bin/env python3

#Author ID: Afaiz-ahmad 

import subprocess

def free_space():
    # Launch the command to get the free disk space in the root directory
    result = subprocess.Popen(
        "df -h | grep '/$' | awk '{print $4}'", 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE, 
        shell=True
    )
    
    # Get the output and strip the newline characters
    output, error = result.communicate()
    
    # Return the output in utf-8, stripped of newline characters
    return output.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
