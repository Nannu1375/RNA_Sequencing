import subprocess

# Function to read SRR_Acc_List and download the corresponding FASTQ files
def download_fastq(srr_id):
    try:
        # prefetch to download SRR data
        print(f"Downloading {srr_id}...")
        subprocess.run(["prefetch", "-O", "/media/nannu/Briefcase/RNA_Seq/fastq_files", srr_id], check = True)

        # use fasterq-dump to convert SRR data to their .fastq files
        print(f"Converting {srr_id} to FASTQ...")
        subprocess.run(["fasterq-dump", "--split-files", "--gzip", "--outdir", "/media/nannu/Briefcase/RNA_Seq/fastq_files" f"{srr_id}.sra"])

        print(f"{srr_id} has been downloaded and converted to FASTQ.")
    except subprocess.CalledProcessError as e:
        print(f"Error processing {srr_id}: {e}")

