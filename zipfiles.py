
import sys
from zipfile import ZipFile

def zip(file1, file2, file3):

    zipObj = ZipFile('Experiment.zip', 'w')


    zipObj.write(file1)
    zipObj.write(file2)
    zipObj.write(file3)
    zipObj.write(file4)



    zipObj.close()














if __name__ == '__main__':
    args = sys.argv
    file1, file2, file3, file4 = str(args[1]), str(args[2]), str(args[3]), str(args[4])
    file1 = file1.split("/")[-1]
    file2 = file2.split("/")[-1]
    file3 = file3.split("/")[-1]
    file4 = file4.split("/")[-1]
    print(file1)



    zip(file1, file2, file3)