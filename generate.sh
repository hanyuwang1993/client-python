#!/usr/bin/env bash

set -euo pipefail

wget https://raw.githubusercontent.com/grafeas/grafeas/master/proto/v1beta1/swagger/grafeas.swagger.json -O grafeas.swagger.json
wget https://raw.githubusercontent.com/grafeas/grafeas/master/proto/v1beta1/swagger/project.swagger.json -O projects.swagger.json

# wget https://repo1.maven.org/maven2/io/swagger/swagger-codegen-cli/2.4.18/swagger-codegen-cli-2.4.18.jar -O swagger-codegen-cli.jar
java -jar ./swagger-codegen-cli.jar generate -i ./grafeas.swagger.json -l python -o ./ -c ./config.py.json
java -jar ./swagger-codegen-cli.jar generate -i ./grafeas.projects.swagger.json -l python -o ./ -c ./config.py.json
