variable "region" {
  description = "AWS Region."
  type        = string
  default     = "ap-south-1"
}

variable "az_count" {
  description = "AZs to use. 1 keeps cost low for learning; use 2 to test AZ symmetry and appliance mode."
  type        = number
  default     = 1

  validation {
    condition     = var.az_count >= 1 && var.az_count <= 3
    error_message = "az_count must be 1, 2 or 3."
  }
}

variable "spokes" {
  description = "Spoke VPC CIDRs. Keys must include \"a\" and \"b\" (used by firewall rules)."
  type        = map(string)
  default = {
    a = "10.11.0.0/16"
    b = "10.12.0.0/16"
  }
}

variable "inspection_cidr" {
  description = "CIDR of the inspection/egress VPC."
  type        = string
  default     = "10.100.0.0/16"
}
