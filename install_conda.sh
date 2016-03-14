# downloading and installing miniconda

type=`uname -m`
if [ $type -eq "x86_64" ]; then
    minconda=Miniconda-latest-Linux-x86_64.sh
else
    minconda=Miniconda-latest-Linux-x86.sh
fi

if [ -e  $minconda ]; then
    echo "File already downloaded."
else
    wget https://repo.continuum.io/miniconda/$minconda
fi

/bin/bash $minconda
#rm $minconda

# prepend path
echo export PATH=~/miniconda2/bin:\$PATH >> ~/.bashrc

