import getpass, tools
from jinja2 import Template

def main():
    while (1):
        moduleName = input("请输入模块名称：");

        if moduleName.isalnum():
            break;
        else:
            print('输错，再输一遍')



    dir_path = './' + moduleName
    tools.mkDir(dir_path)


    Request_path = dir_path+'/Requests'
    tools.mkDir(Request_path)

    saveRequest(Request_path, moduleName)



def saveRequest(dir_path, moduleName):
    # 创建.h文件
    h_path_w = '%s/%sRequest.h' % (dir_path, moduleName)
    h_path_r = './Template/Request.h.txt'
    saveOCFile(moduleName, h_path_w, h_path_r)


    # 创建保存.m文件
    m_path_w = '%s/%sRequest.m' % (dir_path, moduleName)
    m_path_r = './Template/Request.m.txt'
    saveOCFile(moduleName, m_path_w, m_path_r)


def saveOCFile(moduleName, path_w, path_r):
    author = getpass.getuser()
    date = tools.dateFormer(tools.ts(), '%Y/%m/%d')
    year = tools.dateFormer(tools.ts(), '%Y')


    content = tools.readfile(path_r)
    template = Template(content)
    content = template.render(moduleName=moduleName, author=author, date=date, year=year)
    tools.savefile(content, path_w)


main()



