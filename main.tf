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
}

provider "aws" {
  region  = "us-east-1"
  alias   = "acm"
}