import os

# select the files
# rename the files in a pattern from windows selecting batch

# rename py_tut (1).docx files
# to
# py_ang_100dy_day16 file series
# 29 files will be canged from py_ang_100dy_day16 to py_ang_100dy_day44

for i in range(0, 29):
    old_file_name = "\"py_tut ("+str(i+1)+").docx\""
    new_file_name = " py_ang_100dy_day"+str(i+16)+".docx\""
    command = "ren "+ old_file_name + new_file_name
    print(command)
    os.system(command)

# python rename_files.py