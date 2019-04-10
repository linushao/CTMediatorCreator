//
//  YMMobileIndexViewController.h
//  Created by ace on 2019/04/10.
//  Copyright © 2019年 ace. All rights reserved.
//


/**
    用法：
    用NSDictionary传递参数
    1、#import "CTMediator+NextModuleActions.h"（引入下一个模块的action）

    2、
    UIViewController *viewController = [[CTMediator sharedInstance] mediator_actionName:@{@"model":@"123456"}];
    [self.navigationController pushViewController:viewController animated:YES];
*/



#import "YMMobileIndexViewController.h"

// Tools

// Data

// Views

// Models

// Requests

// Actions
//#import "CTMediator+<#actionName#>Actions.h"


@interface YMMobileIndexViewController ()

// Data
//@property (nonatomic, copy) NSArray *dataSource;

// Models

// Views
//@property (nonatomic, strong) <#View#> *<#View#>;

@end

@implementation YMMobileIndexViewController

#pragma mark - LifeCycle（生命周期）
- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.

    [self setupSubviews];
}


#pragma mark - UI（自定义UI）
- (void)setupSubviews
{
    self.view.backgroundColor = [UIColor whiteColor];
    [self addLayout];
}


/**
- (void)add<#View#>
{
    safeInitClass(<#obj#>, <#class#>);
    safeAddSubview(<#view#>, <#superView#>);
}
 */


- (void)addLayout
{
    __block CGFloat offset = 15;
    __weak typeof(self) weakSelf = self;
}


#pragma mark - Action（响应事件）


#pragma mark - Property（属性）


#pragma mark - Delegate（代理)


#pragma mark - Notification（通知）


#pragma mark - Private Method（私有方法）


#pragma mark - Public Method（公有方法）


#pragma mark - Network（网络事件）




@end