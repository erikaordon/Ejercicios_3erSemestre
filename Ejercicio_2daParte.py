from Bio import Entrez 

Entrez.email = "erikog@lcg.unam.mx"

handle = Entrez.einfo(db="pubmed")
result = Entrez.read(handle)
handle.close()
DbInfo = result["DbInfo"]["FieldList"]
description = list((map(lambda lista:lista["Description"], DbInfo)))
print(description[0])