#!/bin/bash
set -e
CIRCLECI_CACHE_DIR="/usr/local/bin"
TERRAFORM_VERSION="0.12.26"
TERRAFORM_URL="https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip"


if [ ! -f "${CIRCLECI_CACHE_DIR}/terraform" ] || [[ ! "$(terraform version)" =~ "Terraform v${PACKER_VERSION}" ]]; then
    wget -O /tmp/terraform.zip "${TERRAFORM_URL}"
    unzip -oud "${CIRCLECI_CACHE_DIR}" /tmp/terraform.zip
fi

terraform version
