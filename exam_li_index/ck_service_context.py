from llama_index import ServiceContext

sc1 = ServiceContext.from_defaults()
sc2 = ServiceContext.from_defaults()

print(sc1)
print(sc2)

if __name__ == "__main__":
    print("hi")