#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections
from bidict import bidict

from ganzhi import *

nayins = {
    ('甲', '子'): '海中金', ('乙', '丑'): '海中金', ('壬', '寅'): '金泊金', ('癸', '卯'): '金泊金',
    ('庚', '辰'): '白蜡金', ('辛', '巳'): '白蜡金', ('甲', '午'): '砂中金', ('乙', '未'): '砂中金',
    ('壬', '申'): '剑锋金', ('癸', '酉'): '剑锋金', ('庚', '戌'): '钗钏金', ('辛', '亥'): '钗钏金',
    ('戊', '子'): '霹雳火', ('己', '丑'): '霹雳火', ('丙', '寅'): '炉中火', ('丁', '卯'): '炉中火',
    ('甲', '辰'): '覆灯火', ('乙', '巳'): '覆灯火', ('戊', '午'): '天上火', ('己', '未'): '天上火',
    ('丙', '申'): '山下火', ('丁', '酉'): '山下火', ('甲', '戌'): '山头火', ('乙', '亥'): '山头火',
    ('壬', '子'): '桑柘木', ('癸', '丑'): '桑柘木', ('庚', '寅'): '松柏木', ('辛', '卯'): '松柏木',
    ('戊', '辰'): '大林木', ('己', '巳'): '大林木', ('壬', '午'): '杨柳木', ('癸', '未'): '杨柳木',
    ('庚', '申'): '石榴木', ('辛', '酉'): '石榴木', ('戊', '戌'): '平地木', ('己', '亥'): '平地木',
    ('庚', '子'): '壁上土', ('辛', '丑'): '壁上土', ('戊', '寅'): '城头土', ('己', '卯'): '城头土',
    ('丙', '辰'): '砂中土', ('丁', '巳'): '砂中土', ('庚', '午'): '路旁土', ('辛', '未'): '路旁土',
    ('戊', '申'): '大驿土', ('己', '酉'): '大驿土', ('丙', '戌'): '屋上土', ('丁', '亥'): '屋上土',
    ('丙', '子'): '涧下水', ('丁', '丑'): '涧下水', ('甲', '寅'): '大溪水', ('乙', '卯'): '大溪水',
    ('壬', '辰'): '长流水', ('癸', '巳'): '长流水', ('丙', '午'): '天河水', ('丁', '未'): '天河水',
    ('甲', '申'): '井泉水', ('乙', '酉'): '井泉水', ('壬', '戌'): '大海水', ('癸', '亥'): '大海水',    
}

empties = {
    ('甲', '子'): ('戌','亥'), ('乙', '丑'):('戌','亥'), 
    ('丙', '寅'): ('戌','亥'), ('丁', '卯'): ('戌','亥'), 
    ('戊', '辰'): ('戌','亥'), ('己', '巳'): ('戌','亥'),
    ('庚', '午'): ('戌','亥'), ('辛', '未'): ('戌','亥'),
    ('壬', '申'): ('戌','亥'), ('癸', '酉'): ('戌','亥'),

    ('甲', '戌'): ('申','酉'), ('乙', '亥'): ('申','酉'),
    ('丙', '子'): ('申','酉'), ('丁', '丑'): ('申','酉'),
    ('戊', '寅'): ('申','酉'), ('己', '卯'): ('申','酉'),
    ('庚', '辰'):('申','酉'), ('辛', '巳'): ('申','酉'),
    ('壬', '午'): ('申','酉'), ('癸', '未'): ('申','酉'),

    ('甲', '申'): ('午','未'), ('乙', '酉'): ('午','未'),
    ('丙', '戌'): ('午','未'), ('丁', '亥'): ('午','未'),
    ('戊', '子'): ('午','未'), ('己', '丑'): ('午','未'), 
    ('庚', '寅'): ('午','未'), ('辛', '卯'): ('午','未'),
    ('壬', '辰'): ('午','未'), ('癸', '巳'): ('午','未'),

    ('甲', '午'): ('辰','己'), ('乙', '未'): ('辰','己'),
    ('丙', '申'): ('辰','己'), ('丁', '酉'): ('辰','己'),
    ('戊', '戌'): ('辰','己'), ('己', '亥'): ('辰','己'),
    ('庚', '子'): ('辰','己'), ('辛', '丑'): ('辰','己'),
    ('壬', '寅'): ('辰','己'), ('癸', '卯'): ('辰','己'),

    ('甲', '辰'): ('寅','卯'), ('乙', '巳'): ('寅','卯'),
    ('丙', '午'): ('寅','卯'), ('丁', '未'): ('寅','卯'),
    ('戊', '申'): ('寅','卯'), ('己', '酉'): ('寅','卯'),
    ('庚', '戌'): ('寅','卯'), ('辛', '亥'): ('寅','卯'),
    ('壬', '子'): ('寅','卯'), ('癸', '丑'): ('寅','卯'), 


    ('甲', '寅'): ('子','丑'), ('乙', '卯'): ('子','丑'),     
    ('丙', '辰'): ('子','丑'), ('丁', '巳'): ('子','丑'), 
    ('戊', '午'): ('子','丑'), ('己', '未'): ('子','丑'),
    ('庚', '申'): ('子','丑'), ('辛', '酉'): ('子','丑'), 
    ('壬', '戌'): ('子','丑'), ('癸', '亥'): ('子','丑'),    
}


emptie4s = {
    ('甲', '子'): '水', ('乙', '丑'):'水', 
    ('丙', '寅'): '水', ('丁', '卯'): '水', 
    ('戊', '辰'):  '水', ('己', '巳'):  '水',
    ('庚', '午'):  '水', ('辛', '未'):  '水',
    ('壬', '申'):  '水', ('癸', '酉'):  '水',

    ('甲', '申'):  '金', ('乙', '酉'):  '金',
    ('丙', '戌'):  '金', ('丁', '亥'):  '金',
    ('戊', '子'):  '金', ('己', '丑'):  '金', 
    ('庚', '寅'):  '金', ('辛', '卯'):  '金',
    ('壬', '辰'):  '金', ('癸', '巳'):  '金',

    ('甲', '午'):  '水', ('乙', '未'):  '水',
    ('丙', '申'):  '水', ('丁', '酉'):  '水',
    ('戊', '戌'):  '水', ('己', '亥'):  '水',
    ('庚', '子'):  '水', ('辛', '丑'):  '水',
    ('壬', '寅'):  '水', ('癸', '卯'):  '水',


    ('甲', '寅'):  '金', ('乙', '卯'):  '金',     
    ('丙', '辰'):  '金', ('丁', '巳'):  '金', 
    ('戊', '午'):  '金', ('己', '未'):  '金',
    ('庚', '申'):  '金', ('辛', '酉'):  '金', 
    ('壬', '戌'):  '金', ('癸', '亥'):  '金',    
}

minggongs = {
    "子": "天贵星、志气不凡、富裕清吉。",
    "丑": "天厄星、先难后吉、离祖劳心、晚年吉。",
    "寅": "天权星、聪明大器、中年有权柄。",
    "卯": "天赦星、慷慨疏财、得权时须谦逊。",
    "辰": "天如星、事多翻覆、机谋多能。",
    "巳": "天文星、文章振发、女命有好夫。",
    "午": "天福星、荣华吉命。",
    "未": "天驿星、一生劳碌、离祖始安。",
    "申": "天孤星、不宜早婚、女命妨夫。",
    "酉": "天秘星、性情刚直、时有是非。",
    "戌": "天艺星、心性平和、艺道有名。",
    "亥": "天寿星、心慈明悟、克己助人。",

}

rizhus = {
	"甲子": "虽坐沐浴，若四往有禄，看印，冬生不作妻败", 
	"乙丑": "身坐财官，有乙庚合最吉", 
	"丙寅": "金绝水死，财官俱背，但丙火长生食神独旺，主有寿，己亥、辛卯、癸巳时贵", 
	"丁卯": "财官俱背，须合气、禄、火扶", 
	"戊辰": "壬庚入墓，乙木自坐财官", 
	"己巳": "水绝木病，丙寅时贵", 
	"庚午": "庚金坐死但午上自坐官、印，虽败不困", 
	"辛未": "身旺，丙申时贵", 
	"壬申": "水辰生位，聪明秀丽", 
	"癸酉": "财官无气，要用旺者吉", 
	"甲戌": "身坐旺官，临火库，心怀慈善，丙寅时贵", 
	"乙亥": "日坐木局，丙壬、壬午、甲申时贵", 
	"丙子": "身坐财啊．癸巳时", 
	"丁丑": "金库荣丰，见辛亥时贵", 
	"戊寅": "甲木当局，官杀者吉", 
	"己卯": "身坐杀地，须身杀力停者吉",
	"庚辰": "魁罡，忌于刑冲", 
	"辛巳": "金局坐死不妨，戊子时贵", 
	"壬午": "财官双美，伶俐有谋，壬寅时贵", 
	"癸未": "身坐杀位须身力二停", 
	"甲申": "坐绝，四柱俱绝者吉", 
	"乙酉": "坐杀四乙酉或有化杀则吉，辛巳时，为化气金局贵", 
	"丙戌": "夏生则财官无气", 
	"丁亥": "日贵，壬寅时，乙巳时皆贵", 
	"戊子": "自坐财，乙卯时，丁巳时贵", 
	"己丑": "有财无官，丙寅时贵", 
	"庚寅": "坐绝反主吉昌", 
	"辛卯": "财衰无妨，见戊子时贵", 
	"壬辰": "魁罡、不喜冲刑，遇建禄反卑", 
	"癸巳": "财官双美最吉祥，丁已时贵", 
	"甲午": "夏生大吉", 
	"乙未": "逢财伤官格", 
	"丙申": "身坐财，庚寅时贵，癸巳时亦吉", 
	"丁酉": "临财学精，壬寅时贵", 
	"戊戌": "魁罡，忌冲刑", 
	"己亥": "自坐财官得高名，丙寅时贵", 
	"庚子": "有丁火则吉", 
	"辛丑": "食神荣昌，主寿", 
	"壬寅": "水火既济，见壬寅时大吉", 
	"癸卯": "日贵，衰神旺吉", 
	"甲辰": "身坐财库水气，性善良，丙寅时吉", 
	"乙巳": "男女妨家室，有壬者轻", 
	"丙午": "日刃喜刑冲，男、女妨家室，见乙、癸者轻", 
	"丁未": "坐印小吉", 
	"戊申": "甲绝有财无官", 
	"己酉": "财禄一背，皆须生扶", 
	"庚戌": "魁罡，忌火旺地支之运及冲刑", 
	"辛亥": "财生，官绝", 
	"壬子": "日刃喜刑冲", 
	"癸丑": "喜冲不作灾论", 
	"甲寅": "财官二背，见辛未时贵", 
	"乙卯": "财官无气，见庚辰时贵", 
	"丙辰": "冬生不吉，庚寅时贵", 
	"丁巳": "男、女妨家室．有戊者重，甲、寅者轻", 
	"戊午": "日刃喜刑冲，四、五月在刑地亦吉", 
	"己未": "丙寅时贵（无水大吉）", 
	"庚申": "日德、日禄、寿", 
	"辛酉": "日禄、戊子、丙申时贵", 
	"壬戌": "元武当权．等作财官双美", 
	"癸亥": "得癸亥时夫贵", 
}

up_down_hes = (('戊','子'),('辛','巳'), ('壬','午'), ('丁','亥'))

lu_types = {
    "甲":{('丙','寅'):'福星禄 名位禄 吉', ('戊','寅'):'伏马禄 吉', 
           ('庚','寅'):'破禄，半吉半凶', ('壬','寅'):'正禄，带截路空亡，必为僧道 不吉',
           ('甲','寅'):'长生禄，大吉', ('乙','卯'):'生成禄，大吉',},
    "乙":{('乙','卯'):'喜神旺禄 吉', ('丁','卯'):'截路空亡 凶', 
           ('己','卯'):'进神禄 吉', ('辛','卯'):'破禄，又为交神，半吉半凶',
           ('癸','卯'):'死禄 虽贵终贫 凶',},
    "丙":{('己','巳'):'九天库禄 吉', ('辛','巳'):'截路空亡 凶', 
           ('乙','巳'):'旺马禄 吉', ('丁','巳'):'库禄 吉',
           ('癸','巳'):'伏贵神禄，半吉半凶',}, 
    "丁":{('庚','午'):'截路空亡 凶', ('壬','午'):'德合禄 吉', 
           ('甲','午'):'进神禄 吉', ('丙','午'):'喜神禄，交羊刃，半吉',
           ('戊','午'):'伏羊刃 禄，多凶',},   
    "戊":{('己','巳'):'九天库禄，吉', ('辛', '巳'):'截路空亡 凶', 
           ('癸','巳'):'贵神禄，戊癸化合，有官位重 吉', ('乙','巳'):'驿马同乡禄 吉',
           ('戊','巳'):'旺库禄 吉',},    
    "己":{('庚','午'):'截路空亡 凶', ('壬','午'):'死鬼禄 凶', 
           ('甲','午'):'进神合禄 显达之象 吉', ('丙','午'):'喜神禄 半吉',
           ('戊','午'):'伏神羊刃禄，凶',},  
    "庚":{('壬','申'):'大败禄 凶', ('甲', '申'):'截路空亡禄 凶', 
           ('丙','申'):'大败禄，多成败 半吉', ('戊','申'):'伏马禄，多滞，若值福星，贵吉',
           ('庚','申'):'长生禄，大吉',},      
    "辛":{('癸','酉'):'伏神禄，水火相犯，凶', ('乙','酉'):'破禄 成败 凶', 
           ('丁','酉'):'空亡贵神禄 丁木受气，辛水沐浴，主奸淫事；值喜神，吉。', 
           ('己','酉'):'进神禄 吉', ('辛','酉'):'正禄 吉',},    
    "壬":{('丁','亥'):'贵神合禄 吉', ('乙', '亥'):'天德禄 吉', 
           ('己','亥'):'旺禄 大吉', ('辛','亥'):'同马乡禄 大吉',
           ('癸','亥'):'大败禄，贫薄 凶',},     
    "癸":{('甲','子'):'进神禄，主登科进达 吉', ('丙','子'):'交羊刃禄，带福星，贵有权。 吉', 
           ('戊','子'):'伏羊刃合贵禄 半吉', 
           ('庚','印禄'):'进神禄 吉', ('壬','子'):'正羊刃禄，凶',},        
}


wenxing = {"甲":'午', "乙":"巳", "丙":"申", "丁":"酉", "戊":"申", "己":"酉", 
           "庚": "戌", "辛":"亥", "壬": "寅", "癸":"卯"}
tianyin =  {"甲":'寅',  "乙":"亥", "丙":"戌", "丁":"酉", "戊":"申", "己":"未", 
            "庚": "午", "辛":"巳", "壬": "辰", "癸":"卯"}
xuetangs = {'金':("辛","巳"), '木':("己","亥"), '水':("甲","申"), 
            '火':("丙", "寅"), '土':("戊","申")}



wangs = {"子":"亥", "丑":"申", "寅":"巳", "卯":"寅", "辰":"亥", "巳":"申", 
            "午":"巳", "未":"寅", "申":"亥", "酉":"申", "戌":"巳", "亥":"寅"}
jieshas = {"子":"巳", "丑":"寅", "寅":"亥", "卯":"申", "辰":"巳", "巳":"寅", 
         "午":"亥", "未":"申", "申":"巳", "酉":"寅", "戌":"亥", "亥":"申"}
            
ma_zhus =  {
    ("甲","申"):'截路空日马', ("丙","申"):'截路空日马', ("戊","申"):'福星伏马', 
    ("庚","申"):'逢天关马', ("壬","申"):'大败马', 
    ("甲","寅"):'正禄文星马', ("丙","寅"):'福星马', ("戊","寅"):'伏马', 
    ("庚","寅"):'破禄马', ("壬","寅"):'截路马',   
    ("乙","亥"):'天德马', ("丁","亥"):'天乙马', ("己","亥"):'旺禄马', 
    ("辛","亥"):'正禄马', ("癸","亥"):'大败马',     
    ("乙","巳"):'正禄马', ("丁","巳"):'旺气马', ("己","巳"):'九天禄库马', 
    ("辛","巳"):'截路马', ("癸","巳"):'天乙伏马',      
}   
    

day_shens = { 
    '将星':{"子":"子", "丑":"酉", "寅":"午", "卯":"卯", "辰":"子", "巳":"酉", 
              "午":"午", "未":"卯", "申":"子", "酉":"酉", "戌":"午", "亥":"卯"},      
    '华盖':{"子":"辰", "丑":"丑", "寅":"戌", "卯":"未", "辰":"辰", "巳":"丑", 
              "午":"戌", "未":"未", "申":"辰", "酉":"丑", "戌":"戌", "亥":"未"}, 
    '驿马': {"子":"寅", "丑":"亥", "寅":"申", "卯":"巳", "辰":"寅", "巳":"亥", 
            "午":"申", "未":"巳", "申":"寅", "酉":"亥", "戌":"申", "亥":"巳"},
    '劫煞': {"子":"巳", "丑":"寅", "寅":"亥", "卯":"申", "辰":"巳", "巳":"寅", 
         "午":"亥", "未":"申", "申":"巳", "酉":"寅", "戌":"亥", "亥":"申"},
    '亡神': {"子":"亥", "丑":"申", "寅":"巳", "卯":"寅", "辰":"亥", "巳":"申", 
            "午":"巳", "未":"寅", "申":"亥", "酉":"申", "戌":"巳", "亥":"寅"},    
    '桃花': {"子":"酉", "丑":"午", "寅":"卯", "卯":"子", "辰":"酉", "巳":"午", 
            "午":"卯", "未":"子", "申":"酉", "酉":"午", "戌":"卯", "亥":"子"},        
}

g_shens = {
    '天乙':{"甲":'未丑',  "乙":"申子", "丙":"酉亥", "丁":"酉亥", "戊":'未丑', "己":"申子", 
            "庚": "未丑", "辛":"寅午", "壬": "卯巳", "癸":"卯巳"},
   
}

shens_infos = {
    '孤辰': "孤僻、孤独：月支容易不合群、容易30岁以后才结婚。女命官杀月干坐顾辰、独居概率大，时支则有阴道之心。",
    '寡宿': "类似孤辰，同柱有天月德没关系。男怕孤，女怕寡。",  
    '大耗': "意外破损，单独没关系。与桃花或驿马之类同柱则危险。",
    '天德': "先天有福，日干终生有福。忌讳冲克，不怕合。女命与夫星同干更佳。",
    '月德': "先天有福，日干终生有福。忌讳冲克，不怕合。女命与夫星同干更佳。",
    '将星': "有理想、气度、即从容不迫。",     
    '华盖': "有艺术、水准与命格相关。",
    '驿马': "多迁移、水准与命格相关。女驿马合贵人，终沦落风尘。",
    '劫煞': "与贵人同柱没关系、与亡神对冲。会三刑不佳，其他情况还好。为日主所克无大碍。",
    '亡神': "与贵人同柱没关系、与劫煞对冲。会三刑不佳，其他情况还好。为日主所克无大碍。",  
    '桃花': "凶居多、女正官坐桃花吉。", 
    '天乙': "后天解难、女命不适合多",
    '文昌': "诗书佳，未必有福，女命多参考李清照。",   
    '阳刃': "性格刚强，女命未必佳。",     
    '红艳': "爱得执著，不顾及地位差异。",  
}

siling =  {                                                
        "寅": "立春后戊土七日，丙火七日，甲木十六日 立春、雨水。",
        "卯": "惊蛰后甲木十日，乙木二十日。 惊蛰、春分。",
        "辰": "清明后乙木九日，癸水三日，戊土十八日。清明、谷雨。",   
        "巳": "立夏后戊土五日，庚金九日，丙火十六日。立夏、小满。",   
        "午": "芒种后丙火十日，己土九日，丁火十一日 芒种、夏至。 ",
        "未": "小暑后丁火九日，乙木三日，己土十八日。小暑、大署。 ",
        "申": "立秋后戊土十日，壬水三日，庚金十七日。立秋、处暑。",
        "酉": "白露后庚金十日，辛金二十日。 白露、秋分。",     
        "戌": "寒露后辛金九日，丁火三日，戊土十八日。寒露、霜降。",
        "亥": "立冬后戊土七日，甲木五日，壬水十八日。立冬、小雪。",
        "子": "大雪后壬水十日，癸水二十日。 大雪、冬至。",
        "丑": "小寒后癸水九日，辛金三日，己土十八日。小寒、大寒。",  
    }