reply=$(~/Desktop/alerter -reply -title 'Open Ref?' -closeLabel 'Open'  -message '' -actions Other -timeout 3 )
echo $reply;
e=0
case $reply in
    "open ref"|"Open ref") open ~/Desktop/Ref;;
    "pinterest"|"Pinterest")  open -a "Google Chrome" https://www.pinterest.com/elendventure/;;
    "Open") open ~/Desktop/Ref;;
    "Other") reply=$(~/Desktop/alerter -reply -title 'What would you like me to do?' -message '' ); e=1 ;; 
    "@CLOSED") ;;
    "@TIMEOUT") ;;
    
    "@CONTENTCLICKED") ;;
    *) $(~/Desktop/alerter -title 'Sorry'  -message "Can't understand");;
esac
echo "2: $reply";
if [ $e -eq 1 ];then
    first=`echo $reply | awk '{print $1}'`
    second=`echo $reply | awk '{print $2}'`
    if [ $first = "open" -o $first = "Open" ]; then 
        open ~/Desktop/$second;
        echo $second;

    fi
fi

if [ $reply == "pinterest" -o $reply == "Pinterest" ];then
    open -a "Google Chrome" https://www.pinterest.com/elendventure/painting/;
fi


#
#reply=$(~/Desktop/alerter -reply -title 'Open Ref?'  -message '~/Desktop/Ref ')
#echo $reply; 
#case $reply in
#    "@CONTENTCLICKED") `open ~/Desktop/Ref`;;
#    "@ACTIONCLICKED") echo "You clicked the alert default action button" ;;
#   *);;
#esac