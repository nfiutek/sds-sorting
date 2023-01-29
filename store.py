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
        continue

    final_name = None

    if file_name.endswith("-SDS-Enamine.pdf"):
        final_name = file_name.replace("-SDS-Enamine.pdf", target_suffix)
    elif file_name.endswith("-SDS-Sigma.pdf"):
        final_name = file_name.replace("-SDS-Sigma.pdf", target_suffix)
    elif file_name.endswith("-SDS-Matrix.pdf"):
        final_name = file_name.replace("-SDS-Matrix.pdf", target_suffix)
    elif file_name.endswith("-SDS-Combi.pdf"):
        final_name = file_name.replace("-SDS-Combi.pdf", target_suffix)
    elif file_name.endswith("-SDS.pdf"):
        final_name = file_name
    else:
        print("Error : Problem with replacing")
        continue

    shutil.copy(source + "/" + file_name, final + "/" + final_name)
