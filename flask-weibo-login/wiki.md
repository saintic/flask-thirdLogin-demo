# Weibo Wiki

```
client_id
client_secret
redirect_uri
```

## Step1


> request(get) ---->  https://api.weibo.com/oauth2/authorize?client_id=client_id&response_type=code&redirect_uri=https%3a%2f%2fpassport.saintic.com

> get code -------->  ed3158e389839de77964547fd77f7697


## Step2

> request(post)  ----> https://api.weibo.com/oauth2/access_token?client_id=client_id&client_secret=client_secret&grant_type=authorization_code&redirect_uri=https%3a%2f%2fpassport.saintic.com&code=ed3158e389839de77964547fd77f7697

> get return -------->

```
{
  "access_token": "xxxxx",
  "remind_in": "157679999",
  "expires_in": 157679999,
  "uid": "3271188341"
}
```

## Step3
> request(get) ----> https://api.weibo.com/2/users/show.json?access_token=xxx&uid=3271188341

> get return ------>
```
{
  "id": 3271188341,
  "idstr": "3271188341",
  "class": 1,
  "screen_name": "姓陶字成伟",
  "name": "姓陶字成伟",
  "province": "11",
  "city": "5",
  "location": "北京 朝阳区",
  "description": "www.saintic.com",
  "url": "http://saintic.com",
  "profile_image_url": "http://tva1.sinaimg.cn/crop.25.0.330.330.50/c2fa5f75gw1en2jxj0o7xj20a5099aae.jpg",
  "cover_image_phone": "http://ww1.sinaimg.cn/crop.0.0.640.640.640/549d0121tw1egm1kjly3jj20hs0hsq4f.jpg",
  "profile_url": "staugur",
  "domain": "staugur",
  "weihao": "",
  "gender": "m",
  "followers_count": 85,
  "friends_count": 418,
  "pagefriends_count": 2,
  "statuses_count": 5,
  "favourites_count": 2,
  "created_at": "Wed Mar 20 16:59:21 +0800 2013",
  "following": false,
  "allow_all_act_msg": false,
  "geo_enabled": false,
  "verified": false,
  "verified_type": -1,
  "remark": "",
  "status": {
    "created_at": "Fri Oct 14 12:39:40 +0800 2016",
    "id": 4030459869973735,
    "mid": "4030459869973735",
    "idstr": "4030459869973735",
    "text": "转发微博",
    "source_allowclick": 0,
    "source_type": 1,
    "source": "<a href=\"http://app.weibo.com/t/feed/6vtZb0\" rel=\"nofollow\">微博 weibo.com</a>",
    "favorited": false,
    "truncated": false,
    "in_reply_to_status_id": "",
    "in_reply_to_user_id": "",
    "in_reply_to_screen_name": "",
    "pic_urls": [],
    "geo": null,
    "reposts_count": 0,
    "comments_count": 0,
    "attitudes_count": 0,
    "isLongText": false,
    "mlevel": 0,
    "visible": {
      "type": 0,
      "list_id": 0
    },
    "biz_feature": 0,
    "hasActionTypeCard": 0,
    "darwin_tags": [],
    "hot_weibo_tags": [],
    "text_tag_tips": [],
    "userType": 0,
    "positive_recom_flag": 0,
    "gif_ids": "",
    "is_show_bulletin": 2
  },
  "ptype": 0,
  "allow_all_comment": true,
  "avatar_large": "http://tva1.sinaimg.cn/crop.25.0.330.330.180/c2fa5f75gw1en2jxj0o7xj20a5099aae.jpg",
  "avatar_hd": "http://tva1.sinaimg.cn/crop.25.0.330.330.1024/c2fa5f75gw1en2jxj0o7xj20a5099aae.jpg",
  "verified_reason": "",
  "verified_trade": "",
  "verified_reason_url": "",
  "verified_source": "",
  "verified_source_url": "",
  "follow_me": false,
  "online_status": 0,
  "bi_followers_count": 33,
  "lang": "zh-cn",
  "star": 0,
  "mbtype": 0,
  "mbrank": 0,
  "block_word": 0,
  "block_app": 0,
  "credit_score": 80,
  "user_ability": 1024,
  "urank": 14
}
```
