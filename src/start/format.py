from datetime import datetime

def format(rest_result, total_time):
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    string_builder = ""
    string_builder += f"<h3>Run at: {now}</h3>"
    string_builder += "<h2>Experiment 1: Benchmark</h2>"

    for key in rest_result:
        string_builder += f"<h2>{key}:</h2>"
        string_builder += f"<h4>Input small: {rest_result[key][0]}s</h4>"
        string_builder += f"<h4>Input medium: {rest_result[key][1]}s</h4>"
        string_builder += f"<h4>Input large: {rest_result[key][2]}s</h4>"
        string_builder += "</br>"
    
    string_builder += f"<h2>Total time: {total_time}s</h2>"
    return string_builder