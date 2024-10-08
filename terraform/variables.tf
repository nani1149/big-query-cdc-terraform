variable "delete_contents_on_destroy" {
  description = "(Optional) If set to true, delete all the tables in the dataset when destroying the resource; otherwise, destroying the resource will fail if tables are present."
  type        = bool
  default     = null
}

variable "default_table_expiration_ms" {
  description = "Default TTL of tables using the dataset in MS."
  default     = null
}

variable "project_id" {
  description = "Project where the dataset and table are created."
  default     = "sacred-alliance-433217-e3"
}

