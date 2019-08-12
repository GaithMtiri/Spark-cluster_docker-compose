FROM spark-base:2.3.1


COPY . app

WORKDIR /app/spring-spark-word-count

RUN apk add maven --update-cache --repository http://dl-4.alpinelinux.org/alpine/edge/community/ --allow-untrusted \
	&& rm -rf /var/cache/apk/*

RUN mvn clean package

EXPOSE 3001

ENTRYPOINT ["java", "-jar", "target/spring-spark-word-count-0.0.1-SNAPSHOT.jar"]