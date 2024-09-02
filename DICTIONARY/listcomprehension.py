list=[9,4,6,8]
square=[n**2 for n in list ]  #[return  iteration  condition]
print(square)

cubes=[n**3 for n in list ]
print(cubes)

even=[n for n in list if n%2==0]
print(even)

odd=[n for n in list if n%2!=0]
print(odd)