provider "aws" {
  region  = var.aws_region
  version = "~> 2.43.0"
}

// remote state in s3 bucket
// test
// add for ci deployment
// add
terraform {
  backend "s3" {
    bucket         = "terraform-bucket-remote-state-strands"
    key            = "global/s3/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-bucket-remote-state-strands-locks"
    encrypt        = true
  }
}




module "sandbox_vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "2.21.0"

  name = "${var.fellow_name}-test-server"

  cidr           = "10.0.0.0/28"
  azs            = ["${var.aws_region}a", "${var.aws_region}b", "${var.aws_region}c"]
  public_subnets = ["10.0.0.0/28"]

  enable_dns_support   = true
  enable_dns_hostnames = true

  enable_s3_endpoint = true

  tags = {
    Owner       = var.fellow_name
    Environment = "dev"
    Terraform   = "true"
  }
}

/* 
open to standard SSH port from local machine only.

For more details and options on the AWS sg module, visit:
https://registry.terraform.io/modules/terraform-aws-modules/security-group/aws/3.3.0

Check out all the available sub-modules at:
https://github.com/terraform-aws-modules/terraform-aws-security-group/tree/master/modules

 */
module "ssh_sg" {
  source  = "terraform-aws-modules/security-group/aws"
  version = "3.3.0"

  name        = "ssh_sg"
  description = "Security group for instances"
  vpc_id      = "${module.sandbox_vpc.vpc_id}"
  
/*
#Get external IP to restrict ingress access
data "http" "getexternalip" {
  url = "http://ipv4.icanhazip.com"
}
*/

// this allows SSH and port 80 for NGINX
  ingress_cidr_blocks      = ["10.0.0.0/28"]
  ingress_with_cidr_blocks = [
    {
      from_port   = 22
      to_port     = 22
      protocol    = "tcp"
      #cidr_blocks = ["${chomp(data.http.getexternalip.body)}/32"]
      cidr_blocks = "0.0.0.0/0"
    },
    {
      from_port = 80
      to_port = 80
      protocol = "tcp"
      cidr_blocks = "0.0.0.0/0"
    }
  ]
  
  egress_cidr_blocks      = ["10.0.0.0/28"]
  egress_with_cidr_blocks = [
    {
      from_port = 0
      to_port = 0
      protocol = "-1"
      cidr_blocks = "0.0.0.0/0"
    }
  ]
   tags = {
    Owner       = "${var.fellow_name}"
    Environment = "dev"
    Terraform   = "true"
  }
}


resource "aws_instance" "ec2_web_app_instance" {
  ami           = var.amis[var.aws_region]
  instance_type = "t2.medium"
  key_name      = var.keypair_name
  count         = 1

  vpc_security_group_ids      = [module.ssh_sg.this_security_group_id]
  subnet_id                   = module.sandbox_vpc.public_subnets[0]
  associate_public_ip_address = true

  root_block_device {
    volume_size = 100
    volume_type = "standard"
  }

  tags = {
    Name        = "${var.cluster_name}-master-${count.index}"
    Owner       = var.fellow_name
    Environment = "dev"
    Terraform   = "true"
    HadoopRole  = "master"
    SparkRole   = "master"
  }


}


# Configuration for an Elastic IP to add to nodes
resource "aws_eip" "elastic_ips_for_instances" {
  vpc = true
  instance = element(
    concat(
      aws_instance.ec2_web_app_instance.*.id,
    ),
    count.index,
  )
  count = length(aws_instance.ec2_web_app_instance)

    // these commands below create a host file for ansible
    provisioner "local-exec" {
      command = "echo [servers] >> ip_address"
    }
    provisioner "local-exec" {
    command = "echo server${count.index} ansible_host=${aws_eip.elastic_ips_for_instances[count.index].public_ip} >> ip_address"
  }
    provisioner "local-exec" {
    command = "echo [all:vars] >> ip_address"
  }
  provisioner "local-exec" {
    command = "echo ansible_python_interpreter=/usr/bin/python3 >> ip_address"
  }

}



