```markdown
### 🧹 Destrucción de la infraestructura – `terraform destroy`

Una vez validados y aplicados correctamente los recursos iniciales (Resource Group y Azure Container Registry), se procedió a su eliminación para evitar consumo innecesario del crédito de estudiante de Azure.

#### 🔧 Comando ejecutado:
```bash
terraform destroy
```

#### 🛑 Confirmación manual:
```bash
Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  Only 'yes' will be accepted to confirm.

  Enter a value: yes
```

#### ✅ Resultado:
- Eliminado el **Resource Group** `rg-casopractico2`
- Eliminado automáticamente el **Azure Container Registry** `acrjavi2025`
- No quedan recursos residuales en la cuenta de Azure
- Confirmado por consola y verificado desde el portal Azure

#### 📤 Evidencia complementaria:
```bash
az group list --query "[?name=='rg-casopractico2']"
# Resultado: []
```

#### 🧠 Observación:
Terraform maneja la destrucción de todos los recursos dependientes al eliminar el grupo principal, por lo que no es necesario borrar los recursos individualmente.
```
