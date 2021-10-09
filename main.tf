terraform {

  backend "remote" {
    organization = "sarah-23"

    workspaces {
      prefix = "portfolio-"
    }
  }
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