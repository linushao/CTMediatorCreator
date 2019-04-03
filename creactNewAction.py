import getpass, tools
from jinja2 import Template

def main():
    while (1):
        targetName = input("请输入Target名称：");
        if targetName.isalnum():
            break;
        else:
            print('输错，再输一遍')


    while (1):
        actionName = input("请输入Action名称：");
        if actionName.isalnum():
            break;
        else:
            print('输错，再输一遍')


    isNative = False;

    while (1):
        nativeType = input("请输入模块是否为公开模块(0为公开模块，1为本地，默认回车为公开0)：");

        if nativeType == '':
            break;
        else:
            if (int(nativeType) == 0):
                isNative = False
                break;
 
            elif (int(nativeType) == 1):
                isNative = True
                break;
            else:
                print('输错，再输一遍')



    dir_path = './' + targetName.capitalize() + actionName.capitalize()
    tools.mkDir(dir_path)

    Controllers_path = dir_path+'/Controllers'
#    Models_path = dir_path+'/Models'
#    Views_path = dir_path+'/Views'
    Mediator_path = dir_path+'/Actions'


    tools.mkDir(Controllers_path)
    tools.mkDir(Mediator_path)


    saveController(Controllers_path, targetName, actionName, isNative)
    saveMediatorTarget(Mediator_path, targetName, actionName, isNative)
    saveMediatorAction(Mediator_path, targetName, actionName, isNative)


def saveController(dir_path, targetName, actionName, isNative):
    hname = 'YM'+targetName.capitalize()+actionName.capitalize()
    # 创建.h文件
    h_path_w = '%s/%sViewController.h' % (dir_path, hname)
    h_path_r = './TemplateV2/ViewController.h.txt'
    saveOCFile(targetName, actionName, h_path_w, h_path_r, isNative)

    # 创建保存.m文件
    m_path_w = dir_path + '/' + hname + 'ViewController.m'
    m_path_r = './TemplateV2/ViewController.m.txt'
    saveOCFile(targetName, actionName, m_path_w, m_path_r, isNative)


def saveMediatorTarget(dir_path, targetName, actionName, isNative):
    # 创建.h文件
    h_path_w = '%s/Target_%s.h' % (dir_path, targetName)
    h_path_r = './TemplateV2/Target.h.txt'
    saveOCFile(targetName, actionName, h_path_w, h_path_r, isNative)


    # 创建保存.m文件
    m_path_w = '%s/Target_%s.m' % (dir_path, targetName)
    m_path_r = './TemplateV2/Target.m.txt'
    saveOCFile(targetName, actionName, m_path_w, m_path_r, isNative)


def saveMediatorAction(dir_path, targetName, actionName, isNative):
    # 创建.h文件
    if isNative:
        h_path_w = '%s/CTMediator+%s%sActions.h' % (dir_path, targetName.capitalize(), actionName.capitalize())
        h_path_r = './TemplateV2/CTMediator+NativeActions.h.txt'
    else:
        h_path_w = '%s/CTMediator+%s%sActions.h' % (dir_path, targetName.capitalize(), actionName.capitalize())
        h_path_r = './TemplateV2/CTMediator+Actions.h.txt'

    saveOCFile(targetName, actionName, h_path_w, h_path_r, isNative)


    # 创建保存.m文件
    if isNative:
        m_path_w = '%s/CTMediator+%s%sActions.m' % (dir_path, targetName.capitalize(), actionName.capitalize())
        m_path_r = './TemplateV2/CTMediator+NativeActions.m.txt'
    else:
        m_path_w = '%s/CTMediator+%s%sActions.m' % (dir_path, targetName.capitalize(), actionName.capitalize())
        m_path_r = './TemplateV2/CTMediator+Actions.m.txt'

    saveOCFile(targetName, actionName, m_path_w, m_path_r, isNative)


def saveOCFile(targetName, actionName, path_w, path_r, isNative):
    author = getpass.getuser()
    date = tools.dateFormer(tools.ts(), '%Y/%m/%d')
    year = tools.dateFormer(tools.ts(), '%Y')


    content = tools.readfile(path_r)
    template = Template(content)
    content = template.render(targetName=targetName, actionName=actionName, author=author, date=date, year=year, isNative=isNative)
    tools.savefile(content, path_w)


main()



