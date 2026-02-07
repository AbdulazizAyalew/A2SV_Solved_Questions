t = int(input())
faces = {"Tetrahedron":4, "Cube":6, "Octahedron":8, "Dodecahedron":12, "Icosahedron":20}
no_faces = 0
for i in range(t):
    polyhedron = input()
    no_faces += faces[polyhedron]

print(no_faces)
