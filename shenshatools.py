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
        print(ganzhi[1] + "ganzhi")
        print(tianyis[year_gan_zhi[0]] + "tianyinian")
        result.append("年天乙贵人")
    if ganzhi[1] in tianyis[day_gan_zhi[0]]:
        result.append("日天乙贵人")

    # 判断玉堂贵人
    if ganzhi[1] in yutangs[year_gan_zhi[0]]:
        result.append("年玉堂贵人")
    if ganzhi[1] in yutangs[day_gan_zhi[0]]:
        result.append("日玉堂贵人")
        
    return result