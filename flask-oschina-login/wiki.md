# OSChina Wiki

```
client_id
client_secret
redirect_uri
```

## Step1


> request(get) ---->  https://www.oschina.net/action/oauth2/authorize?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}


> get code -------->  ed3158e389839de77964547fd77f7697


## Step2

> request(get/post)  ----> https://www.oschina.net/action/openapi/token?client_id=client_id&client_secret=client_secret&grant_type=authorization_code&redirect_uri=redirect_uri&code=ed3158e389839de77964547fd77f7697


> get return -------->

```
{
    "access_token": "8447ff97-9b8c-4224-9cec-63b97d34ba65", 
    "refresh_token": "8447ff97-9b8c-4224-9cec", 
    "token_type": "bearer", 
    "expires_in": 43199,
    "uid": 12
}
```

## Step3
> request(get/post) ----> https://www.oschina.net/action/openapi/user?access_token=xxx


> get return ------>
```
获取成功
{
    id: 899**,
    email: "****@gmail.com",
    name: "彭博",
    gender: "male",
    avatar: "http://www.oschina.net/uploads/user/****",
    location: "广东 深圳",
    url: "http://home.oschina.net/****"
}

获取失败
{
    error: "invalid_token",
    error_description: "Invalid access token: 7fade311-d844-4159-9890-c8f0511337e5"
}

```
