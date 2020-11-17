#!/bin/bash

. ./getdata.sh

cd ../Docker

echo "INSERT INTO \`cpu_usage\` (\`usage\`) VALUES (`cpu_usage`);" | docker-compose exec -T db mysql -uroot -proot newdatabase
echo "INSERT INTO \`disk_usage\` (\`usage\`,\`free\`) VALUES (`mem_usage`,`mem_free`);" | docker-compose exec -T db mysql -uroot -proot newdatabase
echo "INSERT INTO \`mem_usage\` (\`usage\`,\`free\`) VALUES (`disk_usage`,`disk_free`);" | docker-compose exec -T db mysql -uroot -proot newdatabase
