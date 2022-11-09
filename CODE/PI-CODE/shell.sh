#bin/bash


str1="https://raw.githubusercontent.com/Phosvan/PAPI/main/CODE/PI-CODE/Controller.py"
str11="Controller.py"

str2="https://raw.githubusercontent.com/Phosvan/PAPI/main/CODE/PI-CODE/ControllerClass.py"
str22="ControllerClass.py"

str3="https://raw.githubusercontent.com/Phosvan/PAPI/main/CODE/PI-CODE/shell.sh"
str33="shell.sh"

str4="https://raw.githubusercontent.com/Phosvan/PAPI/main/CODE/PI-CODE/Controller*"


SERVICE="python3"



wget -q $str1
wget -q $str2
wget -q $str3

curl --silent $str1 | md5sum > "$str11.md5new"
curl --silent $str2 | md5sum > "$str22.md5new"
curl --silent $str3 | md5sum > "$str33.md5new"


#curl --silent https://raw.githubusercontent.com/Phosvan/PAPI/main/CODE/PI-CODE/Controller.py | md5sum > asdfasdf


md5sum $str11 >> "$str11.md5"
md5sum $str22 >> "$str22.md5"
md5sum $str33 >> "$str33.md5"

if ! cmp "$str11.md5" "$str11.md5new" > /dev/null; then
    printf "%s has changed from baseline!\n" "$str11"
    sudo rm -r Controller.py
    wget -q $str1
    sudo pkill -f $str11
    sudo python3 /home/pi/Documents/Controller.py
fi
printf "up to date "
rm "$str11.md5new"
rm "$str11.md5"

if ! cmp "$str22.md5" "$str22.md5new" > /dev/null; then
    printf "%s has changed from baseline!\n" "$str22"
    sudo rm -r ControllerClass.py
    wget -q $str2
fi
printf "up to date "
rm "$str22.md5new"
rm "$str22.md5"

if ! cmp "$str33.md5" "$str33.md5new" > /dev/null; then
    printf "%s has changed from baseline!\n" "$str33"
    sudo rm -r $str33
    wget -q $str3
    chmod +x $str33
fi
printf "up to date "
rm "$str33.md5new"
rm "$str33.md5"

if pgrep -x "$SERVICE" >/dev/null
then
    echo "$SERVICE is curretly running"
else
    echo "$SERVICE is not currently running, starting "

fi







