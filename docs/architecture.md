# Architecture and Deployment Documentation

## Components

| Component | Purpose |
|---|---|
| AWS VPC | Isolated cloud network |
| Public subnets | Host ALB and demo EC2 instances |
| Application Load Balancer | Distributes HTTP requests |
| EC2 Auto Scaling Group | Maintains and scales application instances |
| Security Groups | Restricts network access |
| IAM role | Gives EC2 controlled AWS permissions |
| CloudWatch | Metrics and application logs |
| GitHub | Source/version control and CI validation |
| Terraform | Repeatable infrastructure provisioning |

## Request flow

1. User opens the public ALB URL.
2. ALB receives HTTP traffic on port 80.
3. ALB forwards the request to a healthy EC2 instance on port 8080.
4. Flask returns the web page.
5. `/health` is used by the target group health check.
6. CloudWatch receives application logs and system metrics.
7. Auto Scaling adjusts capacity using the average CPU target.

## Security model

Internet -> ALB security group -> EC2 security group -> Flask application.

The EC2 security group does not allow port 8080 from the public internet.

## Deployment lifecycle

Git push
  -> GitHub Actions
  -> tests + Terraform validation
  -> Terraform apply
  -> AWS infrastructure
  -> ALB
  -> Auto Scaling EC2 instances
  -> CloudWatch monitoring

## Evidence

Collect screenshots for every requirement and place them in the final internship report.
