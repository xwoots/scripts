import subprocess

outputfile = open("test-ips_result.txt", 'a')

with open("ips-list.txt") as file:
    for line in file:
        command = f'nc -zvw 2 {line.strip()}'
        if subprocess.call(command, shell=True) == 0:
            outputfile.write(line)
