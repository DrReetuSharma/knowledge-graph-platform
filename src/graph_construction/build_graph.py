
import csv
from neo4j import GraphDatabase

class KnowledgeGraphBuilder:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def build_graph(self, file_path):
        with self.driver.session() as session:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    session.write_transaction(self._create_nodes_and_relationships, row)

    @staticmethod
    def _create_nodes_and_relationships(tx, row):
        # Define the Cypher query for creating nodes and relationships
        query = """
        MERGE (d:Drug {id: $drug_id, name: $drug_name})
        MERGE (t:Target {id: $target_id, name: $target_name})
        MERGE (dis:Disease {id: $disease_id, name: $disease_name})
        MERGE (d)-[:TARGETS]->(t)
        MERGE (d)-[:TREATS]->(dis)
        """
        # Execute the query with the provided data
        tx.run(query, 
               drug_id=row['drug_id'], 
               drug_name=row['drug_name'], 
               target_id=row['target_id'], 
               target_name=row['target_name'], 
               disease_id=row['disease_id'], 
               disease_name=row['disease_name'])

if __name__ == "__main__":
    # Neo4j database connection settings
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "password"

    # Initialize the knowledge graph builder
    kg_builder = KnowledgeGraphBuilder(uri, user, password)
    
    # Path to the preprocessed CSV file
    file_path = 'dataset_HTN_cleaned.csv'
    
    # Build the graph
    kg_builder.build_graph(file_path)
    
    # Close the connection
    kg_builder.close()
