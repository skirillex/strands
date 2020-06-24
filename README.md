# Strands

Strands is a reference implementation of a robust CI/CD pipeline which allows Decentralized Apps to be deployed on the ICON blockchain.

The sample application used for this implementation is the Icon Daedric Price Oracle while also supporting AWS infrastructure.


## Tech Stack
This implementation uses:

* CircleCI
* Terraform 
* Docker
* Ansible
* AWS


## Motivation

According to the [state of DevOps 2019 report](https://services.google.com/fh/files/misc/state-of-devops-2019.pdf):
organizations that practice CI/CD produce higher quality software more quickly.

unfortunately, certain industried, such as the Blockchain industry, are devoid of open-source CI/CD tools. 
This project aims to address that issue by providing a reference implementation for the deployment of Decentralized Applications


## Project Architecture

<img src="https://raw.githubusercontent.com/skirillex/strands/master/strands_app_tester/Strands_Architecturev5.png" width="100%">


This tool works in Three phases of automated testing:

Phase 1:
* Kicked off when Developer pushes code to github
* CircleCi is triggered and creates a docker image of the source code
* Then unit tests are run on the application
* If those tests pass then terraform provisions necessary infrastructure and EC2 instances

Phase 2:
* CircleCI runs integration tests on the infrastructure
* It checks if the EC2 instances are provisioned and online
* If those tests pass Ansible configures the EC2 instances and deploys the application
* Then another round of integration tsts run on the application

Phase 3:
* Ansible deploys the decentralized appliccation on the ICON blockchain
* API Tests then run on the EC2 instaces as well as the blockchain
* once that is complete, performance tests are run

If any tests fail and the deployment pipeline is brokem, the entire team is notified of failure and the commit is rolled back

