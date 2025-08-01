from autowsgr.fight.event.event_2025_0710 import EventFightPlan20250710
from autowsgr.scripts.main import start_script


timer = start_script("./user_settings.yaml")
# set_support(timer,True) # 如果要在战斗前开启战役支援请取消这一行的注释
plan = EventFightPlan20250710(
    timer,
    plan_path="E9AC夜战",
    fleet_id=2,
)  # 修改E9AC夜战为相对于的plan，详细的plan名可在data/plans/event/20250710查看，fleet_id为出击编队


plan.run_for_times(
    500,
)  # 第一个参数是战斗次数,还有个可选参数为检查远征时间，默认为1800S
