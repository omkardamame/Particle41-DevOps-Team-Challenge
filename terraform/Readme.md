# SimpleTimeService - Terraform ECS Deployment

This repository contains the Terraform code to create a **VPC**, **ECS Fargate** cluster, **Application Load Balancer (ALB)**, and deploy a Docker container (`omkardamame/simpletimeservice:latest`) in **AWS**. The container is deployed in **private subnets** within the VPC, with traffic routed through the **ALB** in the public subnets.

## 🛠️ Prerequisites

- **Terraform** installed
- **AWS IAM role** attached to your EC2 instance with sufficient permissions to manage AWS resources (e.g., EC2, VPC, ECS, ALB)
  
  If you're using an IAM role attached to the EC2 instance, make sure your EC2 instance has the following policies:
  - `AmazonEC2FullAccess`
  - `AmazonECS_FullAccess`
  - `AmazonVPCFullAccess`
  - `ElasticLoadBalancingFullAccess`

## 📦 How to Deploy

1. **Clone this repository**:

```bash
git clone https://github.com/omkardamame/Particle41-DevOps-Team-Challenge/terraform
cd omkardamame/Particle41-DevOps-Team-Challenge/terraform
```

2. **Initialize Terraform**:

    Initialize Terraform with the following command. This will install the necessary provider plugins.

```bash
terraform init
```

3. **Create a Plan**:

    Generate an execution plan, which shows what actions Terraform will take to create the infrastructure.

```bash
terraform plan
```

4. **Apply the Plan**:

    Apply the plan to create the infrastructure and deploy the Docker container.

```bash
terraform apply
```

    You'll be prompted to confirm the action. Type `yes` to proceed.

5. **Access the Service**:

    After the deployment is complete, Terraform will output the DNS name of the **Application Load Balancer (ALB)**. Use this DNS name to access the application.

```bash
output "alb_dns_name"
```

    Example URL: http://simple-alb-1626330895.ap-south-1.elb.amazonaws.com/

## 🧑‍💻 How to Authenticate to AWS

Since the project uses an **IAM role** attached to the EC2 instance, Terraform will automatically use the instance's IAM role for authentication, provided the IAM role has sufficient permissions as mentioned above. You don’t need to manually set AWS credentials on your local machine.

## 🧩 Terraform Modules Used

- **VPC Module**: For creating the VPC and subnets
    - Source: `terraform-aws-modules/vpc/aws`
- **ECS Fargate Module**: For creating ECS clusters and services

# 🧹 Clean-up

To delete all the resources created by Terraform, run:

```bash
terraform destroy
```

This will remove the VPC, ECS services, ALB, and all associated resources.

# 📜 License

This project is licensed under the [MIT License](https://github.com/omkardamame/Particle41-DevOps-Team-Challenge/blob/main/LICENSE).
