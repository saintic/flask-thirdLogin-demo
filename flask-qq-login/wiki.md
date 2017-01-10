# QQ OAuth2.0 Wiki


*Gloabl Variable*

```
client_id
client_secret
redirect_uri
```


## Step1：获取Authorization Code


https://graph.qq.com/oauth2.0/authorize?response_type=code&client_id=client_id&redirect_uri=https%3a%2f%2fpassport.saintic.com&scope=get_user_info

```
#response_type	必须	授权类型，此值固定为“code”。
#client_id	必须	申请QQ登录成功后，分配给应用的appid。
#redirect_uri	必须	成功授权后的回调地址，必须是注册appid时填写的主域名下的地址，建议设置为网站首页或网站的用户中心。注意需要将url进行URLEncode。
#state	必须	client端的状态值。用于第三方应用防止CSRF攻击，成功授权后回调时会原样带回。请务必严格按照流程检查用户与state参数状态的绑定。
#scope	可选	请求用户授权时向用户显示的可进行授权的列表。 
    可填写的值是API文档中列出的接口，以及一些动作型的授权（目前仅有：do_like），如果要填写多个接口名称，请用逗号隔开。
    例如：scope=get_user_info,list_album,upload_pic,do_like, 不传则默认请求对接口get_user_info进行授权。
#display	可选	仅PC网站接入时使用。 用于展示的样式。不传则默认展示为PC下的样式。如果传入“mobile”，则展示为mobile端下的样式。
#g_ut	可选	仅WAP网站接入时使用。 QQ登录页面版本（1：wml版本； 2：xhtml版本），默认值为1。
```

#跳转回
https://passport.saintic.com/?code=D08DCC3F287F34F2DECA05C83AA81A1B


## Step2：通过Authorization Code获取Access Token

https://graph.qq.com/oauth2.0/token?grant_type=authorization_code&client_id=client_id&client_secret=client_secret&code=D08DCC3F287F34F2DECA05C83AA81A1B&state=test&redirect_uri=https%3a%2f%2fpassport.saintic.com

```
#grant_type	必须	授权类型，在本步骤中，此值为“authorization_code”。
#client_id	必须	申请QQ登录成功后，分配给网站的appid。
#client_secret	必须	申请QQ登录成功后，分配给网站的appkey。
#code	必须	上一步返回的authorization code。 
    如果用户成功登录并授权，则会跳转到指定的回调地址，并在URL中带上Authorization Code。
    例如，回调地址为www.qq.com/my.php，则跳转到：
    http://www.qq.com/my.php?code=520DD95263C1CFEA087******
    注意此code会在10分钟内过期。
#redirect_uri	必须	与上面一步中传入的redirect_uri保持一致。
 ```

#返回
```
access_token=79D493208A237BAB3C9AE93FAD2798CE&expires_in=7776000&refresh_token=30AF0BD336324575029492BD2D1E134B
```


## Step3：（可选）权限自动续期，获取Access Token

https://graph.qq.com/oauth2.0/token?grant_type=refresh_token&client_id=client_id&client_secret=client_secret&refresh_token=30AF0BD336324575029492BD2D1E134B

```
#grant_type	必须	授权类型，在本步骤中，此值为“refresh_token”。
#client_id	必须	申请QQ登录成功后，分配给网站的appid。
#client_secret	必须	申请QQ登录成功后，分配给网站的appkey。
#refresh_token	必须	在Step2中，返回的refres_token。
```

#返回
```
access_token=E8BF2BCAF63B7CE749796519F5C5D5EB&expires_in=7776000&refresh_token=30AF0BD336324575029492BD2D1E134B
```


## Step4：使用Access Token来获取用户的OpenID

1. 发送请求到如下地址（请将access_token等参数值替换为你自己的）：
https://graph.qq.com/oauth2.0/me?access_token=E8BF2BCAF63B7CE749796519F5C5D5EB

2. 获取到用户OpenID，返回包如下：
```
callback( {"client_id":"client_id","openid":"AF8AA7E0F77451736DD97FB796849024"} );
```


## Step5：使用Access Token以及OpenID 调用API
（1）发送请求到get_user_info的URL（请将access_token，appid等参数值替换为你自己的）：
https://graph.qq.com/user/get_user_info?access_token=E8BF2BCAF63B7CE749796519F5C5D5EB&oauth_consumer_key=client_id&openid=AF8AA7E0F77451736DD97FB796849024

（2）成功返回后，即可获取到用户数据：
```
{
  "ret": 0,
  "msg": "",
  "is_lost": 0,
  "nickname": "Together Forever!",
  "gender": "男",
  "province": "北京",
  "city": "朝阳",
  "year": "1995",
  "figureurl": "http://qzapp.qlogo.cn/qzapp/client_id/openId/30",
  "figureurl_1": "http://qzapp.qlogo.cn/qzapp/client_id/openId/50",
  "figureurl_2": "http://qzapp.qlogo.cn/qzapp/client_id/openId/100",
  "figureurl_qq_1": "http://q.qlogo.cn/qqapp/client_id/openId/40",
  "figureurl_qq_2": "http://q.qlogo.cn/qqapp/client_id/openId/100",
  "is_yellow_vip": "0",
  "vip": "0",
  "yellow_vip_level": "0",
  "level": "0",
  "is_yellow_year_vip": "0"
}
```
