

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
