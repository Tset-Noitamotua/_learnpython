# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

#xfile = open(filename, encoding='utf-8')
#print(type(xfile))


# print(md_file.read())
# end_position = md_file.tell()

# Lesekopf wieder auf null
# position = md_file.seek(0)

class RF_MardDown_File():
    """This script is your friend if you want to extract
    Robot Framework code blocks from a MarkDown (.md) file
    to execute it with robot.
    Usage:
    1. save your robot test suite in one or more ```robot
       (or ```robotframework) code blocks inside a .md file.
       Check example_01.md or example_02.md!
    2. run `python rf_scanner.py example_02.md`
       --> this will create a robot_data.robot file in cwd
    3. run `robot robot_data.robot`
    4. enjoy :)
    """

    def __init__(self):
        pass
        self.file = open(filename, encoding='utf-8')
        #self.text = self.file.read()
        self.position = self.file.tell()
        #self.file.seek(0)
        self.line = None

    def closed(self):
        if self.file.closed:
            return True

    def close(self):
        self.file.close()

    def go_to_beginning_of_file(self):
        # self.file.seek(0)
        print(self.file.tell())

    def get_position(self):
        self.position = self.file.tell()
        return self.position

    def read_hole_file(self):
        self.file.seek(0)
        self.text = self.file.read()
        self.position = self.file.tell()
        return self.file, self.text, self.position

    def read_file_line_by_line(self):
        self.line = self.file.readline()
        return self.line

    def extract_rf_code_block(self):
        # saves robot framework code to `robot_data.robot`  file 
        robot_code = open('robot_data.robot', mode='a', encoding='utf-8')
        print('--- START OF ROBOT CODE ---')
        while not self.file.closed:
            self.line = self.file.readline()
            if self.line == '```\n':
                print('--- END OF ROBOT CODE ---')
                break
            robot_code.write(self.line)
            print(self.line)
        robot_code.write('\n')
        robot_code.close()
        # print(self.line)
        #while self.line != '```\n':
        #    self.line = self.file.readline()
        #    print(self.line)



def main():
    file = RF_MardDown_File()
    while not file.closed():
        file.read_file_line_by_line()
        if file.line.startswith('```robot'):
            file.extract_rf_code_block()
        if file.line == '':
            # When end of file is reached close it!
            print('END OF FILE REACHED - CLOSING!')
            file.close()


if __name__ == '__main__':
    main()
