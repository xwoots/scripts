#!/bin/bash

read -p 'Input PFX file : ' pfx
read -p 'Output Certificate file : ' pem
read -p 'Output Key file : ' key

openssl pkcs12 -in $pfx -nocerts -out $key
openssl pkcs12 -in $pfx -clcerts -nokeys -out $pem
