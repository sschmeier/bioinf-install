# downloading and installing miniconda

# miniconda
if [ -e  Miniconda-latest-Linux-x86.sh ]; then
    echo "File already downloaded."
else
    wget https://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86.sh
fi

/bin/bash Miniconda-latest-Linux-x86.sh
#rm Miniconda-latest-Linux-x86.sh

# prepend path
echo export PATH=~/miniconda2/bin:\$PATH >> ~/.bashrc
source ~/.bashrc

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
