from peewee import *

database = MySQLDatabase('osclass', **{'host': 'localhost', 'password': 'oscu', 'user': 'osclassadmin'})

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class OcTAdmin(BaseModel):
    b_moderator = IntegerField()
    pk_i = PrimaryKeyField(db_column='pk_i_id')
    s_email = CharField(null=True, unique=True)
    s_name = CharField()
    s_password = CharField()
    s_secret = CharField(null=True)
    s_username = CharField(unique=True)

    class Meta:
        db_table = 'oc_t_admin'

class OcTAlerts(BaseModel):
    b_active = IntegerField()
    dt_date = DateTimeField(null=True)
    dt_unsub_date = DateTimeField(null=True)
    e_type = CharField()
    fk_i_user = IntegerField(db_column='fk_i_user_id', null=True)
    pk_i = PrimaryKeyField(db_column='pk_i_id')
    s_email = CharField(null=True)
    s_search = TextField(null=True)
    s_secret = CharField(null=True)

    class Meta:
        db_table = 'oc_t_alerts'

class OcTAlertsSent(BaseModel):
    d_date = DateField(primary_key=True)
    i_num_alerts_sent = IntegerField()

    class Meta:
        db_table = 'oc_t_alerts_sent'

class OcTBanRule(BaseModel):
    pk_i = PrimaryKeyField(db_column='pk_i_id')
    s_email = CharField()
    s_ip = CharField()
    s_name = CharField()

    class Meta:
        db_table = 'oc_t_ban_rule'

class OcTCategory(BaseModel):
    b_enabled = IntegerField()
    b_price_enabled = IntegerField()
    fk_i_parent = ForeignKeyField(db_column='fk_i_parent_id', null=True, rel_model='self', to_field='pk_i')
    i_expiration_days = IntegerField()
    i_position = IntegerField(index=True)
    pk_i = PrimaryKeyField(db_column='pk_i_id')
    s_icon = CharField(null=True)

    class Meta:
        db_table = 'oc_t_category'

class OcTLocale(BaseModel):
    b_enabled = IntegerField()
    b_enabled_bo = IntegerField()
    i_num_dec = IntegerField(null=True)
    pk_c_code = CharField(primary_key=True)
    s_author_name = CharField()
    s_author_url = CharField()
    s_currency_format = CharField()
    s_date_format = CharField()
    s_dec_point = CharField(null=True)
    s_description = CharField()
    s_name = CharField()
    s_short_name = CharField(unique=True)
    s_stop_words = TextField(null=True)
    s_thousands_sep = CharField(null=True)
    s_version = CharField()

    class Meta:
        db_table = 'oc_t_locale'

class OcTCategoryDescription(BaseModel):
    fk_c_locale_code = ForeignKeyField(db_column='fk_c_locale_code', rel_model=OcTLocale, to_field='pk_c_code')
    fk_i_category = ForeignKeyField(db_column='fk_i_category_id', rel_model=OcTCategory, to_field='pk_i')
    s_description = TextField(null=True)
    s_name = CharField(null=True)
    s_slug = CharField(index=True)

    class Meta:
        db_table = 'oc_t_category_description'
        indexes = (
            (('fk_i_category', 'fk_c_locale_code'), True),
        )
        primary_key = CompositeKey('fk_c_locale_code', 'fk_i_category')

class OcTCategoryStats(BaseModel):
    fk_i_category = ForeignKeyField(db_column='fk_i_category_id', primary_key=True, rel_model=OcTCategory, to_field='pk_i')
    i_num_items = IntegerField()

    class Meta:
        db_table = 'oc_t_category_stats'

class OcTCountry(BaseModel):
    pk_c_code = CharField(primary_key=True)
    s_name = CharField(index=True)
    s_slug = CharField(index=True)

    class Meta:
        db_table = 'oc_t_country'

class OcTRegion(BaseModel):
    b_active = IntegerField()
    fk_c_country_code = ForeignKeyField(db_column='fk_c_country_code', rel_model=OcTCountry, to_field='pk_c_code')
    pk_i = PrimaryKeyField(db_column='pk_i_id')
    s_name = CharField(index=True)
    s_slug = CharField(index=True)

    class Meta:
        db_table = 'oc_t_region'

class OcTCity(BaseModel):
    b_active = IntegerField()
    fk_c_country_code = ForeignKeyField(db_column='fk_c_country_code', null=True, rel_model=OcTCountry, to_field='pk_c_code')
    fk_i_region = ForeignKeyField(db_column='fk_i_region_id', rel_model=OcTRegion, to_field='pk_i')
    pk_i = PrimaryKeyField(db_column='pk_i_id')
    s_name = CharField(index=True)
    s_slug = CharField(index=True)

    class Meta:
        db_table = 'oc_t_city'

class OcTCityArea(BaseModel):
    fk_i_city = ForeignKeyField(db_column='fk_i_city_id', rel_model=OcTCity, to_field='pk_i')
    pk_i = PrimaryKeyField(db_column='pk_i_id')
    s_name = CharField(index=True)

    class Meta:
        db_table = 'oc_t_city_area'

class OcTCityStats(BaseModel):
    fk_i_city = ForeignKeyField(db_column='fk_i_city_id', primary_key=True, rel_model=OcTCity, to_field='pk_i')
    i_num_items = IntegerField(index=True)

    class Meta:
        db_table = 'oc_t_city_stats'

class OcTCountryStats(BaseModel):
    fk_c_country_code = ForeignKeyField(db_column='fk_c_country_code', primary_key=True, rel_model=OcTCountry, to_field='pk_c_code')
    i_num_items = IntegerField(index=True)

    class Meta:
        db_table = 'oc_t_country_stats'

class OcTCron(BaseModel):
    d_last_exec = DateTimeField()
    d_next_exec = DateTimeField()
    e_type = CharField()

    class Meta:
        db_table = 'oc_t_cron'

class OcTCurrency(BaseModel):
    b_enabled = IntegerField()
    pk_c_code = CharField(primary_key=True)
    s_description = CharField(null=True)
    s_name = CharField(unique=True)

    class Meta:
        db_table = 'oc_t_currency'

class OcTUser(BaseModel):
    b_active = IntegerField()
    b_company = IntegerField()
    b_enabled = IntegerField()
    d_coord_lat = DecimalField(null=True)
    d_coord_long = DecimalField(null=True)
    dt_access_date = DateTimeField()
    dt_mod_date = DateTimeField(null=True)
    dt_reg_date = DateTimeField()
    fk_c_country_code = ForeignKeyField(db_column='fk_c_country_code', null=True, rel_model=OcTCountry, to_field='pk_c_code')
    fk_i_city_area = ForeignKeyField(db_column='fk_i_city_area_id', null=True, rel_model=OcTCityArea, to_field='pk_i')
    fk_i_city = ForeignKeyField(db_column='fk_i_city_id', null=True, rel_model=OcTCity, to_field='pk_i')
    fk_i_region = ForeignKeyField(db_column='fk_i_region_id', null=True, rel_model=OcTRegion, to_field='pk_i')
    i_comments = IntegerField(null=True)
    i_items = IntegerField(null=True)
    pk_i = PrimaryKeyField(db_column='pk_i_id')
    s_access_ip = CharField()
    s_address = CharField(null=True)
    s_city = CharField(null=True)
    s_city_area = CharField(null=True)
    s_country = CharField(null=True)
    s_email = CharField(unique=True)
    s_name = CharField(index=True)
    s_pass_code = CharField(null=True)
    s_pass_date = DateTimeField(null=True)
    s_pass_ip = CharField(null=True)
    s_password = CharField()
    s_phone_land = CharField(null=True)
    s_phone_mobile = CharField(null=True)
    s_region = CharField(null=True)
    s_secret = CharField(null=True)
    s_username = CharField(index=True)
    s_website = CharField(null=True)
    s_zip = CharField(null=True)

    class Meta:
        db_table = 'oc_t_user'

class OcTItem(BaseModel):
    b_active = IntegerField()
    b_enabled = IntegerField()
    b_premium = IntegerField(index=True)
    b_show_email = IntegerField(null=True)
    b_spam = IntegerField()
    dt_expiration = DateTimeField()
    dt_mod_date = DateTimeField(null=True)
    dt_pub_date = DateTimeField(index=True)
    f_price = FloatField(null=True)
    fk_c_currency_code = ForeignKeyField(db_column='fk_c_currency_code', null=True, rel_model=OcTCurrency, to_field='pk_c_code')
    fk_i_category = ForeignKeyField(db_column='fk_i_category_id', rel_model=OcTCategory, to_field='pk_i')
    fk_i_user = ForeignKeyField(db_column='fk_i_user_id', null=True, rel_model=OcTUser, to_field='pk_i')
    i_price = BigIntegerField(index=True, null=True)
    pk_i = PrimaryKeyField(db_column='pk_i_id')
    s_contact_email = CharField(index=True)
    s_contact_name = CharField(null=True)
    s_ip = CharField()
    s_secret = CharField(null=True)

    class Meta:
        db_table = 'oc_t_item'

class OcTItemComment(BaseModel):
    b_active = IntegerField()
    b_enabled = IntegerField()
    b_spam = IntegerField()
    dt_pub_date = DateTimeField()
    fk_i_item = ForeignKeyField(db_column='fk_i_item_id', rel_model=OcTItem, to_field='pk_i')
    fk_i_user = ForeignKeyField(db_column='fk_i_user_id', null=True, rel_model=OcTUser, to_field='pk_i')
    pk_i = PrimaryKeyField(db_column='pk_i_id')
    s_author_email = CharField()
    s_author_name = CharField()
    s_body = TextField()
    s_title = CharField()

    class Meta:
        db_table = 'oc_t_item_comment'

class OcTItemDescription(BaseModel):
    fk_c_locale_code = CharField()
    fk_i_item = IntegerField(db_column='fk_i_item_id')
    s_description = TextField()
    s_title = CharField()

    class Meta:
        db_table = 'oc_t_item_description'
        indexes = (
            (('fk_i_item', 'fk_c_locale_code'), True),
            (('s_description', 's_title'), False),
        )
        primary_key = CompositeKey('fk_c_locale_code', 'fk_i_item')

class OcTItemLocation(BaseModel):
    d_coord_lat = DecimalField(null=True)
    d_coord_long = DecimalField(null=True)
    fk_c_country_code = ForeignKeyField(db_column='fk_c_country_code', null=True, rel_model=OcTCountry, to_field='pk_c_code')
    fk_i_city_area = ForeignKeyField(db_column='fk_i_city_area_id', null=True, rel_model=OcTCityArea, to_field='pk_i')
    fk_i_city = ForeignKeyField(db_column='fk_i_city_id', null=True, rel_model=OcTCity, to_field='pk_i')
    fk_i_item = ForeignKeyField(db_column='fk_i_item_id', primary_key=True, rel_model=OcTItem, to_field='pk_i')
    fk_i_region = ForeignKeyField(db_column='fk_i_region_id', null=True, rel_model=OcTRegion, to_field='pk_i')
    s_address = CharField(null=True)
    s_city = CharField(null=True)
    s_city_area = CharField(null=True)
    s_country = CharField(null=True)
    s_region = CharField(null=True)
    s_zip = CharField(null=True)

    class Meta:
        db_table = 'oc_t_item_location'

class OcTMetaFields(BaseModel):
    b_required = IntegerField()
    b_searchable = IntegerField()
    e_type = CharField()
    pk_i = PrimaryKeyField(db_column='pk_i_id')
    s_name = CharField()
    s_options = CharField(null=True)
    s_slug = CharField()

    class Meta:
        db_table = 'oc_t_meta_fields'

class OcTItemMeta(BaseModel):
    fk_i_field = ForeignKeyField(db_column='fk_i_field_id', rel_model=OcTMetaFields, to_field='pk_i')
    fk_i_item = ForeignKeyField(db_column='fk_i_item_id', rel_model=OcTItem, to_field='pk_i')
    s_multi = CharField()
    s_value = TextField(index=True, null=True)

    class Meta:
        db_table = 'oc_t_item_meta'
        indexes = (
            (('fk_i_item', 'fk_i_field', 's_multi'), True),
        )
        primary_key = CompositeKey('fk_i_field', 'fk_i_item', 's_multi')

class OcTItemResource(BaseModel):
    fk_i_item = ForeignKeyField(db_column='fk_i_item_id', rel_model=OcTItem, to_field='pk_i')
    pk_i = PrimaryKeyField(db_column='pk_i_id')
    s_content_type = CharField(null=True)
    s_extension = CharField(null=True)
    s_name = CharField(null=True)
    s_path = CharField(null=True)

    class Meta:
        db_table = 'oc_t_item_resource'
        indexes = (
            (('pk_i', 's_content_type'), False),
        )

class OcTItemStats(BaseModel):
    dt_date = DateField()
    fk_i_item = ForeignKeyField(db_column='fk_i_item_id', rel_model=OcTItem, to_field='pk_i')
    i_num_bad_classified = IntegerField()
    i_num_expired = IntegerField()
    i_num_offensive = IntegerField()
    i_num_premium_views = IntegerField()
    i_num_repeated = IntegerField()
    i_num_spam = IntegerField()
    i_num_views = IntegerField()

    class Meta:
        db_table = 'oc_t_item_stats'
        indexes = (
            (('dt_date', 'fk_i_item'), False),
            (('fk_i_item', 'dt_date'), True),
        )
        primary_key = CompositeKey('dt_date', 'fk_i_item')

class OcTKeywords(BaseModel):
    fk_c_locale_code = ForeignKeyField(db_column='fk_c_locale_code', rel_model=OcTLocale, to_field='pk_c_code')
    fk_i_category = ForeignKeyField(db_column='fk_i_category_id', null=True, rel_model=OcTCategory, to_field='pk_i')
    fk_i_city = ForeignKeyField(db_column='fk_i_city_id', null=True, rel_model=OcTCity, to_field='pk_i')
    s_anchor_text = CharField()
    s_md5 = CharField()
    s_normalized_text = CharField()
    s_original_text = CharField()

    class Meta:
        db_table = 'oc_t_keywords'
        indexes = (
            (('s_md5', 'fk_c_locale_code'), True),
        )
        primary_key = CompositeKey('fk_c_locale_code', 's_md5')

class OcTLatestSearches(BaseModel):
    d_date = DateTimeField()
    s_search = CharField()

    class Meta:
        db_table = 'oc_t_latest_searches'

class OcTLocationsTmp(BaseModel):
    e_type = CharField()
    id_location = CharField()

    class Meta:
        db_table = 'oc_t_locations_tmp'
        indexes = (
            (('id_location', 'e_type'), True),
        )
        primary_key = CompositeKey('e_type', 'id_location')

class OcTLog(BaseModel):
    dt_date = DateTimeField()
    fk_i = IntegerField(db_column='fk_i_id')
    fk_i_who = IntegerField(db_column='fk_i_who_id')
    s_action = CharField()
    s_data = CharField()
    s_ip = CharField()
    s_section = CharField()
    s_who = CharField()

    class Meta:
        db_table = 'oc_t_log'

class OcTMetaCategories(BaseModel):
    fk_i_category = ForeignKeyField(db_column='fk_i_category_id', rel_model=OcTCategory, to_field='pk_i')
    fk_i_field = ForeignKeyField(db_column='fk_i_field_id', rel_model=OcTMetaFields, to_field='pk_i')

    class Meta:
        db_table = 'oc_t_meta_categories'
        indexes = (
            (('fk_i_category', 'fk_i_field'), True),
        )
        primary_key = CompositeKey('fk_i_category', 'fk_i_field')

class OcTPages(BaseModel):
    b_indelible = IntegerField()
    b_link = IntegerField()
    dt_mod_date = DateTimeField(null=True)
    dt_pub_date = DateTimeField()
    i_order = IntegerField()
    pk_i = PrimaryKeyField(db_column='pk_i_id')
    s_internal_name = CharField(null=True)
    s_meta = TextField(null=True)

    class Meta:
        db_table = 'oc_t_pages'

class OcTPagesDescription(BaseModel):
    fk_c_locale_code = ForeignKeyField(db_column='fk_c_locale_code', rel_model=OcTLocale, to_field='pk_c_code')
    fk_i_pages = ForeignKeyField(db_column='fk_i_pages_id', rel_model=OcTPages, to_field='pk_i')
    s_text = TextField(null=True)
    s_title = CharField()

    class Meta:
        db_table = 'oc_t_pages_description'
        indexes = (
            (('fk_i_pages', 'fk_c_locale_code'), True),
        )
        primary_key = CompositeKey('fk_c_locale_code', 'fk_i_pages')

class OcTPluginCategory(BaseModel):
    fk_i_category = ForeignKeyField(db_column='fk_i_category_id', rel_model=OcTCategory, to_field='pk_i')
    s_plugin_name = CharField()

    class Meta:
        db_table = 'oc_t_plugin_category'

class OcTPreference(BaseModel):
    e_type = CharField()
    s_name = CharField()
    s_section = CharField()
    s_value = TextField()

    class Meta:
        db_table = 'oc_t_preference'
        indexes = (
            (('s_section', 's_name'), True),
        )
        primary_key = CompositeKey('s_name');

class OcTRegionStats(BaseModel):
    fk_i_region = ForeignKeyField(db_column='fk_i_region_id', primary_key=True, rel_model=OcTRegion, to_field='pk_i')
    i_num_items = IntegerField(index=True)

    class Meta:
        db_table = 'oc_t_region_stats'

class OcTUserDescription(BaseModel):
    fk_c_locale_code = ForeignKeyField(db_column='fk_c_locale_code', rel_model=OcTLocale, to_field='pk_c_code')
    fk_i_user = ForeignKeyField(db_column='fk_i_user_id', rel_model=OcTUser, to_field='pk_i')
    s_info = TextField(null=True)

    class Meta:
        db_table = 'oc_t_user_description'
        indexes = (
            (('fk_i_user', 'fk_c_locale_code'), True),
        )
        primary_key = CompositeKey('fk_c_locale_code', 'fk_i_user')

class OcTUserEmailTmp(BaseModel):
    dt_date = DateTimeField()
    fk_i_user = ForeignKeyField(db_column='fk_i_user_id', primary_key=True, rel_model=OcTUser, to_field='pk_i')
    s_new_email = CharField()

    class Meta:
        db_table = 'oc_t_user_email_tmp'

class OcTWidget(BaseModel):
    e_kind = CharField()
    pk_i = PrimaryKeyField(db_column='pk_i_id')
    s_content = TextField()
    s_description = CharField()
    s_location = CharField()

    class Meta:
        db_table = 'oc_t_widget'

