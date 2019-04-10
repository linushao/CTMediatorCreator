//
//  Target_mobile.h
//  Created by ace on 2019/04/10.
//  Copyright © 2019年 ace. All rights reserved.
//
//  XXX://mobile/success?XXX=xxx

#import "Target_mobile.h"
#import "YMMobileSuccessViewController.h"

@implementation Target_mobile


- (UIViewController *)Action_success:(NSDictionary *)params

{
    YMMobileSuccessViewController *vc = [[YMMobileSuccessViewController alloc] init];

    /**
        example:
        if ([params valueForKey:@"<#model#>"]) {
            vc.<#model#> = params[@"<#model#>"];
        }
     */

    return vc;
}

@end