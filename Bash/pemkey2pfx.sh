#!/bin/bash

read -p 'Input Certificate file : ' pem
read -p 'Input Key file : ' key
read -p 'Output PFX file : ' pfx

openssl pkcs12 -export -out $pfx -in $pem -inkey $key
