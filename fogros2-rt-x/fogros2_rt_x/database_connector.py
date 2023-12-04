
class BaseDataBaseConnector():
    def __init__(self):
        pass

    def query(self, query_string):
        pass

    def insert(self, rows):
        pass


class BigQueryConnector(BaseDataBaseConnector):
    def __init__(self, project_name, dataset_name, table_name):
        self.project_name = project_name
        self.dataset_name = dataset_name
        self.table_name = table_name
        self.table_id = f"{project_name}.{dataset_name}.{table_name}"
        self.client = bigquery.Client(project_name = project_name)

    def query(self, query_string):
        query_job = self.client.query(query_string)
        return query_job.to_dataframe()

    def insert(self, rows):
        errors = self.client.insert_rows_json(self.table_id, rows)
        if errors:
            raise BigQueryError(errors)