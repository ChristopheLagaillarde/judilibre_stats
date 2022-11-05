#!/bin/bash

# This is a script get 1000 decisions from the cours of cassation

source key_id.sh

declare -i i
echo '[' >> judilibre.json

for i in {0..99}
do
	curl -s -H "accept: application/json" -H "KeyId: ${key_id}" -X GET "https://sandbox-api.piste.gouv.fr/cassation/judilibre/v1.0/export?batch_size=100&batch=${i}" >> judilibre.json

	if [ "$i" != 99 ]
	then
	  echo ', ' >> judilibre.json
  fi
done

echo ']' >> judilibre.json

