variable "enable" {
  description = "Enable / Disable (e.g. `true`)"
  type        = bool
  default     = true
}

variable "alicloud_access_key" {
  type    = string
  default = "xxx"
}

variable "alicloud_secret_key" {
  type    = string
  default = "xxx"
}

variable "region" {
  description = "The region used to launch this module resources."
  type        = string
  default     = "cn-shanghai"
}