# Reading in .csv files
import csv

# Provides function for viewing, creating, and removing a directory
import os

# Moving files
import shutil

# Paths
sds_root = "/Users/nfiutek/Documents/Sorting python test"
sds_source = sds_root + "/Source"
sds_dangerous = sds_root + "/Dangerous"
sds_safe = sds_root + "/Safe"
sds_unknown = sds_root + "/Unknown"
sds_index = sds_root + "/sds_index.csv"


# Initialize file system
def create_missing_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)


if not os.path.exists(sds_root):
    raise SystemExit("Unable to find root project path: " + sds_root)
if not os.path.exists(sds_index):
    raise SystemExit("Unable to find sds index file at: " + sds_index)
create_missing_folder(sds_source)
create_missing_folder(sds_dangerous)
create_missing_folder(sds_safe)
create_missing_folder(sds_unknown)

index_csv = {}

with open(sds_index, 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)
    for row in csvreader:
        index_csv[row[0]] = row[2]


def index_folder(folder):
    index_local = {}
    for file_sds in os.listdir(folder):
        if not file_sds.endswith(".pdf"):
            continue
        cas_id = file_sds.replace("-SDS.pdf", "")
        index_local[cas_id] = file_sds
    return index_local


index_dangerous = index_folder(sds_dangerous)
index_safe = index_folder(sds_safe)
index_start = index_folder(sds_source)
#
# for dangerous_file in os.listdir(sds_dangerous):
#     if not dangerous_file.endswith(".pdf"):
#         continue
#     cas_id = dangerous_file.replace("-SDS.pdf", "")
#     index_dangerous[cas_id] = dangerous_file


mismatch_csv = index_csv.keys() - index_dangerous.keys() - index_safe.keys() - index_start.keys()

with open(sds_unknown + '/cas missing from files.txt', 'w') as file:
    file.write("\n".join(mismatch_csv))


def remove_mismatches(known_cas, folder_index, source_folder, target_folder):
    for cas, file_name in folder_index.items():
        if cas not in known_cas:
            shutil.move(source_folder + "/" + file_name , target_folder + "/" + file_name)


remove_mismatches(index_csv.keys(), index_dangerous, sds_dangerous, sds_unknown)
remove_mismatches(index_csv.keys(), index_safe, sds_safe, sds_unknown)
remove_mismatches(index_csv.keys(), index_start, sds_source, sds_unknown)

index_dangerous = index_folder(sds_dangerous)
index_safe = index_folder(sds_safe)
index_start = index_folder(sds_source)


def move_files_by_tag(cas_index, folder_index, source_folder, tag, tag_folder):
    if source_folder.strip().casefold() == tag_folder.strip().casefold():
        return
    for cas, file_name in folder_index.items():
        file_tag = cas_index[cas]
        if tag.strip().casefold() == file_tag.strip().casefold():
            shutil.move(source_folder + "/" + file_name, tag_folder + "/" + file_name)


move_files_by_tag(index_csv, index_dangerous, sds_dangerous, "No", sds_safe)
move_files_by_tag(index_csv, index_safe, sds_safe, "Yes", sds_dangerous)
move_files_by_tag(index_csv, index_start, sds_source, "No", sds_safe)
move_files_by_tag(index_csv, index_start, sds_source, "Yes", sds_dangerous)


#lst = os.listdir("/Users/nfiutek/Documents/Sorting python test/Start")

# for sds in os.listdir(sds_source):
#     chemical_id = sds.replace("-SDS.pdf", "")
#     is_dangerous = index[chemical_id]
#     print("SDS: %s, chemical: %s, is dangerous: %s" % (sds, chemical_id, is_dangerous))
#     if is_dangerous == "Yes":
#         shutil.copy(sds_source + "/" + sds, sds_dangerous + "/" + sds)
#     elif is_dangerous == "No":
#         shutil.copy(sds_source + "/" + sds, sds_safe + "/" + sds)
#
#     else:
#         print("Unable to move sds file" % (sds, is_dangerous))




#print(lst)

