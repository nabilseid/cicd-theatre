#!/bin/sh

# Decrypt the file
mkdir $HOME/secrets
# --batch to prevent interactive command
# --yes to assume "yes" for questions
gpg --quiet --batch --yes --decrypt --passphrase="$SECRET_PASS" \
--output $HOME/secrets/my_secret.txt ../secrets/my_secret.txt.gpg
