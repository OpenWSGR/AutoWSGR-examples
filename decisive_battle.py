import os
from autowsgr.fight import DecisiveBattle
from autowsgr.scripts.main import start_script

#实现决战的自动化
timer = start_script(f"{os.path.dirname(os.path.abspath(__file__))}/user_settings.yaml")
decisive_battle = DecisiveBattle(
    timer,
    6,
    1,
    "A",
    level1=["肥鱼", "U-1206", "U-47", "射水鱼", "U-96", "U-1405"],
    level2=["U-81", "大青花鱼"],
    flagship_priority=["U-1405", "U-47"],
    repair_level=1 , #维修策略，1为中破修，2为大破修
)
decisive_battle.run_for_times(20) # 数字为决战出击的次数