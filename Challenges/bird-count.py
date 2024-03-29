birds = [{'name':'mus','key':'m','count':0},
          {'name':'duif','key':'d','count':0},
          {'name':'koolmees','key':'k','count':0},
          {'name':'kraai','key':'i','count':0},
          ]

key = ""

print('Bird counter until dot')
for bird in (birds):
    print(f"{bird['key']} : {bird['name']}")

def get_bird_by_key(birds: list, key:str):
    for bird in (birds):
        if key == bird['key']:
            return bird
    return None

while key != '.':
    key = input("key of bird")
    if key == '.':
        break
    bird = get_bird_by_key(birds, key)
    if bird != None:
        bird['count'] += 1
        print(f"{bird['name']} : {bird['count']}") 
    else:
        print('Die key staat niet in de lijst')

for b in birds:
    print(f"{b['name']} : {b['count']}")

totaal = 0
for b in birds:
    totaal += b['count']

if totaal > 0:
    for b in birds:
        procent = b['count'] / totaal * 100
        print(f"{bird['name']} {procent}%")
    
# TO DO:

# 1) print all birds with key and name

# 2) define function get_bird_by_key(birds: list, key:str) returns bird or None

# 3) repeat until given '.'
#       input key of bird 
#    find bird with get_bird_by_key
#    if bird found: 
#       increment bird count
#       show bird name and count

# 4) print all birds with name and count

# 5) print per bird also the percentage of the total count