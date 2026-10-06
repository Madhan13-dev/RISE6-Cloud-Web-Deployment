# RISE 6.0 – Industry-Oriented Cloud-Based Web Application Deployment and Scaling

## Selected project
**Project 1: Industry-Oriented Cloud-Based Web Application Deployment and Scaling**

The RISE 6.0 Cloud Computing PDF requires:
- Cloud virtual machine or managed service setup
- Web application deployment on cloud
- Load balancer configuration
- Auto-scaling configuration
- Secure access using security groups/firewall rules
- Basic monitoring and logging
- Version control integration
- Architecture and deployment documentation

This implementation uses **AWS + EC2 + Application Load Balancer + Auto Scaling + CloudWatch + GitHub + Terraform**.

## Architecture

Internet
  |
  v
Application Load Balancer
  |
  +---- EC2 instance 1
  |
  +---- EC2 instance 2
  |
  +---- EC2 instance 3/4 when scaling is required

CloudWatch collects metrics/logs.
Security groups allow HTTP to the ALB and application traffic only from the ALB.

## Prerequisites

Install:
- AWS CLI
- Terraform >= 1.6
- Git
- Python 3.12 (for local testing)

Configure AWS credentials with an IAM identity that is allowed to create the resources in this project.

## 1. Test locally

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
# source .venv/bin/activate

pip install -r requirements.txt
pytest -q
python app.py
```

Open `http://localhost:8080`.

## 2. Deploy to AWS

From the project root:

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

Type `yes` when Terraform asks for confirmation.

After deployment:

```bash
terraform output application_url
```

Open the returned URL in a browser.

## 3. Verify the requirements

### Web deployment
Open the `application_url` output.

### Load balancer
AWS Console -> EC2 -> Load Balancers.
Confirm the target group shows healthy instances.

### Auto scaling
AWS Console -> EC2 -> Auto Scaling Groups.
The project starts with 2 instances and can scale up to 4 based on average CPU.

### Security
- Internet HTTP access is allowed only to the ALB.
- EC2 port 8080 accepts traffic only from the ALB security group.
- SSH is not opened by this project.
- EC2 instances receive the SSM role for management without opening SSH.

### Monitoring
AWS Console -> CloudWatch.
Look for:
- `/rise6/rise6-cloud-web/app`
- EC2 memory and disk metrics
- Auto Scaling CPU metrics

### Health endpoint
```text
/health
```

Expected response:
```json
{"hostname":"...","status":"UP"}
```

## 4. Git version control

```bash
git init
git add .
git commit -m "Initial RISE 6.0 cloud project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

The included GitHub Actions workflow runs:
- Python tests
- Terraform formatting check
- Terraform validation

## 5. Demonstrate auto scaling

For the internship demonstration, use the AWS console to generate controlled CPU load on an instance and observe the Auto Scaling Group respond. Do not run uncontrolled stress tests or leave extra instances running.

## 6. Cleanup

When the demonstration is finished:

```bash
cd terraform
terraform destroy
```

This is important because AWS resources can incur charges.

## Screenshots to collect for the internship report

1. GitHub repository with source code.
2. Successful GitHub Actions workflow.
3. Terraform `apply` success.
4. Application running through the ALB URL.
5. ALB and target group with healthy instances.
6. Auto Scaling Group showing desired/min/max capacity.
7. CloudWatch dashboard/metrics.
8. CloudWatch application log group.
9. Security groups showing restricted EC2 port 8080.
10. Architecture diagram.

## Suggested project title for your report

**Industry-Oriented Cloud-Based Web Application Deployment and Scaling Using AWS**

## Note

This repository is designed as an internship demonstration project. Review AWS permissions, costs, regional availability, and your organization's security requirements before using it in production.
