fis.match('/vendor/**.js', {
        packTo: '/static/aio.js',
		  useHash: false, // default is true
		  // 指定压缩插件 fis-optimizer-uglify-js 

})
fis.match('/vendor/**.css', {
        packTo: '/static/aio.css',
  useHash: false, //default is `true`
  // compress css invoke fis-optimizer-clean-css

})
