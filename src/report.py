from flask import Blueprint, request
import requests
from datetime import datetime
from src.utils.dailyReport import get_daily_report
from src.utils.toNotion import save_to_notion
from src.history import notes
report = Blueprint('report', __name__, url_prefix="/report")
@report.get('/daily')
def generate_daily_report():
    report = get_daily_report()['choices'][0]['message']['content']
    save = save_to_notion(datetime.now().date(), report)
    return save

@report.get('/delete')
def delete_history():
    notes.clear()
    return "delete notes"
        

