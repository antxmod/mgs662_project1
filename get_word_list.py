import os,glob
import re
import csv
import pandas as pd
#Navigating to the directory 
paths = [os.getcwd()+"\songs"]
                  
Terms_by_file = []
def freq(file_paths):
    for path in file_paths:
        for filename in glob.glob(os.path.join(path, '*.txt')):
            with open(filename, 'r') as f:
                print(filename)
                #splitting file by word and removing all special characters, special characters are not permitted as dict keys.
                #also converting all files to lowercase only as the dictionary is all lowercase.
                contents=f.read()
                contents=contents.lower()
                contents=re.sub(r'[^\w]',' ',contents)
                contents=contents.split()
                Terms=[]
                #loop through each word in the file.
                #each unique word is added to the dictionary with their frequency
                for word in contents:
                    if word not in Terms:
                        Terms.append(word)
                Terms_by_file.append({'file name':os.path.split(filename)[1], 'terms':str(Terms)})
                print(Terms_by_file)
    df=pd.DataFrame.from_dict(Terms_by_file)
    print(df)
    df.to_csv('wordlist.csv')        

    return Terms_by_file