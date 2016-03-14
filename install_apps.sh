# channnels for bioinf
conda config --add channels r
conda config --add channels bioconda

# update existing
conda update conda
conda update --all

# install software
conda install -y fastqc       # quality assessment
conda install -y sickle-trim  # dynamic trimming of reads
conda install -y velvet       # assembly
