time=$(date +%H)
if [ $time -lt 12 ]; then
    message="Good Morning"
elif [ $time -lt 18 ]; then
    message="Good afternoon user"
else
    message="Good evening user"
fi
echo "$message"