# Import to read from commandline
import sys
import pandas

# Get ONE file from the commandline
filename = sys.argv[-1]
# Turn into a DataFrame
file = pandas.read_csv(filename)

# Move through the DataFrame by column
for column in file:
	# If the column is not numbers (or boolean), look through it for strings
	if file[column].dtype == 'object':
		# Use the index to move down the row
		for i in file[column].index:
			# If the cell contains a number, make it uppercase
			if isinstance(file[column][i],basestring):
				file[column][i] = file[column][i].upper()

#print(file)
# Save the file back
file.to_csv(filename,index=False)
print('Done')
