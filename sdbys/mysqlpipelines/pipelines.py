from .sql import Sql
from sdbys.items import SdbysItem


class SdbysPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, SdbysItem):
            guid = item['guid']
            ret = Sql.select_guid(guid)
            # 去重
            if ret[0] == 1:
                print('已经存在了')
                pass
            else:
                name = item['name']
                xueli = item['xueli']
                zhuanye = item['zhuanye']
                school = item['school']
                year = item['year']
                sex = item['sex']
                time = item['time']
                guid = item['guid']
                Sql.insert_sdbys(name, xueli, zhuanye, school, year, sex, time, guid)
                print('成功存储 '+name)
