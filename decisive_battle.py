from autowsgr.scripts.main import start_script

timer = start_script('./user_settings.yaml')
timer.run_decisive_battle(1)  # 数字为决战出击的次数
