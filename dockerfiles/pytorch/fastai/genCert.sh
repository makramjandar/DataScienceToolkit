#!/bin/bash

openssl \
  req \
  -newkey rsa:2048 -nodes \
  -keyout pkey.pem \
  -x509 -days 36500 -out cert.pem \
  -subj "/C=FR/ST=PARIS/L=Earth/O=Jupyter/OU=IT/CN=www.makramjandar.com/emailAddress=makramjandar@gmail.com"  
