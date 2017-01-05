#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Execute Robot Framework (RF) test inside of MarkDown files (.md).

Usage examples:
> robot_1.bat example_01.md
> robot_1.bat example_02.md
> robot_1.bat example_03.robot

Limitations:
You can run only one .md / .robot file at one without commandline options!


----- robot_1.bat ---------------------------
@echo off
python.exe -m rf_scanner_1 %*
python.exe -m robot.run robot_data.robot
-------------------------------------------


"""
from sys import argv
script, filename = argv


def main(filename):
    robot_lines = []
    with open(filename, encoding='utf-8') as md_file:
        include_line = False
        for line in md_file:
            if not include_line:
                include_line = line.strip().lower() == "```robotframework"
            elif line.strip() == "```":
                include_line = False
            else:
                robot_lines.append(line)
    robot_data = str(''.join(robot_lines))
    robot_file = open('robot_data.robot', mode='w', encoding='utf-8')
    robot_file.write(robot_data)
    robot_file.close()

def copy_original_robot_file(file):
    """In case a .robot file is called"""
    file = open(filename, encoding='utf-8')
    clipboard = file.read()
    robot_file = open('robot_data.robot', mode='w', encoding='utf-8')
    robot_file.write(clipboard)
    file.close()
    robot_file.close()


if __name__ == '__main__':
    if str(filename).endswith('.robot'):
        copy_original_robot_file(filename)
    else:
        main(filename)
