# Terraform
terraform {
  required_providers {
    aws = {
      version = ">= 4.0.0"
      source = "hashicorp/aws"
    }
  }
}
# Region
provider "aws" {
  region = "us-west-2"
}
# DynamoDB
resource "aws_dynamodb_table" "htc2023" {

  name = "htc2023-DB"
  billing_mode = "PROVISIONED"
  read_capacity = 1
  write_capacity = 1
  hash_key = "email"
  range_key = "ctx"

  attribute {
      name = "email"
      type = "S"
  }
  attribute {
      name = "ctx"
      type = "S"
  }
}