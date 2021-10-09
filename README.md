# Personal Portfolio website on AWS S3 with CloudFront and custom domain

### Prerequisites
- An AWS account
- A domain registered with Route53
- Terraform installed locally or a Terraform cloud account if you want to use the [GitHub actions workflow](.github/workflows/terraform.yml)

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
- This repo uses GitHub actions to copy files to S3 and rebuild the CloudFront cache. You can use this [gist](https://gist.github.com/sarahb23/484efc66ca121d8586f2f0916ca8c944) to create an IAM user and add the access keys to the repo as secrets.

### Resources created
- Two S3 buckets
  - Website content hosting
  - CloudFront logging
- Website content uploaded via the `aws cli`
- ACM certificate with DNS validation through Route53
- A CloudFront distribution with a custom domain and ACM certificate for HTTPS

### Customizing the website
- Site configuration data is located in [`web/public/siteData.json`](web/public/siteData.json)
- Replace values in `resumeData` with your relevant information
- Editing `siteConfig`:
    ```json
    "siteConfig": {
      "title": "Your Name",
      "embedResume": null
    }
    ```
    - If you would like to include a PDF resume, upload it to [`web/public/docs`](web/public/docs/) and change the value of `resumeFileName` from `null` to your file name.
    - If you would like to use Google Analytics, replace the value of `analyticsID` with your GA Tag ID.
- If using the GitHub actions to deploy via Terraform Cloud make sure to run this command locally to include images and files that do not go into source:
  ```bash
  # Build the static HTML via Python
  cd web/ && python3 build_site.py && cd ..

  # Copy static files to S3
  aws s3 sync src/ s3://<WEBSITE_BUCKET_NAME>/web/public --exclude '*.git*' --exclude '*README*'

  # OPTIONAL Invalidate CloudFront cache to reflect new changes
  aws cloudfront create-invalidation --distribution-id <CLOUDFRONT_ID> --paths "/"
  ```
- You can also completely remove the code from `web/public` and replace it with your own!
    