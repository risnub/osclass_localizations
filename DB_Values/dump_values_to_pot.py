import peewee
from peewee import *

import osclass_models
from osclass_models import database 
from osclass_models import OcTPreference, OcTMetaFields, OcTRegion, OcTCountry, OcTCity, OcTCityArea;

database.connect();

print "Database connected.";

msgid_dict = {};
msgid_dict['keyword_placeholder'] = OcTPreference.get(OcTPreference.s_name == 'keyword_placeholder').s_value;
# row = OcTPreference.get(OcTPreference.s_name == 'keyword_placeholder');
# print row;

msgid_dict['pageTitle'] = OcTPreference.get(OcTPreference.s_name == 'pageTitle').s_value;
msgid_dict['pageDesc'] = OcTPreference.get(OcTPreference.s_name == 'pageDesc').s_value;

customFields = OcTMetaFields.select().where(OcTMetaFields.s_slug != 'new-custom-field');
for cf in customFields:
	if cf.e_type == 'RADIO' or cf.e_type == 'DROPDOWN' or cf.e_type == 'CHECKBOX':
		cf_options = cf.s_options.split(',');
		for opt in cf_options:
			msgid_dict[cf.s_name + '_' + opt] = opt;


regions = OcTRegion.select();
for r in regions:
	msgid_dict['region_' + str(r.pk_i)] = r.s_name;

countries = OcTCountry.select();
for c in countries:
	msgid_dict['country_' + c.pk_c_code] = c.s_name;
	
cities = OcTCity.select();
for c in cities:
	msgid_dict['city_' + str(c.pk_i)] = c.s_name;
	
cityAreas = OcTCityArea.select();
for c in cityAreas:
	msgid_dict['cityarea_' + str(c.pk_i)] = c.s_name;


database.close();

print "Database closed";

# the makepot script actually parses the PHP input file.
print "<?php"
for k, v in msgid_dict.items():
	print "_e(\"%s\");" % (v);
print "?>"			
	

