# GitHub OAuth Wiki


*Gloabl Variable*

```
client_id
client_secret
redirect_uri
```


## Step1：获取Authorization Code


https://github.com/login/oauth/authorize?client_id=client_id&redirect_uri=https%3a%2f%2fpassport.saintic.com%2fcallback%2fgithub%2f

#跳转回
https://passport.saintic.com/callback/github/?code=D08DCC3F287F34F2DECA05C83AA81A1B


## Step2：通过Authorization Code获取Access Token

curl -sL "https://github.com/login/oauth/access_token?client_id=32d6eea53343476e62ac&code=$code&client_secret=847b038ae547c41d0ba07f9641bef74309870224&redirect_uri=https%3a%2f%2fpassport.saintic.com%2fcallback%2fgithub%2f&" -XPOST


#返回
```
access_token=token&scope=&token_type=bearer
```


## Step3:接口
curl -sL "https://api.github.com/user?access_token=token"
