from re import finditer

text="abc 7Klefg@#"

# pattern="\d"#[0-9]
# pattern="\\D"#[^0-9]


# pattern="\w"#[a-zA-Z0-9]
# pattern="\\W"#[^a-zA-Z0-9]

pattern="\\S"#[^\s]

matchers=finditer(pattern,text)

for m in matchers:

    print(m.start(),"==",m.group())