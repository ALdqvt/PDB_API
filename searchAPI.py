from rcsbapi.search import AttributeQuery, TextQuery
from rcsbapi.search import search_attributes as attrs

#
# q1 = AttributeQuery(
#     attribute = "rcsb_entity_source_organism.scientific_name",
#     operator = "exact_match",
#     value = "Escherichia Coli"
# )
#
# q2 = AttributeQuery(
#     attribute = "rcsb_membrane_lineage.name",
#     operator = "exists",
#     value = "outer membrane"
# )

#q3 = attrs.rcsb_entity_source_organism.scientific_name == "Homo sapiens"

query = TextQuery(value="OmpA")

a = 0
for rId in query():
    print(rId)
    print(a)
    a = a+1

