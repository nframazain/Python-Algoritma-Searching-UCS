import json
from src.ucs import uniform_cost_search
from src.visualize import draw_graph

with open("data/cities_graph.json") as f:
    city_graph = json.load(f)

start_city = input("Masukkan kota asal: ")
end_city = input("Masukkan kota tujuan: ")

if start_city not in city_graph or end_city not in city_graph:
    print("Kota tidak ditemukan dalam data.")
else:
    cost, path = uniform_cost_search(city_graph, start_city, end_city)
    print(f"\nJarak minimum dari {start_city} ke {end_city}: {cost} km")
    print("Rute yang dilewati:", " -> ".join(path))

    draw_graph(city_graph, path)
    print("Visualisasi rute disimpan di 'output/route_result.png'")