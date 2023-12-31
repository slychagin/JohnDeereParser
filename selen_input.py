HOST = 'https://partscatalog.deere.com/jdrc/search'
SEARCH_URL = 'https://partscatalog.deere.com/jdrc/search/type/parts/term/'
HEADERS = {
    "authority": "partscatalog.deere.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6",
    "cache-control": "no-cache,no-store",
    "captcha-token": "03AL8dmw-opbXmwEsdcq43EzniFQrAftx_j1oiZd-prbyOivKKExvOByD-6H1dSJVloLJdhthlVLOWem79j-c9uHRNSPd0unHOAS7qB72ovcsQbvdoIjxOLS9oLq6sVwxfzAeGJWmDFqGwFWGFoTS-n-2jDXcI0ZADwFRXa7zKzM4hZzADIZIBVafwXjEoznIX1ftzfmXfhJyDy_eMpqoEQZ4g8lXYW27SeRApnBmtrc8Zd-plqHqVGNAbAWW4zpyuZ_CT2Jty9lePBc2A_ERlgeQwA9JCK4OKhRYDZv5eSf971qrY5ORyTPwh0SeiJzqaXFlYGFqJM2de9OS5bK4x65H58_PIiTtoZ5P8_IZ0P9TuU2ekQaM8Ox7uChLsxGU39nw9lrJbh8nu8E12RwTUdKjlK_oOkkxe61qMAnjlfH_-tRujkpij0WMA2r97qdZYlj4jJ3q9nZZtZ-voBlTXWtZlAGKDhsdHVpZ-o5T1-UejZ5I0nYWoex6M1Szd2x-aJr35JgI_k_oLfqzSDB32EZ4MU44VAzqJvEXbnG-dWsqNAOMzSqs0qjtu8wAdYWI4kJCy0lDvpaeRN634lKOa57uFq8TZH7340ZSejjy3yhDO6JJFaMDK6Cm1BEQuQAN7OKQ6Q69JoigpnKyhWS5tKPHim0sECErdaAGyIM_omOuGoc8R777UwQpX66KasilpUJg8MSXE4N4WcmUvb2Ope5VBd-fY8R_FM3xH6N9G158WlynJ-RKrDLbEO0maUpxxGqkKKwIWRubm-T39Oh4XyBacIwtYi9M5qz3Qpn8z-Zv_aDpJJSij7XkttdhEdda5bx3Ghjw8XFmyItAiP9tbImu-3M5xmLXkX7iQ5hlJg8bhRcCV2uGDzaRVHecLYF1-A_e-GHA811k_NRh7B5yXj7D2VB-9BxieOGdeFR9WITyfQOH4Hp9u0M78II5MxD_lmSivzuGO__zUZHhUXk4qCnrkqGjBc7Zexh2q-563wJncuOX5UCyjqKUEdkYip32DbMHOrN8fAWiQ0F4FzAp3o_uFUOxVn0UuN16t0jjKxveELw9pcK5-4vjwZ25oGMp1ZO7I0Qp5_rIATWY1mfWi9QQC6qkQp43StJGa-qTxY6q5scn91vsXFjvNJt_yjwlY6Jgm_isJwwzbHt6Swq5lLWVvLDT5je56vmAHe52mbIxNXpO_dqidXOAapCyQjLNExGuH9a-ZPpBh1jK3FjEghZwZ4qf5x2nn1xUvVG4RC4L1e0ZLwA78B9mIpiOcpy7xbJUvNWqk1AOJX5aiHfp0ss9GAhWm_b7DyVvH6ynpceIkh-kBxr95L2C6VCzZxbxiNXfWX9QT5hxqYkShiyTiNHYCHMQZEoHgVPVQ3-81vQCt1LV8nyn4dIaSoS6x95uyFA1cHVHU69tPoVwnjs5sY6wqtALtOlI5DhCxJR8DM7NuedpKz3D82VJLO2C7H2E1aivdCuJVQPg8u5R2U7ImylwM1gX2_qvgEg",
    "captcha-version": "Enterprise",
    "content-type": "application/json",
    "cookie": "s_ecid=MCMID^%^7C34411222976331746953165167180167218425; aam_uuid=26917405547382902362411474729006153314; _gcl_au=1.1.1989196887.1686222498; _ga=GA1.2.1481994413.1686416949; _gid=GA1.2.1529901238.1686416949; coSkipAddEquipment-2571241=test; kndctr_8CC867C25245ADC30A490D4C_AdobeOrg_identity=CiYzNDQxMTIyMjk3NjMzMTc0Njk1MzE2NTE2NzE4MDE2NzIxODQyNVIPCK6d47KKMRgBKgRKUE4z8AGuneOyijE=; s_evar47=First^%^20Visit; s_evar50=Weekday; AMCVS_8CC867C25245ADC30A490D4C^%^40AdobeOrg=1; s_cc=true; INDUSTRY_TYPE=Agriculture; at_check=true; mbox=session^#7341f763f4c2424aba34e57dc41b43bf^#1686462283^|PC^#7341f763f4c2424aba34e57dc41b43bf.37_0^#1749705223; s_ppvl=ru_ru^%^2520^%^253A^%^2520partslookup^%^2520^%^253A^%^2520search^%^2520results^%^2520^%^253A^%^2520parts^%^2C100^%^2C100^%^2C969^%^2C1261^%^2C969^%^2C1920^%^2C1080^%^2C1^%^2CP; AMCV_8CC867C25245ADC30A490D4C^%^40AdobeOrg=-1124106680^%^7CMCIDTS^%^7C19519^%^7CMCMID^%^7C34411222976331746953165167180167218425^%^7CMCAAMLH-1687091683^%^7C6^%^7CMCAAMB-1687091683^%^7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y^%^7CMCOPTOUT-1686494083s^%^7CNONE^%^7CMCAID^%^7CNONE^%^7CMCCIDH^%^7C-1339625781^%^7CvVersion^%^7C5.2.0; s_sq=^%^5B^%^5BB^%^5D^%^5D; s_evar48=9^%^3A07^%^20AM^%^7CSunday; s_evar49=9^%^3A07^%^20AM^%^7CSunday; AWSALB=EEnJ8PvQkAHvaz+MDMwBub1Sb2966xZAJ4m4dhMxulil/AUp4u8hxPlovEtNYIcYpQzcSTZtHcMoQ7ktj5NcA6JZxfu8+BUyTeRXY0Amd0+Gr5grO3a08y2amypJ; AWSALBCORS=EEnJ8PvQkAHvaz+MDMwBub1Sb2966xZAJ4m4dhMxulil/AUp4u8hxPlovEtNYIcYpQzcSTZtHcMoQ7ktj5NcA6JZxfu8+BUyTeRXY0Amd0+Gr5grO3a08y2amypJ; s_ppv=ru_ru^%^2520^%^253A^%^2520partslookup^%^2520^%^253A^%^2520search^%^2520results^%^2520^%^253A^%^2520parts^%^2C100^%^2C100^%^2C969^%^2C1261^%^2C969^%^2C1920^%^2C1080^%^2C1^%^2CP; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Jun+11+2023+17^%^3A07^%^3A21+GMT^%^2B0300+(^%^D0^%^9C^%^D0^%^BE^%^D1^%^81^%^D0^%^BA^%^D0^%^B2^%^D0^%^B0^%^2C+^%^D1^%^81^%^D1^%^82^%^D0^%^B0^%^D0^%^BD^%^D0^%^B4^%^D0^%^B0^%^D1^%^80^%^D1^%^82^%^D0^%^BD^%^D0^%^BE^%^D0^%^B5+^%^D0^%^B2^%^D1^%^80^%^D0^%^B5^%^D0^%^BC^%^D1^%^8F)&version=202304.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=fc919cad-6eb1-4414-b005-dc242da9a2f1&interactionCount=1&landingPath=NotLandingPage&groups=C0001^%^3A1^%^2CC0003^%^3A1^%^2CC0004^%^3A1^%^2CC0002^%^3A1&AwaitingReconsent=false",
    "expires": "0",
    "origin": "https://partscatalog.deere.com",
    "pragma": "no-cache",
    "product-line": "JDRC",
    "referer": "https://partscatalog.deere.com/jdrc/search/type/parts/term/AAX10002",
    "sec-ch-ua": '"Not.A/Brand";v="8",,\^"Chromium";v="114",,\^"Google Chrome";v="114"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
}
ARTICLES_FILE = 'files/articles.txt'
FILE = 'files/parts.csv'
