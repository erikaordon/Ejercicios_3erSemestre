from Bio import Entrez
from pprint import pprint  # para mejor visualización de diccionarios!!
# Correo
Entrez.email = "erikaog@lcg.unam.mx"  # IMPORTANTE!!!
# handle con einfo
#handle = Entrez.einfo()
#result = handle.read() 
#handle.close()
"""
record = Entrez.read(handle)
#chequemos qué hay en einfo 
#print(result)
print(record["DbList"][0:3])
handle.close()
"""
"""handle = Entrez.esearch(db = "pubmed", term='Mateo-Estrada V [AUTH]')
record = Entrez.read(handle) 
handle.close()
print(handle.url)
print(record["IdList"])
print(len(record["IdList"]))"""

"""termino = "(Aedes[Title] OR Aedes[All Fields])AND((RNA-Seq[Title] OR transcriptomic[Title]) OR (transcriptome[Title] OR sequencing[Title]))"
handle = Entrez.esearch(db = "pubmed", term = termino)
record = Entrez.read(handle)
print(record["Count"])"""

"""termino = "biopythoon"
handle = Entrez.espell(term = termino)
record = Entrez.read(handle)
print(record["Query"])
print(record["CorrectedQuery"])"""

"""handle = Entrez.einfo(db="pubmed")
result = Entrez.read(handle)
print(result["DbInfo"]["Description"])"""



# EJERCICIOS:
#Ejemplos con einfo 
# Este ejemplo está bien 
"""handle = Entrez.einfo(db="pubmed", terms="Jones[AUTH], Sanger[AFFL]")
result = Entrez.read(handle)
for field in result['DbInfo']['FieldList']:
    print('%(Name)s, %(FullName)s, %(Description)s' % field)"""

#Información completa 
"""handle = Entrez.einfo(db='pubmed')
result = Entrez.read(handle)
print(result['DbInfo'].values())"""


#Ejemplos con esearch
"""handle = Entrez.esearch(db="pubmed", term="biopython")
result = Entrez.read(handle)
print(len(result))"""

"""handle = Entrez.esearch(db="nucleotide", term="txid158330[Orgn] AND matK[Gene] AND complete[prop]")
result = Entrez.read(handle)
print(result)"""

#nlmcatalog
#handle = Entrez.esearch(db="nlmcatalog", term="computational")
#record = Entrez.read(handle)
#print(record["Count"])

"""handle = Entrez.esearch(db="nlmcatalog", term="biopython[Journal]", RetMax='20')
result = Entrez.read(handle)
print("{} computacional Journals found".format(result["Count"]))
print("The first 20 are\n{}".format(result['IdList']))"""


"""handle = Entrez.einfo(db="pubmed")
result = Entrez.read(handle)
handle.close()
for field in result["DbInfo"]["FieldList"]:
    #print(field["Name"]+", "+field["FullName"]+": "+field["Description"])
    print("%(Name)s, %(FullName)s, %(Description)s" %field)"""

"""handle = Entrez.einfo(db="pubmed")
result = Entrez.read(handle)
handle.close()
print(result["DbInfo"]["LastUpdate"])"""

"""handle = Entrez.einfo(db="pubmed", term="biopython")
result = Entrez.read(handle)
print(handle.url)"""