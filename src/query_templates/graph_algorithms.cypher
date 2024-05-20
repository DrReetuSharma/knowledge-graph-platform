// If you use Neo4j's Graph Data Science library or other graph algorithms,
you can keep the queries for these algorithms in a separate file for better organization and reference.

// PageRank Algorithm
CALL algo.pageRank.stream('Drug', 'TARGETS', {iterations: 20, dampingFactor: 0.85})
YIELD nodeId, score
RETURN algo.asNode(nodeId).name AS drugName, score
ORDER BY score DESC
