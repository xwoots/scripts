ip_list=("x" "y" "z")

for i in "${ip_list[@]}"
do
    grep "$i" firewall_logs.log
    echo "$i"
done
