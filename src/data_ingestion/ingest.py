import csv
from neo4j import GraphDatabase

class KnowledgeGraphIngestion:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def ingest_data(self, file_path):
        with self.driver.session() as session:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    session.write_transaction(self._create_nodes_and_relationships, row)

    @staticmethod
    def _create_nodes_and_relationships(tx, row):
        query = """
        MERGE (d:Drug {id: $drug_id, name: $drug_name})
        MERGE (t:Target {id: $target_id, name: $target_name})
        MERGE (dis:Disease {id: $disease_id, name: $disease_name})
        MERGE (d)-[:TARGETS]->(t)
        MERGE (d)-[:TREATS]->(dis)
        """
        tx.run(query, row)

if __name__ == "__main__":
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "password"

    kg_ingestion = KnowledgeGraphIngestion(uri, user, password)
    kg_ingestion.ingest_data('dataset_HTN.csv')
    kg_ingestion.close()
