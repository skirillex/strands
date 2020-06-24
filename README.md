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

## Project Directory Explained:
| Directory | Description |
| --------- | ----------- |
| .circleci  | Main component of this project. where the CircleCI config file lives |
| Daedric    | Sample decentralized app that is deployed on the blockchain. A price oracle for ICON blockchain | 
| ansible    | Ansible playbooks for configuring EC2 instances and deploying DApp |
| api_tests  | Api tests for EC2 instances |
| docker    | The Daedric price oracle DApp but dockerized |
| integration_tests    | Integration tests for Ec2 isntances |
| strands_app_tester   | GUI frontend to visually show something was deployed on an EC2 instance |
| terraform    | Terraform IaC files |


## Motivation

According to the [state of DevOps 2019 report](https://services.google.com/fh/files/misc/state-of-devops-2019.pdf):
organizations that practice CI/CD produce higher quality software more quickly.

Unfortunately, certain industries, such as the Blockchain industry, are devoid of open-source CI/CD tools. 
This project aims to address that issue by providing a reference implementation for the deployment of Decentralized Applications


## Project Architecture

<img src="https://raw.githubusercontent.com/skirillex/strands/master/strands_app_tester/Strands_Architecturev5.png" width="100%">


This tool works in Three phases of automated testing:

#### Phase 1:
* Kicked off when Developer pushes code to github
* CircleCi is triggered and creates a docker image of the source code
* Then unit tests are run on the application
* If those tests pass then terraform provisions necessary infrastructure and EC2 instances

#### Phase 2:
* CircleCI runs integration tests on the infrastructure
* It checks if the EC2 instances are provisioned and online
* If those tests pass Ansible configures the EC2 instances and deploys the application
* Then another round of integration tsts run on the application

#### Phase 3:
* Ansible deploys the decentralized appliccation on the ICON blockchain
* API Tests then run on the EC2 instaces as well as the blockchain
* once that is complete, performance tests are run

If any tests fail and the deployment pipeline is brokem, the entire team is notified of failure and the commit is rolled back

## Engineering Challenges
An engineering challenge I ran into is that the CI Pipeline would store Terraform state files in a docker container.

The issue with this that the state files are necessary to modify or destroy the infrastructure. Therefore, as the container is destroyed so is the terraform state file.
This causes headaches when coupled with CI/CD and also prevents collaboration with members of the team.

The solution to this was configuring terraform to not use local storage and instead use a remote state with an S3 bucket.

## Development

This reference architecture relies on the following dependencies:

* Terraform >= 0.12
* Ansible
* iconservice and T-Bears (for deployment of ICON blockchain applications)

The key part of this reference architecture is to use the Config files from CircleCI and Terraform and alter them as necessary. While also following the pattern of tests necessary. 

| Step | Directions |
| ---- | ---------- |
| 1    | Configure files, and ensure CircleCI is loaded with your AWS credentials |
| 2    | in the CircleCI GUI point CircleCI to your respository | 
| 3    | Ensure the patterns of this reference architecture is followed with relevant and robust tests |
| 4    | once configured, push code to the repository CircleCi is listening on |
