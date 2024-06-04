from flask import Flask, jsonify
import datetime

from data_fetch import main_getdata

from data_fetch import get_stock_eastmoney_concept
from data_fetch import get_stock_eastmoney_industry

app = Flask(__name__)


#每日取数批了
@app.route('/api/getDataByDate/run', methods=['GET','POST'])
def get_data_by_date_task():


    current_date = datetime.datetime.now().__str__() + "\n"
    response_data = {'message': 'success' }
    with open('scheduler_log', 'a') as file:
        file.write('Scheduling successful,starting get data in '+ current_date)  # 将追加的内容写入文件

    main_getdata.get_data_by_date()

    current_date = datetime.datetime.now().__str__() + "\n"
    with open('scheduler_log', 'a') as file:
        file.write('get over in '+ current_date)  # 将追加的内容写入文件

    return jsonify(response_data)

#获得股票所属概念数据
@app.route('/api/getConceptData/run', methods=['GET','POST'])
def get_data_concept_data_task():
    current_date = datetime.datetime.now().__str__() + "\n"
    response_data = {'message': 'success' }
    with open('scheduler_log', 'a') as file:
        file.write('Scheduling successful,starting get concept data in '+ current_date)  # 将追加的内容写入文件

    get_stock_eastmoney_concept.get_all_stock_eastmoney_concept()

    current_date = datetime.datetime.now().__str__() + "\n"
    with open('scheduler_log', 'a') as file:
        file.write('get concept data over in '+ current_date)  # 将追加的内容写入文件

    return jsonify(response_data)

#获得股票所属行业数据
@app.route('/api/getConceptData/run', methods=['GET','POST'])
def get_data_concept_data_task():
    current_date = datetime.datetime.now().__str__() + "\n"
    response_data = {'message': 'success' }
    with open('scheduler_log', 'a') as file:
        file.write('Scheduling successful,starting get industry data in '+ current_date)  # 将追加的内容写入文件

    get_stock_eastmoney_industry.get_all_stock_eastmoney_industry()

    current_date = datetime.datetime.now().__str__() + "\n"
    with open('scheduler_log', 'a') as file:
        file.write('get industry data over in '+ current_date)  # 将追加的内容写入文件

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)