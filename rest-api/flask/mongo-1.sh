docker run -it --rm dev-mongo \
    mongo -u admin \
          -p admin@123 \
          --authenticationDatabase admin \
          some-db

