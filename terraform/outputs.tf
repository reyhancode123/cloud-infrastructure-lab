output "docker_network_name" {
  description = "Name of the Docker network created by Terraform"
  value       = docker_network.terraform_network.name
}

output "docker_network_id" {
  description = "ID of the Docker network created by Terraform"
  value       = docker_network.terraform_network.id
}

output "docker_network_driver" {
  description = "Driver used by the Docker network"
  value       = docker_network.terraform_network.driver
}

output "container_name" {
  description = "Name of the Alpine container"
  value       = docker_container.alpine_lab.name
}

output "container_id" {
  description = "ID of the Alpine container"
  value       = docker_container.alpine_lab.id
}

output "container_ip_address" {
  description = "IP address assigned to the Alpine container"
  value       = docker_container.alpine_lab.network_data[0].ip_address
}

output "container_memory_limit_mb" {
  description = "Container memory limit in MB"
  value       = docker_container.alpine_lab.memory
}

output "container_memory_swap_limit_mb" {
  description = "Total container memory and swap limit in MB"
  value       = docker_container.alpine_lab.memory_swap
}
