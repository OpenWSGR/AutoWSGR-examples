from autowsgr.fight.event.event_2025_0424 import EventFightPlan2025_0424
from autowsgr.scripts.main import start_script

timer = start_script()

# E1 炸鱼, 替换成你自己电脑上的绝对路径
e1_plan = EventFightPlan2025_0424(timer, r'C:\Users\huany\Desktop\Projects\Auto-WSGR-dev\AutoWSGR\examples\plans\event\20250424\E1炸鱼.yaml')
e1_plan.run_for_times(200)

# E2 战术
# e2_plan = EventFightPlan2025_0424(timer, r'C:\Users\huany\Desktop\Projects\Auto-WSGR-dev\AutoWSGR\examples\plans\event\20250424\E2战术.yaml') 
# e2_plan.run_for_times(10)
