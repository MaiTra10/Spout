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
# Lambda Role
resource "aws_iam_role" "lambda" {
  
  name = "iam-for-lambda-htc2023"
  assume_role_policy = jsonencode({

    "Version": "2012-10-17",
    "Statement": [
      {
        "Action": "sts:AssumeRole",
        "Effect": "Allow",
        "Sid": "",
        "Principal": {
          "Service": "lambda.amazonaws.com"
        }
      }
    ]
  })
}
# Lambda Policy to allow use of DynamoDB
resource "aws_iam_policy" "lambda-policy-htc2023" {
  
  name = "lambda_policies_htc2023"
  policy = jsonencode({

    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Effect" : "Allow",
        "Action" : ["dynamodb:*"],
        "Resource" : "${aws_dynamodb_table.htc2023.arn}"
      },
    ]

  })
}
# Lambda Policy Attachment
resource "aws_iam_role_policy_attachment" "attach" {
  
  role = aws_iam_role.lambda.name
  policy_arn = aws_iam_policy.lambda-policy-htc2023.arn

}
# Zip start
data "archive_file" "start" {

  type = "zip"
  source_file = "../../start/main.py"
  output_path = "start-artifact.zip"

}
# Lambda htc2023-start
resource "aws_lambda_function" "htc2023-start" {
  
  role = aws_iam_role.lambda.arn
  function_name = "htc2023-start"
  handler = "main.lambda_start"
  timeout = 20
  filename = "start-artifact.zip"
  source_code_hash = data.archive_file.start.output_base64sha256
  runtime = "python3.9"

}
# Creates a lambda function URL for htc2023-start
resource "aws_lambda_function_url" "htc2023-start-url" {
  
  function_name = aws_lambda_function.htc2023-start.function_name
  authorization_type = "NONE"

  cors {
    
    allow_credentials = true
    allow_origins = ["*"]
    allow_methods = ["POST"]
    allow_headers = ["*"]
    expose_headers = ["keep-alive", "date"]

  }
}
# Outputs the URLs for the lambda functions for convenience
output "lambda-start-url" {
  value = aws_lambda_function_url.htc2023-start-url.function_url
}