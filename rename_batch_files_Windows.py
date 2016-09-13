import os

##to give a new file extension to a batch of files in a particular folder:
# for file in os.listdir('C:\\Users\\USERNAME\\Documents\\testFolder'):
#     orig_filename = str(file[:-4])
#     new_extension = ".txt"
#     new_filename = orig_filename+new_extension
#     os.rename('C:\\Users\\USERNAME\\Documents\\testFolder\\'+file, 'C:\\Users\\USERNAME\\Documents\\testFolder\\'+new_filename)
# print(); print("Done.")

##to give a new file name to files without changing the extension:
# a=0
# for file in os.listdir('C:\\Users\\USERNAME\\Documents\\testFolder'):
#     new_filename = "IMS00"+str(a)
#     extension = str(file[-4:])
#     newFile = new_filename+extension
#     os.rename('C:\\Users\\USERNAME\\Documents\\testFolder\\'+file, 'C:\\Users\\USERNAME\\Documents\\testFolder\\'+newFile)
#     a+=1
# print(); print("Done.")

##change both file name and extension simultaneously:
a=0
for file in os.listdir('C:\\Users\\USERNAME\\Documents\\testFolder'):
    new_filename = "IMG00"+str(a)
    new_extension = ".jpg"
    newFile = new_filename+new_extension
    os.rename('C:\\Users\\USERNAME\\Documents\\testFolder\\'+file, 'C:\\Users\\USERNAME\\Documents\\testFolder\\'+newFile)
    a+=1
print(); print("Done.")