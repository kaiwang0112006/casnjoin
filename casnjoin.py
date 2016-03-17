import csv
content = {}
            
with open('22.csv') as fin:
    fcsv = csv.reader(fin,delimiter = ',')
    for eachline in fcsv:
        if fcsv.line_num == 1:
            title = eachline
        else:
            content[eachline[4]] = eachline

writer = csv.writer(file('3.csv', 'wb'))
  
with open('11.csv','rb') as fin:
    fcsv = csv.reader(fin,delimiter = ',', quotechar = '"')
    for eachline in fcsv:
        if fcsv.line_num == 1:
            titlenew = title + eachline
            writer.writerow(titlenew)
        else:
            if eachline[2] in content:
                newcontent = content[eachline[2]] + eachline
                writer.writerow(newcontent)

            else:
                print eachline
                print 'unmatch'