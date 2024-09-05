def make_pizza(*topins,base):
    print(topins,base)

amit=make_pizza("tomato","onion", base="thin")# we need to specifically mention the base otherwise it will consider as topins only
gani=make_pizza("Beans","Cheese","Butter",base="thick")
