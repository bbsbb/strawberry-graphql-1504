#!/usr/bin/env bash

curl 'http://localhost:8000/graphql' -H 'Content-Type: application/json' -H 'Accept: application/json' --data-binary '{"query":"query{\n  bug{\n    b\n    aRef {\n      a\n      b\n    }\n  }\n}","variables":{}}' --compressed
