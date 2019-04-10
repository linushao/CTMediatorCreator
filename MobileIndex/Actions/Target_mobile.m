//
//  Target_mobile.h
//  Created by ace on 2019/04/10.
//  Copyright © 2019年 ace. All rights reserved.
//
//  XXX://mobile/index?XXX=xxx

#import "Target_mobile.h"
#import "YMMobileIndexViewController.h"

@implementation Target_mobile


- (UIViewController *)Action_index:(NSDictionary *)params

{
    YMMobileIndexViewController *vc = [[YMMobileIndexViewController alloc] init];

    /**
        example:
        if ([params valueForKey:@"<#model#>"]) {
            vc.<#model#> = params[@"<#model#>"];
        }
     */

    return vc;
}

@end