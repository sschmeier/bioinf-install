# channnels for bioinf
conda config --add channels r
conda config --add channels bioconda

# update existing
conda update conda
conda update --all

# install software
conda install -y boost
conda install -y zlib

type=`uname -m`
if [ $type -eq "x86_64" ]; then
    # exist for 64bit chnannel not for 32
    conda install -y fastqc       # quality assessment
    conda install -y sickle-trim  # dynamic trimming of reads
    conda install -y velvet       # assembly
else
    wget https://github.com/dzerbino/velvet.git
    echo "Execute: cd velvet; make;"
    wget https://github.com/najoshi/sickle/archive/v1.33.tar.gz
    tar xvzf v1.33.tar.gz
    wget http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.5.zip
    unzip fastqc_v0.11.5.zip
fi


