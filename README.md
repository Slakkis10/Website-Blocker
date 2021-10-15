# Website-Blocker
## Overview
This repository is a beginner-level project. The purpose is to create a script for a Website Blocker. The user will define a list of websites they want to have blocked during 
specific times of the day

## Procedures:
1. Update "BlockedWebsites.txt" with the list of websites to block
2. Update "start_hour" (line 17. with the hour in the day to begin blocking the list of websites
3. Update "end_hour" (line 18. with the hour in the day to stop blocking the list of websites
4. Updates "hostLoc" (line 19. with the location to your OS host file
	1. For Windows: C:\Windows\System32\drivers\etc\hosts
	2. For Linux: /etc/hosts
5. Update "redirect" with IP address to redirect to if website is accessed

## Dependencies
*python3 | 3.7.10

