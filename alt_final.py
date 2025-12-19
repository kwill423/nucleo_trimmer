#Alternative Final Assignment
#Kayla Williams
'''
Allow the user to trim a series of nucleotide sequence record based 
on the quality score. User should be prompted for a score cutoff, 
after which a new file ("assignment2_trimmed.fastq") should be 
generated of the FASTQ records with the sequence and quality score 
lines trimmed based on that selection.  Two things of note: first, 
the scoring line is scored using ASCII characters. The score, from 
0 - 42 (with 42 being the highest) can be found by using the built 
in function ord() on the character, then subtracting 64.  For
instance:

ord("g") -64 = 39

Secondly, these quality scores are subject to a degree of randomness.
Generally speaking, the first part of the read is high quality, and
that tends to drop off the longer the read continues.  It is best to
use a sliding window approach, similar to how you identify codons, 
to find the area at which the score drops off.  Once the average 
score in your window drops below the threshold, then trim at that 
location.  How big you make your window is up to you.

Your code should be organized using a main function and others. 
'''
#this is the function that reads in the fastq file and produces a list to store the records
def read_fastq(file):
	all_records = []
	with open(file) as fh:
		while True:
			header = fh.readline().strip()
			if not header:
				break
			sequence = fh.readline().strip()
			plus_header = fh.readline().strip()
			qual_score = fh.readline().strip()
			all_records.append((header,sequence,plus_header,qual_score))
		return all_records

#this function then takes the records and trims at the appropriate index for each record and allows user to choose reading frame and cut off point
def fastq_trimmer(all_records,frame=3):
	cut_off = float(input("Please enter a cut off value from 0-42: "))
	trimmed_records = []

	for content in all_records:
		trimmed_header = content[0]
		trimmed_sequence = content[1]
		trimmed_plus_header = content[2]
		trimmed_qual_score = content[3]

		trim_index = len(trimmed_qual_score)
		for s in range(len(trimmed_qual_score)-frame+1):
			score = 0
			for f in range(frame):
				score += ord(trimmed_qual_score[s+f])-64
			frame_avg = score/frame
			if frame_avg < cut_off:
				trim_index = s
				break
		trimmed_sequence = trimmed_sequence[:trim_index]
		trimmed_qual_score = trimmed_qual_score[:trim_index]

		trimmed_records.append((trimmed_header,trimmed_sequence,trimmed_plus_header,trimmed_qual_score))
		return trimmed_records

#this function turns the trimmed records into a new FASTQ file 
def updated_fastq(trimmed_records,file):
	with open(file, "w") as fout:
		for records in trimmed_records:
			for element in records:
				fout.write(element+'\n')
	return
#the main() function is what allows us to call all the functions above together for the same file and return the new FASTQ file
def main():

	all_records = read_fastq("assignment2v2.fastq")	
	trimmed_records = fastq_trimmer(all_records)
	updated_fastq(trimmed_records,"assignment2_trimmed.fastq")
	return

if __name__ == '__main__':
	main()











		



























