import secret_var, random
URL = secret_var.URL
#QUERY = 'q=mods_abstract_mt%3A*'
QUERY = 'q=dc.title%3A*'
SUB_QUERY = 'q=dc.subject%3A'
SUBJECT = 'louisiana'
#QUERY = 'q=dc.title%3Atugboat'
#QUERY = 'q=dc.title%3Aschooner'
#QUERY = 'q=mods_subject_topic_mt%3Agoats'
#QUERY = 'q=mods_subject_topic_ms%3A%22Louisiana%22'
#&fl=PID%2C+mods_titleInfo_title_ms&wt=json&indent=true&row=1
#QUERY = 'q=goat'

# NOT = '+AND+NOT+'
#QUERY =QUERY + NOT

REQ = '+AND+RELS_EXT_hasModel_uri_ms%3A%22info%3Afedora%2Fislandora%3Asp_large_image_cmodel%22&fl=PID%2C+dc.description+mods_titleInfo_title_ms+mods_abstract_mt&wt=json&indent=true'
ROW = '&row=100'
START = '&start='
RAND = str(random.randint(0, 239379))

S_RAND = str(random.randint(0, 1000))

SOLR_DATA  = URL + QUERY + REQ + ROW + START + RAND

SUBJECT_SOLR_DATA = URL + SUB_QUERY + SUBJECT + REQ + START + S_RAND

print(SOLR_DATA)
