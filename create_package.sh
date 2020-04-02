#!/bin/bash
echo "Creation du package $1"
package_name=$1
class_name=`sed -e "s/-\(.\)/\U\1/g" -e  "s/^\(.\)/\U\1/" <<< $package_name`
echo "nom du paquet : $package_name" 
echo "nom de la classe : $class_name" 
cp -r ../temp $package_name
cd $package_name
sed -i "s/@class name@/$class_name/g" package.py
sed -i "s/@package name@/$package_name/g" package.py
for vers in 2.7.0 2.6.0 2.5.2 2.5.1 2.5.0 2.4.2 2.4.1 2.4.0
do
   echo 1 | spack checksum $package_name $vers | grep "version(" >> checksum
done
cat checksum
sed -i "/.*#@CHECKSUM@/r checksum" package.py
sed -i "/.*#@CHECKSUM@/d" package.py

