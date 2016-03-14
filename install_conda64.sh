# downloading and installing miniconda

# miniconda 64bit
wget https://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
/bin/bash Miniconda-latest-Linux-x86_64.sh
rm Miniconda-latest-Linux-x86_64.sh

# prepend path
echo "export PATH=~/miniconda2/bin/:$PATH" >> ~/.bashrc
