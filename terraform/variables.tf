variable "network_name" {
  description = "Name of the Docker network managed by Terraform"
  type        = string
  default     = "terraform-lab-network"
}

variable "network_subnet" {
  description = "Subnet CIDR for the Terraform Docker network"
  type        = string
  default     = "172.20.0.0/16"
}
