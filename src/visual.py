import neo4j
import config
from nodegraph import *

def visualize_graph(dsg:graph, mdg:graph, R):
    # visualization using neo4j
    driver = neo4j.GraphDatabase.driver(config.url, auth=(config.usr, config.pwd))
    with driver.session() as session:
        print("verify:", driver.verify_authentication())
        # Clear existing nodes
        session.run("MATCH (n) DETACH DELETE n")  
        # clear existing relationships
        session.run("MATCH ()-[r]->() DELETE r")
        for node in dsg.nodes:
            session.run("CREATE (n:Node {value: $value, id: $id})", value=node.value, id=node.nodeid)
        for from_node, to_nodes in dsg.edges.items():
            for to_node in to_nodes:
                session.run("MATCH (a:Node {id: $from_id}), (b:Node {id: $to_id}) "
                            "CREATE (a)-[:DOMINATES]->(b)", 
                            from_id=from_node.nodeid, to_id=to_node.nodeid)
        for from_node, to_nodes in mdg.edges.items():
            for to_node in to_nodes:
                session.run("MATCH (a:Node {id: $from_id}), (b:Node {id: $to_id}) "
                            "CREATE (a)-[:MDG]->(b)", 
                            from_id=from_node.nodeid, to_id=to_node.nodeid)

        if config.importgskyline:   
            for k, group in enumerate(R):
                for i in range(0, len(group)):
                    session.run("CREATE (n:Node {value: $value, id: $id, GSky: $sky})", value=group[i].value, id=group[i].nodeid, sky=k)
                for i in range(0, len(group)-1):
                    for j in range(i+1, len(group)):
                        session.run("MATCH (a:Node {id: $from_id, GSky: $sky}), (b:Node {id: $to_id, GSky: $sky}) "
                                "CREATE (a)-[:GSky]->(b)", 
                                from_id=group[i].nodeid, to_id=group[j].nodeid, sky=k)
    driver.close()
