// 获取slb资源信息
data "alicloud_slbs" "instances" {
  name_regex = ".*"
}

// 获取ecs资源信息
data "alicloud_instances" "instances" {
  name_regex = ".*"
}

// 获取mongodb资源信息
data "alicloud_mongodb_instances" "instances" {
  name_regex = "dds-.+\\d+"
}

// 获取rds资源信息
data "alicloud_db_instances" "instances" {
  name_regex = "data-\\d+"
}

// nas和oss资源信息
data "alicloud_nas_service" "open" {
    enable = "On"
}

data "alicloud_oss_service" "open" {
    enable = "On"
}
