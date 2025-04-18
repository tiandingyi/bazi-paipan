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

        
    return result