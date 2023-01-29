import os
import shutil
import re

target_suffix = "-SDS.pdf"
suffix_tester = r"(.*?)-SDS-(.*?)\.pdf"

# Paths
source = "/Users/nfiutek/Documents/Rename python test/Start"
final = "/Users/nfiutek/Documents/Rename python test/Finish"

for file_name in os.listdir(source):

    if not file_name.endswith(".pdf"):
        print("Unsupported file format:" + file_name)
        continue

    final_name = None

    if file_name.endswith(target_suffix):
        final_name = file_name
    elif re.match(suffix_tester, file_name):
        start = file_name.find("SDS") + 3
        finish = file_name.find(".pdf")
        final_name = file_name[:start] + file_name[finish:]
    else:
        print("Unknown file name pattern: " + file_name)
        continue

    shutil.copy(source + "/" + file_name, final + "/" + final_name)
