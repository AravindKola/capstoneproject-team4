from Level_1.Findfile import FileFinder
from Level_1.SystemDriveFinder import SystemDriveFinder
class Test_Drive:
    def test_DriveCase(self):
        obj=SystemDriveFinder()
        self.expected=obj.find_drives()
        self.actual=['C']
        assert self.expected==self.actual

    def test_searchfile(self):
        obj=FileFinder()
        d=obj.find_file('demo.txt','c:\hcl')
        self.expected_filename=d[0]
        self.actual_res='c:\\hcl\\demo.txt'
        assert self.expected_filename==self.actual_res