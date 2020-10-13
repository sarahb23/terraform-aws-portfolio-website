locals {
  log_bucket = var.env != "prod" ? "logs.${var.env}.${var.my_url}" : "logs.${var.my_url}"
  web_bucket = var.env != "prod" ? "${var.env}.${var.my_url}" : var.my_url
}

resource "aws_s3_bucket" "logs" {
  provider      = aws.main
  bucket        = local.log_bucket
  force_destroy = true
}

resource "aws_s3_bucket" "web" {
  provider      = aws.main
  bucket        = local.web_bucket
  acl           = "private"
  policy        = data.aws_iam_policy_document.bucket_policy.json
  force_destroy = true

  website {
    index_document = "index.html"
  }
}

data "aws_iam_policy_document" "bucket_policy" {
  provider = aws.main

  statement {
    sid = "AllowedIPReadAccess"

    actions = [
      "s3:GetObject",
    ]

    resources = [
      "arn:aws:s3:::${local.web_bucket}/*",
    ]

    condition {
      test     = "IpAddress"
      variable = "aws:SourceIp"

      values = ["0.0.0.0/0"]
    }

    principals {
      type        = "*"
      identifiers = ["*"]
    }
  }

  statement {
    sid = "AllowCFOriginAccess"

    actions = [
      "s3:GetObject",
    ]

    resources = [
      "arn:aws:s3:::${local.web_bucket}/*",
    ]

    condition {
      test     = "StringEquals"
      variable = "aws:UserAgent"

      values = [
        base64sha512("REFER-SECRET-19265125-${local.web_bucket}-52865926"),
      ]
    }

    principals {
      type        = "*"
      identifiers = ["*"]
    }
  }
}

resource "null_resource" "placeholder" {

}