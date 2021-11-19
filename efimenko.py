docker pull dpage/pgadmin4

docker run —rm -p 81:80 \
--network ais2_default \
--name pgadmin4 \
-e "PGADMIN_DEFAULT_EMAIL=asd@asd.asd" \
-e "PGADMIN_DEFAULT_PASSWORD=123456" \
-d dpage/pgadmin4