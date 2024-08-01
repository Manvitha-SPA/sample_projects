import re

def scraping():
    with open("1.txt",'r') as file1:
        data = file1.read()
        scmatch = re.search(r'SCR\s*(\w+)', data)
        if scmatch:
            print( "SCR",scmatch.group(1))
        else:
            print("Pattern not found")

        date_match = re.search(r'(\w+\s*\d{1,2},\s*\d{4})', data)
        if date_match:
            print("Date of Decision:", date_match.group(1))
        else:
            print("Date of Decision not found")

        judge_match = re.search(r'\[DR(.*?)\]', data)
        if judge_match:
            print("Judge Name:", judge_match.group(1))
        else:
            print("Judge Name not found")

           
        nature_match = re.search(r'\((.*?)\)', data)
        if nature_match:
            print("Nature of Decision:", nature_match.group(1))
        else:
            print("Nature of Decision not found")

        # case_match = re.search(r'CASE\s*DETAILS\s\n*(.*?)\s*v.\n*(\w*?)', data)
        case_match = re.search(r'CASE\s*DETAILS\s*\n*(.*?)\s*v\.\s*(\w.*?)\s*&?\s*ORs?\s*', data)
        if case_match:
            print("Petitioner:", case_match.group(1))
            print("Respondent:", case_match.group(2))
        else:
            print("Party Names not found")
        

scraping()
# import csv
# import re

# def scraping():
#     with open("1.txt",'r') as file1:
#         data = file1.read()
#         with open("output.csv", 'w', newline='') as csvfile:
#             fieldnames = ['SCR', 'Date of Decision', 'Judge Name', 'Nature of Decision', 'Petitioner', 'Respondent']
#             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#             writer.writeheader()
#             scmatch = re.search(r'SCR\s*(\w+)', data)
#             if scmatch:
#                 writer.writerow({'SCR': scmatch.group(1)})
#             else:
#                 writer.writerow({'SCR': 'Pattern not found'})

#             date_match = re.search(r'(\w+\s*\d{1,2},\s*\d{4})', data)
#             if date_match:
#                 writer.writerow({'Date of Decision': date_match.group(1)})
#             else:
#                 writer.writerow({'Date of Decision': 'Date of Decision not found'})

#             judge_match = re.search(r'\[DR(.*?)\]', data)
#             if judge_match:
#                 writer.writerow({'Judge Name': judge_match.group(1)})
#             else:
#                 writer.writerow({'Judge Name': 'Judge Name not found'})

#             nature_match = re.search(r'\((.*?)\)', data)
#             if nature_match:
#                 writer.writerow({'Nature of Decision': nature_match.group(1)})
#             else:
#                 writer.writerow({'Nature of Decision': 'Nature of Decision not found'})

#             case_match = re.search(r'CASE\s*DETAILS\s*\n*(.*?)\s*v\.\s*(\w.*?)\s*&?\s*ORs?\s*', data)
#             if case_match:
#                 writer.writerow({'Petitioner': case_match.group(1), 'Respondent': case_match.group(2)})
#             else:
#                 writer.writerow({'Petitioner': 'Party Names not found'})

# scraping()
