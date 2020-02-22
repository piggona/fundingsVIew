docker run --name kibana01 \
--net es_vanlink \
-v ${KIBANAVANLINK}/kibana.yml:/usr/share/kibana/config/kibana.yml --privileged=true \
-d \
docker.elastic.co/kibana/kibana:7.5.0