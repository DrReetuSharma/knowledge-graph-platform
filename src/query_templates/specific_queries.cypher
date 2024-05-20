//If you have queries that are specific to certain analyses, tasks, or questions, you can store them in this file. 
//For instance, queries related to drug-disease relationships, network analysis, or advanced graph algorithms.

// Get Drugs for a Specific Disease
MATCH (drug:Drug)-[:TREATS]->(:Disease {name: 'Hypertension'})
RETURN drug.name AS drugName

// Count of Drugs per Target
MATCH (drug:Drug)-[:TARGETS]->(target:Target)
RETURN target.name AS targetName, count(drug) AS drugCount
