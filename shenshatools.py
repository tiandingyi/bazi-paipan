# 神煞相关的方法
from shensha_data import *

def get_shensha(sizhu, ganzhi):
    """
    计算八字对特定干支的神煞
    
    Args:
        sizhu: 四柱八字列表，格式如[('乙', '亥'), ('丙', '子'), ('庚', '寅'), ('丁', '未')]
        ganzhi: 待判断的干支，格式如('乙', '亥')
    
    Returns:
        list: 返回神煞列表
    """
    
    result = []
    year_gan_zhi = sizhu[0]  # 获取年柱
    month_gan_zhi = sizhu[1]  # 获取月柱
    day_gan_zhi = sizhu[2]  # 获取日柱

    year_kongwang = kongwangs[sizhu[0]] # 年空亡
    day_kongwang = kongwangs[sizhu[2]] # 日空亡

    
    # 判断天乙贵人
    if ganzhi[1] in tianyis[year_gan_zhi[0]]:
        result.append("年天乙贵人")
    if ganzhi[1] in tianyis[day_gan_zhi[0]]:
        result.append("日天乙贵人")

    # 判断玉堂贵人
    if ganzhi[1] in yutangs[year_gan_zhi[0]]:
        result.append("年玉堂贵人")
    if ganzhi[1] in yutangs[day_gan_zhi[0]]:
        result.append("日玉堂贵人")
    
    # 判断天月德贵人
    if ganzhi[0] in tiandes[month_gan_zhi[1]]:
        result.append("天德贵人")
    if ganzhi[1] in tiandes[month_gan_zhi[1]]:
        result.append("天德贵人")
    if ganzhi[0] in yuedes[month_gan_zhi[1]]:
        result.append("月德贵人")
    if ganzhi[1] in yuedes[month_gan_zhi[1]]:
        result.append("月德贵人")

    # 判断孤辰
    if ganzhi[1] in guchens[year_gan_zhi[1]]:
        result.append("年孤辰")
    if ganzhi[1] in guchens[day_gan_zhi[1]]:
        result.append("日孤辰")

    # 判断寡宿
    if ganzhi[1] in guasus[year_gan_zhi[1]]:
        result.append("年寡宿")
    if ganzhi[1] in guasus[day_gan_zhi[1]]:
        result.append("日寡宿")

    # 判断文昌
    if ganzhi[1] in wenchangs[year_gan_zhi[0]]:
        result.append("年文昌")
    if ganzhi[1] in wenchangs[day_gan_zhi[0]]:
        result.append("日文昌")
    
    # 判断阳刃
    if ganzhi[1] in yangrens[year_gan_zhi[0]]:
        result.append("年阳刃")
    if ganzhi[1] in yangrens[day_gan_zhi[0]]:
        result.append("日阳刃")

    # 判断飞刃
    if ganzhi[1] in feirens[year_gan_zhi[0]]:
        result.append("年飞刃")
    if ganzhi[1] in feirens[day_gan_zhi[0]]:
        result.append("日飞刃")

    # 判断红艳
    if ganzhi[1] in hongyans[year_gan_zhi[0]]:
        result.append("年红艳煞")
    if ganzhi[1] in hongyans[day_gan_zhi[0]]:
        result.append("日红艳煞")
    
    # 判断将星
    if ganzhi[1] in jiangxings[year_gan_zhi[1]]:
        result.append("年将星")
    if ganzhi[1] in jiangxings[day_gan_zhi[1]]:
        result.append("日将星")

    # 判断华盖
    if ganzhi[1] in huagais[year_gan_zhi[1]]:
        result.append("年华盖")
    if ganzhi[1] in huagais[day_gan_zhi[1]]:
        result.append("日华盖")

    # 判断驿马
    if ganzhi[1] in yimas[year_gan_zhi[1]]:
        result.append("年驿马")
    if ganzhi[1] in yimas[day_gan_zhi[1]]:
        result.append("日驿马")

    # 判断劫煞
    if ganzhi[1] in jieshas[year_gan_zhi[1]]:
        result.append("年劫煞")
    if ganzhi[1] in jieshas[day_gan_zhi[1]]:
        result.append("日劫煞")

    # 判断亡神
    if ganzhi[1] in wangshens[year_gan_zhi[1]]:
        result.append("年亡神")
    if ganzhi[1] in wangshens[day_gan_zhi[1]]:
        result.append("日亡神")

    # 判断桃花
    if ganzhi[1] in taohuas[year_gan_zhi[1]]:
        result.append("年桃花")
    if ganzhi[1] in taohuas[day_gan_zhi[1]]:
        result.append("日桃花")

    # 判断天厨贵人
    if ganzhi[1] in tianchus[month_gan_zhi[0]]:
        result.append("年天厨贵人")
    
    # 判断天医
    if ganzhi[1] in tianyi[month_gan_zhi[1]]:
        result.append("月天医")

    # 判断卦气
    if ganzhi[1] in guaqis[year_gan_zhi[0]]:
        result.append("年卦气")
    if ganzhi[1] in guaqis[day_gan_zhi[0]]:
        result.append("日卦气")
    
    # 判断祿勋
    if ganzhi[1] in luxuns[year_gan_zhi[0]]:
        result.append("年祿勋")
    if ganzhi[1] in luxuns[day_gan_zhi[0]]:
        result.append("日祿勋")

    # 判断国印
    if ganzhi[1] in guoyins[year_gan_zhi[0]]:
        result.append("年国印")
    if ganzhi[1] in guoyins[day_gan_zhi[0]]:
        result.append("日国印")
    
    # 判断空亡
    if ganzhi[1] in year_kongwang:
        result.append("年空亡")
    if ganzhi[1] in day_kongwang:
        result.append("日空亡")

    # 判断阴差阳错
    if ganzhi in yinchayangcuo_list:
        result.append("阴差阳错")

    # 判断金舆
    if ganzhi[1] in jin_yu_dict[year_gan_zhi[0]]:
        result.append("年金舆")
    if ganzhi[1] in jin_yu_dict[day_gan_zhi[0]]:
        result.append("日金舆")

    # 红鸾
    if ganzhi[1] in hongluan_dict[year_gan_zhi[1]]:
        result.append("年红鸾")
    if ganzhi[1] in hongluan_dict[day_gan_zhi[1]]:
        result.append("日红鸾")

    # 天喜
    if ganzhi[1] in tianxi_dict[year_gan_zhi[1]]:
        result.append("年天喜")
    if ganzhi[1] in tianxi_dict[day_gan_zhi[1]]:
        result.append("日天喜")

    # 丧门
    if ganzhi[1] in sangmen_dict[year_gan_zhi[1]]:
        result.append("年丧门")

    # 吊客
    if ganzhi[1] in diaoke_dict[year_gan_zhi[1]]:
        result.append("年吊客")

    # 大耗
    if ganzhi[1] in dahao_dict[year_gan_zhi[1]]:
        result.append("年大耗")

    # 小耗
    if ganzhi[1] in xiaohao_dict[year_gan_zhi[1]]:
        result.append("年小耗")

    # 病符
    if ganzhi[1] in bingfu_dict[year_gan_zhi[1]]:
        result.append("年病符")

    # 死符
    if ganzhi[1] in sifu_dict[year_gan_zhi[1]]:
        result.append("年死符")

    # 官符
    if ganzhi[1] in guanfu_dict[year_gan_zhi[1]]:
        result.append("年官符/五鬼")
    
    # 旌德煞
    if ganzhi[0] in jingde_year_dict[year_gan_zhi[1]]:
        result.append("年旌德煞")

    # 旌钺煞
    if ganzhi[1] in jingyue_dict[year_gan_zhi[1]]:
        result.append("年旌钺煞")

    # 血支
    if ganzhi[1] in xuezhi_dict[year_gan_zhi[1]]:
        result.append("年血支")

    # 血刃
    if ganzhi[1] in xueren_dict[month_gan_zhi[1]]:
        result.append("月血刃")
    
    # 流霞
    if ganzhi[1] in liuxia_dict[day_gan_zhi[0]]:
        result.append("日流霞")

    # 福星贵人
    if ganzhi[1] in fuxing_dict[day_gan_zhi[0]]:
        result.append("日福星贵人")

    # 自缢煞
    if ganzhi[1] in ziyi_dict[year_gan_zhi[1]]:
        result.append("年自缢煞")
    if ganzhi[1] in ziyi_dict[day_gan_zhi[1]]:
        result.append("日自缢煞")
    

    return result