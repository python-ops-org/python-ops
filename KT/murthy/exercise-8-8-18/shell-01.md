

```

read -p "Enter username: " username
read -p "Enter password: " password
useradd -m -s /bin/bash -p $(openssl passwd -1 $password) $username
if [ $? -eq 0 ]; then
usermod -a -G sudo $username
mkdir /home/$username/mydir
chown -R $username:$username /home/$username/mydir
usermod -d /home/$username/mydir $username
echo "$username ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
echo "User $username created successfully!"
echo "User $username added to sudo group!"
else
echo "Error while creating user!"
fi

```

```

#!/bin/bash
while true
do
cpu=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" |
awk '{print 100 - $1"%"}')
mem=$(free -m | awk 'NR==2{printf "%.2f%%", $3*100/$2 }')
echo "$(date) CPU Usage: $cpu, Memory Usage: $mem"
sleep 10
done

```


```

#!/bin/bash
read -p "Enter the filename containing URLs: " url_file
while read -r url; do
filename=$(basename "$url")
curl -o "$filename" "$url"
echo "Completed Download $filename"
done < "$url_file"
echo
"--------------------------------------------------------------------------
------------------"
echo "All files downloaded successfully!"


```


```

#!/bin/bash
read -p "Enter network interface to monitor traffic (ex. eth0): " net
while true
do
rx=$(ifconfig $net | grep "RX packets" | awk '{print $3 $6 $7}')
tx=$(ifconfig $net | grep "TX packets" | awk '{print $3 $6 $7}')
echo "$(date) RX: $rx, TX: $tx"
sleep

```

```
#!/bin/bash
read -p "Enter filename to write alert: " file
touch $file
read -p "Enter disk space threshold: " threshold
df -H | grep -vE "^Filesystem|tmpfs|cdrom" | awk '{ print $5 " " $1 }' |
while read output;
do
usage=$(echo $output | awk '{ print $1}' | cut -d'%' -f1)
if [ $usage -ge $threshold ]; then
partition=$(echo $output | awk '{ print $2 }')
echo "Alert for \"$partition: Almost out of disk space $usage% as on
$(date) " >> $file
break
fi
done
cat $file

```

```

#!/bin/bash
mem=$(free -m | awk 'NR==2{printf "%.2f%%", $3*100/$2}')
echo "Current Memory Usage: $mem"

```
```
#!/bin/bash
disk=$(df -h | awk '$NF=="/"{printf "%s", $5}')
echo "Current Disk Usage: $disk"

```

```
#!/bin/bash
read -p "Enter memory usage threshold (in KB): " threshold
if [ "$(ps -eo pid,%mem | awk -v t=$threshold '$2 > t {print $1}' | wc -c)"
-gt 0 ]; then
for pid in $(ps -eo pid,%mem | awk -v t=$threshold '$2 > t {print $1}')
do

kill $pid
done
echo "All processes consuming more than $threshold KB memory killed."
else
echo "There are no process consuming more than $threshold KB memory."
fi

```

```

#!/bin/bash
read -p "Enter CPU usage threshold: " threshold
if [ "$(ps -eo pid,%cpu | awk -v t=$threshold '$2 > t {print $1}' | wc -c)"
-gt 0 ]; then
for pid in $(ps -eo pid,%cpu | awk -v t=$threshold '$2 > t {print $1}')
do
kill $pid
done
echo "All processes consuming more than $threshold% CPU killed."
else
echo "There are no process consuming more than $threshold% CPU."
fi

```


```

#!/bin/bash
read -p "Enter process name: " process
process_path=$(which $process)
while true
do
if pgrep $process > /dev/null
then
echo "The Process $process is running."
sleep 5
else
$process_path &
echo "The Process $process restarted."
continue
fi
done

```

```

#!/bin/bash
read -p "Enter process name: " process
pid=$(pgrep -f $process)
if [ -n "$pid" ]; then
kill $pid
sleep 5
if pgrep -f $process> /dev/null; then
echo "Process did not exit properly, force killing..."
kill -9 $pid
fi
fi
process_path=$(which $process)
$process_path & echo "Process restarted."

```

```

#!/bin/bash
read -p "Enter host address:" HOST
read -p "Enter port number:" PORT
nc -z -v -w5 "$HOST" "$PORT"
if [ $? -eq 0 ]; then
echo "----------------------------------------------"
echo "Port $PORT on $HOST is open"
echo "----------------------------------------------"
else
echo "----------------------------------------------"
echo "Port $PORT on $HOST is closed"
echo "----------------------------------------------"
fi

```
```
#!/bin/bash
read -p "Enter remote host IP address:" ip
ping -c 1 $ip
if [ $? -eq 0 ]
then
echo "-----------------------"
echo "Host is up!"
echo "-----------------------"
else
echo "-----------------------"
echo "Host is down!"
echo "-----------------------"
fi



```

```

#!/bin/bash
read -p "Enter the 1st file name: " file1
read -p "Enter the 2nd file name: " file2
if [ ! -f $file1 ] || [ ! -f $file2 ]
then
echo "Error! One of the files does not exists."
exit 1
fi
if cmp -s "$file1" "$file2"
then
echo "The Files $file1 and $file2 are identical."
else
echo "The Files $file1 and $file2 are different."
fi

```

```

#!/bin/bash
read -p "Enter filename: " filename
read -p "Enter a pattern to search for: " pattern
grep -w -n $pattern $filename
if [ $? -eq 1 ]; then
echo "Pattern did not match."
fi

```
```

Grade() {
score=$1
if (( $score >= 80 )); then
grade="A+"
elif (( $score >= 70 )); then
grade="A"
elif (( $score >= 60 )); then
grade="B"
elif (( $score >= 50 )); then
grade="C"
elif (( $score >= 40 )); then


grade="D"
else
grade="F"
fi
echo "The grade for mark $s is $grade"
}
read -p "Enter a score between 1-100:" s
Grade $s

```


```
#!/bin/bash
Area() {
width=$1
height=$2
area=$(($width * $height))
echo "Area of the rectangle is: $area"

}
read -p "Enter height and width of the ractangle:" h w
Area $h $w

```

```

#!/bin/bash
Prime () {
num=$1
if [ $num -lt 2 ]
then
echo "The number $num is Not Prime"
return
fi
for (( i=2; i<=$num/2; i++ ))
do
if [ $((num%i)) -eq 0 ]
then

echo "The number $num is Not Prime"
return
fi
done
echo "The number $num is Prime"
}
read -p "Enter a number: " num
Prime "$num"

```

```

#!/bin/bash
Palindrome () {
s=$1
if [ "$(echo $s | rev)" == "$str" ]
then
echo "The string is a Palindrome"
else
echo "The string is not a palindrome"
fi
}
read -p "Enter a string: " str
Palindrome "$str"

```

```

#!/bin/bash
arr=(24 27 84 11 99)
echo "Given array: ${arr[*]}"
s=100000
l=0
for num in "${arr[@]}"
do
if [ $num -lt $s ]
then
s=$num
fi
if [ $num -gt $l ]
then
l=$num
fi
done
echo "The smallest element: $s"
echo "The largest: $l"

```

```

arr=("mango" "grape" "apple" "cherry" "orange")
for item in "${arr[@]}"; do
echo $item
done

```

```

#!/bin/bash
read -p "Enter a number: " num
sum=0
for (( i=1; i<=$num; i++ ))
do
sum=$((sum + i))
done
echo "Sum of first $num numbers: $sum"

```

```


#!/bin/bash
read -p "Enter a number: " num

temp=1
for (( i=1; i<=$num; i++ ))
do
temp=$((temp*i))
done
echo "The factorial of $num is: $temp"

```

```

#!/bin/bash
for (( i=1; i<=10; i++ ))
do
if [ $((i%2)) == 0 ]
then
echo $i
fi
done

```

```
#!/bin/bash
n=5
until [ $n == 0 ]

do
echo $n
n=$((n-1))
done

```

```

#!/bin/bash
str="Linuxsimply"
str=$(echo "$str" | rev)
echo "The reversed string: $str"

```

```

#!/bin/bash
read -p "Enter a string: " str
echo "Converted String:" $str | tr '[:upper:]' '[:lower:]'

```




🚀 5 More DevOps Automation Scripts You Need! (Part 11) 🔥


5️⃣1️⃣ Check SSL Certificate Expiry for a Domain 🔒

Avoid downtime by monitoring SSL certificate expiration.


```

#!/bin/bash
DOMAIN="example.com"
echo | openssl s_client -servername $DOMAIN -connect $DOMAIN:443 2>/dev/null | openssl x509 -noout -enddate


```


5️⃣2️⃣ Identify Large Log Files Consuming Disk Space 💾

Find and manage oversized log files before they fill up your disk.


```

#!/bin/bash
echo "Finding log files larger than 500MB..."
find /var/log -type f -size +500M -exec ls -lh {} \;


```

5️⃣3️⃣ Restart Kubernetes Pods with High Memory Usage ☸️

Ensure stability by restarting pods that consume excessive memory.

```

#!/bin/bash
echo "Restarting pods with high memory usage..."
kubectl top pods --all-namespaces | awk '$3 > 500 {print $2}' | xargs kubectl delete pod

```


5️⃣4️⃣ Check Unused Security Groups in AWS ☁️

Identify security groups that are not attached to any instances.

```

aws ec2 describe-security-groups --query "SecurityGroups[*].GroupId" --output text | while read SG; do
 aws ec2 describe-instances --filters "Name=instance.group-id,Values=$SG" --query "Reservations[*].Instances[*].InstanceId" --output text | grep -q . || echo "Unused: $SG"
done

```

5️⃣5️⃣ Automate Daily Backup for a Directory 🔄

Keep your critical files safe by scheduling daily backups.


```
#!/bin/bash
SRC_DIR="/important/data"
BACKUP_DIR="/backup"
mkdir -p $BACKUP_DIR
tar -czf $BACKUP_DIR/backup_$(date +%F).tar.gz $SRC_DIR
```



