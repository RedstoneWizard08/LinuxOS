#!/usr/bin/env python3.8

'''Downloads all files shown in a wget-list file.'''
import urllib.request
import os
from pathlib import Path


def rmdir(directorypath: str):
    '''Recursively deletes a directory.'''
    directory = Path(directorypath)

    for item in directory.iterdir():
        if item.is_dir():
            rmdir(item)
        else:
            item.unlink()

    directory.rmdir()


def download(file: str, root: str, clear: bool):
    '''Downloads all the files in a wget-list file.'''

    if clear:
        if os.path.exists(root):
            rmdir(root)

    if not os.path.exists(root):
        os.mkdir(root)

    with open(file, mode="r", encoding="utf-8") as file:
        raw = file.read().strip()
        file.close()

        urls = raw.split("\n")

        def downloadfile(downloadurl: str, output: str):
            '''Downloads a file from a URL to the output provided.'''
            urllib.request.urlretrieve(downloadurl, output.lower())

        for url in urls:
            if url.startswith("#") or url.startswith(";"):
                continue

            name = url.split("/").pop()
            host = url.replace("http://", "").replace("https://",
                                                      "").split("/")[0]
            proto = url.split(":")[0]

            if not os.path.exists(root + "/" + name):
                print(
                    f"Downloading {root}/{name.lower()} from {host} ({proto})...")
                downloadfile(url, root + "/" + name.lower() + ".incomplete")
                os.rename(root + "/" + name.lower() +
                          ".incomplete", root + "/" + name.lower())
