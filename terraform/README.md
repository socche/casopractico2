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