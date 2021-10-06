terraform {
  required_version = "~> 1.0.5"
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = ">= 3.60"
    }
  }
}

provider "aws" {
  region = "us-east-1"
  profile = "gophish"
}
