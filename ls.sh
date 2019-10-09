#!/bin/bash
if [ -f /tmp/NULL ]
  then rm /tmp/NULL
fi
logstash -f logstash.conf
