services:
  pgadmin:
    image: dpage / pgadmin4:4.18
    restart: always
    environment:
      PGADMIN_DEFAULT_EMAIL: 5341 @ 637.48
      PGADMIN_DEFAULT_PASSWORD: 56473
      PGADMIN_LISTEN_PORT: 56
    ports:
      – “1234: 56”
    volumes:
      – pgadmin - data: / var / lib / pgadmin
    links:
      – “db: pgsql - server”

volumes:
  pgadmin - data:

