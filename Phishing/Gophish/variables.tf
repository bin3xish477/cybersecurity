variable "vpc_cidr" {
  description = "CIDR block for VPC"
  default = "10.10.0.0/16"
}

variable "public_subnet_cidr" {
  description = "CIDR block for public subnet"
  default = "10.10.0.0/16"
}

variable "az" {
  description = "Availability zone"
  default = "us-east-1a"
}

variable "ami" {
  description = "Amazon Linux 2 AMI"
  default = "ami-087c17d1fe0178315"
}

variable "instance_type" {
  description = "EC2 instance type"
  default = "t2.micro"
}
