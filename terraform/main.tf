module "bigquery" {
  source  = "terraform-google-modules/bigquery/google"
  version = "~> 7.0"

  dataset_id                 = "bigquery_cdc"
  dataset_name               = "bigquery_cdc"
  description                = "dataset for storing llm evalution results"
  project_id                 = var.project_id
  location                   = "US"
  delete_contents_on_destroy = var.delete_contents_on_destroy
  tables = [
    {
      table_id           = "bigquery_customers_cdc",
      schema             = file("cdc.json"),
      time_partitioning  = null,
      range_partitioning = null,
      expiration_time    = 2524604400000, # 2050/01/01
      clustering         = [],
      labels = {
        env      = "devops"
        billable = "true"
        owner    = "ndonthi1"
      },
    }
  ]
  dataset_labels = {
    env      = "dev"
    billable = "true"
    owner    = "janesmith"
  }
}