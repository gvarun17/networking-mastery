variable "region" {
  description = "AWS Region for the lab."
  type        = string
  default     = "ap-south-1"
}

variable "owner" {
  description = "Tag value that identifies who owns the lab resources."
  type        = string
  default     = "varun"
}

variable "name" {
  description = "Name prefix for all resources."
  type        = string
  default     = "nm14"
}

variable "vpcs" {
  description = "VPCs to create. Keys are short names; values are non-overlapping CIDRs."
  type        = map(string)
  default = {
    shared = "10.99.0.0/16"
    app    = "10.1.0.0/16"
    data   = "10.2.0.0/16"
  }

  validation {
    condition     = alltrue([for c in values(var.vpcs) : can(cidrnetmask(c))])
    error_message = "Every VPC value must be a valid IPv4 CIDR."
  }
}

variable "az_count" {
  description = "Number of Availability Zones to use (2 is enough for the lab)."
  type        = number
  default     = 2
}

variable "instance_type" {
  description = "Instance type for the two test instances (Graviton keeps cost low)."
  type        = string
  default     = "t4g.nano"
}

variable "enable_flow_logs" {
  description = "Send VPC Flow Logs for the app VPC to CloudWatch Logs."
  type        = bool
  default     = true
}
