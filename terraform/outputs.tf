output "application_url" {
  description = "Public URL of the load-balanced application"
  value       = "http://${aws_lb.app.dns_name}"
}

output "load_balancer_dns" {
  value = aws_lb.app.dns_name
}

output "autoscaling_group" {
  value = aws_autoscaling_group.app.name
}
