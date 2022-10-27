from datetime import datetime

def format_other(dijkstra, floyd, kruskal, prim):
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    string_builder = ""
    string_builder += f"<h3>Run at: {now}</h3>"
    string_builder += "<h2>Experiment 2: Dijkstra, Floyd, Kruskal and Prim</h2>"

    string_builder += "<h3>Dijkstra</h3>"
    for item in dijkstra:
        string_builder += f"<p>{item}</p>"
    
    string_builder += "<h3>Floyd</h3>"
    for item in floyd:
        string_builder += f"<p>{item}</p>"
    
    string_builder += "<h3>Kruskal</h3>"
    for item in kruskal:
        string_builder += f"<p>{item}</p>"
    
    string_builder += "<h3>Prim</h3>"
    for item in prim:
        string_builder += f"<p>{item}</p>"
    
    return string_builder