# these tokens are now public :S
# headers= {
#     "authorization":'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
#     "cookie": 'guest_id=v1%3A162565435833526566; dnt=1; ads_prefs="HBESAAA="; kdt=Wj0OHbG3GdvAqDfJ6kQdusLNWJr7XPRBlTbirof9; remember_checked_on=1; auth_token=7fe462acc295c74be5b65e1d5d8ad8cab0c1ba48; ct0=6c63a65301fb7da57c077166bf01b6c6e34030ea4a931105d8e1e2dc06bf06c1c326abd384e0d04e56f2beee34a316ff7bbe511bb53d824b859ae6c122b180440c152a88dd92eebb9f71ed8cf57bfb8a; twid=u%3D1144376135360438272; d_prefs=MToxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw; guest_id_ads=v1%3A162565435833526566; guest_id_marketing=v1%3A162565435833526566; personalization_id="v1_8ymSq/dxTsY6p737H/CPgg=="; _ga=GA1.2.95830049.1667929269; _gid=GA1.2.1816015515.1668895869; lv-uid=AAAAEIA3bzSJ3opNYmaEFvB6O-YMRKzbHx5IgNtyDV2ketElsGghcRUxMPGXuMGY',
#     "x-csrf-token": '6c63a65301fb7da57c077166bf01b6c6e34030ea4a931105d8e1e2dc06bf06c1c326abd384e0d04e56f2beee34a316ff7bbe511bb53d824b859ae6c122b180440c152a88dd92eebb9f71ed8cf57bfb8a'
# }
# httplink = 'https://twitter.com/i/api/graphql/BoHLKeBvibdYDiJON1oqTg/TweetDetail?variables=%7B%22focalTweetId%22%3A%221594090777772457985%22%2C%22with_rux_injections%22%3Afalse%2C%22includePromotedContent%22%3Atrue%2C%22withCommunity%22%3Atrue%2C%22withQuickPromoteEligibilityTweetFields%22%3Atrue%2C%22withBirdwatchNotes%22%3Afalse%2C%22withSuperFollowsUserFields%22%3Atrue%2C%22withDownvotePerspective%22%3Afalse%2C%22withReactionsMetadata%22%3Afalse%2C%22withReactionsPerspective%22%3Afalse%2C%22withSuperFollowsTweetFields%22%3Atrue%2C%22withVoice%22%3Atrue%2C%22withV2Timeline%22%3Atrue%7D&features=%7B%22responsive_web_twitter_blue_verified_badge_is_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22unified_cards_ad_metadata_container_dynamic_card_content_query_enabled%22%3Atrue%2C%22tweetypie_unmention_optimization_enabled%22%3Atrue%2C%22responsive_web_uc_gql_enabled%22%3Atrue%2C%22vibe_api_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Afalse%2C%22interactive_text_enabled%22%3Atrue%2C%22responsive_web_text_conversations_enabled%22%3Afalse%2C%22responsive_web_enhance_cards_enabled%22%3Atrue%7D'
# from urllib.parse import unquote
#print(unquote(httplink))

# r = requests.get(unquote(httplink), params={"variables": data}, headers=headers)
# print(r.status_code, r.text)

import requests, pprint

cookies = {
    'guest_id': 'v1%3A162565435833526566',
    'dnt': '1',
    'ads_prefs': '"HBESAAA="',
    'kdt': 'Wj0OHbG3GdvAqDfJ6kQdusLNWJr7XPRBlTbirof9',
    'remember_checked_on': '1',
    'auth_token': '7fe462acc295c74be5b65e1d5d8ad8cab0c1ba48',
    'ct0': '6c63a65301fb7da57c077166bf01b6c6e34030ea4a931105d8e1e2dc06bf06c1c326abd384e0d04e56f2beee34a316ff7bbe511bb53d824b859ae6c122b180440c152a88dd92eebb9f71ed8cf57bfb8a',
    'twid': 'u%3D1144376135360438272',
    # 'd_prefs': 'MToxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw',
    # 'guest_id_ads': 'v1%3A162565435833526566',
    # 'guest_id_marketing': 'v1%3A162565435833526566',
    'personalization_id': '"v1_8ymSq/dxTsY6p737H/CPgg=="',
    # '_ga': 'GA1.2.95830049.1667929269',
    # '_gid': 'GA1.2.1816015515.1668895869',
    # 'lv-uid': 'AAAAEIA3bzSJ3opNYmaEFvB6O-YMRKzbHx5IgNtyDV2ketElsGghcRUxMPGXuMGY',
}

headers = {
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'x-csrf-token': '6c63a65301fb7da57c077166bf01b6c6e34030ea4a931105d8e1e2dc06bf06c1c326abd384e0d04e56f2beee34a316ff7bbe511bb53d824b859ae6c122b180440c152a88dd92eebb9f71ed8cf57bfb8a',
}
# looks like all params are necessary
params = {
    'variables': '{\
        "focalTweetId":"1594090777772457985",\
        "with_rux_injections":false,\
        "includePromotedContent":true,\
        "withCommunity":true,\
        "withQuickPromoteEligibilityTweetFields":true,\
        "withBirdwatchNotes":false,\
        "withSuperFollowsUserFields":true,\
        "withDownvotePerspective":false,\
        "withReactionsMetadata":false,\
        "withReactionsPerspective":false,\
        "withSuperFollowsTweetFields":true,\
        "withVoice":true,\
        "withV2Timeline":true\
    }',
    'features': '{\
        "responsive_web_twitter_blue_verified_badge_is_enabled":true,\
        "verified_phone_label_enabled":false,\
        "responsive_web_graphql_timeline_navigation_enabled":true,\
        "unified_cards_ad_metadata_container_dynamic_card_content_query_enabled":true,\
        "tweetypie_unmention_optimization_enabled":true,\
        "responsive_web_uc_gql_enabled":true,\
        "vibe_api_enabled":true,\
        "responsive_web_edit_tweet_api_enabled":true,\
        "graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,\
        "standardized_nudges_misinfo":true,\
        "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":false,\
        "interactive_text_enabled":true,\
        "responsive_web_text_conversations_enabled":false,\
        "responsive_web_enhance_cards_enabled":true\
    }'
}
response = requests.get('https://twitter.com/i/api/graphql/BoHLKeBvibdYDiJON1oqTg/TweetDetail', params=params, cookies=cookies, headers=headers)
print(response.status_code)
pprint.pprint(response.json())
