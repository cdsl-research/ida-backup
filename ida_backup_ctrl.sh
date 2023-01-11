sleep 60
pid=`ps | grep vmkfstools | grep -v FSTo | grep -v vthr | cut -f 1 -d " "`
url="http://192.168.100.148:8000/"

while true;
do
    bool=`wget -q -O - $url`

    if [ $bool = "True" ]; then
        kill -18 $pid
    elif [ $bool = "False" ]; then
        kill -19 $pid
    fi

    sleep 1
done