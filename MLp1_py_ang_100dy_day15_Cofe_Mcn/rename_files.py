import os

# select the files
# rename the files in a pattern from windows selecting batch

# rename_files_1 (1).py

for i in range(0, 17):
    old_file_name = "\"rename_files_1 ("+str(i+1)+").py\""
    new_file_name = " test_by_pythn_day_15_"+str(i+1)+".py\""
    command = "ren "+ old_file_name + new_file_name
    print(command)
    os.system(command)

# python rename_files.py