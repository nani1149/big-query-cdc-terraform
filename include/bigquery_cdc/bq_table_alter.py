from google.cloud import bigquery

def alter_table_max_staleness():

    # Create a BigQuery client
    client = bigquery.Client()

    # Define the SQL query
    query = """
    ALTER TABLE `sacred-alliance-433217-e3.bigquery_cdc.bigquery_customers_cdc`
    SET OPTIONS (
    max_staleness = INTERVAL 0 MINUTE
    )
    """

    # Execute the query
    query_job = client.query(query)

    # Wait for the query to finish
    query_job.result()

    print("ALTER TABLE query executed successfully.")
