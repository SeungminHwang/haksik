from urllib.request import *
from bs4 import BeautifulSoup
# load html content from url
kaimaru = "http://www.kaist.ac.kr/_prog/fodlst/index.php?site_dvs_cd=kr&menu_dvs_cd=050303&dvs_cd=fclt&stt_dt=2018-04-28&site_dvs="
west = "http://www.kaist.ac.kr/_prog/fodlst/index.php?site_dvs_cd=kr&menu_dvs_cd=050303&dvs_cd=west&stt_dt=2018-04-28&site_dvs="
east1 = "http://www.kaist.ac.kr/_prog/fodlst/index.php?site_dvs_cd=kr&menu_dvs_cd=050303&dvs_cd=east1&stt_dt=2018-04-28&site_dvs="
east2 = "http://www.kaist.ac.kr/_prog/fodlst/index.php?site_dvs_cd=kr&menu_dvs_cd=050303&dvs_cd=east2&stt_dt=2018-04-28&site_dvs="
prof = "http://www.kaist.ac.kr/_prog/fodlst/index.php?site_dvs_cd=kr&menu_dvs_cd=050303&dvs_cd=emp&stt_dt=2018-04-28&site_dvs="



url_kaist_fodlst = "http://www.kaist.ac.kr/_prog/fodlst/index.php"
url_reader = urlopen(url_kaist_fodlst)
html_content = url_reader.read()

food_dict = {}


# crawl food table
html_crawler = BeautifulSoup(html_content, "lxml")
food_table = html_crawler.table
table_list = food_table.find_all('td')

breakfast = table_list[0]
lunch = table_list[1]
dinner = table_list[2]
food_dict = {'breakfast': breakfast, 'lunch': lunch, 'dinner': dinner}

def get_food_table(target) :
    global food_dict
    return food_dict