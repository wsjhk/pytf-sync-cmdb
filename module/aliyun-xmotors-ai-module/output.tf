output "slb_info" {
  description = "The slb ids."
  value       = data.alicloud_slbs.instances.slbs
}

output "ecs_info" {
  description = "The ecs instance ids."
  value = data.alicloud_instances.instances.instances
}

output "mongodb_info" {
  description = "The mongodb instance ids."
  value = data.alicloud_mongodb_instances.instances.instances
}

output "rds_info" {
  description = "The rds instance ids."
  value = data.alicloud_db_instances.instances.instances
}

output "nas_info" {
  description = "The nas instance ids."
  value = data.alicloud_nas_service.open
}

output "oss_info" {
  description = "The oss instance ids."
  value = data.alicloud_oss_service.open
}