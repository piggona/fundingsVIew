docker run --rm -it --name=logstash \
--mount type=bind,source=/home/haohao/Documents/fundingsView/1/,target=/nsf/ --privileged=true \
-v /home/haohao/Documents/elk/node1/logstash/pipeline:/usr/share/logstash/pipeline/ \
-v /home/haohao/Documents/elk/node1/logstash/logstash.yml:/usr/share/logstash/config/logstash.yml \
--net es_vanlink \
docker.elastic.co/logstash/logstash:7.5.0 \
> logstash.log
