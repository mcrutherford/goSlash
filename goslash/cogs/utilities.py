"""
File: utilities.py
Author: Mark Rutherford
Created: 8/4/2021 10:58 PM
"""
import os
import json
from typing import Optional, Union

from dotenv import load_dotenv

VERSION = '1.0.0'

load_dotenv()
TOKEN: str = os.environ['DISCORD_TOKEN'] or os.getenv('DISCORD_TOKEN')