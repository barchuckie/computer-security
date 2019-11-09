openssl genrsa -out privkeyA.pem
openssl req -new -key privkeyA.pem -out certA.csr
openssl genrsa -out privkeyB.pem