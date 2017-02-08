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

# from robot.utils import Utf8Reader
# from io import StringIO

from io import BytesIO
from io import StringIO
from .txtreader import TxtReader

def MarkDownReader():

    class MarkDownReader(object):

        def __init__(self):
            self.line = ''
            self.robot_lines = []
            self.robot_data = ''

        def read(self, md_file, rawdata):
            md_file.seek(0)
            print(md_file)
            f = StringIO(md_file.read().decode('UTF-8'))
            try:
                include_line = False
                for line in f.readlines():
                    # print(line)
                    if not include_line:
                        include_line = line.strip().lower() == "```robotframework"
                    elif line.strip() == "```":
                        include_line = False
                    else:
                        self.robot_lines.append(line)
                self.robot_data = str(''.join(self.robot_lines))
            finally:
                f.close()
                print('\n========== OUTPUT :\n', self.robot_data)
                return self._read_text(self.robot_data, rawdata)

        def _read_text(self, data, rawdata):
            txtfile = BytesIO(data.encode('UTF-8'))
            print(txtfile)
            return TxtReader().read(txtfile, rawdata)

        # def _read_html(self, doctree, rawdata):
        #     htmlfile = BytesIO()
        #     htmlfile.write(publish_from_doctree(
        #         doctree, writer_name='html',
        #         settings_overrides={'output_encoding': 'UTF-8'}))
        #     htmlfile.seek(0)
        #     return HtmlReader().read(htmlfile, rawdata)

    return MarkDownReader()