from tulkit import download_fastq

with open('SRR_Acc_List.txt', 'r') as file:
    srr_list = [line.strip() for line in file.readlines()]

for srr in srr_list:
    download_fastq(srr)
