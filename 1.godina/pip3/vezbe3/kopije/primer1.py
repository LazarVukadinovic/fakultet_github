import re

pattern = r'\d{3}/\d{3}-\d{3}'
telefon_regex = re.compile(pattern)
brojTelefona = telefon_regex.search('Ovo je moj broj telefona 064/555-111 065/999-444')
if(brojTelefona):
    print(brojTelefona.group(0))

