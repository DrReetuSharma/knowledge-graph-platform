//This file can contain commonly used queries that are general and applicable across different use cases. 
//For example, queries to get all drugs, all targets, relationships between drugs and targets.

// Get all Drugs
MATCH (drug:Drug)
RETURN drug.name AS drugName

// Get all Targets
MATCH (target:Target)
RETURN target.name AS targetName

// Get Drugs and their Targets
MATCH (drug:Drug)-[:TARGETS]->(target:Target)
RETURN drug.name AS drugName, target.name AS targetName

