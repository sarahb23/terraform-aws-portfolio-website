# Personal Portfolio website on AWS S3 with CloudFront and custom domain

### Prerequisites
- An AWS account
- A domain registered with Route53
- Terraform 0.13 installed locally or a Terraform cloud account if you want to use the [GitHub actions workflow](.github/workflows/terraform.yml)

### Use this as a Terraform module
- Fork this repository
- Remove the `backend` block from [`main.tf`](main.tf)
- Declare the module
  ```terraform
     module "website" {
         source = "https://github.com/<YOUR_GH_USERNAME>/terraform-aws-portfolio-website"
         region = "us-east-1"
         my_url = "example.com" # This is the domain name registered with Route53
         env    = "dev" # either prod or dev
     }
  ```
### Use this with GitHub Actions and Terraform Cloud
- Fork this repository
- Follow [this guide](https://learn.hashicorp.com/tutorials/terraform/github-actions?in=terraform/automation)
- When following the guide, create TWO workspaces with the same prefix with suffixes of `prod` and `dev` (i.e. `portfolio-dev` and `portfolio-prod`)
- Edit the `backend` block in [`main.tf`](main.tf)
  ```terraform
    terraform {
      required_version = "~> 0.13"
    
      backend "remote" {
        organization = "REPLACE ME"
    
        workspaces {
          prefix = "REPLACE ME"
        }
      }
    }
  ```
- The `dev` workspace is used as a placeholder for pull request validation but can also be used to deploy using the Terraform CLI
- Once a pull request to `main` is completed and merged, Terraform will deploy to the `prod` workspace

### Resources created
- Two S3 buckets
  - Website content hosting
  - CloudFront logging
- Website content uploaded via the `aws cli`
- ACM certificate with DNS validation through Route53
- A CloudFront distribution with a custom domain and ACM certificate for HTTPS

### Customizing the website
- Site configuration data is located in [`src/js/siteData.js`](src/js/siteData,js')
- Replace values in `resumeData` with your relevant information
- Editing `siteConfig`:
    ```javascript
    let siteConfig = {
      "analyticsId": null,
      "title": "Your Name",
      "resumeFileName": null
    };
    ```
    - If you would like to include a PDF resume, upload it to [`src/docs/`](src/docs/) and change the value of `resumeFileName` from `null` to your file name.
    - If you would like to use Google Analytics, replace the value of `analyticsID` with your GA Tag ID.
- If using the GitHub actions to deploy via Terraform Cloud make sure to run this command locally to include images and files that do not go into source:
  ```bash
  aws s3 sync src/ s3://<WEBSITE_BUCKET_NAME>/src/ --exclude '*.git*' --exclude '*README*'
  ```
- You can also completely remove the code from `src/` and replace it with your own!
    