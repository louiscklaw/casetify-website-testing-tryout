
# reference to project root
import os,sys

TEST_DIR=os.path.join(os.getcwd(), 'test')
TEST_RESULT=os.path.join(TEST_DIR, 'test_result')
TEST_EXPECTED_RESULT=os.path.join(TEST_DIR,'expected')

# text
LEFT_NAV_CUSTOM_STUDIO='CUSTOM STUDIO Custom Studio'
SEL_LEFT_NAV_CUSTOM_STUDIO='//android.view.View[@text="CUSTOM STUDIO"]'

LEFT_NAV_SMARTPHONE='智能手機'
SEL_LEFT_NAV_SMARTPHONE='//android.view.View[@text="智能手機"]'

LEFT_NAV_APPLE_WATCH='APPLE WATCH'
SEL_LEFT_NAV_APPLE_WATCH='//android.view.View[@text="APPLE WATCH"]'

LEFT_NAV_AIRPODS='AIRPODS'
SEL_LEFT_NAV_AIRPODS='//android.view.View[@text="AIRPODS"]'

LEFT_NAV_TECH_ACCESSORIES = '電子產品配件'
SEL_LEFT_NAV_TECH_ACCESSORIES ='//android.view.View[@text="電子產品配件"]'

LEFT_NAV_SIGNATURE_PRINTS = '經典印花'
SEL_LEFT_NAV_SIGNATURE_PRINTS ='//android.view.View[@text="經典印花"]'

LEFT_NAV_FEATURE_ARTIST = '合作藝術家'
SEL_LEFT_NAV_FEATURE_ARTIST ='//android.view.View[@text="合作藝術家"]'

LEFT_NAV_CO_LAB = '品牌聯乘'
SEL_LEFT_NAV_CO_LAB ='//android.view.View[@text="品牌聯乘"]'

IDX_FILENAME = 0
IDX_SELECTOR=1
left_nav_settings = {
  LEFT_NAV_CUSTOM_STUDIO:[
    TEST_RESULT+'/zh_left_nav_menu_custom_studio.jpg',
    SEL_LEFT_NAV_CUSTOM_STUDIO
    ],

  LEFT_NAV_SMARTPHONE :[
    TEST_RESULT+'/zh_left_nav_menu_智能手機.jpg',
    SEL_LEFT_NAV_SMARTPHONE
    ],
  LEFT_NAV_APPLE_WATCH :[
    TEST_RESULT+'/zh_left_nav_menu_智能手機.jpg',
    LEFT_NAV_APPLE_WATCH
    ],
  LEFT_NAV_FEATURE_ARTIST :[
    TEST_RESULT+'/zh_left_nav_menu_合作藝術家.jpg',
    SEL_LEFT_NAV_FEATURE_ARTIST
    ],
  LEFT_NAV_CO_LAB :[
    TEST_RESULT+'/zh_left_nav_menu_品牌聯乘.jpg',
    SEL_LEFT_NAV_CO_LAB
    ],
  LEFT_NAV_SMARTPHONE :[
    TEST_RESULT+'/zh_left_nav_menu_智能手機.jpg',
    SEL_LEFT_NAV_SMARTPHONE
    ],
  LEFT_NAV_SIGNATURE_PRINTS :[
    TEST_RESULT+'/zh_left_nav_menu_經典印花.jpg',
    SEL_LEFT_NAV_SIGNATURE_PRINTS
    ],
  LEFT_NAV_TECH_ACCESSORIES :[
    TEST_RESULT+'/zh_left_nav_menu_電子產品配件.jpg',
    SEL_LEFT_NAV_TECH_ACCESSORIES
    ]
}

HAMBURGER_BUTTON_XY = (68, 144)
