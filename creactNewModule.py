import getpass, tools
from jinja2 import Template

def main():
    while (1):
        moduleName = input("请输入模块名称：");

        if moduleName.isalnum():
            break;
        else:
            print('输错，再输一遍')


    isNative = True;

    while (1):
        nativeType = input("请输入模块是否为本地模块(1为本地，0为公开模块，默认回车为本地1)：");

        if nativeType == '':
            break;
        else:
            if (int(nativeType) == 0):
                isNative = False
                break;
            else:
                print('输错，再输一遍')



    dir_path = './' + moduleName
    tools.mkDir(dir_path)

    Controllers_path = dir_path+'/Controllers'
    Models_path = dir_path+'/Models'
    Views_path = dir_path+'/Views'
    Mediator_path = dir_path+'/Mediator'


    tools.mkDir(Controllers_path)
    tools.mkDir(Models_path)
    tools.mkDir(Views_path)
    tools.mkDir(Mediator_path)


    saveController(Controllers_path, moduleName, isNative)
    saveMediatorTarget(Mediator_path, moduleName, isNative)
    saveMediatorAction(Mediator_path, moduleName, isNative)


def saveController(dir_path, moduleName, isNative):
    # 创建.h文件
    h_path_w = '%s/%sViewController.h' % (dir_path, moduleName)
    h_path_r = './Template/ViewController.h.txt'
    saveOCFile(moduleName, h_path_w, h_path_r, isNative)

    # 创建保存.m文件
    m_path_w = dir_path + '/' + moduleName + 'ViewController.m'
    m_path_r = './Template/ViewController.m.txt'
    saveOCFile(moduleName, m_path_w, m_path_r, isNative)


def saveMediatorTarget(dir_path, moduleName, isNative):
    # 创建.h文件
    h_path_w = '%s/Target_%s.h' % (dir_path, moduleName)
    h_path_r = './Template/Target.h.txt'
    saveOCFile(moduleName, h_path_w, h_path_r, isNative)


    # 创建保存.m文件
    m_path_w = '%s/Target_%s.m' % (dir_path, moduleName)
    m_path_r = './Template/Target.m.txt'
    saveOCFile(moduleName, m_path_w, m_path_r, isNative)


def saveMediatorAction(dir_path, moduleName, isNative):
    # 创建.h文件
    if isNative:
        h_path_w = '%s/CTMediator+%sActions.h' % (dir_path, moduleName)
        h_path_r = './Template/CTMediator+NativeActions.h.txt'
    else:
        h_path_w = '%s/CTMediator+%sActions.h' % (dir_path, moduleName)
        h_path_r = './Template/CTMediator+Actions.h.txt'

    saveOCFile(moduleName, h_path_w, h_path_r, isNative)


    # 创建保存.m文件
    if isNative:
        m_path_w = '%s/CTMediator+%sActions.m' % (dir_path, moduleName)
        m_path_r = './Template/CTMediator+NativeActions.m.txt'
    else:
        m_path_w = '%s/CTMediator+%sActions.m' % (dir_path, moduleName)
        m_path_r = './Template/CTMediator+Actions.m.txt'

    saveOCFile(moduleName, m_path_w, m_path_r, isNative)


def saveOCFile(moduleName, path_w, path_r, isNative):
    author = getpass.getuser()
    date = tools.dateFormer(tools.ts(), '%Y/%m/%d')
    year = tools.dateFormer(tools.ts(), '%Y')


    content = tools.readfile(path_r)
    template = Template(content)
    content = template.render(moduleName=moduleName, author=author, date=date, year=year, isNative=isNative)
    tools.savefile(content, path_w)


main()



