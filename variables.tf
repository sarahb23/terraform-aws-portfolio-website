variable region {
  type        = string
  description = "The AWS region for your deployment"
}

variable my_url {
  type        = string
  description = "The TLD of your Route53 Hosted Zone"
}

variable env {
  type        = string
  description = "Deployment environment"
  default     = ""
}