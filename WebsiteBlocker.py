# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 15:36:39 2021

@author: Joela

This repository is a beginner-level project. The purpose is to create a script
for a Website Blocker. The user will define a list of websites they want to
have blocked during specific times of the day
"""

# Initialize
blockedWebsites = []
websiteIdx = []

hostLoc = r"C:\Windows\System32\drivers\etc\hosts" #Location of host file
redirect = "127.0.0.1" #IP redirect address

# Import modules
from datetime import datetime as dt
import ctypes
import sys

# Main
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    def BlockWebsites(start_hour, end_hour, blocked_websites):
        while True:
            if (
                dt(dt.now().year, dt.now().month, dt.now().day, start_hour)
                < dt.now()
                < dt(dt.now().year, dt.now().month, dt.now().day, end_hour)
                ):
                
                with open(hostLoc, "r+") as hostfile:
                    hosts = hostfile.read()
                    for site in blocked_websites:
                        if site not in hosts:
                            hostfile.write(redirect + " " + site + "\n")
            else:
                with open(hostLoc, "r+") as hostfile:
                    hosts = hostfile.readlines()
                    hostfile.seek(0)    #seek method used to set pointer back to start of file
                    for line in hosts:
                        if not any([site in line for site in blocked_websites]):
                            hostfile.write(line)
                    
                    hostfile.truncate() #truncate method used to re-write remaining data since file is opened with 'r+' option
                            
        # ######################################################################
        # ''' File read method 1'''
        # ######################################################################
        # if __name__ == "__main__":    
        #     with open("BlockedWebsites.txt", "r") as blockedWebsitesFile:
        #         # Read all lines one by one
        #         for line in blockedWebsitesFile:
        #             line = line.rstrip('\n')    #Remove newline character from string
        #             line = line.replace('"', '')
                    
        #             # Check if current line is a comment or is empty
        #             if "#" in line or len(line) == 0:
        #                 # if line is a comment or is empty, do nothing
        #                 continue
        #             else:
        #                 # Otherwise, add to list of blocked websites
        #                  blockedWebsites.append(line)
            
        #     # Execute Wesbite-Blocker Logic
        #     BlockWebsites(9, 22)            
            
        #######################################################################
        ''' File read method 2'''
        #######################################################################
        if __name__ == "__main__":
            with open("BlockedWebsites.txt", "r") as blockedWebsitesFile:
                # Read all lines into list
                lines = blockedWebsitesFile.readlines()
                        
            # Determine indices of websites to block
            for ii in range(len(lines)):
                lines[ii] = lines[ii].rstrip('\n')  #Remove newline character from string
                lines[ii] = lines[ii].replace('"', '')
                
                # Check if current line is a comment or is empty
                if '#' in lines[ii] or len(lines[ii]) == 0:
                    # if line is a comment or is empty, do nothing
                    continue
                else:
                    # Otherwise, get index
                    websiteIdx.append(ii)
            
            # Create list of blocked wesbites using websiteIdx        
            blockedWebsites = [lines[ii] for ii in websiteIdx]
            
            # Execute Wesbite-Blocker Logic
            BlockWebsites(9, 22, blockedWebsites)
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)