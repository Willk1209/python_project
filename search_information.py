# 此方法是调用了浏览器进行访问，速度相对requests较慢
from lxml import etree
import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth  # 反爬虫第三方库
import pandas as pd
import time

# 读数据集，只取有效的列（序号和公司名）
df = pd.read_excel('./0106需要查找数据底稿（明天下午三点）(1)(1).xls')
start_id = 1 #起始序号
end_id = 100 #末尾序号
df = df[df.序号.isin(range(start_id, end_id + 1))]
df = df.iloc[:,[0,1]]

async def main(url):
    # launch方法会新建一个browser对象,然后赋值给browser
    browser = await launch({
        # 路径就是你的谷歌浏览器的安装路径
        'executablePath': '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        # Pyppeteer 默认使用的是无头浏览器,所以要显示需要给False
        'headless': False,
        # 设置Windows-size和Viewport大小来实现网页完整显示
        'args': ['--no-sandbox', '--window-size=1366,850']
    })

    # 调用 newPage 方法相当于浏览器中新建了一个选项卡,同时新建了一个Page对象
    page = await browser.newPage()
    await page.setViewport({'width': 1366, 'height': 768})
    # 防止页面识别出脚本(反爬虫关键语句)
    await stealth(page)
    # 调用了Page对象的goto方法就相当于在浏览器中输入对应的网址,浏览器跳转到了对应的页面进行加载
    await page.goto(url)

    # 读取页面内容
    page_text = await page.content()
    # 读取html源码
    tree = etree.HTML(page_text)
    try:
        # 对页面进行解析，此页面应当是与搜索公司相关的公司列表，这里默认选择其中的第一个公司
        info = tree.xpath('/html/body/div[1]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/span[5]/span[2]/text()'
                          )[0]
        # 如果需要点进进入详情页面，uncomment下列行：
        # detail_website = tree.xpath('/html/body/div[1]/div[1]/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/h3/a/@href')
        # detail_website = 'https://aiqicha.baidu.com/' + detail_website[0]
        # # print(detail_website)
        # await page.goto(detail_website)
        # page_text = await page.content()
        # # 对对应项的内容解析
        # tree = etree.HTML(page_text)
        # info = tree.xpath('//*[@id="basic-business"]/table/tbody/tr[12]/td[2]/div/text()')
        # info = info[0].split('\n')[0]
        # # print(info)
        await browser.close()
        return info
    except:
        # 公司列表有可能没有符合的公司
        # print("这家公司查不到")
        await browser.close()
        return "这家公司查不到"


for i in df.序号:
    start_time = time.time()
    # 遍历每一个公司名称
    company_name = df.loc[df.序号 == i]['主体名称']
    company_name = company_name.values[0]
    # 提示进度
    print("开始搜索序号为{}的公司:{}".format(i,company_name))
    # 设定访问的搜索页面
    url = 'https://aiqicha.baidu.com/s?q=' + company_name + '&t=0'
    # 执行主函数：
    info = asyncio.get_event_loop().run_until_complete(main(url))
    # 看看获取的信息
    print(info)
    # 计时
    print('此轮用时:{}s'.format(time.time()-start_time))
