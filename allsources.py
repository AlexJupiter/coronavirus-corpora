#This combines all sources into one file
import glob

read_files = glob.glob("../Raw_data/Sources/txts/*.txt")

with open("allsources.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())


                
