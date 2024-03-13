import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com'    # HACKER NEWS (goood hacker - bad fucker)
response = requests.get(url)

print(response.text)   # anacodna cloud does not allow tunel openning:  OSError('Tunnel connection failed: 403 Forbidden')))  # test it on window
# OUT:
########################################################################################################################################################################
# # <html lang="en" op="news"><head><meta name="referrer" content="origin"><meta name="viewport" content="width=device-width, initial-scale=1.0"><link rel="stylesheet" type="text/css" href="news.cs
# s?GdEqjKGLzqVECauUsnEy">
#         <link rel="icon" href="y18.svg">
#                   <link rel="alternate" type="application/rss+xml" title="RSS" href="rss">
#         <title>Hacker News</title></head><body><center><table id="hnmain" border="0" cellpadding="0" cellspacing="0" width="85%" bgcolor="#f6f6ef">
#         <tr><td bgcolor="#ff6600"><table border="0" cellpadding="0" cellspacing="0" width="100%" style="padding:2px"><tr><td style="width:18px;padding-right:4px"><a href="https://news.ycombinat
# or.com"><img src="y18.svg" width="18" height="18" style="border:1px white solid; display:block"></a></td>
#                   <td style="line-height:12pt; height:10px;"><span class="pagetop"><b class="hnname"><a href="news">Hacker News</a></b>
#                             <a href="newest">new</a> | <a href="front">past</a> | <a href="newcomments">comments</a> | <a href="ask">ask</a> | <a href="show">show</a> | <a href="jobs">jobs</a>
# | <a href="submit" rel="nofollow">submit</a>            </span></td><td style="text-align:right;padding-right:4px;"><span class="pagetop">    ETC....
########################################################################################################################################################################

soup = BeautifulSoup(response.text, 'html5lib')

articles = []

for item in soup.find_all('tr', class_='athing'):
    title_tag = item.find('span', class_='titleline').find('a')
    title = title_tag.text
    link = title_tag.get('href', 'N/A')
    new_article = {
        'title': title,
        'link': link,
    }
    articles.append(new_article)

for index, item in enumerate(soup.find_all('span', class_='score')):
    articles[index]['upvotes'] = item.text

print(articles)

# OUT:
# (PilotPythonProject) C:\SRC\Py\teasers\ShaunWasselsFP\EPIV>python scraping-basics.py
# [{'title': 'Nvtop: Linux Task Monitor for Nvidia, AMD and Intel GPUs', 'link': 'https://github.com/Syllo/nvtop', 'upvotes': '57 points'}, {'title': "Building Meta's GenAI infrastructure", 'link': 'https://engineering.fb.com/2024/03/12/
# data-center-engineering/building-metas-genai-infrastructure/', 'upvotes': '490 points'}, {'title': 'How Mandelbrot set images are affected by floating point precision', 'link': 'https://github.com/ProfJski/FloatCompMandelbrot', 'upvote
# s': '148 points'}, {'title': "Bluesky's stackable approach to moderation", 'link': 'https://bsky.social/about/blog/03-12-2024-stackable-moderation', 'upvotes': '33 points'}, {'title': 'Multi-Threading and Mutation', 'link': 'https://ww
# w.rfleury.com/p/multi-threading-and-mutation', 'upvotes': '8 points'}, {'title': 'Launch HN: Glide (YC W24) – AI-assisted technical design docs', 'link': 'item?id=39682183', 'upvotes': '110 points'}, {'title': 'LOCS: Language developed
#  at age 9 in Z80 machine code (1988)', 'link': 'https://nanochess.org/locs.html', 'upvotes': '35 points'}, {'title': 'Weather forecasts have become more accurate', 'link': 'https://ourworldindata.org/weather-forecasts', 'upvotes': '249
#  points'}, {'title': 'Vulkan Foliage rendering using GPU Instancing', 'link': 'https://www.thegeeko.me/blog/foliage-rendering', 'upvotes': '129 points'}, {'title': 'How to colorize Game Boy games – Backgrounds', 'link': 'https://toruzz
# .com/blog/how-to-colorize-gb-games-04/', 'upvotes': '89 points'}, {'title': 'Apple announces ability to download apps directly from websites in EU', 'link': 'https://www.macrumors.com/2024/03/12/apple-announces-app-downloads-from-websi
# tes/', 'upvotes': '593 points'}, {'title': 'Chyrp Lite – An Ultra-Lightweight Tumblelogging Engine Using PHP and SQLite', 'link': 'https://chyrplite.net/', 'upvotes': '76 points'}, {'title': 'To write a great essay, think and care deep
# ly (2015)', 'link': 'https://www.theatlantic.com/entertainment/archive/2015/06/to-write-a-great-essay-think-and-care-deeply/394628/', 'upvotes': '38 points'}, {'title': 'Screen Space Reflection', 'link': 'https://zznewclear13.github.io
# /posts/screen-space-reflection-en/', 'upvotes': '56 points'}, {'title': 'Byte-Sized Swift: Building Tiny Games for the Playdate', 'link': 'https://www.swift.org/blog/byte-sized-swift-tiny-games-playdate/', 'upvotes': '143 points'}, {'t
# itle': 'Direct File officially opens in 12 pilot states', 'link': 'https://www.irs.gov/newsroom/direct-file-officially-opens-in-12-pilot-states-following-positive-early-reviews-eligible-taxpayers-can-file-online-directly-with-the-irs-f
# or-free', 'upvotes': '52 points'}, {'title': 'Show HN: Comma Separated Values (CSV) to Unicode Separated Values (USV)', 'link': 'https://crates.io/crates/csv-to-usv', 'upvotes': '181 points'}, {'title': '40 Years of Programming', 'link
# ': 'https://liw.fi/40/', 'upvotes': '80 points'}, {'title': 'Deterministic simulation testing for our entire SaaS', 'link': 'https://www.warpstream.com/blog/deterministic-simulation-testing-for-our-entire-saas', 'upvotes': '175 points'
# }, {'title': 'How engineers straightened the Leaning Tower of Pisa [video]', 'link': 'https://www.youtube.com/watch?v=0ZhHoyqQEhA', 'upvotes': '45 points'}, {'title': 'A ragtag band of internet friends became the best at forecasting wo
# rld events', 'link': 'https://www.vox.com/future-perfect/2024/2/13/24070864/samotsvety-forecasting-superforecasters-tetlock', 'upvotes': '92 points'}, {'title': 'Open Policy Agent', 'link': 'https://www.openpolicyagent.org/', 'upvotes'
# : '73 points'}, {'title': "The NYPD sent a warrantless subpoena for a copwatcher's Twitter account", 'link': 'https://hellgatenyc.com/nypd-warrantless-subpoena-copwatcher-social-media', 'upvotes': '363 points'}, {'title': 'The inventio
# n of blue and purple pigments in ancient times (2006)', 'link': 'https://pubs.rsc.org/en/content/articlehtml/2007/cs/b606268g', 'upvotes': '45 points'}, {'title': 'Infisical (YC W23) is hiring to build an open-source secret management
# platform', 'link': 'https://www.ycombinator.com/companies/infisical/jobs/MteMdIQ-full-stack-engineer', 'upvotes': '8 points'}, {'title': "Japan's Space One rocket explodes seconds after liftoff", 'link': 'https://twitter.com/BNONews/st
# atus/1767735668262752601/video/1', 'upvotes': '120 points'}, {'title': 'Vehicle brakes produce charged particles that may harm public health: study', 'link': 'https://news.uci.edu/2024/03/12/uc-irvine-study-vehicle-brakes-produce-charg
# ed-particles-that-may-harm-public-health/', 'upvotes': '58 points'}, {'title': 'Quantum Soccer (2009)', 'link': 'https://www.gregegan.net/BORDER/Soccer/Soccer.html', 'upvotes': '32 points'}, {'title': 'The complete story of Gödel incom
# pleteness', 'link': 'https://billwadge.com/2024/03/11/the-complete-story-of-godel-incompleteness/', 'upvotes': '119 points'}, {'title': 'Fig is sunsetting', 'link': 'https://fig.io/blog/post/fig-is-sunsetting'}]
