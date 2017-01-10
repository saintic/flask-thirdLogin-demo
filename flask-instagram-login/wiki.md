# Instagram OAuth Wiki


*Gloabl Variable*

```
client_id
client_secret
redirect_uri
```


## Step1：获取Authorization Code

https://api.instagram.com/oauth/authorize?client_id=client_id&redirect_uri=https%3a%2f%2fpassport.saintic.com%2fcallback%2finstagram%2f

#跳转回
https://passport.saintic.com/callback/instagram/?code=D08DCC3F287F34F2DECA05C83AA81A1B


## Step2：通过Authorization Code获取Access Token

curl -sL "https://api.instagram.com/oauth/access_token?client_id=32d6eea53343476e62ac&code=$code&client_secret=847b038ae547c41d0ba07f9641bef74309870224&redirect_uri=https%3a%2f%2fpassport.saintic.com%2fcallback%2finstagram%2f&" -XPOST


#返回
```
{
    "access_token": "fb2e77d.47a0479900504cb3ab4a1f626d174d2d",
    "user": {
        "id": "1574083",
        "username": "snoopdogg",
        "full_name": "Snoop Dogg",
        "profile_picture": "..."
    }
}
```


## Step3:接口
curl -sL "https://api.instagram.com/v1/users/self/?access_token=token"
