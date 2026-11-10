resource "docker_network" "terraform_network" {
  name   = var.network_name
  driver = "bridge"

  ipam_config {
    subnet      = var.network_subnet
    gateway     = "172.20.0.1"
    aux_address = {}
  }
}

resource "docker_image" "alpine" {
  name         = "alpine:3.22"
  keep_locally = true
}
resource "docker_container" "alpine_lab" {
  name  = "terraform-alpine-lab"
  image = docker_image.alpine.image_id

  command = [
    "sh",
    "-c",
    "while true; do sleep 3600; done"
  ]

  must_run    = true
  restart     = "unless-stopped"
  memory      = 64
  memory_swap = 128

  networks_advanced {
    name = docker_network.terraform_network.name
  }
}
