provider "aws" {
  alias       = "eu-central-1"
  region      = "eu-central-1"
  access_key  = var.aws_access_key
  secret_key  = var.aws_secret_key
}

provider "aws" {
  alias       = "us-west-1"
  region      = "us-west-1"
  access_key  = var.aws_access_key
  secret_key  = var.aws_secret_key
}