# -*- coding: utf-8 -*-

class robotized():

    def __init__(self, md_file):
        self.md_file = md_file
        self.md_file.read()

    def __enter__(self):
        # set things up
        robot_lines = []
        include_line = False
        for line in self.md_file:

            if not include_line:
                include_line = line.strip().lower() == "```robotframework"
            elif line.strip() == "```":
                include_line = False
            else:
                robot_lines.append(line)
        result = str(''.join(robot_lines))
        return result

    def __exit__(self, *exc_info):
        # tear things down
        pass

# with robotized() as robot_data:
#   ++ some code here ++

    def main_pekka(filename):
        # makes an empty list where we are going to store robot code
        robot_lines = []
        # opens our file under alias 'md_file' and operates all the following
        # statments on it
        with open(filename, 'rb') as md_file:
            # creates a boolean var
            include_line = False
            # for each line of the file that we passed as arguement to this script
            # do the steps below
            for line in md_file:
                if not include_line:
                    include_line = line.strip().lower() == "```robotframework"
                elif line.strip() == "```":
                    include_line = False
                else:
                    robot_lines.append(line)
        # robot_data = StringIO(''.join(robot_lines))
        robot_data = str(''.join(robot_lines))