//
//  CTMediator+MobileIndexActions.h
//
//  Created by ace on 2019/04/10.
//  Copyright © 2019年 ace. All rights reserved.
//

#import "CTMediator+MobileIndexActions.h"

@implementation CTMediator (indexActions)

- (UIViewController *)mediator_mobileIndex:(NSDictionary *)dict
{
    UIViewController *viewController = [self performTarget:@"mobile"
                                  action:@"index"
                                  params:dict
                       shouldCacheTarget:YES];

    if ([viewController isKindOfClass:[UIViewController class]]) {
        return viewController;
    } else {
        NSLog(@"%@ 未能实例化页面", NSStringFromSelector(_cmd));
        return [[UIViewController alloc] init];
    }
}

@end