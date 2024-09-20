string = "dadaddadaadada"
sub = "dad"
index  = []
for i in range(len(string)):
    if string[i:i+len(sub)] == sub:
        index.append(i)
print(f"{string} has {len(index)} occurances of {sub} at indexes {index}")