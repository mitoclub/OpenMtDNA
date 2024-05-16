Questions that are interesting to think about:
=> is our beloved common repeat open (and other important pieces - contact zone/etc)?
=> are there any transcription factor signatures?
=> is there some pattern/gradient within the discovered molecules that the authors overlooked? For example, can we see a wave of replication fork movement within a major arc or even across the entire genome?


We have raw GEO data from https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE212611 (Single-nucleoid architecture reveals heterogeneous packaging of mitochondrial DNA): GSE212611_RAW.tar

For each sample there are reads for it that can be downloaded, as well as a “positions versus reads” matrix where for each position in the mitogenome there are numbers from each read (though I don’t understand why there are 6 million reads in the source data, and in the final file we are talking about 20 thousand, maybe read means something else, especially since each read ultimately evaluates the entire genome). A positive value indicates footprint/protection and a negative value indicates available DNA. The number indicates the size of the region spanning that genomic position. Basically, in the sample I'm looking at, all the values mostly vary between 5k, 16k and 49k. Very occasionally reads with -16k slip through. Moreover, each of the 20k reads evaluates each of the 16568 genome positions equally. That is, according to this logic, either the read says that the entire genome is accessible, or the entire genome has a trace/protection. I checked another sample - the same thing: one read = the same number for all positions, sometimes it slips -16569, -6, -11, -98. I will attach 5 lines from the matrix file: columns are positions, rows are reads.

Here is the original description of the files that are available for each sample:
1) bed formatted mapped molecule locations with ZMW ID in column 4 and methylation locations in column 12
2) tsv formatted per-read footprint information with read ID in column 1. Each additional column represents a position in the genome. A positive value indicates a footprint/protection and a negative value indicates accessible DNA. The number indicates the size of the region covering that genomic position
3) pq formatted read info file to go along with tsv file. Contains information on individual footprinted reads including ZMW ID, read ID corresponding to TSV, and methylation count. 


On the other hand, the bed file contains instructions for the coordinates of the blocks.
The file contains the location of the mapped molecules in a layer format with the ZMW ID in column 4 and methylation locations in column 12):
For example, for the first sample: 20446 rows - the same number of rows in the matrix (10414 positive circuits and 10032 negative circuits)
There are row names, ratings and blocks with different coordinates (last column)
For example, here is one line corresponding to the file from which I threw above
chrM 0 16565 m64018_220317_223759/186/ccs 7 + 0 16565 128,0,128 119 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1, 1.1 0.122,125,478,520,555,845,851,865,917,1276,1416,1750,1913,2026,2028,2059,2064,2141,2143,2145,2147,2472,2609,2640,267 1,2873,2874,2878,2879,2983,2999,3002 ,3217,3219,3277,3342,3401,3433,3440,3771,3801,4172,4410,4601,4637,4810,4816,4983,5113,5119,5450,5572,5920,5923,6079,6217, 6379 ,6386,6435,6478,6484,6537,6637,6793,6795,6985,6988,7183,7186,7384,7504,7667,7859,7907,7910,7913,7915,8143,8216,8224,8395, 8398 ,8401,8404,8410,8412,8419,8421,8585,8717,8944,9079,10286,11114,11243,11450,13164,13442,14268,14407,14632,14757,14789,1479 2.14953.15365.15416 ,15483,15665,15702,15959,16248,16384,16386,16398,16404,16434,16564
The last piece of the line is the positions separated by commas


