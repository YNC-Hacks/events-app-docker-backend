FROM postgres 
ENV POSTGRES_PASSWORD postgres 
ENV POSTGRES_DB ynchacks
COPY init.sql /docker-entrypoint-initdb.d/
COPY relations.sql /docker-entrypoint-relations-init.d/
COPY populate.sql /docker-entrypoint-populate-init.d/

