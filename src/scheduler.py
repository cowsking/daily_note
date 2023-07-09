from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from src.history import notes
from src.utils.dailyReport import get_daily_report
from src.utils.toNotion import save_to_notion
# 定义定时任务
def clear_history():
    if notes:
        report = get_daily_report()['choices'][0]['message']['content']
        save = save_to_notion(datetime.now().date(), report)
        notes.clear()
    
    

# 创建后台调度器
scheduler = BackgroundScheduler()

# 添加定时任务，每天11:30执行
scheduler.add_job(clear_history, 'cron', hour=23, minute=30)

