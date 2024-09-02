email_id="saniya@123"

at_index_position=email_id.index("@")

username=email_id[:at_index_position]

mail=email_id[at_index_position:]
 
print(username)
print(mail)
