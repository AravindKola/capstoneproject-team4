import os
class SystemDriveFinder:

    def __init__(self):
        pass

    def find_drives(self):
        #Write the logic to get all the drives in the system(Active or inactive)
        print("This is the find find drives method of System Drive Finder class:")
        drives=[]
        for i in range(65,91):
            if os.path.exists(chr(i)+":"):
                drives.append(chr(i))
        return drives

if __name__ == '__main__':
    sdf=SystemDriveFinder()
    print(sdf.find_drives())
