#Imports
from NameData import *


#Name data
##############################################################################################
#en_US data
print( "There are " + str(len(en_US_first_names) ) + " en-US first names." )
print( "There are " + str( len(en_US_last_names) ) + " en-US last names." )
print( "There are " + str( len( en_US_prefixes ) ) + " en-US prefixes." )
print( "There are " + str( len( en_US_suffixes ) ) + " en-US suffixes." )
print( "There are " + str( len( en_US_formats ) ) + " en-US formats." )

print("\n")

#es_MX data
print( "There are " + str(len(es_MX_first_names) ) + " es-MX first names." )
print( "There are " + str( len(es_MX_last_names) ) + " es-MX last names." )
print( "There are " + str( len( es_MX_prefixes ) ) + " es-MX prefixes." )
print( "There are " + str( len( es_MX_formats ) ) + " es-MX formats." )

print("\n")

#es_ES data
print( "There are " + str(len(es_ES_first_names) ) + " es-ES first names." )
print( "There are " + str( len(es_ES_last_names) ) + " es-ES last names." )
print( "There are " + str( len( es_ES_prefixes ) ) + " es-ES prefixes." )
print( "There are " + str( len( es_ES_formats ) ) + " es-ES formats." )

print("\n")

#fr_FR data
print( "There are " + str(len(fr_FR_first_names) ) + " fr_FR first names." )
print( "There are " + str( len(fr_FR_last_names) ) + " fr_FR last names." )
print( "There are " + str( len( fr_FR_prefixes ) ) + " fr_FR prefixes." )
print( "There are " + str( len( fr_FR_formats ) ) + " fr_FR formats." )

print("\n")

#ru_RU data
print( "There are " + str(len(ru_RU_first_names) ) + " ru_RU first names." )
print( "There are " + str( len(ru_RU_last_names) ) + " ru_RU last names." )
print( "There are " + str( len( ru_RU_prefixes ) ) + " ru_RU prefixes." )
print( "There are " + str( len( ru_RU_formats ) ) + " ru_RU formats." )

print("\n")

#cs_CZ data
print( "There are " + str(len(cs_CZ_first_names_male) ) + " cs_CZ male first names." )
print( "There are " + str(len(cs_CZ_first_names_female) ) + " cs_CZ female first names." )
print( "There are " + str(len(cs_CZ_last_names_male) ) + " cs_CZ male last names." )
print( "There are " + str(len(cs_CZ_last_names_male) ) + " cs_CZ female last names." )
print( "There are " + str(len(cs_CZ_prefixes_female) ) + " cs_CZ female prefixes (includes degrees)." )
print( "There are " + str(len(cs_CZ_prefixes_male) ) + " cs_CZ male prefixes (includes degrees)." )
print( "There are " + str(len(cs_CZ_degrees) ) + " cs_CZ degrees." )
print( "There are " + str(len(cs_CZ_suffixes) ) + " cs_CZ suffixes." )
print( "There are " + str(len(cs_CZ_formats) ) + " cs_CZ formats." )

print("\n")

#de_DE data
print( "There are " + str(len(de_DE_first_names_male) ) + " de_DE male first names." )
print( "There are " + str(len(de_DE_first_names_female) ) + " de_DE female first names." )
print( "There are " + str(len(de_DE_last_names) ) + " de_DE last names." )
print( "There are " + str(len(de_DE_prefixes_female) ) + " de_DE female prefixes." )
print( "There are " + str(len(de_DE_prefixes_male) ) + " de_DE male prefixes." )
print( "There are " + str(len(de_DE_suffixes) ) + " de_DE suffixes." )
print( "There are " + str(len(de_DE_formats) ) + " de_DE formats." )

print("\n")

#fr_FI data
print( "There are " + str(len(fr_FI_first_names) ) + " fr_FI first names." )
print( "There are " + str( len(fr_FI_last_names) ) + " fr_FI last names." )
print( "There are " + str( len( fr_FI_prefixes ) ) + " fr_FI prefixes." )
print( "There are " + str( len( fr_FI_suffixes ) ) + " fr_FI suffixes." )
print( "There are " + str( len( fr_FI_formats ) ) + " fr_FI formats." )

print("\n")

#dk_DK data
print( "There are " + str(len(dk_DK_first_names_male) ) + " dk_DK male first names." )
print( "There are " + str(len(dk_DK_first_names_female) ) + " dk_DK female first names." )
print( "There are " + str(len(dk_DK_last_names) ) + " dk_DK last names." )
print( "There are " + str(len(dk_DK_prefixes_female) ) + " dk_DK female prefixes." )
print( "There are " + str(len(dk_DK_prefixes_male) ) + " dk_DK male prefixes." )
print( "There are " + str(len(dk_DK_formats) ) + " dk_DK formats." )

print("\n")

#el_GR data
print( "There are " + str(len(el_GR_first_names_male) ) + " el_GR male first names." )
print( "There are " + str(len(el_GR_first_names_female) ) + " el_GR female first names." )
print( "There are " + str(len(el_GR_last_names_male) ) + " el_GR male last names." )
print( "There are " + str(len(el_GR_last_names_female) ) + " el_GR female last names." )
print( "There are " + str(len(el_GR_formats) ) + " el_GR formats." )

print("\n")

#it_IT data
print( "There are " + str(len(it_IT_first_names) ) + " it_IT first names." )
print( "There are " + str( len(it_IT_last_names) ) + " it_IT last names." )
print( "There are " + str( len( it_IT_prefixes ) ) + " it_IT prefixes." )
print( "There are " + str( len( it_IT_formats ) ) + " it_IT formats." )

#Write data to XML
############################################ 
#en_US data
f = open( "en_US_names.txt", 'w+')
for name in en_US_first_names:
    f.write( "<name type=\"first\">" + name + "</name>\n" )

for name in en_US_last_names:
	f.write( "<name type=\"last\">" + name + "</name>\n" )

for prefix in en_US_prefixes:
	f.write( "<prefix>" + prefix + "</prefix>\n" )

for suffix in en_US_suffixes:
	f.write( "<suffix>" + suffix + "</suffix>\n" )
    
for format in en_US_formats:
    f.write( "<format>" + format + "</format>\n" )
    
############################################ 
#es_MX data
f = open( "es_MX_names.txt", 'w+')
for name in es_MX_first_names:
    f.write( "<name type=\"first\">" + name + "</name>\n" )

for name in es_MX_last_names:
	f.write( "<name type=\"last\">" + name + "</name>\n" )

for prefix in es_MX_prefixes:
	f.write( "<prefix>" + prefix + "<prefix>\n" )

for format in es_MX_formats:
    f.write( "<format>" + format + "</format>\n" )
    
############################################ 
#es_ES data
f = open( "es_ES_names.txt", 'w+')
for name in es_ES_first_names:
    f.write( "<name type=\"first\">" + name + "</name>\n" )

for name in es_ES_last_names:
	f.write( "<name type=\"last\">" + name + "</name>\n" )

for prefix in es_ES_prefixes:
	f.write( "<prefix>" + prefix + "<prefix>\n" )

for format in es_ES_formats:
    f.write( "<format>" + format + "</format>\n" )
    
############################################ 
#fr_FR data
f = open( "fr_FR_names.txt", 'w+')
for name in fr_FR_first_names:
    f.write( "<name type=\"first\">" + name + "</name>\n" )

for name in fr_FR_last_names:
	f.write( "<name type=\"last\">" + name + "</name>\n" )

for prefix in fr_FR_prefixes:
	f.write( "<prefix>" + prefix + "</prefix>\n" )

for format in fr_FR_formats:
    f.write( "<format>" + format + "</format>\n" )

############################################    
#ru_RU data
f = open( "ru_RU_names.txt", 'w+')
for name in ru_RU_first_names:
    f.write( "<name type=\"first\">" + name + "</name>\n" )

for name in ru_RU_last_names:
	f.write( "<name type=\"last\">" + name + "</name>\n" )

for prefix in ru_RU_prefixes:
	f.write( "<prefix>" + prefix + "</prefix>\n" )

for format in ru_RU_formats:
    f.write( "<format>" + format + "</format>\n" )

############################################    
#cs_CZ data
f = open( "cs_CZ_names.txt", 'w+' )
for name in cs_CZ_first_names_male:
    f.write( "<name type=\"first\" sex=\"male\">" + name + "</name>\n" )

for name in cs_CZ_first_names_female:
    f.write( "<name type=\"first\" sex=\"female\">" + name + "</name>\n" )

for name in cs_CZ_last_names_male:
	f.write( "<name type=\"last\" sex=\"male\">" + name + "</name>\n" )
    
for name in cs_CZ_last_names_female:
	f.write( "<name type=\"last\" sex=\"female\">" + name + "</name>\n" )
    
for prefix in cs_CZ_prefixes_male:
	f.write( "<prefix sex=\"male\">" + prefix + "</prefix>\n" )
    
for prefix in cs_CZ_prefixes_female:
	f.write( "<prefix sex=\"female\">" + prefix + "</prefix>\n" )
    
for suffix in cs_CZ_suffixes:
	f.write( "<suffix>" + suffix + "</suffix>\n" )
    
for format in cs_CZ_formats:
	f.write( "<format>" + format + "</format>\n" )
    
############################################    
#de_DE data
f = open( "de_DE_names.txt", 'w+' )
for name in de_DE_first_names_male:
    f.write( "<name type=\"first\" sex=\"male\">" + name + "</name>\n" )

for name in de_DE_first_names_female:
    f.write( "<name type=\"first\" sex=\"female\">" + name + "</name>\n" )

for name in de_DE_last_names:
	f.write( "<name type=\"last\" sex=\"male\">" + name + "</name>\n" )
    
for prefix in de_DE_prefixes_male:
	f.write( "<prefix sex=\"male\">" + prefix + "</prefix>\n" )
    
for prefix in de_DE_prefixes_female:
	f.write( "<prefix sex=\"female\">" + prefix + "</prefix>\n" )
    
for suffix in de_DE_suffixes:
	f.write( "<suffix>" + suffix + "</suffix>\n" )
    
for format in de_DE_formats:
	f.write( "<format>" + format + "</format>\n" )

############################################ 
#fr_FI data
f = open( "fr_FI_names.txt", 'w+')
for name in fr_FI_first_names:
    f.write( "<name type=\"first\">" + name + "</name>\n" )

for name in fr_FI_last_names:
	f.write( "<name type=\"last\">" + name + "</name>\n" )

for prefix in fr_FI_prefixes:
	f.write( "<prefix>" + prefix + "</prefix>\n" )

for suffix in fr_FI_suffixes:
	f.write( "<suffix>" + suffix + "</suffix>\n" )
    
for format in fr_FI_formats:
    f.write( "<format>" + format + "</format>\n" )
    
############################################    
#dk_DK data
f = open( "dk_DK_names.txt", 'w+' )
for name in dk_DK_first_names_male:
    f.write( "<name type=\"first\" sex=\"male\">" + name + "</name>\n" )

for name in dk_DK_first_names_female:
    f.write( "<name type=\"first\" sex=\"female\">" + name + "</name>\n" )

for name in dk_DK_last_names:
	f.write( "<name type=\"last\">" + name + "</name>\n" )
    
for prefix in dk_DK_prefixes_male:
	f.write( "<prefix sex=\"male\">" + prefix + "</prefix>\n" )
    
for prefix in dk_DK_prefixes_female:
	f.write( "<prefix sex=\"female\">" + prefix + "</prefix>\n" )
    
for format in dk_DK_formats:
	f.write( "<format>" + format + "</format>\n" )
    
############################################    
#el_GR data
f = open( "el_GR_names.txt", 'w+' )
for name in el_GR_first_names_male:
    f.write( "<name type=\"first\" sex=\"male\">" + name + "</name>\n" )

for name in el_GR_first_names_female:
    f.write( "<name type=\"first\" sex=\"female\">" + name + "</name>\n" )

for name in el_GR_last_names_male:
	f.write( "<name type=\"last\" sex=\"male\">" + name + "</name>\n" )
    
for name in el_GR_last_names_female:
	f.write( "<name type=\"last\" sex=\"female\">" + name + "</name>\n" )
    
for format in el_GR_formats:
	f.write( "<format>" + format + "</format>\n" )
    
############################################    
#it_IT data
f = open( "it_IT_names.txt", 'w+')
for name in it_IT_first_names:
    f.write( "<name type=\"first\">" + name + "</name>\n" )

for name in it_IT_last_names:
	f.write( "<name type=\"last\">" + name + "</name>\n" )

for prefix in it_IT_prefixes:
	f.write( "<prefix>" + prefix + "</prefix>\n" )

for format in it_IT_formats:
    f.write( "<format>" + format + "</format>\n" )
