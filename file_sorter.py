#!/anaconda/bin/python

import os
import re
import shutil


class file_sorter(object):

    def __init__(self, main_dir):

        self.main_dir = main_dir
        self.files = []
        files = os.listdir(main_dir)
        for f in files:
            if '.' in f:
                self.files.append(f)
            else:
                pass
        self.extensions = (r'\.([pdf]|[jpg]|[csv]|[dmg]|[iso]|[app]|'
                           '[tar]|[xip])+$')
        self.exceptions = r'([\$recycle\.bin]|[\.ds_store]|[\.localized])+'
        self.filetypes = []

    def create_dir(self, file_type):
        new_dir = self.main_dir + file_type.replace(".", "") + "/"
        if os.path.exists(new_dir):
            return(new_dir)
        else:
            os.makedirs(new_dir)
            print("%s directory created" % new_dir)
            return(new_dir)

    def sort(self):

        for f in self.files:
            try:
                file = f.lower()
                search = re.search(self.extensions, file)
                temp = search.group(0)
                destination = self.create_dir(temp)
                current = self.main_dir + file
                shutil.move(current, destination)
                print("moved %s to %s" % (file, destination))
            except (TypeError, AttributeError) as e:
                if re.match(self.exceptions, file) is not None:
                    pass
                else:
                    print("There was an issue with %s" % file)
                    print(e)
                    pass


if __name__ == "__main__":
    main_dir = "/Users/dustin/Downloads/"
    sorter = file_sorter(main_dir)
    sorter.sort()
