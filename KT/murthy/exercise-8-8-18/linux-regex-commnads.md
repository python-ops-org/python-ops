

```

vivek hostname=/etc/init.d/httpd start, /etc/init.d/httpd stop,/etc/init.d/httpd restart, /sbin/services httpd restart
webalizer ALL=NOPASSWD: /sbin/service httpd start, /sbin/service httpd stop, /sbin/service httpd restart

ls *csv | awk -F"." '{print"mv -v "$0" "$1".txt"}' | sh

ps aux  |  grep -i csp_build  |  awk '{print $2}'  |  xargs  kill -9
ps aux  |  grep -i supervisor  |  awk '{print $2}'  |  xargs  kill -9

awk -v term="$n1" -v ns="$n2" 'BEGIN {print "RAML="term; print "NKS="ns}' 
awk -v term="$n1" -v ns="$n2" 'BEGIN {print term"\n"ns}'
printf "$n1""\n""$n2"



grep -rl 'apples' /opt | xargs sed -i 's/apples/oranges/g'


cat art.xml | grep -i sizeOnDisk | awk  'NR==1 || NR==6' | sed 's/.............$//' | sed 's/^..................//'
cat art.xml | grep -i sizeOnDisk | sed -n '1p;7p' | sed 's/.............$//' | sed 's/^..................//'


for i in *.txt; do mv "$i" "unix$i"; done

top -b -n1 | sed -n '1,/^$/p'

find test9/* -type f -exec chmod 777 {} ";"

find test9/* -type d -exec chmod 777 {} ";"

sed -e '=' data | sed -n -e '{h;n;G;s/.\n//p;}'

cat test32 | sed 's/.$//g' | awk '{x+=1}{print$1" "$2x}'

ls biometric_photo_28520131604_09_02477_12.FMR | awk -F"_" '{for(x=1;x<=9;x++) {print"cp -rvf " $0" "$1"_"$2"_"$3"_0"x"_"$5"_"$6}}' | sh

!/bin/bash
Parent="/root/Script"
Ven="15 16 17 18"
Date=`date +'%d/%m/%y'`
printf "$Date \t"
for V in $Ven
do
List=`ls $Parent | awk -F"_" '$4 == "'$V'" {print}' | wc -l`
printf "$List \t"
done
printf "\n"

ls -ltr | grep "$Date" | awk '$1!~/^d/{print"cp -rvf '$Source'/"$9 " '$Dest'"}' | sed '1d' | sh
ls -ltr *csv | date --date=yesterday +'%b %d' | awk '$1!~/^d/{print"cp -rvf 
cat hips9 | awk '{print $0":385:root:redhat"}' > tg
for i in *.TD2; do echo mv $i ${i/_/}; done
for i in *.TD2; do mv $i /root/kx/${i/_/}; done
'{if (substr($0,length($0)) % 2 == 1) print "#"$0; else print $0 }' ip1 > ip2
echo "#10.137.2.19" | egrep -o "[0-9\.]+"
sed -i "s/#//g" file
echo "10.136.4.5 675 root redhat" | tr " " ":"
cat test | awk '{print $1": "$2":" $3": "$4}'
sed 's/$/:385:root:redhat/g' test
cat hips9 | awk '{print $0":385:root:redhat"}' > tg
ls -ltr | awk '$6 == "Aug" {print"cp -rvf "$9" /tmp/"}'
`find $SOURCE -type f -name \*.csv -mtime -1 | xargs -I {} cp -rvf {} $DEST`
sed -i '$ a\idcadm ALL=(ALL) NOPASSWD: ALL' /etc/sudoers
find / -name *201401* -type d -exec rm -rf {} \;
sed 's/under monitoring //g' file.txt
egrep -o "([\.0-9]{1,4})+" file.txt
/etc/init/docker.conf
DOCKER_OPTS='-H tcp://0.0.0.0:4243 -H unix:///var/run/docker.sock'
curl -X GET http://localhost:4243/images/json
python jenkins.py -i p3.yml
python ec2.py ec2.yml -s stop
python s3update.py  copy-6.yml
python s3update_working_new.py  -s  STANDARD_IA   -u  copy.yml 
ls *csv | awk -F"." '{print"mv -v "$0" "$1".txt"}' | sh
jq . test.log | egrep -i "eventti|eventsou|eventname|awsregi|creationdate" | tr -d '\n' | tr -s ' | uniq

ls | awk '{print"mv "$0" "$0}' | grep _04 | sed 's/_04/_40/2'

awk '{for (i=NF;i>0;i--) printf("%s ",$i)} {printf("%s","\n")}' $InFile

echo "00000006949873633_06.FMR" | rev

ls | head -n 1 | sed 's/_01/_05/g'

sed = sedr.txt | sed 'N;s/\n/\t/'

sed = emp.txt | sed 'N;s/\n/\. /' > emp1.txt

sed -n '$=' sedr.txt


sort -u kbc.txt -o tt.txt

for i in `cat list`; do cp "$i"  "$i".bak ; done

for counter in {1...5};do useradd user$counter;done

for user in `cat user.list`;do useradd $user;done

rsync -v -e ssh emp.txt  root@172.16.113.152:/opt

tac -s ' ' rev.txtsed '8,$ { $! s:</\?i>::g }'

dd if=/dev/zero of=/swap bs=1M count=1024
mkswap /swap

swapon /swap

date --date='2 days ago'

date --date='25 Dec' +%j

date '+%B %d'

date -s "2 OCT 2006 18:00:00"


date --set="2 OCT 2006 18:00:00"

date +%Y%m%d -s "20081128"


date +%T -s "10:13:13"

date +%T%p -s "6:10:30AM"

date +%T%p -s "12:10:30PM"


fuser -k 80/tcp


sed -e 's~,~~7' data7.txt 

sed '3 a\  u r my love' data7.txt

awk -v OFS='|' '{$1=$1};1' ts.txt

awk '{ print $1"|"$2"|"$3"|"$4"|"$5 }' ts.txt

cat biometric_photo_1105131308_05_508546_0001.FPP | cut -d "_" -f 4

for x in `cat gt.txt` do grep $x fg.txt >> asw.txt done


cp comp2.txt comp11.txt

for i in `cat comp1.txt` ;do grep -v $i comp11.txt > comp12.txt cp comp12.txt comp11.txt done

curl -IL "127.0.0.1:8080/jenkins
curl -IL "localhost:9090/DMaaP/dmaaprest/apiKeys"
count=0;while true;do;if [ $count -lt 10 ];then;let count++;status1=`curl -sI http://www.google.com|head -1`;
echo "loadtesting:$status1";else exit 0;fi;done
find test9/* -type f -exec chmod 777 {} ";"
find test9/* -type d -exec chmod 777 {} ";"
for i in *.TD2; do mv $i /root/kx/${i/_/}; done 
for i in `ls -1` ;do x=`echo $i |sed 's/_//1'` mv $i /<destination_path>/$x done 
 
echo "00202_19042013_99_16_508546.TD2" |awk -F'_' 'BEGIN{OFS="_";} {print $1$2,$3,$4,$5}' 
 
for i in *.TD2; do mv $i /root/kx/${i/_/}; done 
ls -ltr | awk '$6 == "Aug" {print"cp -rvf "$9" /tmp/"}'
cat test32 | sed 's/.$//g' | awk '{x+=1}{print$1" "$2x}' 
ls biometric_photo_28520131604_09_02477_12.FMR | awk -F"_" '{for(x=1;x<=9;x++) {print"cp -rvf " $0" "$1"_"$2"_"$3"_0"x"_"$5"_"$6}}' | sh 
cat td | egrep -o "[0-9\.]+" > td1 
cat fbtest.txt | awk '{print $1": "$2": "$3": "$4}' 
cat hips9 | awk '{print $0":385:root:redhat"}' > tg 
sed 's/$/:385:root:redhat/g' test 
'{if (substr($0,length($0)) % 2 == 1) print "#"$0; else print $0 }' ip1 > ip2 

echo RGB_DAILY_SNAPSHOT_20140926.txt | egrep -o "[[:digit:]]+"

echo "RGB_DAILY_SNAPSHOT_20140926.txt"|tr -d [A-Z][a-z][","] 

ps -ef | grep [t]ail | awk '{print $2}' | xargs -I {} kill {}

ls *csv | awk -F"." '{print"mv -v "$0" "$1".txt"}' | sh 
 
for file in (ls *.csv) ; do mv $file $(file%.csv).txt done 



10.135.2.16   www.abc.com www 
10.135.2.16   www.xyz.com www 
 
sed -e "\$a10.135.2.16 www.abc.com www \n10.135.2.16 www.xyz.com www" -i <filename>
sed -i "9i auth  sufficient    pam_unix.so likeauth nullok" /etc/pam.d/system-auth





vagrant scp ec2_lambda_less_v0.2.py centnode1:/tmp


chown -R nik:root /etc/pam.d/
chown -R nik:root /etc/sysconfig/selinux 
chown -R nik:root /etc/selinux/
chown -R nik:root /etc/modprobe.d/
chown -R nik:root /etc/fstab
chown -R nik:root /etc

ansible all -i inv.yml -m setup -a "filter=ansible_eth1_0"


kubectl get secrets -o jsonpath='{range .items[*]}{.metadata.name}{.metadata.creationTimestamp}}{end}' | tr "}" "\n" | sed 's/2022-.*/ 2022/g'

cat tx | tr '}' '\n'|sed -e 's/\([0-9][0-9][0-9][0-9]\)-[0-9][0-9]-[0-9][0-9].*$/ \1/'

cat tx | tr "}" "\n" | sed 's/2022-.*/ 2022/g'
kubectl get secrets -o jsonpath='{range .items[*]}{.metadata.name}{.metadata.creationTimestamp}}{end}' | tr "}" "\n" | awk -F'2022' '{print $1" 2022"}' | cut -d " " -f1

kubectl get secrets -o jsonpath='{range .items[*]}{.metadata.name}{.metadata.creationTimestamp}}{end}' | tr "}" "\n" | awk -F'2022' '{print $1" 2022"}' | cut -d " " -f1 | grep '^db-user-pass' | xargs -I {} kubectl delete secret {}


 echo "ram-rohit-21-07-22" |  cut -d "-" -f 1-2
 echo "ram-rohit-21-07-22" |  cut -d "-" -f1
 
 cat t3 |sed -e 's/^[0-9][0-9]* .*[ \t][0-9][ \t]*//' |
 
 cat t2 |sed -e 's/^[0-9][0-9]* .*[ \t][0-9][ \t]*//'
 
 while read -r x;do echo ${x} | sed -e 's/^[0-9].*KB\.[0-9]\{1,4\}.*[0-9]\.[0-9].[0-9].//';done < t2.dat
 
 sed -e 's/^[0-9].*KB\.[0-9]\{1,4\}[[:space:]][[:space:]][0-9]\.[0-9][[:space:]][0-9][[:space:]]//' t2.dat
 
s/^[0-9].*KB\.[0-9]\{1,4\}[[:space:]][[:space:]][0-9]\.[0-9][[:space:]][0-9][[:space:]]//
s/\(.*2019[[:space:]][0-9]\.[0-9]\.[0-9]\.[0-9][[:space:]][[:space:]][0-9]\)\(.*\)/\2/

pun in  a file and run  like :
sed -f script t2.dat

grep -irs --include="nginx.log" '^[2022-08-10.09.*STATUS=..'/var/log/nginx/* | egrep -o "STATUS=[0-9]{3}" | sort | uniq -c 


egrep -v "\-mta|100|\-mti|1\-pea|RUN|\-mbs|\-ttl|6000|\-twto|3000" test3

echo "release(_)2.5_OAT_GL"  | tr  -d '()' | sed 's/release_/release\//'

echo "release()2.5_OAT_GL" | sed  "s#()#/#"



Replace value after key with = by escape character
echo 'var=lemon'  | sed 's/var=.*/\k9=app/'

Without escape
sed -i 's/f1=.*/var=lemon/'

awk '{gsub("startup", "");print}' startup.json 

```
