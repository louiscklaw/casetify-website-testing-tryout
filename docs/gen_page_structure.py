#!/usr/bin/env python3

import os,sys
from string import Template
DOT_FILE_TEMPLATE=Template('''
graph {
    rankdir=LR;

    $CONTENT
}
'''.strip())

NAV_ROOT={
  'Custom Studio':{
    '個人化手機殼':[ '竹纖維可分解再生手機殼','背帶手機殼','Monogram Studio','強悍防摔手機殼','閃亮流沙手機殼','霓虹流沙手機殼','特強防摔手機殼','反光鏡面手機殼','個人化圖案手機殼','壓花手機殼','雲石手機殼','閃亮珠片手機殼','全系列個人化手機殼' ],
    '個人化錶帶':[ 'Monogram錶帶', '個人化透明果凍錶帶', '真皮錶帶', '全系列錶帶款式'],
    '個人化電子產品配件':[ '個人化AirPods保護殼','Custom Mirror AirPods Case','個人化iPad保護套','個人化Macbook保護殼','個人化手機單肩包','個人化折疊式iPad保護套','個人化MacBook收納袋']
  },
  '智能手機':{
    'iPhone':['Phone SE','Phone 11','Phone 11 Pro','Phone 11 Pro Max','Phone XS','Phone XS Max','Phone XR','Phone X','Phone 8','系列iPhone手機殼'],
    'Android':[ 'Galaxy S20','Galaxy S20+','Galaxy S20 Ultra','Galaxy S10 Plus','Galaxy S10','Galaxy S10e','Galaxy Note 9','Galaxy S9','Galaxy S9 Plus','全系列Samsung 手機殼' ]
  },
  'Apple Watch':{
    "錶帶尺寸":[ '38mm','40mm','42mm','44mm'],
    '錶帶款式':[ 'Saffiano皮革錶帶','閃亮Apple Watch錶帶','真皮錶帶','個人化Monogram錶帶','Apple Watch 錶鏈帶','個人化透明果凍錶帶','意大利皮革二合一錶帶','全系列錶帶款式' ]
  },
  '電子產品配件':{
    '電子小物':[ '紫外線手機消毒器', 'AirPods 保護殼', 'AirPods Pro 保護殼', '充電線', '鋼化玻璃螢幕保護貼', '個人化手機單肩包', '皮革手機背貼卡套', '手機指環扣 (Grip)', 'Apple Watch保護殼', '無線充電器', '全系列電子小物' ],
    'iPad保護套':[ 'iPad Pro 11吋 (2020)', 'iPad Pro 12.9吋 (2020)', 'iPad 10.2吋 (2019)', 'iPad Mini (2019)', 'iPad Pro 12.9吋 (第三代)', 'iPad Pro 11吋 (2018)', 'iPad Pro 12.9吋 (第一及第二代)', 'iPad Pro 10.5吋', 'iPad 9.7吋 (第五及第六代)', 'iPad Air 2', 'iPad Mini 4', 'iPad Air 2019', '全系列iPad保護套' ],
    'MacBook保護殼':[ 'Pro 16吋', 'Pro Touch Bar 15吋', 'Touch Bar 13吋', 'Pro Retina 13吋', 'Pro 13吋', 'Air Retina 13吋', 'Air 13吋', '12吋', '全系列Macbook保護殼' ]
  },
  '產品系列':{
    '經典印花':['CONSCiOUS','卡式錄音帶系列','特強悍防摔手機保護殼系列','花卉系列','寵物系列','城市設計系列','透明設計系列','Instagram系列','藝術系列','搭配系列','完整系列' ],

    '聯乘藝術家':['Bodil Jane 2020','LOVE WATTS','Avrey Ovard','designlovefest 2020','Hidden Gems','Quotes by Christie','Letizilla','Holly Nichols','Ann Marie Coolick','Martina Martian', ],

    '品牌聯乘系列':['Pangram Pangram®','HEINZ','Hello Kitty','Coca-Cola','Cases for a Cause','Yu Nagaba','ohora','NEIGHBORHOOD','PARASITE','The M Jewelers','全部品牌聯乘系列' ]
  }
}

LANGS=[
      'English',
      'Español',
      'Português',
      'Deutsch',
      '日本語',
      '한국어',
      'Française',
      '中文（繁體）',
      'ภาษาไทย',
  ]

ob = []

for key in NAV_ROOT.keys():
  # print(key)
  print('nav_root -- "{}"'.format(key))
  ob.append('nav_root -- "{}"'.format(key))
  for kkey in NAV_ROOT[key]:
    print('"{}" -- "{}"'.format(key, kkey))
    ob.append('"{}" -- "{}"'.format(key, kkey))
    # print(kkey)
    pages = NAV_ROOT[key][kkey]

    for page in pages:
      print('"{}" -- "{}"'.format(kkey, page))
      ob.append('"{}" -- "{}"'.format(kkey, page))
      print(page)

for lang in LANGS:
  ob.append('"語言" -- "{}"'.format(lang))

ob.append('"index.html" -- "語言"')
ob.append('"index.html" -- nav_root')
ob.append('"index.html" -- "shopping cart"')
ob.append('"index.html" -- "search"')
ob.append('"index.html" -- "sign_up_page"')
ob.append('"sign_up_page" -- "login_page"')
ob.append('"login_page" -- "sign_up_page"')
ob.append('"login_page" -- "forgot_password"')
ob.append('"forgot_password" -- "login_page"')

with open('site-structure.dot','w') as fo:
  fo.write(DOT_FILE_TEMPLATE.substitute(
    CONTENT='\n'.join(ob)
  ))
