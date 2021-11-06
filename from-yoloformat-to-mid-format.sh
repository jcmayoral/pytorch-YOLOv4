#/usr/bin/bash
echo $2
while read -r image;
do
  #echo "IMAGE " $image
  label_file=${image/jpg/txt}
  #echo "LABEL FILE NAME " $label_file
  if [ -f $label_file ]; then
    while read -r label;
    do
      echo $image $label >> $2
    done < $label_file
  #else
    #echo "ARCHIVO " $label_file " no existe"
  fi
done < $1
