# nucleo_trimmer
This is a nucleotide sequence trimmer when given a FASTQ file. The program was created following the prompt below:
Allow the user to trim a series of nucleotide sequence record based on the quality score. User should be prompted for a score cutoff, after which a new file ("assignment2_trimmed.fastq") should be generated of the FASTQ records with the sequence and quality score lines trimmed based on that selection.  Two things of note: first, 
the scoring line is scored using ASCII characters. The score, from 0 - 42 (with 42 being the highest) can be found by using the built in function ord() on the character, then subtracting 64. Secondly, these quality scores are subject to a degree of randomness.
Please use a sliding window approach, similar to how you identify codons, 
to find the area at which the score drops off.  Once the average score in your window drops below the threshold, then trim at that location. Your code should be organized using a main function and others.
