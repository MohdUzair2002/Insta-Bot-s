# import requests

# cookies = {
#     'bev': '1672766979_ZTVlZGZiMjAxZTI2',
#     'everest_cookie': '1672766980.5m98pKgW5TvzyAs_stIO.b2DdYLwlcsKjaQuhKSsVpYN3HEChtd4zzPtZANOZDRc',
#     '_user_attributes': '%7B%22curr%22%3A%22USD%22%2C%22guest_exchange%22%3A1.0%2C%22device_profiling_session_id%22%3A%221672766980--ef2effb0da9fc6d966ee9c43%22%2C%22giftcard_profiling_session_id%22%3A%221672839578--dad0af64f8016528a08982d8%22%2C%22reservation_profiling_session_id%22%3A%221672839578--bd442eeaf09a4349dd2654d1%22%7D',
#     'jitney_client_session_id': 'bc12f100-3db4-4cd1-8af5-2e68e1a57881',
#     'jitney_client_session_created_at': '1672839579',
#     'frmfctr': 'wide',
#     '_gcl_au': '1.1.356625796.1672767075',
#     '_ga_2P6Q8PGG16': 'GS1.1.1672839662.4.1.1672839782.0.0.0',
#     '_ga': 'GA1.1.627090830.1672767077',
#     'cfrmfctr': 'MOBILE',
#     'tzo': '300',
#     'cbkp': '2',
#     'country': 'PK',
#     'previousTab': '%7B%22id%22%3A%220b46840d-1653-4374-9d3e-b41f8773c6f8%22%2C%22url%22%3A%22https%3A%2F%2Fwww.airbnb.com%2F%22%7D',
#     '_csrf_token': 'V4%24.airbnb.com%24rRmh01B5lCQ%24GMAEmT5AmyVdwc2kTRjD9che5N-yhqoF2o0h5EJaEzI%3D',
#     'jitney_client_session_updated_at': '1672839778',
#     'flags': '0',
#     'OptanonAlertBoxClosed': 'NR',
#     'ak_bmsc': 'CF29D8CC184C57012980FC7446CFD8BD~000000000000000000000000000000~YAAQRJ4QAqDSUEmFAQAAMUYCfRIr/r1+wxS86+JKgKDwFMJK+dJ4dOdXvbpLULG7v91Ytv6ruy3UStrjdb4itAlPXxgqm9KdueBTDjVDYbEdcODN5Ga2GHiaQxJu+VM8SPE4+VSULQwHtne7tEjF8cLTos0AWzhBwl+7zPE/kvzkrIqueq1y0QT6XE1ZsYo2P8zacX/auQfNTYrdig4toy5GVuexC6GVh5IdJArXgNxMdO3NewIkgpA4id4GXRkmKK28cMdOamtK7CNynJOEthlLPtt6WHapeOCMU8uBZNTocGVm4UHJMdjQYhEGj6n9q0faX5gK0Y0jvboIbAJ9eb78JoxNmuy8bkleiWYF7K90Q0Iy0z8YZQaXtDXkLA==',
#     'bm_sv': '22FE79038A9CE94F76C231074B615D72~YAAQXZ4QApOodnmFAQAA3igEfRKAi+FCUf7keKPiUwKDxQzLdXyIcDkFCqMYBIqcd6hHwfp9E8CsVtf++TZFNRpgHunV9e+xWYJUbLuUKfVRo/O2+amKPpitWfvWfrhvOXUtw3LH1238FwxzNILrKE+bJ/+R5ZLta3+pmNvBjKIJAHxxlsjPIcvvj3Gosj8ydE0xkMomF+j1E6GTdkTj2PbJg+AODZtxtTKTZ75mmtLKzBCXKK2Ewm1gMZM+/aQ/nQ==~1',
#     '_uetsid': '6da8fb608b8c11edac2d4f77654f0a43',
#     '_uetvid': '6da918908b8c11ed85dc27d560bc6c82',
# }

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
#     'Accept': '*/*',
#     'Accept-Language': 'en-US,en;q=0.5',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     'Referer': 'https://www.airbnb.com/',
#     'X-Airbnb-Supports-Airlock-V2': 'true',
#     'Content-Type': 'application/json',
#     'X-Airbnb-API-Key': 'd306zoyjsyarp7ifhu67rjxn52tv0t20',
#     'X-CSRF-Token': 'V4$.airbnb.com$rRmh01B5lCQ$GMAEmT5AmyVdwc2kTRjD9che5N-yhqoF2o0h5EJaEzI=',
#     'X-CSRF-Without-Token': '1',
#     'X-Airbnb-GraphQL-Platform': 'web',
#     'X-Airbnb-GraphQL-Platform-Client': 'minimalist-niobe',
#     'X-Niobe-Short-Circuited': 'true',
#     'x-client-request-id': '1530ied0e5juub142306m036bedm',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-origin',
#     'Connection': 'keep-alive',
#     # 'Cookie': 'bev=1672766979_ZTVlZGZiMjAxZTI2; everest_cookie=1672766980.5m98pKgW5TvzyAs_stIO.b2DdYLwlcsKjaQuhKSsVpYN3HEChtd4zzPtZANOZDRc; _user_attributes=%7B%22curr%22%3A%22USD%22%2C%22guest_exchange%22%3A1.0%2C%22device_profiling_session_id%22%3A%221672766980--ef2effb0da9fc6d966ee9c43%22%2C%22giftcard_profiling_session_id%22%3A%221672839578--dad0af64f8016528a08982d8%22%2C%22reservation_profiling_session_id%22%3A%221672839578--bd442eeaf09a4349dd2654d1%22%7D; jitney_client_session_id=bc12f100-3db4-4cd1-8af5-2e68e1a57881; jitney_client_session_created_at=1672839579; frmfctr=wide; _gcl_au=1.1.356625796.1672767075; _ga_2P6Q8PGG16=GS1.1.1672839662.4.1.1672839782.0.0.0; _ga=GA1.1.627090830.1672767077; cfrmfctr=MOBILE; tzo=300; cbkp=2; country=PK; previousTab=%7B%22id%22%3A%220b46840d-1653-4374-9d3e-b41f8773c6f8%22%2C%22url%22%3A%22https%3A%2F%2Fwww.airbnb.com%2F%22%7D; _csrf_token=V4%24.airbnb.com%24rRmh01B5lCQ%24GMAEmT5AmyVdwc2kTRjD9che5N-yhqoF2o0h5EJaEzI%3D; jitney_client_session_updated_at=1672839778; flags=0; OptanonAlertBoxClosed=NR; ak_bmsc=CF29D8CC184C57012980FC7446CFD8BD~000000000000000000000000000000~YAAQRJ4QAqDSUEmFAQAAMUYCfRIr/r1+wxS86+JKgKDwFMJK+dJ4dOdXvbpLULG7v91Ytv6ruy3UStrjdb4itAlPXxgqm9KdueBTDjVDYbEdcODN5Ga2GHiaQxJu+VM8SPE4+VSULQwHtne7tEjF8cLTos0AWzhBwl+7zPE/kvzkrIqueq1y0QT6XE1ZsYo2P8zacX/auQfNTYrdig4toy5GVuexC6GVh5IdJArXgNxMdO3NewIkgpA4id4GXRkmKK28cMdOamtK7CNynJOEthlLPtt6WHapeOCMU8uBZNTocGVm4UHJMdjQYhEGj6n9q0faX5gK0Y0jvboIbAJ9eb78JoxNmuy8bkleiWYF7K90Q0Iy0z8YZQaXtDXkLA==; bm_sv=22FE79038A9CE94F76C231074B615D72~YAAQXZ4QApOodnmFAQAA3igEfRKAi+FCUf7keKPiUwKDxQzLdXyIcDkFCqMYBIqcd6hHwfp9E8CsVtf++TZFNRpgHunV9e+xWYJUbLuUKfVRo/O2+amKPpitWfvWfrhvOXUtw3LH1238FwxzNILrKE+bJ/+R5ZLta3+pmNvBjKIJAHxxlsjPIcvvj3Gosj8ydE0xkMomF+j1E6GTdkTj2PbJg+AODZtxtTKTZ75mmtLKzBCXKK2Ewm1gMZM+/aQ/nQ==~1; _uetsid=6da8fb608b8c11edac2d4f77654f0a43; _uetvid=6da918908b8c11ed85dc27d560bc6c82',
# }

# params = {
#     'operationName': 'ExploreSections',
#     'locale': 'en',
#     'currency': 'USD',
#     'variables': '{"isInitialLoad":true,"hasLoggedIn":false,"cdnCacheSafe":false,"source":"EXPLORE","exploreRequest":{"metadataOnly":false,"version":"1.8.3","tabId":"all_tab","refinementPaths":["/homes"],"searchMode":"flex_destinations_search","itemsPerGrid":20,"cdnCacheSafe":false,"treatmentFlags":["flex_destinations_june_2021_launch_web_treatment","merch_header_breakpoint_expansion_web","flexible_dates_12_month_lead_time","storefronts_nov23_2021_homepage_web_treatment","lazy_load_flex_search_map_compact","lazy_load_flex_search_map_wide","im_flexible_may_2022_treatment","im_flexible_may_2022_treatment","flex_v2_review_counts_treatment","search_add_category_bar_ui_ranking_web","flexible_dates_options_extend_one_three_seven_days","super_date_flexibility","micro_flex_improvements","micro_flex_show_by_default","search_input_placeholder_phrases","pets_fee_treatment"],"screenSize":"large","isInitialLoad":true,"hasLoggedIn":false,"flexibleTripLengths":["one_week"],"locationSearch":"MIN_MAP_BOUNDS","categoryTag":"Tag:8225","priceFilterInputType":0,"priceFilterNumNights":5,"itemsOffset":40,"sectionOffset":0,"federatedSearchSessionId":"d6250d51-a23c-4b15-bdc2-af408de96e90"},"gpRequest":{"expectedResponseType":"INCREMENTAL"}}',
#     'extensions': '{"persistedQuery":{"version":1,"sha256Hash":"35c9235d2e6a25065fbed52b46ce8ebabf17d6f9fe5b26f97abd8d4ea01a2985"}}',
# }

# response = requests.get('https://www.airbnb.com/api/v3/ExploreSections', params=params, cookies=cookies, headers=headers)
# print(response.text)
from kivy.app import App
from kivy.uix.label import Label

class ExampleApp(App):
    def build(self):
        a = 1
        output = str(a + 1)
        return Label(text=output)

ExampleApp().run()