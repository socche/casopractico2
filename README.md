# Caso Práctico 2 – Automatización de Despliegues en Entornos Cloud

Este proyecto consiste en la creación y configuración automática de una infraestructura en Azure utilizando Terraform y Ansible. Se despliegan dos aplicaciones diferentes: una sobre una máquina virtual con Podman y otra en un clúster AKS con almacenamiento persistente.

## Estructura del proyecto
```
├── terraform
│   ├── main.tf
│   ├── acr.tf
│   ├── vm.tf
│   ├── aks.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── terraform.tfvars (ignorado)
│
└── ansible
    ├── playbook.yml
    ├── hosts
    ├── group_vars/
    │   └── secrets.yml (ignorado)
    ├── roles/
        ├── acr
        ├── vm
        └── aks

```
## Archivos de ejemplo para configuración

Este repositorio incluye archivos `.save` con las variables necesarias para ejecutar Terraform y Ansible, pero **sin valores sensibles**. Puedes usarlos como plantilla para crear los reales.

### Terraform

- `terraform.tfvars.save` → Plantilla vacía:
```hcl
subscription_id = ""
tenant_id       = ""
client_id       = ""
client_secret   = ""
```

### Ansible

- `group_vars/secrets.yml.save` → Variables sensibles:
```yaml
acr_username: "acrjcollado"
acr_password: ""
acr_login_server: acrjcollado.azurecr.io

kubeconfig_path: "{{ lookup('env', 'HOME') }}/.kube/config"

postgres_db: ""
postgres_user: ""
postgres_password: ""
postgres_host: ""

db_name: encuesta
db_user: encuesta_user
db_password: ""
```

> Asegúrate de **copiar estos archivos** (sin la extensión `.save`) y rellenarlos correctamente antes de ejecutar los despliegues.

## Tecnologías utilizadas

- Azure
- Terraform
- Ansible
- Kubernetes (AKS)
- Podman
- Apache (web estática)
- Flask + PostgreSQL (app de encuestas)

## Pasos para ejecutar

### 1. Crear la infraestructura con Terraform

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

Al finalizar, exporta los valores necesarios con:

```bash
terraform output -raw clave_vm > ../ansible/clave_vm.pem
```

### 2. Ejecutar Ansible para configurar y desplegar

```bash
cd ../ansible
ansible-playbook -i hosts playbook.yml --ask-vault-pass
```

## Aplicaciones desplegadas

- **VM con Podman:** Servidor Apache.
- **AKS con persistencia:** App Flask con encuesta y base de datos PostgreSQL.