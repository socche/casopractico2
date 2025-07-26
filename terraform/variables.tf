variable "resource_group_name" {
  description = "Nombre del resource group para el caso práctico 2"
  type        = string
  default     = "rg-casopractico2"
}

variable "location" {
  description = "Región de Azure donde desplegar los recursos"
  type        = string
  default     = "westeurope"
}

variable "subscription_id" {
  description = "ID de la suscripción de Azure"
  type        = string
}

variable "acr_name" {
  description = "Nombre único del Azure Container Registry (ACR)"
  type        = string
  default     = "acrjcollado"
}