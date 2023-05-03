import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt

graph = []

# Draw graph  
def draw_graph(graph):
    G = nx.DiGraph()
    
    for start, end, reach in graph:
        G.add_edge(start, end, weight=reach)

    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', font_size=10, font_weight='bold', node_size=1000)
    
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, bbox=dict(facecolor='white', edgecolor='none', pad=3))
    
    plt.show()
    
# Input graph data    
def parse_graph(text):
    graph = []
    lines = text.strip().split('\n')
    for line in lines:
        start, end, weight = map(int, line.split())
        graph.append((start, end, weight))
    return graph

# Act when click submit button
def submit_form():
    text = entry_text.get("1.0", tk.END)
    global graph
    graph = parse_graph(text)
    draw_graph(graph)

# Act when click close button
def close_form():
    window.destroy()

# Make Gui
window = tk.Tk()
window.title("Graph Input")

# Set the window size
window.geometry("240x400")

frame = ttk.Frame(window, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Add a bold label for "Enter graph"
label_title = ttk.Label(frame, text="Enter graph", font=("Helvetica", 12, "bold"), anchor='center')
label_title.grid(column=0, row=0, sticky='ew', padx=10, pady=5, columnspan=2)

label_text = ttk.Label(frame, text="start end distance", anchor='center')
label_text.grid(column=0, row=1, sticky='ew', padx=10, pady=5, columnspan=2)

entry_text = tk.Text(frame, width=20, height=20)
entry_text.grid(column=0, row=2, padx=10, pady=10, columnspan=2)

button_submit = ttk.Button(frame, text="Submit", command=submit_form)
button_submit.grid(column=0, row=3, padx=10, pady=10)

button_close = ttk.Button(frame, text="Close", command=close_form)
button_close.grid(column=1, row=3, padx=10, pady=10)

window.mainloop()

print(graph)

