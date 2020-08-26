
k=`cat art.xml`
#echo $k

art=($(grep -oP '(?<sizeOnDisk>)[^<]+' "art.xml"))

for i in ${!art[$i]}"

do
	echo $i "${art[$i]}"

done	
