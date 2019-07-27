#Selenium    //pip install selenium==2.48.0    coz new version cannot
#PhantomJS  // apt install phantomjs    http://phantomjs.org

#截屏jpg，pdf
# var page=require('webpage').create();
# page.open('http://leettest.com',function(){
#     page.viewportSize={width:1920,height:968};
#     page.render('leettest.png');
#     phantom.exit();
# });
#异步js获取
#jquery

#


from selenium import webdriver


browser =  webdriver.PhantomJS()

browser.get('https://www.google.com')
#browser.implicitly_wait(10)
print(browser.page_source)