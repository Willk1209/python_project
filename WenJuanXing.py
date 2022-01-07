import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth  # 反爬虫第三方库
import numpy as np
import time


async def main():
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

    # 调用了Page对象的goto方法就相当于在浏览器中输入问卷的网址,浏览器跳转到了对应的页面进行加载
    await page.goto('https://www.wjx.cn/vm/hMFdONJ.aspx')
    # # 填空题：page.type(selector,text),在指定selector的元素上填写text
    # await page.type('#q1', '姓名')
    # await page.type('#q2', '学号')
    # await page.type('#divquestion5 > table > tbody > tr:nth-child(1) > td > div > textarea', '体温')

    # 单选题：先用page.querySelector(selector)找到指定的元素,再调用元素的click()方法

    # 1
    choice = np.random.choice([7,8,9,10])
    button = await page.querySelector("#div1 > div.ui-controlgroup > div:nth-child(" + str(choice) + ") > div")
    await button.click()
    await asyncio.sleep(1)

    # 2
    special_choice = np.random.choice([1, 2])
    button = await page.querySelector("#div2 > div.ui-controlgroup > div:nth-child(" + str(special_choice) + ") > div")
    await button.click()
    await asyncio.sleep(1)

    # 3
    choice = np.random.choice([2, 3, 4])
    button = await page.querySelector("#div3 > div.ui-controlgroup > div:nth-child(" + str(choice) + ") > div")
    await button.click()
    await asyncio.sleep(1)

    # 4
    choice = np.random.choice([3, 4], p=[0.7, 0.3])
    button = await page.querySelector("#div4 > div.ui-controlgroup > div:nth-child(" + str(choice) + ") > div")
    await button.click()
    await asyncio.sleep(1)

    # 5
    choice = np.random.choice([1, 3], p=[0.7, 0.3])
    button = await page.querySelector("#div5 > div.ui-controlgroup > div:nth-child(" + str(choice) + ") > div")
    await button.click()
    await asyncio.sleep(1)

    # 6
    choice = np.random.choice([1, 2, 3, 4], p=[0.2, 0.3, 0.4, 0.1])
    button = await page.querySelector("#div6 > div.ui-controlgroup > div:nth-child(" + str(choice) + ") > div")
    await button.click()
    await asyncio.sleep(1)

    # 7
    choice = np.random.choice([1,3],p=[0.4,0.6])
    button = await page.querySelector("#div7 > div.ui-controlgroup > div:nth-child(" + str(choice) + ") > div")
    await button.click()
    await asyncio.sleep(1)

    # 8
    button = await page.querySelector("#div8 > div.ui-controlgroup > div:nth-child(2) > div")
    await button.click()
    await asyncio.sleep(1)
    button = await page.querySelector("#div8 > div.ui-controlgroup > div:nth-child(3) > div")
    await button.click()
    await asyncio.sleep(1)
    button = await page.querySelector("#div8 > div.ui-controlgroup > div:nth-child(6) > div")
    await button.click()
    await asyncio.sleep(1)

    # 9
    button = await page.querySelector("#div9 > div.ui-controlgroup > div:nth-child(3) > div")
    await button.click()
    await asyncio.sleep(1)
    button = await page.querySelector("#div9 > div.ui-controlgroup > div:nth-child(5) > div")
    await button.click()
    await asyncio.sleep(1)
    button = await page.querySelector("#div9 > div.ui-controlgroup > div:nth-child(8) > div")
    await button.click()
    await asyncio.sleep(1)

    # 10
    button = await page.querySelector("#div10 > div.ui-controlgroup > div:nth-child(3) > div")
    await button.click()
    await asyncio.sleep(1)

    # 11
    button = await page.querySelector("#div11 > div.ui-controlgroup > div:nth-child(3) > div")
    await button.click()
    await asyncio.sleep(1)

    # 12
    choice = np.random.choice([4, 5], p=[0.6, 0.4])
    button = await page.querySelector("#div12 > div.scale-div > div > ul > li:nth-child(" + str(choice) + ") > a")
    await button.click()
    await asyncio.sleep(1)

    # 13
    choice = np.random.choice([4, 5], p=[0.4, 0.6])
    button = await page.querySelector("#div13 > div.scale-div > div > ul > li:nth-child(" + str(choice) + ") > a")
    await button.click()
    await asyncio.sleep(1)

    # 14
    button = await page.querySelector("#div14 > div.ui-controlgroup > div:nth-child(2) > div")
    await button.click()
    await asyncio.sleep(1)

    # 15
    button = await page.querySelector("#div15 > div.ui-controlgroup > div:nth-child(1) > div")
    await button.click()
    await asyncio.sleep(1)
    button = await page.querySelector("#div15 > div.ui-controlgroup > div:nth-child(2) > div")
    await button.click()
    await asyncio.sleep(1)
    button = await page.querySelector("#div15 > div.ui-controlgroup > div:nth-child(4) > div")
    await button.click()
    await asyncio.sleep(1)

    # 16
    button = await page.querySelector("#div16 > div.ui-controlgroup > div:nth-child(1) > div")
    await button.click()
    await asyncio.sleep(1)

    # 17
    button = await page.querySelector("#div17 > div.ui-controlgroup > div:nth-child(1) > div")
    await button.click()
    await asyncio.sleep(1)
    button = await page.querySelector("#div17 > div.ui-controlgroup > div:nth-child(3) > div")
    await button.click()
    await asyncio.sleep(1)
    button = await page.querySelector("#div17 > div.ui-controlgroup > div:nth-child(5) > div")
    await button.click()
    await asyncio.sleep(1)

    # 18
    if special_choice == 1:
        button = await page.querySelector("#div18 > div.ui-controlgroup > div:nth-child(3) > div")
        await button.click()
        await asyncio.sleep(1)
        button = await page.querySelector("#div18 > div.ui-controlgroup > div:nth-child(6) > div")
        await button.click()
        await asyncio.sleep(1)
    else:
        button = await page.querySelector("#div18 > div.ui-controlgroup > div:nth-child(1) > div")
        await button.click()
        await asyncio.sleep(1)
        button = await page.querySelector("#div18 > div.ui-controlgroup > div:nth-child(2) > div")
        await button.click()
        await asyncio.sleep(1)

    # 19
    button = await page.querySelector("#div19 > div.ui-controlgroup > div:nth-child(1) > div")
    await button.click()
    await asyncio.sleep(1)

    # 20
    choice = np.random.choice([1, 2], p=[0.4, 0.6])
    if choice == 1:
        button = await page.querySelector("#div20 > div.ui-controlgroup > div:nth-child(1) > div")
        await button.click()
        await asyncio.sleep(1)
    else:
        button = await page.querySelector("#div20 > div.ui-controlgroup > div:nth-child(2) > div")
        await button.click()
        await asyncio.sleep(1)
        button = await page.querySelector("#div20 > div.ui-controlgroup > div:nth-child(3) > div")
        await button.click()
        await asyncio.sleep(1)
        button = await page.querySelector("#div20 > div.ui-controlgroup > div:nth-child(4) > div")
        await button.click()
        await asyncio.sleep(1)

    # 21
    button = await page.querySelector("#div21 > div.ui-controlgroup > div:nth-child(1) > div")
    await button.click()
    await asyncio.sleep(1)

    # 22
    button = await page.querySelector("#div22 > div.ui-controlgroup > div:nth-child(1) > div")
    await button.click()
    await asyncio.sleep(1)

    # 23
    button = await page.querySelector("#div23 > div.ui-controlgroup > div:nth-child(2) > div")
    await button.click()
    await asyncio.sleep(1)
    button = await page.querySelector("#div23 > div.ui-controlgroup > div:nth-child(5) > div")
    await button.click()
    await asyncio.sleep(1)

    # 24
    button = await page.querySelector("#div24 > div.ui-controlgroup > div:nth-child(3) > div")
    await button.click()
    await asyncio.sleep(1)


    # # 地址题：先点击手动填写地址,再在地址框内填写相应地址
    # address = await page.querySelector("#divquestion7 > ul > li:nth-child(1) > label")
    # await address.click()
    # await page.type('#q9', '地址')
    #

    # # 日期选择题：先点击日期选择框,在出现的iframe寻找元素并调用click()方法
    # date1 = await page.querySelector("#q4")
    # await date1.click()
    # frame = page.frames
    # date2 = await frame[1].querySelector('#selectTodayButton')
    # await date2.click()

    # 找到提交按钮提交
    submit = await page.querySelector('#ctlNext')
    await asyncio.sleep(np.random.randint(15,23))
    await submit.click()
    await asyncio.sleep(2)  # 页面延迟2s看是否提交成功
    try:
        auth_code = await page.querySelector('#SM_BTN_1')
        await auth_code.click()
        await asyncio.sleep(5)  # 页面延迟5s看是否验证成功
        await browser.close()
    except:
        await browser.close()


i = 0
initial_time = time.time()
# 刷问卷数量
for i in range(46):
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(main())
    i += 1
    print("第{}份问卷已完成，用时{:.2f}秒".format(i,time.time() - start_time))
    time.sleep(np.random.randint(8,16))
print("总耗时为{:.2f}秒".format(time.time()-initial_time))

