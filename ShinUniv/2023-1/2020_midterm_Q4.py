# 4. 문자열로 주어진 URL 주소 정보로부터 도메인 이름을 반환하는 프로그램을 구현하세요. (4점)
# – domain_name(string) 함수
# • 예)
# domain_name(“http://github.com/carbonfive/raygun”) == "github"
# domain_name("www.google.com") == “google"
# domain_name("https://www.netflix.com") == “netflix"

string = input('문자열 string:')

rm = {'http://':'', 'https://':'', 'www.':''}

def domain_name(string):
    for i, j in rm.items() :
        string = string.replace(i, j)

    string=string.split('.')
    # print(type(name[0]))
    return string[0]

print(domain_name(string))



# def domain_name(string):
#     name = ""
#     string = string.replace('http://', '')
#     # print(string)
#     string = string.replace('https://', '')
#     string = string.replace('www.', '')

#     # print(name)
#     string=string.split('.')
#     # print(type(name[0]))
#     return string[0]

# print(domain_name(string))