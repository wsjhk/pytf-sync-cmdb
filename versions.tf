terraform {
  required_version = "1.1.7"
  required_providers {
    alicloud = {
      source = "aliyun/alicloud"
      version = "1.165.0"
    }
//    aws = {
//      source  = "hashicorp/aws"
//      version = "4.13.0"
//      configuration_aliases = [ aws.src, aws.dst ]
//    }
  }
}