from Bio import Entrez

Entrez.email = "erikaog@lcg.unam.mx" 

handle = Entrez.einfo(db="pubmed")
result = Entrez.read(handle)
handle.close()
for field in result["DbInfo"]["FieldList"]:
    #Las líneas a partir de esta solo es para darle un formato más amigable. 
    FieldList='%(Name)s, %(Description)s' % field
    print(FieldList.replace(",", ":"))