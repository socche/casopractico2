resource "azurerm_kubernetes_cluster" "aks" {
  name                = "aks-casopractico2"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  dns_prefix          = "aks-casopractico2"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_B2s"

    # Red
    vnet_subnet_id = azurerm_subnet.main.id
  }

  identity {
    type = "SystemAssigned"
  }

  network_profile {
    network_plugin = "azure"
    dns_service_ip = "10.0.2.10"
    service_cidr   = "10.0.2.0/24"
   }

  tags = {
    environment = "casopractico2"
  }
}

resource "azurerm_role_assignment" "aks_acr_pull" {
  scope                = azurerm_container_registry.acr.id
  role_definition_name = "AcrPull"
  principal_id         = azurerm_kubernetes_cluster.aks.kubelet_identity[0].object_id
}
