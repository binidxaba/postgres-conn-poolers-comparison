#! /bin/sh
#
# test.sh
# Copyright (C) 2023 binidxaba <binidxaba@noemail.com>
#
# Distributed under terms of the MIT license.
#

set -xe 

SERVER_IP=10.182.0.4
SERVER_PORT=6432
#SERVER_PORT=6543
#DURATION=60
DURATION=3600
POOLER=pgbouncer
RESULT_DIR=${HOME}/${POOLER}-`date "+%s"` 

OS_USER=binidxaba
PRIV_KEY=/home/binidxaba/.ssh/id_rsa

mkdir -p ${RESULT_DIR}
rm -rf ${RESULT_DIR}/*

for i in 10 25 50 75 100 250 500 750 1000 1250 1500 1750 2000 2250 2500;
do
  #-- For PgBouncer
  ssh -i ${PRIV_KEY} ${OS_USER}@${SERVER_IP} sudo truncate -s 0 /var/log/messages
  ssh -i ${PRIV_KEY} ${OS_USER}@${SERVER_IP} sudo truncate -s 0 /var/log/user.log
  ssh -i ${PRIV_KEY} ${OS_USER}@${SERVER_IP} sudo -u postgres truncate -s 0 /var/log/postgresql/pgbouncer.log
  ssh -i ${PRIV_KEY} ${OS_USER}@${SERVER_IP} sudo systemctl restart pgbouncer.service
  sleep 15

  echo "Running with clients=$i"

  f=${RESULT_DIR}/${POOLER}_${i}.out
  > ${f}

  #-- Connect/Disconnect
  #PGPASSWORD=hello123 pgbench  -c ${i} -j ${i} -T ${DURATION} -P 5 -C -S -h ${SERVER_IP} -p ${SERVER_PORT} -U postgres postgresdb  2>&1 | tee ${f}

  #-- Transaction mode (pgbouncer and pgcat)
  #PGPASSWORD=hello123 pgbench  -c ${i} -j ${i} -T ${DURATION} -P 5 -S -h ${SERVER_IP} -p ${SERVER_PORT} -U postgres postgresdb  2>&1 | tee ${f}
  PGPASSWORD=hello123 pgbench  -c ${i} -j 8 -l -T ${DURATION} -P 5 -S -h ${SERVER_IP} -p ${SERVER_PORT} -U postgres postgresdb  2>&1 | tee ${f}

  #-- Transaction mode (supavisor)
  #PGPASSWORD=hello123 pgbench  -c ${i} -j ${i} -T ${DURATION} -P 5 -S -h ${SERVER_IP} -p ${SERVER_PORT} -U postgres.dev_tenant postgres 2>&1 | tee ${f}
  #PGPASSWORD=hello123 pgbench  -c ${i} -j 8 -l -T ${DURATION} -P 5 -S -h ${SERVER_IP} -p ${SERVER_PORT} -U postgres.dev_tenant postgres 2>&1 | tee ${f}
done
