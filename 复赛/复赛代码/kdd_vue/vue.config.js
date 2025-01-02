/*
 * @Author: chenxuan
 * @Date: 2021-12-22 22:10:02
 * @LastEditTime: 2021-12-22 22:10:02
 * @LastEditors: chenxuan
 */
module.exports = {
    productionSourceMap: false,
    lintOnSave: false,
    publicPath:'./',
    devServer: {
      port: 8001,//不能是80
        proxy: {                 //设置代理，必须填
            '/api': {              //设置拦截器  拦截器格式   斜杠+拦截器名字，名字可以自己定
                target: 'http://121.43.145.10:9090',     //代理的目标地址
                ws: true,
                secure: false,
                changeOrigin: true,                 //是否设置同源，输入是的
                pathRewrite: {                      //路径重写
                    '^/api': ''                     //选择忽略拦截器里面的单词
                }
            },
        }
    },
    configureWebpack: {
      module: {
          rules: [
              {
                  test: /\.mjs$/,
                  include: /node_modules/,
                  type: "javascript/auto"
              },
          ]
      }
  }
};
