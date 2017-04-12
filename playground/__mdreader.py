#  Copyright 2008-2015 Nokia Networks
#  Copyright 2016-     Robot Framework Foundation
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from io import BytesIO
from io import StringIO
from robot.utils import Utf8Reader


NBSP = u'\xA0'


class MarkDownReader(object):

    def read(self, markdown_file, populator):
        process = False

        # makes an empty list where we are going to store robot code
        robot_lines = []
        # opens our file under alias 'md_file' and operates all the following
        # statments on it
        with open(markdown_file) as md_file:
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
        robot_data = str(''.join(robot_lines))
        print(robot_data)
        # txtfile = BytesIO(robot_data.encode('UTF-8'))
        a = StringIO(robot_data)

        for row in a.readlines():
            row = self._process_row(row)
            cells = [self._process_cell(cell) for cell in self.split_row(row)]
            if cells and cells[0].strip().startswith('*') and \
                    populator.start_table([c.replace('*', '') for c in cells]):
                process = True
            elif process:
                populator.add(cells)
        populator.eof()

    def _process_row(self, row):
        if NBSP in row:
            row = row.replace(NBSP, ' ')
        return row.rstrip()

    @classmethod
    def split_row(cls, row):
        return row.split('\t')

    def _process_cell(self, cell):
        if len(cell) > 1 and cell[0] == cell[-1] == '"':
            cell = cell[1:-1].replace('""', '"')
        return cell
