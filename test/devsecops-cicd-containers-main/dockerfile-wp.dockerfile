FROM ubuntu:latest
# APT Update/Upgrade, then install packages we need
RUN apt-get update \
    apt-get install -y curl \
    curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add - \
    apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main" \
    apt-get update \
    apt-get install -y terraform 

#ADD wp-config.php /var/www/html/wp-config.php

# Install WP-CLI

