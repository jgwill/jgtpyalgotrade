pversion=0.23
nversion=0.23
cdir=$(pwd)

cd jgtpyalgotrade
for f in $(ls *);do sed -i 's/'$pversion'/'$nversion'/g' $f &>/dev/null;done
cd $cdir
cd doc
for f in $(ls *);do sed -i 's/'$pversion'/'$nversion'/g' $f &>/dev/null;done
cd $cdir
cd docker
for f in $(ls *);do sed -i 's/'$pversion'/'$nversion'/g' $f &>/dev/null;done
cd $cdir
cd testcases
for f in $(ls *);do sed -i 's/'$pversion'/'$nversion'/g' $f &>/dev/null;done
cd $cdir
for f in $(ls *);do sed -i 's/'$pversion'/'$nversion'/g' $f &>/dev/null;done

