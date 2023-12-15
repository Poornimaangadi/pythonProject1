d2={1:"ramesh",2:"ram",3:"sunil"}
print("dictionary values",d2)
d2={1:"ramesh",2:"ram",3:"sunil",1:"sham"}
print("dictionary values",d2)
print("key available in d2",d2.keys())

d3={1:"ramesh",2:"ram",3:"sunil",4:"sham"}
d3[5]="Ind"
print("after adding",d3)

d3.update({6:"Kiran"})
print("using update",d3)
print("d3.get(4)",d3.get(4))
print("d3(4)",d3[4])

#remove elements from dictionary
print("dictionary d3 before pop",d3)
print("d3.pop(1)", d3.pop(1))
print("dictionary d3 after pop",d3)
