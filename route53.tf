data "aws_route53_zone" "this" {
  provider = aws.main
  name     = var.my_url
}

resource "aws_route53_record" "website" {
  provider = aws.main
  zone_id  = data.aws_route53_zone.this.id
  name     = var.my_url
  type     = "A"

  alias {
    name                   = aws_cloudfront_distribution.this.domain_name
    zone_id                = aws_cloudfront_distribution.this.hosted_zone_id
    evaluate_target_health = false
  }
}