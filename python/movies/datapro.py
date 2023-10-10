from json import load
path="C:\\Users\\Hamad\\Desktop\\python\\movies\\mdb.json"
with open(path,encoding="utf-8")as f:
    films=load(f)
    # total number of films
# print(len(films))
#   
# print all  movie names released in 2015
# movie_names=[f.get("title")for f in films if f.get("year")=="2015"]
# print(movie_names)

# print comedy genre movie title
# comedy_movie=[f.get("title")for f in films if "Comedy" in f.get("genres")]
# print(comedy_movie)

# m_fil=[f.get("title")for f in films if f.get("id")in range(20,31)and f.get("runtime")>="110"]
# print(m_fil)

# title=[f.get("title")for f in films if len(f.get("title").split(" "))==1]
# print(title)

# genre=drama highest runtime
# films_genre=[f for f in films if "Drama"in f.get("genres")]
# longest_runtime=max(films_genre,key=lambda d:int(d.get("runtime")))
# print(longest_runtime)

# genre={b for r in films for b in r.get("genres")}
# print(genre)

wc={}
for m in films:
   year=m.get("year")
   if year in wc:
         wc[year]+=1
   else:    
         wc[year]=1
print(max(wc,key=lambda d:wc.get(d)))        

print(max((v,k) for k,v in wc.items()))


