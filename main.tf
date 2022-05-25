module "aws-datasource-module" {
  source    = "./module/aws-datasource-module"
  providers = {
    aws = aws.us-west-1
  }
}

module "aws-datasource-module1" {
  source    = "./module/aws-datasource-module"
  providers = {
    aws = aws.eu-central-1
  }
}

//module "aliyun-139" {
//  source = "./module/aliyun-1394827281333977-module"
//}
//
//module "aliyun-179" {
//  source = "./module/aliyun-1792071803654837-module"
//}
//
//module "aliyun-xmotors-ai" {
//  source = "./module/aliyun-xmotors-ai-module"
//}
