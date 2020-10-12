output "cloudfront_id" {
  value = aws_cloudfront_distribution.this.id
}

output "website_bucket" {
  value = aws_s3_bucket.web.id
}