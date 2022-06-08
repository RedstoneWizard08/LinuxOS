#!/usr/bin/env python3.8

'''Downloader and stuff'''
import os
import zlib

from download import download
from organize import organize
from extract import extract

if not os.path.exists("packages/.organized"):
    download("wget-list", "packages", False)
    organize("packages")

with open("packages/.organized", mode="w", encoding="utf-8") as file:
    file.write("")
    file.close()

if not os.path.exists("packages/.extracted"):
    extract("packages", "sources")

with open("packages/.extracted", mode="w", encoding="utf-8") as file:
    file.write("")
    file.close()
