output "ecs_info" {
  description = "The ecs instance ids."
  value = data.aws_instances.instances.ids
}
