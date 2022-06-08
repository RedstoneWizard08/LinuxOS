#!/usr/bin/env python3.8

'''Organizer for raw source packages.'''
import os
import re


def organize(root: str):
    '''Organizes all the raw source packages in a directory.'''
    raw = os.listdir(root)
    files = {}

    for file in raw:
        if (
            file.endswith(".gz")
            or file.endswith(".xz")
            or file.endswith(".bz2")
            or file.endswith(".patch")
        ):
            if not file[0] in files:
                files[file[0]] = []

            files[file[0]].append(file)

    for (key, value) in files.items():
        if not os.path.exists(root + "/" + key):
            os.mkdir(root + "/" + key)

        for file in value:
            if not os.path.exists(root + "/" + key + "/" + file):
                if "-" in file:
                    package = file.split("-")[0]
                else:
                    regex = re.compile("([a-zA-Z]+)([0-9]+)")
                    package = regex.match(file).group(1)

                folder = root + "/" + key + "/" + \
                    package.replace("tcl8.6.12", "tcl")

                if not os.path.exists(folder):
                    os.mkdir(folder)

                os.rename(root + "/" + file, folder + "/" + file)
