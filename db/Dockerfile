FROM alpine:3.9
RUN apk --update add bash postgresql-client && rm -rf /var/cache/apk/*
COPY ./versions /db-versions
COPY ./goto-version.sh /goto-version.sh
COPY ./all-versions.sh /all-versions.sh
COPY ./create-database.sh /create-database.sh
COPY ./bin/migrate /usr/local/bin/migrate
RUN chmod 755 /all-versions.sh && \
    chmod 755 /goto-version.sh && \
    chmod 755 /create-database.sh && \
    chmod +x /usr/local/bin/migrate
CMD /goto-version.sh
