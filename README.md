# nucleo_trimmer
This is a nucleotide sequence trimmer when given a FASTQ file. The file contains quality score given in ASCII characters and the user is asked to give a score cutoff. Restrictions include using a sliding window approach, trim once the average of the window drops below the threshold, and use a main() function.
