# Substituindo caracteres repetidos
name = 'Fifa 23'
char = name[0].lower()
new_name = name.replace(char, '$')
new_name = char + new_name[1:]
print(new_name)

# Troca de caracteres

st1 = 'cab'  # zyb
st2 = 'zyx'  # cax

new_st1 = st2[:2] + st1[2:]
print(new_st1)
new_st2 = st1[:2] + st2[2:]
print(new_st2)
