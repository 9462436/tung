import csv
import re
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from sklearn.preprocessing import LabelEncoder

# CSV文件列表
csv_list = []


# 通过传入的url获取对应的HTML文本
def getHTMLText(url):
    headers = {
        "User-Agent": "Mozilla/5.0(Windows NT 6.1;WOW64) AppleWebKit/537.36(KABUL, like Gecko) "
                      "Chrome/86.0.4240.198Safari/537.36 "}
    try:
        resp = requests.get(url=url, headers=headers, timeout=10)
        resp.raise_for_status()
        resp.encoding = 'utf-8'
        return resp.text
    except:
        return ''


# 获取单流派
def get_genre(html):
    genre_pattern = re.compile(r'(?<=流派：<!-- -->)(\w+)')
    if '流派' in html:
        genre = genre_pattern.search(html)
        if genre:
            return genre.group(1)
    else:
        return '无'


# 获取唱片公司
def get_RecordCompany(html):
    RecordCompany_pattern = re.compile(r'(?<=唱片公司：<!-- -->)(\w+)')
    if '唱片公司' in html:
        RecordCompany = RecordCompany_pattern.search(html)
        if RecordCompany:
            return RecordCompany.group(1)
        else:
            return None
    else:
        return '无'


# 获取发行时间
def get_Releasetime(html):
    Releasetime_pattern = re.compile(r'(?<=发行时间：<!-- -->)([\w\-]+)')
    if '发行时间' in html:
        Releasetime = Releasetime_pattern.search(html)
        if Releasetime:
            return Releasetime.group(1)
        else:
            return '空'
    else:
        return '空'


# 编写成方法,使用正则表达式获取冒号之后的字符串
def get_text_after_colon(input_str):
    match = re.search(r'(?<=：)\s*.+', str(input_str))
    if match:
        result_str = match.group(0).strip()
        return result_str
    else:
        return '空'


# 获取语种
def get_language(html):
    language_pattern = re.compile(r'(?<=语种：<!-- --> )(\w+)')
    if '语种' in html:
        language = language_pattern.search(html)
        if language:
            return language.group(1)


# 获取歌曲的具体详情
def get_song_info(url, idx):
    # 统一编码
    html = getHTMLText(url)
    # html.parser表示用BeautifulSoup库解析网页
    bs = BeautifulSoup(html, 'html.parser')

    # 歌手
    name = []
    # 排名
    rank = []
    # 时长
    time = []
    # 歌名
    song = []
    # 记录歌曲数
    count = 0
    # 上升指数
    popular = []
    # 排名变化
    change = []

    # 查找所有的'ul' class='songlist_list'标签
    ul = bs.find('ul', class_='songlist__list')
    # 在ul标签中查找所有'li'标签
    li_list = ul.find_all('li')

    for item in li_list:
        count += 1
        # 判断当前元素的排名是否在前3名, 如果是, 则使用songlist__number - -top类名提取排名文本, 否则使用songlist__number类名提取排名文本。
        if count <= 3:
            songlist_number = item.find('div', class_='songlist__number songlist__number--top').text
        else:
            songlist_number = item.find('div', class_='songlist__number').text

        songname_div = item.find('div', class_='songlist__songname')
        songname = songname_div.text.strip()

        # 使用正则表达式re.sub()方法,去除歌名文本songlist_songname中的字符“MV”、“播放”、“添加到歌单”、“分享”
        songname = re.sub('MV|播放添加到歌单|分享', '', songname)

        songlist_artist = item.find('div', class_='songlist__artist').text
        songlist_time = item.find('div', class_='songlist__time').text

        # 获取上升指数
        i_tag = item.find('i', class_='icon_rank_popular')
        if i_tag and i_tag.nextSibling:
            rank_change = i_tag.nextSibling.strip()
            popular.append(rank_change)
            # print('上升指数:', rank_change)
        else:
            pass

        # 获取排名变化
        # 排名下降
        i_tag2 = item.find('i', class_='icon_rank_down')
        if i_tag2 and i_tag2.nextSibling:
            rank_change = i_tag2.nextSibling.strip()
            change.append('↓' + rank_change)
        # 排名上升
        i_tag3 = item.find('i', class_='icon_rank_up')
        if i_tag3 and i_tag3.nextSibling:
            rank_change = i_tag3.nextSibling.strip()
            change.append('↑' + rank_change)
        # 新歌
        i_tag4 = item.find('i', class_='icon_rank_new')
        if i_tag4:
            change.append('NEW')
        # 保持不变
        i_tag5 = item.find('i', class_='icon_rank_keep')
        if i_tag5:
            change.append('━')

        # 添加数据
        rank.append(songlist_number)
        time.append(songlist_time)
        song.append(songname)
        name.append(songlist_artist)

    # 查找所有的'ul' class='songlist_list'标签
    ul = bs.find('ul', class_='songlist__list')
    # 在ul标签中查找所有'li'标签
    li_list = ul.find_all('li')

    link_list = []  # 定义空列表存储标题链接
    for item in li_list:
        a_tags = item.find_all('a')
        for a in a_tags:
            href = a.get('href')
            if href:
                link_list.append(href)  # 如果找到href,则添加到列表

    # 使用列表推导式过滤None
    link_list = [i for i in link_list if i is not None]

    # 歌曲链接
    song_link = []
    for link in link_list:
        if '/songDetail/' in link:
            song_link.append('https://y.qq.com' + link)  # 组合成歌曲完整链接

    # 专辑
    album = []
    # 语种
    language = []
    # 唱片公司
    RecordCompany = []
    # 发行时间
    Releasetime = []
    # 流派
    genre = []
    # ul有效标签
    ul_list = []

    # 记录可能出现歌曲下架的列表
    missing_song = []

    # 所有ul标签
    ul_list0 = []

    # 遍历所有歌曲详情网址，获取所有含有歌曲详情的ul、li标签
    for link in song_link:
        html = getHTMLText(link)
        bs = BeautifulSoup(html, 'html.parser')
        ul = bs.find('ul', class_='data__info')

        # 获取所有ul标签
        ul_list0.append(ul)

        # 若歌曲下架，ul为None
        # 获取ul有效标签
        if ul != None:

            ul_list.append(ul)
            # 查找所有的li标签
            li_list2 = ul.find_all('li', class_='data_info__item_song')
            for item in li_list2:
                # 文本
                n = item.text
                # 调用方法获取冒号之后的具体文本内容
                m = get_text_after_colon(n)

                if '专辑' in n:
                    album.append(m)

                if '语种' in n:
                    language.append(m)

    # 获取下架歌曲序号
    for i in range(len(ul_list0)):
        if ul_list0[i] is None:
            missing_song.append(i)

    # 缺少'专辑'字样的歌曲序号列表
    album_count = []
    # 记录缺少'专辑'字样的歌曲序号
    m = 0
    # 正则表达式无法获取'唱片公司'的歌曲序号列表，即处理None
    RecordCompany_count = []
    # 处理含有流派字样，但无具体流派,即处理None
    genre_count = []

    # 遍历所有ul标签，添加所有歌曲详情，若不存在某项，则添加'无'
    for i in ul_list:

        # 将HTML标签类型转换为str
        i = str(i)

        # 获取缺少'专辑'字样的歌曲序号,
        m += 1
        if not re.search('专辑', i):
            album_count.append(m)

        if '流派' in i and get_genre(i):
            genre.append(get_genre(i))
        # 无具体流派或get_genre()方法无法正确获取流派
        elif '流派' in i and not get_genre(i):
            genre.append(None)
        else:
            genre.append('无')

        Releasetime.append(get_Releasetime(i))

        RecordCompany.append(get_RecordCompany(i))

    # 处理缺少'专辑'字样的序号
    for i in album_count:
        album.insert(i - 1, '无')

    # 处理唱片公司名称含特殊符号及不存在具体唱片公司名称
    for i in range(len(RecordCompany)):
        if RecordCompany[i] is None:
            RecordCompany_count.append(i)
    # print(count3)
    for i in RecordCompany_count:
        # 查找所有的li标签
        li_list3 = ul_list[i].find_all('li', class_='data_info__item_song')
        for item in li_list3:
            k = get_text_after_colon(item.text)
            if '唱片公司' in item.text:
                RecordCompany[i] = k

    # 无具体流派或get_genre()方法无法正确获取流派
    for i in range(len(genre)):
        if genre[i] is None:
            genre_count.append(i)
    for i in genre_count:
        li_list4 = ul_list[i].find_all('li', class_='data_info__item_song')
        for item in li_list4:
            k = get_text_after_colon(item.text)
            if '流派' in item.text:
                genre[i] = k

    # 处理下架歌曲信息
    for i in missing_song:
        album.insert(int(i), '空')
        language.insert(int(i), '空')
        genre.insert(int(i), '空')
        Releasetime.insert(int(i), '空')
        RecordCompany.insert(int(i), '空')

    # CSV文件名
    csv_name = 'song' + str(idx) + '.csv'

    # 将数据整理成表格
    if len(change) == 0:
        print(
            '{:^5}\t{:^4}\t{:<10}\t{:<20}\t{: ^5}\t{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}'.format('排名', '时长', '作者',
                                                                                                  '歌名',
                                                                                                  '上升指数', '专辑',
                                                                                                  '语种', '流派', '发行时间',
                                                                                                  '唱片公司'))
        for i in range(count):
            print(
                '{:^5}\t{:^5}\t{:<10}\t{:<20}\t{: ^5}\t{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}'.format(rank[i], time[i],
                                                                                                      name[i],
                                                                                                      song[i],
                                                                                                      popular[i],
                                                                                                      album[i],
                                                                                                      language[i],
                                                                                                      genre[i],
                                                                                                      Releasetime[i],
                                                                                                      RecordCompany[i]))
        # 写入csv文件
        with open(csv_name, 'w', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(['排名', '时长', '作者', '歌名', '上升指数', '专辑', '语种', '流派', '发行时间', '唱片公司'])
            for i in range(count):
                csv_writer.writerow(
                    [rank[i], time[i], name[i], song[i], popular[i], album[i], language[i], genre[i], Releasetime[i],
                     RecordCompany[i]])
            f.close()

    else:
        print(
            '{:^5}\t{:^4}\t{:<10}\t{:<20}\t{: ^5}\t{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}'.format('排名', '时长', '作者',
                                                                                                  '歌名',
                                                                                                  '排名变化', '专辑',
                                                                                                  '语种', '流派', '发行时间',
                                                                                                  '唱片公司'))
        for i in range(count):
            print(
                '{:^5}\t{:^5}\t{:<10}\t{:<20}\t{: ^5}\t{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}'.format(rank[i], time[i],
                                                                                                      name[i],
                                                                                                      song[i],
                                                                                                      change[i],
                                                                                                      album[i],
                                                                                                      language[i],
                                                                                                      genre[i],
                                                                                                      Releasetime[i],
                                                                                                      RecordCompany[i]))
        # 写入csv文件
        with open(csv_name, 'w', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(['排名', '时长', '作者', '歌名', '排名变化', '专辑', '语种', '流派', '发行时间', '唱片公司'])
            for i in range(count):
                csv_writer.writerow(
                    [rank[i], time[i], name[i], song[i], change[i], album[i], language[i], genre[i], Releasetime[i],
                     RecordCompany[i]])
            f.close()


# 网址列表
url_list = []
# 网址数字列表
num_list = []

print('飙升榜--62      热歌榜--26       新歌榜--27      流行指数榜--4')
print('腾旭音乐人原创榜--52   听歌识曲榜--67   内地榜--5   香港地区榜--59')
print('台湾地区榜--61         欧美榜--3       韩国榜--16      日本榜--17')
print('网络歌曲榜--28        DJ舞曲榜--63     抖快榜--60       综艺新歌榜--64')
print('影视金曲榜--29         电音榜--57      国风热歌榜--65    说唱榜--58')
print('动漫音乐榜--72       游戏音乐榜--73    k歌金曲榜--36    美国金曲榜--108')
print('韩国Melon榜--129    英国UK榜--107    日本公信榜--105  JOOX本地热播榜--126')
print('香港TVB劲歌金榜--130     台湾KBOX榜--127           YouTube音乐排行榜--128')
print('请输入数字(输入后换行输入下一个数字)：')
while 1:
    # 搜索网址
    num = input()
    if num:
        # 获取网址
        url_list.append('https://y.qq.com/n/ryqq/toplist/' + num)
    else:
        break

print('--------运行中--------')
print()
# 计数
m = 0
# 遍历网址列表，获取CSV文件
for url in url_list:
    m += 1
    get_song_info(url, m)
    csv_list.append('song' + str(m) + '.csv')
    print()
print()
print('--------运行完成--------')

# 选取特定列进行合并
cols = ['排名', '时长', '作者', '歌名', '专辑', '语种', '流派', '发行时间', '唱片公司']


# 读取CSV文件
def read_csv(file, cols):
    return pd.read_csv(file, usecols=cols, encoding='utf-8-sig')


# 写入CSV文件
def to_csv(df, file, header, mode='w'):
    df.to_csv(file, index=False, header=header, mode=mode, encoding='utf-8-sig')


# 循环合并CSV文件
for csv in csv_list:
    df = read_csv(csv, cols)
    if csv == csv_list[0]:
        # 第一个CSV文件写入表头，'w'模式会覆盖写入文件,相当于删除文件重新写入。
        to_csv(df, 'song.csv', True, 'w')
    else:
        # 'a+'模式会以追加的方式打开CSV文件进行读写。
        to_csv(df, 'song.csv', False, 'a+')

# 数据分析及可视化
# 汉字字体，优先使用楷体，找不到则使用黑体
plt.rcParams['font.sans-serif'] = ['Kaitt', 'SimHei','Arial Unicode MS','Calibri','Cambria','Times New Roman','Lucida Sans Unicode']


# 读取CSV文件
df = pd.read_csv('song.csv', names=['排名', '时长', '作者', '歌名', '专辑', '语种', '流派', '发行时间', '唱片公司'])


# 流派分布
df_plot = df.loc[df['流派'] != '流派']
# 设定图的大小
fig, ax = plt.subplots(figsize=(10, 9))
genre_count = df_plot['流派'].value_counts().rename(None)
genre_count.plot(kind='bar')

plt.xlabel('流派')
plt.ylabel('数量')
plt.title('流派分布')
plt.show()

# 排名与时长的散点图
# 按照时长排序
df = df.sort_values('时长')
# 设定图的大小
fig, ax = plt.subplots(figsize=(10, 8))
# 绘制散点图
df.plot(x='排名', y='时长', kind='scatter', ax=ax)
plt.xlabel('排名')
plt.ylabel('时长')
plt.title('排名与时长分布')
plt.show()


# 唱片公司饼状图
# 对'发行公司'列做label encoding
company_le = LabelEncoder()
company_le.fit(df['唱片公司'])
df['公司_编码'] = company_le.transform(df['唱片公司'])
# 设定图的大小
fig, ax = plt.subplots(figsize=(10, 8))
# 获取每个公司的数量和百分比
company_count = df.groupby('公司_编码')['公司_编码'].count()
company_pct = company_count / df.shape[0] * 100
# 绘制饼图
company_count.rename(None).plot(kind='pie',
                                labels=company_le.inverse_transform(company_count.index),
                                autopct='%1.2f%%')
plt.title('唱片公司分布(百分比)')
plt.show()

# 语种分布饼状图
# 选择行
df_plot = df.loc[df['语种'] != '语种']
# 设定图的大小
fig, ax = plt.subplots(figsize=(10, 8))
# 查看语种 value_counts
# print(df_plot['语种'].value_counts())
# df_plot['语种'].value_counts().rename(None)去除'Name: count, dtype: int64'的元信息,保留了索引及对应的值
df_plot['语种'].value_counts().rename(None).plot(kind='pie', autopct='%.2f%%')
plt.title('语种分布图')
plt.show()



# 创建雷达图
df = pd.read_csv('song.csv')
# 将缺省的秒数加上去
df['时长'] = df['时长'].apply(lambda x: x + ':00' if len(x) == 5 else x)

# 将时间转化为 timedelta 类型然后转化为分钟单位
df['时长'] = pd.to_timedelta(df['时长']).dt.total_seconds() / 60

# 按照流派进行分组，计算平均时长
grouped_df = df.groupby(['流派'])['时长'].agg([np.mean])

# 将结果的列名重命名为labels和stats
grouped_df.columns = ['平均时长']
grouped_df = grouped_df.reset_index()

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, polar=True)

# 计算每个类别的角度数
labels = grouped_df['流派']
stats = grouped_df['平均时长']
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)

# 将最后一个角度闭合起来
stats = np.concatenate((stats, [stats[0]]))
angles = np.concatenate((angles, [angles[0]]))

# 绘制多边形
ax.plot(angles, stats, 'o-', linewidth=2, label='平均时长')
ax.fill(angles, stats, alpha=0.25)

# 设置刻度标签和刻度位置
ax.set_thetagrids(angles[:-1] * 180 / np.pi, labels, fontproperties='SimHei', fontsize=12)
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)

# 添加标签和标题
plt.title('歌曲流派和时长雷达图', fontproperties='SimHei', fontsize=20)
plt.legend(loc='upper right', prop={'family': 'SimHei', 'size': 15})
plt.show()

# 折线图
# 读取song.csv文件，将发行时间列解析为日期
df = pd.read_csv('song.csv', parse_dates=['发行时间'])
# 将日期转化为年份月份
df['发行时间'] = pd.to_datetime(df['发行时间'])
df['年月'] = pd.PeriodIndex(df['发行时间'], freq='M')
# 按照年份月份进行分组
grouped = df.groupby('年月')
# 统计每个年份月份的歌曲数量
month_count = grouped.size()
# 调整绘图的大小
plt.figure(figsize=(10, 8))
# 绘制折线图，并将Period对象转化为字符串
plt.plot(month_count.index.astype(str), month_count.values)
# 添加标题和轴标签
plt.xticks(rotation=90)  # 添加 rotation 参数
plt.title('每一年每月发行歌曲数量')
plt.xlabel('时间')
plt.ylabel('歌曲数量')
# 显示折线图
plt.show()
