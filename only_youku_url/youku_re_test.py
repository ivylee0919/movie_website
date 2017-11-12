import re

trailer_youku_url = "http://v.youku.com/v_show/id_XMzE5MDUxNjM2.html?spm=a2h0j.8191423.module_basic_relation.5~5!2~5~5!4~5!2~1~3~A"
trailer_youku_url = "http://v.youku.com/v_show/id_XMTMzMTM3MTY2OA==.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1"

youku_id_match = re.search(
            r'(id_)(\w+=*)(\.html)', trailer_youku_url)


print youku_id_match.group(2)
