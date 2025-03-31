from rcsbapi.search import AttributeQuery, TextQuery
from rcsbapi.search import search_attributes as attrs


q1 = TextQuery(value="OmpA")
#q2 = TextQuery(value="Escherichia coli")
#q3 = TextQuery(value="Membrane")
q2 = AttributeQuery(
   attribute="rcsb_entity_source_organism.scientific_name",
    operator = "exact_match",
    value = "Escherichia coli",
)
#q3 = AttributeQuery(
#    attribute="struct_keywords.text",
#    operator = "exact_match",
#    value = "Lipoprotein",
#)

query = q1 & q2
results = query()

for rId in results:
    print(rId)

print()





def fippel(pdb_id, source_organism):
    q1 = TextQuery(value=pdb_id)
    q2 = AttributeQuery(
   attribute="rcsb_entity_source_organism.scientific_name",
    operator = "exact_match",
    value = source_organism,
    )
    query = q1 & q2
    results = query