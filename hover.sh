#!/usr/bin/sh

host=www.citforum.ru
ports_list=(21 80 443)
verbosity=silent
#verbosity=verbose
for port in "${ports_list[@]}"
do
  ./tcp-check.py $host $port $verbosity
  if [ $? -eq 0 ]
  then
    echo --- Connected to ${host}:${port} succesfully ---
  else
    echo --- Unable to connect to ${host}:${port}  ---
  fi
done
