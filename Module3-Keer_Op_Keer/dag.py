dagen = ['ma', 'di', 'wo', 'do', 'vr', 'za', 'zo']
dag = input("Welke dag is het?")

index_dag = dagen.index(dag)
i = 0

while i < len(dagen):
    print(dagen[i])
    i = i + 1
    if i > index_dag:
        break

