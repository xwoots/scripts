more ns.conf | grep -E "add (cs|lb) vserver" -i >> output.txt
cat output.txt | awk '{print $6 " " $7}' | grep -v "0.0.0.0" > vservers-ip.txt
