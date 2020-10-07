terraform {
  required_version = "~> 0.13"
}

provider "aws" {
  region  = var.region
  alias   = "main"
  version = "~> 3.0"
}

provider "aws" {
  region  = "us-east-1"
  alias   = "acm"
  version = "~> 3.0"
}