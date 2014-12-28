# Import to read from commandline
import pandas

# List the csv file, the name for the DataFrame, and the file for the DataFrame
csvName = "C:\PandP\GenITypes\genItypechart.csv"
dataFrameName = "typeChart"
dataFrameFile = "C:\PandP\Utilities\genItypechart.txt"

# Turn the csv into a DataFrame
dataFrame = pandas.read_csv(csvName)

# Open text file
textFile = open(dataFrameFile, "w")

# Write the first line
textFile.write(str(dataFrameName) + " = { \n")
# Fill in the rest
for column in dataFrame:
	# If it's not the last column end on ", \n"
	if column != dataFrame.columns[len(dataFrame)]:
		textFile.write("'" + str(column) + "' : " + 
			str(dataFrame[column].tolist()) + ", \n")
	# Last column ends on " }"
	else:
		textFile.write("'" + str(column) + "' : " + 
			str(dataFrame[column].tolist()) + " }")

textFile.write("\n" + str(dataFrameName) + " = pandas.DataFrame(" + 
	str(dataFrameName) + ")")

# Close text file			
textFile.close()

# Finished
print('Done')
