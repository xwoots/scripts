#/bin/bash

cat ip_list.txt | while read line 
do
   curl -G https://api.abuseipdb.com/api/v2/check --data-urlencode "ipAddress=$line" -d maxAgeInDays=90 -H "Key: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" -H "Accept: application/json" >> report.txt
   echo -e "\n" >> report.txt
done
