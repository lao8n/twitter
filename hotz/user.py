import requests, pprint

# curl 'https://twitter.com/i/api/graphql/ptQPCD7NrFS_TW71Lq07nw/UserByScreenName?variables=%7B%22screen_name%22%3A%22lao8n%22%2C%22withSafetyModeUserFields%22%3Atrue%2C%22withSuperFollowsUserFields%22%3Atrue%7D&features=%7B%22responsive_web_twitter_blue_verified_badge_is_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%7D' \
#   -H 'authority: twitter.com' \
#   -H 'accept: */*' \
#   -H 'accept-language: en-GB,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,ko-KR;q=0.6,ko;q=0.5,en-US;q=0.4' \
#   -H 'authorization: Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA' \
#   -H 'cache-control: no-cache' \
#   -H 'content-type: application/json' \
#   -H 'cookie: guest_id=v1%3A162565435833526566; dnt=1; ads_prefs="HBESAAA="; kdt=Wj0OHbG3GdvAqDfJ6kQdusLNWJr7XPRBlTbirof9; remember_checked_on=1; auth_token=7fe462acc295c74be5b65e1d5d8ad8cab0c1ba48; ct0=6c63a65301fb7da57c077166bf01b6c6e34030ea4a931105d8e1e2dc06bf06c1c326abd384e0d04e56f2beee34a316ff7bbe511bb53d824b859ae6c122b180440c152a88dd92eebb9f71ed8cf57bfb8a; twid=u%3D1144376135360438272; d_prefs=MToxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw; guest_id_ads=v1%3A162565435833526566; guest_id_marketing=v1%3A162565435833526566; personalization_id="v1_8ymSq/dxTsY6p737H/CPgg=="; _ga=GA1.2.95830049.1667929269; _gid=GA1.2.1816015515.1668895869; lv-uid=AAAAEIA3bzSJ3opNYmaEFvB6O-YMRKzbHx5IgNtyDV2ketElsGghcRUxMPGXuMGY' \
#   -H 'pragma: no-cache' \
#   -H 'referer: https://twitter.com/lao8n' \
#   -H 'sec-ch-ua: "Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "Windows"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36' \
#   -H 'x-csrf-token: 6c63a65301fb7da57c077166bf01b6c6e34030ea4a931105d8e1e2dc06bf06c1c326abd384e0d04e56f2beee34a316ff7bbe511bb53d824b859ae6c122b180440c152a88dd92eebb9f71ed8cf57bfb8a' \
#   -H 'x-twitter-active-user: yes' \
#   -H 'x-twitter-auth-type: OAuth2Session' \
#   -H 'x-twitter-client-language: en' \
#   --compressed

# use curlconverter.com

cookies = {
    'guest_id': 'v1%3A162565435833526566',
    'dnt': '1',
    'ads_prefs': '"HBESAAA="',
    'kdt': 'Wj0OHbG3GdvAqDfJ6kQdusLNWJr7XPRBlTbirof9',
    'remember_checked_on': '1',
    'auth_token': '7fe462acc295c74be5b65e1d5d8ad8cab0c1ba48',
    'ct0': '6c63a65301fb7da57c077166bf01b6c6e34030ea4a931105d8e1e2dc06bf06c1c326abd384e0d04e56f2beee34a316ff7bbe511bb53d824b859ae6c122b180440c152a88dd92eebb9f71ed8cf57bfb8a',
    'twid': 'u%3D1144376135360438272',
    'd_prefs': 'MToxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw',
    'guest_id_ads': 'v1%3A162565435833526566',
    'guest_id_marketing': 'v1%3A162565435833526566',
    'personalization_id': '"v1_8ymSq/dxTsY6p737H/CPgg=="',
    '_ga': 'GA1.2.95830049.1667929269',
    '_gid': 'GA1.2.1816015515.1668895869',
    'lv-uid': 'AAAAEIA3bzSJ3opNYmaEFvB6O-YMRKzbHx5IgNtyDV2ketElsGghcRUxMPGXuMGY',
}

headers = {
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'x-csrf-token': '6c63a65301fb7da57c077166bf01b6c6e34030ea4a931105d8e1e2dc06bf06c1c326abd384e0d04e56f2beee34a316ff7bbe511bb53d824b859ae6c122b180440c152a88dd92eebb9f71ed8cf57bfb8a',
}

# variables = {
#     "screen_name": 'lao8n',
#     "withSafetyModeUserFields": True,
#     "withSuperFollowsUserFields": True,
# }
# features = {
#     "responsive_web_twitter_blue_verified_badge_is_enabled": True,
#     "verified_phone_label_enabled": False,
#     "responsive_web_graphql_timeline_navigation_enabled": True
# }
# params = {"variables": variables, "features": features}
params = {
    'variables': '{"screen_name":"lao8n","withSafetyModeUserFields":true,"withSuperFollowsUserFields":true}',
    'features': '{"responsive_web_twitter_blue_verified_badge_is_enabled":true,"verified_phone_label_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true}',
}
response = requests.get('https://twitter.com/i/api/graphql/ptQPCD7NrFS_TW71Lq07nw/UserByScreenName', params=params, cookies=cookies, headers=headers)
print(response.status_code)
pprint.pprint(response.json())
