# 传统的requests爬取，速度较快
import pandas as pd
import time
import requests

# 读数据集，只取有效的列（序号和公司名）
df = pd.read_excel('./0106需要查找数据底稿（明天下午三点）(1)(1).xls')
start_id = 1 #起始序号
end_id = 10 #末尾序号
df = df[df.序号.isin(range(start_id, end_id + 1))]
df = df.iloc[:,[0,1]]

def main(key_word, num):
    params = {
        "q": key_word,
        "t": "",
        "p": num,
        "s": "10",
        "o": "0",
        "f": "{}"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Referer": "https://aiqicha.baidu.com/s?q=%E6%95%B0%E6%8D%AE&t=0"  # 防盗链

    }
    url = "https://aiqicha.baidu.com/s/advanceFilterAjax"
    response = requests.get(url, headers=headers, params=params)
    # print(response.json())
    try:
        resultList = response.json()["data"]["resultList"]
        #     for item in resultList:
        #         print(item)
        data = resultList[0]
        return data['scope']
    except:
        return "这家公司查不到"


if __name__ == '__main__':
    b = 0
    info_list = []
    for i in df.序号:
        # start_time = time.time()
        company_name = df.loc[df.序号 == i]['主体名称']
        company_name = company_name.values[0]
        print('')
        print("开始搜索序号为{}的公司:{}".format(i, company_name))
        key_word = company_name  # 搜索公司
        num = "1"  # 页码
        data = main(key_word, num)
        # 将读取信息计入list
        info_list.append(data)
        # 测试数据有效性
        print(data[:10])
    # 爬取信息列
    df_1 = pd.DataFrame(info_list, columns=['information'], index=df.index)
    # 合并信息
    result = pd.concat([df, df_1], axis=1)
    # 输出结果
    result.to_excel('result_from'
                    + str(start_id)
                    + '_to'
                    + str(end_id)
                    + '.xls')