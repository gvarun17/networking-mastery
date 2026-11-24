#!/usr/bin/env bash
# Create a self-signed certificate for lab.local and bundle it for HAProxy.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p certs
openssl req -x509 -newkey rsa:2048 -nodes -days 30 \
  -subj "/CN=lab.local" -addext "subjectAltName=DNS:lab.local,DNS:localhost" \
  -keyout certs/lab.key -out certs/lab.crt
cat certs/lab.crt certs/lab.key > certs/lab.pem
echo "wrote certs/lab.pem"
