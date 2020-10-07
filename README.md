# Personal Portfolio website on AWS S3 with CloudFront and custom domain

### Prerequisites
- An AWS account
- A domain registered with Route53
- Terraform 0.13

### Use this as a Terraform module
  ```terraform
     module "website" {
         source = "https://github.com/zach-23/terraform-aws-portfolio-website
         region = "us-west-2"
         my_url = "example.com" # This is the domain name registered with Route53
     }
  ```

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
    