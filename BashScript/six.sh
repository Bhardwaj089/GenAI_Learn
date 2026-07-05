read x
if [ $x -gt 100 ]
then
echo failed
exit 1
else
echo Passed
exit 0
fi
