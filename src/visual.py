import neo4j
import config

def visualize_graph(graph):
    # visualization using neo4j
    driver = neo4j.GraphDatabase.driver("neo4j+ssc://fc86cbe5.databases.neo4j.io", auth=(config.usr, config.pwd))
    with driver.session() as session:
        print("verify:", driver.verify_authentication())
        # Clear existing nodes
        session.run("MATCH (n) DETACH DELETE n")  
        # clear existing relationships
        session.run("MATCH ()-[r]->() DELETE r")
        for node in graph.nodes:
            session.run("CREATE (n:Node {value: $value, id: $id})", value=node.value, id=node.nodeid)
        for from_node, to_nodes in graph.edges.items():
            for to_node in to_nodes:
                session.run("MATCH (a:Node {id: $from_id}), (b:Node {id: $to_id}) "
                            "CREATE (a)-[:CONNECTED]->(b)", 
                            from_id=from_node.nodeid, to_id=to_node.nodeid)
    driver.close()
