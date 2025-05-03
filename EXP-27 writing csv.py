import csv
fields=['NAME','BRANCH','YEAR','CGPA']
rows=[['nikhil','coe',2,9.1],['sanchit','EEE',2,4.4],['bha','ECE',3,4.3]]
file="university_records.csv"
with open(file,'w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
