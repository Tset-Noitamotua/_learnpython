#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from io import StringIO
from io import BytesIO
from robot import run
from robot import run_cli


script, file = argv




# class RF_MardDown_File():
#     """This script is your friend if you want to extract
#     Robot Framework code blocks from a MarkDown (.md) file
#     to execute it with robot.
#     Usage:
#     1. save your robot test suite in one or more ```robot
#        (or ```robotframework) code blocks inside a .md file.
#        Check example_01.md or example_02.md!
#     2. run `python rf_scanner.py example_02.md`
#        --> this will create a robot_data.robot file in cwd
#     3. run `robot robot_data.robot`
#     4. enjoy :)

#     TODO: modify robot.bat and/or robots's run.py to execute
#           .md files in one step like:
#           run `robot cool_markdown_testsuite.md`
#     TODO: combine with mkdocs
#     """

#     def __init__(self):
#         self.file = open(md_file, encoding='utf-8')
#         #self.text = self.file.read()
#         self.position = self.file.tell()
#         #self.file.seek(0)
#         self.line = None

#     def closed(self):
#         if self.file.closed:
#             return True

#     def close(self):
#         self.file.close()

    # def go_to_beginning_of_file(self):
    #     # self.file.seek(0)
    #     print(self.file.tell())

    # def get_position(self):
    #     self.position = self.file.tell()
    #     return self.position

    # @property
    # def position(self,):
    # if self.closed():
    #     raise Exception("File is not opened")
    # return self.file.tell()

    # def read_hole_file(self):
    #     self.file.seek(0)
    #     self.text = self.file.read()
    #     self.position = self.file.tell()
    #     return self.file, self.text, self.position

    # def read_file_line_by_line(self):
    #     self.line = self.file.readline()
    #     return self.line

    # def extract_rf_code_block(self):
    #     # saves robot framework code to `robot_data.robot`  file 
    #     robot_file = open('robot_data.robot', mode='a', encoding='utf-8')
    #     print('--- START OF ROBOT CODE ---')
    #     while not self.file.closed:
    #         self.line = self.file.readline()
    #         if self.line == '```\n':
    #             print('--- END OF ROBOT CODE ---')
    #             break
    #         robot_file.write(self.line)
    #         print(self.line)
    #     robot_file.write('\n')
    #     robot_file.close()



# def main():
#     file = RF_MardDown_File()
#     while not file.closed():
#         file.read_file_line_by_line()
#         if file.line.startswith('```robot'):
#             file.extract_rf_code_block()
#         if file.line == '':
#             # When end of file is reached close it!
#             print('END OF FILE REACHED - CLOSING!')
#             file.close()

def main_pekka(md_file):
    # makes an empty list where we are going to store robot code
    robot_lines = []
    # opens our md_file under alias 'f' and operates all the following
    # statments on it
    with open(md_file, mode='rb', buffering=1) as f:
        # creates a boolean var
        include_line = False
        # for each line of the md_file that we passed as arguement to this script
        # do the steps below
        for line in f:
            if not include_line:
                include_line = line.strip().lower() == "```robotframework"
            elif line.strip() == "```":
                include_line = False
            else:
                robot_lines.append(line)
    robot_data = str(''.join(robot_lines))
    # robot_data = str(''.join(robot_lines))
    print('robot_data: ', robot_data)
    txtfile = BytesIO(robot_data.encode('UTF-8'))
    print('txtfile: ', txtfile)
    return txtfile

    # # print(robot_data)
    # robot_data = str(''.join(robot_lines))
    # robot_file = open('robot_data.robot', mode='w', encoding='utf-8')
    # robot_file.write(robot_data)
    # robot_file.close()

# def copy_original_robot_file(file):
#     file = open(filename, encoding='utf-8')
#     clipboard = file.read()
#     robot_file = open('robot_data.robot', mode='w', encoding='utf-8')
#     robot_file.write(clipboard)
#     file.close()
#     robot_file.close()


if __name__ == '__main__':
    main_pekka(file)
    # main()
