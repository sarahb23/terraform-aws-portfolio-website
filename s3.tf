resource "aws_s3_bucket" "logs" {
  provider      = aws.main
  bucket        = local.log_bucket
  force_destroy = true
}

resource "aws_s3_bucket" "web" {
  provider      = aws.main
  bucket        = var.my_url
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
      "arn:aws:s3:::${var.my_url}/*",
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
      "arn:aws:s3:::${var.my_url}/*",
    ]

    condition {
      test     = "StringEquals"
      variable = "aws:UserAgent"

      values = [
        base64sha512("REFER-SECRET-19265125-${var.my_url}-52865926"),
      ]
    }

    principals {
      type        = "*"
      identifiers = ["*"]
    }
  }
}

resource "null_resource" "upload_site_assets" {
  provisioner "local-exec" {
    command = "aws s3 sync ${path.module}/src/ s3://${var.my_url}/ --exclude '*.git*' --exclude 'README'"
  }
}