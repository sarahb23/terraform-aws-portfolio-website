resource "aws_acm_certificate" "cert" {
  provider          = aws.acm
  domain_name       = var.my_url
  validation_method = "DNS"
}

resource "aws_route53_record" "cert_validation" {
  provider        = aws.acm
  allow_overwrite = true
  name            = tolist(aws_acm_certificate.cert.domain_validation_options)[0].resource_record_name
  type            = tolist(aws_acm_certificate.cert.domain_validation_options)[0].resource_record_type
  zone_id         = data.aws_route53_zone.this.id
  records         = [tolist(aws_acm_certificate.cert.domain_validation_options)[0].resource_record_value]
  ttl             = 60
}

resource "aws_acm_certificate_validation" "cert" {
  provider                = aws.acm
  certificate_arn         = aws_acm_certificate.cert.arn
  validation_record_fqdns = [aws_route53_record.cert_validation.fqdn]
}