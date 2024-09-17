# AWS SAM Application - DynamoDB CRUD with Lambda and API Gateway

This project demonstrates a simple serverless application built using AWS Lambda, API Gateway, and DynamoDB. It enables basic CRUD operations (Create, Read, Update, Delete) on a DynamoDB table.

## Project Structure

- template.yaml: Defines the AWS infrastructure including Lambda functions, API Gateway, and DynamoDB table.
- app.py: Contains the Lambda function for handling CRUD operations on DynamoDB items.
- .aws-sam: This directory is generated after you build the project using SAM CLI.
- README.md: This document.

## Prerequisites

- AWS CLI installed and configured 
        Open your terminal:
        Follow this :
        $ aws configure
        AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
        AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
        Default region name [None]: us-west-2
        Default output format [None]: json

        Follow this for sso user:

        $ aws configure sso
        SSO session name (Recommended): my-sso
        SSO start URL [None]: https://my-sso-portal.awsapps.com/start
        SSO region [None]:us-east-1

        Attempting to automatically open the SSO authorization page in your default browser.

        There are 2 AWS accounts available to you.
        > DeveloperAccount, developer-account-admin@example.com (111122223333) 
          ProductionAccount, production-account-admin@example.com (444455556666)

        Using the account ID 111122223333

        There are 2 roles available to you.
        > ReadOnly
          FullAccess

        Using the role name "ReadOnly"

        CLI default client Region [None]: us-west-2
        CLI default output format [None]: json
        CLI profile name [123456789011_ReadOnly]: user1
- AWS SAM CLI installed ----> https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html
- Python 3.8 or newer
- boto3 installed

    DynamoDB Table
    The DynamoDB table is defined with a partition key empid. This table stores employee information including:
    empid: Employee ID
    department: Employee's department
    city: Employee's city
    Emp_Name: Employee's name
    Gender: Employee's gender
    
## Setup Instructions
Go to your terminal

git clone https://github.com/your-repo-url
cd your-repo-directory
sam build
sam deploy --guided



