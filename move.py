import re

suffix_tester = r"-SDS-(.*?)\.pdf"

file_name = "12345-5-6-SDS-Combi.pdf"

print("12345-5-6-SDS-Sigma.pdf".find('SDS'))
print("12345-5-6-SDS-Sigma.pdf".find('.pdf'))

print(file_name[:13] + file_name[19:])